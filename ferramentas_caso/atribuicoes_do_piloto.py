"""Atribuições peça → atividade (saida/fase2/atribuicoes_<cod>.csv) a partir dos vínculos do piloto
(saida/bpmn/vinculos_<cod>.json), para coorte formada só pelo(s) caso(s)-piloto. Os vínculos são o gabarito do
classificador de atividade (scripts/classificar_atividades.py); com coorte = piloto não há peça a classificar fora
dele, então o rótulo é o próprio vínculo. Peça própria sem vínculo = fora_do_modelo. Mesmo esquema de colunas."""
import json, sys
from pathlib import Path
import pandas as pd
RAIZ = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(RAIZ / "scripts"))
from comum import ORGAO, SAIDA, documentos

coorte = pd.read_csv(SAIDA / "coorte_fase2.csv")
docs = documentos()
for cod, g in coorte.groupby("processo_principal"):
    vin = json.loads((SAIDA / "bpmn" / f"vinculos_{cod}.json").read_text(encoding="utf-8"))["atividades"]
    rot = {r: t for t, a in vin.items() for r in a.get("docs", [])}
    d = docs[docs.numero_processo.isin(g.numero) & docs.unidade.str.startswith(ORGAO, na=False)
             & (docs.categoria != "processo_relacionado")].copy()
    d["ref"] = d.numero_processo + ":" + d.numero.astype(str)
    d["atividade"] = d.ref.map(rot).fillna("fora_do_modelo")
    out = pd.DataFrame(dict(codigo=cod, processo=d.numero_processo, ref=d.ref, unidade=d.unidade, tipo=d.tipo,
                            atividade=d.atividade, confianca="gabarito",
                            motivo=["vínculo do piloto (saida/bpmn/vinculos)" if a != "fora_do_modelo" else "peça sem vínculo no piloto" for a in d.atividade]))
    (SAIDA / "fase2").mkdir(exist_ok=True)
    out.sort_values("ref").to_csv(SAIDA / "fase2" / f"atribuicoes_{cod}.csv", index=False, encoding="utf-8-sig")
    print(cod, len(out), "peças;", out.atividade.value_counts().to_dict())
