"""Leitura das peças por subagentes (Claude Code) no lugar da chamada direta à API, com o mesmo prompt e formato.

Por que existe: no curso, a leitura das peças (análise por peça de coleta/extrair.py e ficha de trabalho de
scripts/fichas_trabalho.py) pode ser feita por subagentes em paralelo em vez de uma chave de API. Este módulo
(1) grava os prompts originais e uma entrada por peça para os agentes lerem e (2) injeta as respostas dos agentes
nos dois scripts como se fossem a resposta do LLM — validação de esquema, ancoragem literal das evidências, cache e
saídas continuam os do repositório.

Uso (da raiz):
  python -m coleta.agentes preparar      # dados/agentes/{PROMPT_*.md, entrada/<doc>.txt}
  (agentes gravam dados/agentes/saida/extracao/<doc>.json e dados/agentes/saida/ficha/<doc>.json)
  python -m coleta.agentes extracao      # → dados/relator/extractions.parquet
  python -m coleta.agentes fichas        # → saida/fichas_trabalho.{csv,jsonl}"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ))
sys.path.insert(0, str(RAIZ / "scripts"))

from coleta import extrair  # noqa: E402
from coleta.util import RELATOR  # noqa: E402

AG = RELATOR.parent / "agentes"
MODELO = "agente/claude-haiku-5-5"


def _resposta(tipo: str, sei_doc_id: str) -> dict:
    arq = AG / "saida" / tipo / f"{sei_doc_id}.json"
    if not arq.exists():
        raise RuntimeError(f"sem resposta do agente em {arq}")
    return json.loads(arq.read_text(encoding="utf-8"))


def preparar():
    import pandas as pd
    import fichas_trabalho as ft
    (AG / "entrada").mkdir(parents=True, exist_ok=True)
    esquema = json.dumps(extrair.ESQUEMA, ensure_ascii=False, indent=1)
    (AG / "PROMPT_EXTRACAO.md").write_text(f"{extrair.SISTEMA}\n\nResponda APENAS um JSON neste esquema (todos os "
                                           f"campos obrigatórios, nenhum a mais):\n{esquema}\n", encoding="utf-8")
    (AG / "PROMPT_FICHA.md").write_text(ft.SISTEMA + "\n", encoding="utf-8")
    docs = pd.read_parquet(RELATOR / "documentos.parquet")
    txt = pd.read_parquet(RELATOR / "doc_text_piloto.parquet")
    textos = {(p, str(s)): t for p, s, t in zip(txt.processo, txt.sei_doc_id, txt.texto)}
    n = 0
    for d in sorted(docs.to_dict("records"), key=lambda r: str(r["sei_doc_id"])):
        sid = str(d["sei_doc_id"])
        t = (textos.get((d["processo"], sid)) or "").strip()
        if d.get("restrito") or len(t) < extrair.MIN_CHARS:
            continue
        (AG / "entrada" / f"{sid}.txt").write_text(extrair.mensagem_usuario(dict(d, sei_doc_id=sid), t),
                                                    encoding="utf-8")
        n += 1
    print(f"{n} peças com texto em {AG / 'entrada'}")


def extracao():
    import pandas as pd
    docs = pd.read_parquet(RELATOR / "documentos.parquet")
    txt = pd.read_parquet(RELATOR / "doc_text_piloto.parquet")
    textos = {(p, str(s)): t for p, s, t in zip(txt.processo, txt.sei_doc_id, txt.texto)}
    regs = [{k: (None if not isinstance(v, (list, dict)) and pd.isna(v) else v) for k, v in r.items()}
            for r in docs.to_dict("records")]

    def chamar(modelo, usuario, esforco):
        sid = re.search(r"Documento SEI nº (\S+)", usuario).group(1)
        return _resposta("extracao", sid), {}

    linhas, erros = extrair.extrair_todos(regs, textos, "agente", MODELO, chamar=chamar, workers=1)
    out = pd.DataFrame(linhas, columns=["processo", "sei_doc_id", "model_id", "prompt_version", "extraction_json"])
    out.to_parquet(RELATOR / "extractions.parquet", index=False)
    print(f"extractions={len(out)} (stub={int((out.model_id == 'stub').sum())})")
    for e in erros:
        print("ERRO", e)


def fichas():
    import fichas_trabalho as ft

    def chamar(modelo, usuario, chave):
        sid = re.search(r"Documento SEI (\S+) ·", usuario).group(1)
        return _resposta("ficha", sid), {}

    ft.chamar = chamar
    sys.argv = ["fichas_trabalho.py", "--modelo", MODELO, "--workers", "1"]
    ft.main()


if __name__ == "__main__":
    {"preparar": preparar, "extracao": extracao, "fichas": fichas}[sys.argv[1]]()
