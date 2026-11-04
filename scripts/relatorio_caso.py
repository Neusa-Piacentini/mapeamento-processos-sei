"""Relatório consolidado de um estudo de caso único (um processo SEI, um código do catálogo), das fases 0 a 4.

Junta as saídas já validadas pelos portões (trilha, fichas, auditorias, modelo, avaliação carimbada, conformidade,
TO-BE simulado, controles e priorização) num documento único. Todo número vem dos arquivos de saida/; o texto só
descreve. Uso: python relatorio_caso.py P06 → docs/RELATORIO_CASO_<cod>.md"""
from __future__ import annotations

import json
import sys

import pandas as pd

from comum import RAIZ, SAIDA


def _j(p):
    return json.loads((SAIDA / p).read_text(encoding="utf-8"))


def br(x, casas=1):
    return f"{x:,.{casas}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def main(cod: str):
    pil = pd.read_csv(SAIDA / "piloto.csv").iloc[0]
    ind = pd.read_csv(SAIDA / "processos_indicadores.csv").set_index("numero").loc[pil.numero]
    est = pd.read_csv(SAIDA / "estadias.csv")
    fatos = {f["id"]: f for f in _j(f"bpmn/fatos_{cod}.json")["fatos"]}
    F = lambda k: fatos[k]["valor"]  # noqa: E731
    mod, ava = _j(f"bpmn/modelo_{cod}.json"), _j(f"bpmn/avaliacao_{cod}.json")
    vin = _j(f"bpmn/vinculos_{cod}.json")["atividades"]
    aud_auto, aud_f = _j("auditoria/auditoria_automatica.json"), _j("auditoria/auditoria_fichas.json")
    ver = _j(f"auditoria/verificacao_avaliacao_{cod}.json")["resumo"]
    nor, conf = _j(f"fase3/normas_{cod}.json"), _j(f"fase3/conformidade_{cod}.json")
    mel, res, ctl = _j(f"fase3/melhorias_{cod}.json"), _j(f"fase3/resultado_tobe_{cod}.json"), _j(f"fase3/controles_{cod}.json")
    mat = _j("fase4/matriz_automacao.json")["codigos"][0]
    tarefas = [e for e in mod["elementos"] if e["tipo"] == "tarefa"]
    md = [f"# Mapeamento do processo {pil.numero}", "",
          f"Estudo de caso único da metodologia do curso, aplicada ao processo **{pil.numero}** "
          f"({ind.tipo}; interessada: {ind.interessado}), classificado como **{cod} — {pil.nome_processo}**. "
          f"Fonte: Pesquisa Pública do SEI-RJ. Gerado por `scripts/relatorio_caso.py` a partir das saídas validadas.", "",
          "> **Ressalvas.** Um caso só: medianas são o próprio caso, nada aqui é padrão do tipo de processo. Horas de "
          "trabalho são estimativa por peça (hipótese, a calibrar com os servidores). O volume anual do tipo não foi "
          "medido, então não há totais anuais, FTE nem R$. As paradas de validação humana do roteiro estão pendentes.", "",
          "## 1. Base e trilha (fase 0)", "",
          f"| Indicador | Valor |", "|---|---|",
          f"| Gerado em | {ind.data_geracao} |", f"| Último andamento (corte) | {ind.ultimo_andamento} |",
          f"| Situação | {'encerrado' if ind.encerrado else 'aberto (sobrestado no último andamento)'} |",
          f"| Lead time | {br(F('critico.lead'), 0)} du ({ind.lead_dias} dias corridos) |",
          f"| Documentos / processos anexados | {ind.n_docs} / {ind.n_processos_relacionados} |",
          f"| Relatórios de fiscalização / pareceres / ofícios | {ind.n_relatorios} / {ind.n_pareceres} / {ind.n_oficios} |",
          f"| Sequência de unidades ativas | {ind.sequencia_ativa} |",
          f"| Espera entre atividades / execução | {br(F('critico.espera_total'), 0)} du / "
          f"{br(F('critico.lead') - F('critico.espera_total'), 0)} du |",
          f"| Espera de resposta da concessionária (confirmada) | {br(F('critico.terceiros'), 0)} du |",
          f"| Indeterminado (não separável de processo parado) | {br(F('critico.indeterminado'), 0)} du |", "",
          "Posse por unidade (du): " + "; ".join(f"{k.split('.')[-1]} {br(v['valor'], 0)}" for k, v in sorted(fatos.items())
                                                  if k.startswith("critico.posse.")) + ".", "",
          f"Estadias: {len(est)} ({int((est.perfil != 'passagem').sum())} com trabalho). Tabelas: `saida/estadias.csv`, "
          "`posse.csv`, `documentos.csv`, `janelas_terceiros.csv`, `processos_indicadores.csv`.", "",
          "## 2. Conteúdo, esforço e modelo (fase 1)", "",
          f"- Fichas de trabalho: {sum(1 for _ in open(SAIDA / 'fichas_trabalho.jsonl', encoding='utf-8'))} peças "
          f"próprias da agência (`saida/fichas_trabalho.jsonl`), evidência ancorada literalmente no texto.",
          f"- Auditoria automática: números sem âncora nas fichas {br(aud_auto['B_fichas']['pct_sem_ancora'])}% "
          f"(critério ≤ 1%); posse sem lacuna nem sobreposição "
          f"({aud_auto['A_trilha']['posse_com_lacuna_ou_sobreposicao']} casos com problema).",
          f"- Auditoria às cegas de {aud_f['amostra']} fichas ({aud_f['contagem_da_lista']['total']} afirmações): sem lastro "
          f"ou contradita {br(aud_f['pct_sem_lastro_ou_contradita'], 2)}% (≤ 2%), imprecisa {br(aud_f['pct_imprecisa'], 2)}% (≤ 10%).",
          f"- Trabalho estimado no caso: {br(F('critico.horas_piso'))}–{br(F('critico.horas_teto'))} h (hipótese).", "",
          f"**Modelo BPMN AS-IS** (`saida/bpmn/{cod}.bpmn`, visualizador em `docs/bpmn/index.html`): "
          f"{len(mod['elementos'])} elementos, raias {', '.join(r['id'] for r in mod['raias'])}.", "",
          "| Tarefa | Raia | Peças vinculadas | Gatilho → saída |", "|---|---|---|---|"]
    md += [f"| {t['id']} {t['nome']} | {t['raia']} | {len(vin.get(t['id'], {}).get('docs', []))} | "
           f"{t['gatilho']} → {t['saida']} |" for t in tarefas]
    md += ["", "## 3. Avaliação AS-IS", "", ava["sintese"], "", f"**Gargalo.** {ava['gargalo']['onde']}", "",
           ava["gargalo"]["evidencia"], "", "| Desperdício | Severidade | Evidência |", "|---|---|---|"]
    md += [f"| {d['tipo']} | {d['severidade']} | {d['evidencia']} |" for d in ava["desperdicios"]]
    md += ["", "| Oportunidade | Categoria | Impacto | Esforço |", "|---|---|---|---|"]
    md += [f"| {o['titulo']} | {o['categoria']} | {o['impacto']} | {o['esforco']} |" for o in ava["oportunidades"]]
    md += ["", f"Verificação independente da avaliação: {ver['total']} afirmações, {ver['correta']} corretas, "
               f"{ver['imprecisa']} imprecisas (corrigidas antes do carimbo), {ver['alucinacao']} alucinações. "
               f"Avaliação carimbada contra os fatos ({ava['validado_contra']['fatos_sha']}).", "",
           "## 4. Conformidade legal (fase 3)", "", "| Requisito | Exigência | Teste | Resultado |", "|---|---|---|---|"]
    for rid, r in conf["requisitos"].items():
        resultado = "manual (não computado)" if r["tipo"] == "manual" else f"{br(r['pct_conforme'], 0)}% conforme"
        md.append(f"| {rid} | {r['exigencia']} | {r['tipo']} | {resultado} |")
    ext = [n for n in nor["normas"] if n["fonte"].get("base") == "externa"]
    md += ["", f"Normas: {len(nor['normas'])} ({len(ext)} de fonte externa, a conferir à mão: "
               + "; ".join(f"{n['norma']} {n['dispositivo']}" for n in ext) + "). Trechos literais conferidos por "
               "`verificar_normas.py`. Interpretações a validar com a Procuradoria em `normas_P06.json` → `interpretacao`.",
           "", "## 5. TO-BE e simulação (fase 3)", "",
           "| Melhoria | Fase | Título | Hipótese |", "|---|---|---|---|"]
    md += [f"| {m['id']} | {m['fase']} | {m['titulo']} | {'sim' if m.get('hipotese') else 'não'} |" for m in mel["melhorias"]]
    lb = res["linha_base"]
    md += ["", "| Fase | Lead (du), conservador / esperado / otimista | Horas piso–teto (esperado) | Ganho de lead (esperado) |",
           "|---|---|---|---|",
           f"| AS-IS | {br(lb['lead']['mediana'], 0)} | {br(lb['horas_piso']['mediana'])}–{br(lb['horas_teto']['mediana'])} | — |"]
    for f, x in res["fases"].items():
        md.append(f"| {f} | " + " / ".join(br(x[c]["lead"]["mediana"], 0) for c in ("conservador", "esperado", "otimista"))
                  + f" | {br(x['esperado']['horas_piso']['mediana'])}–{br(x['esperado']['horas_teto']['mediana'])} | "
                  f"{br(x['esperado']['ganho_lead_mediano_pct'])}% |")
    sens = sorted(res["sensibilidade"]["sem_cada_melhoria"], key=lambda s: -s["lead_mediano_du"])[:3]
    md += ["", "Maior peso na sensibilidade (piora do lead mediano sem a melhoria, fase 3, esperado): "
           + "; ".join(f"{s['melhoria']} +{br(s['lead_mediano_du'], 0)} du" for s in sens)
           + ". São as que mais precisam de validação com a unidade dona (PARADA 8).", "",
           "## 6. Controles e metas", "", "| Indicador | Linha de base | Metas por fase |", "|---|---|---|"]
    for i in ctl["indicadores"]:
        lbv = i["linha_base"]
        md.append(f"| {i['id']} {i['nome']} | {lbv['valor']} {lbv.get('unidade', '')} | "
                  + "; ".join(f"f{m['fase']}: {m['valor']} ({m['origem']['tipo']})" for m in i["metas"]) + " |")
    md += ["", f"Controles de qualidade da IA: {', '.join(q['id'] for q in ctl['controles_qualidade_ia'])}. "
               f"Auditoria contínua: {', '.join(ctl['auditoria_continua'])}.", "",
           "## 7. Priorização da automação (fase 4)", "",
           f"Prioridade na matriz: **{mat['prioridade']}** — com um caso e sem volume medido, os portões "
           f"{', '.join(k for k, v in mat['portoes'].items() if not v)} não passam. Capacidades de IA aplicáveis: "
           f"{', '.join(mat['capacidades'])}. A escolha do piloto do sistema é da gestão (PARADA 10).", "",
           "## 8. Perguntas de validação (paradas pendentes)", ""]
    md += [f"{k}. {p}" for k, p in enumerate(ava["perguntas_validacao"], 1)]
    md += ["", "## 9. Mapa das saídas", "",
           "| Fase | Arquivos |", "|---|---|",
           "| 0 | `saida/estadias.csv`, `posse.csv`, `documentos.csv`, `janelas_terceiros.csv`, `processos_indicadores.csv`, `classificacao_processos.csv`, `Mapeamento_SEI_Fase0.xlsx` |",
           "| 1 | `saida/fichas_trabalho.{csv,jsonl}`, `esforco_documentos.csv`, `Mapeamento_SEI_Piloto.xlsx`, `bpmn/{evidencias,modelo,vinculos,fatos,fichas,avaliacao}_P06.*`, `bpmn/P06.bpmn`, `docs/ASIS_PILOTO.md`, `docs/AVALIACAO_ASIS.md` |",
           "| 2 | `saida/coorte_fase2.csv`, `fase2/{atribuicoes,procedimento,casos}_P06.*`, `docs/RESULTADOS_FASE2.md` |",
           "| 3 | `saida/fase3/{normas,conformidade,linha_base,insumo_tobe,melhorias,resultado_tobe,controles}_P06.*`, `fase3/benchmark/`, `docs/BENCHMARKING.md` |",
           "| 4 | `saida/fase4/matriz_automacao.*`, `capacidades_transversais.csv`, `Priorizacao_Automacao.xlsx`, `docs/PRIORIZACAO_AUTOMACAO.md` |",
           "| Auditoria | `saida/auditoria/auditoria_automatica.json`, `auditoria_fichas.json`, `verificacao_avaliacao_P06.json`, `saida/pipeline_execucao.json` |",
           "| Site | `docs/site/index.html` |", ""]
    arq = RAIZ / "docs" / f"RELATORIO_CASO_{cod}.md"
    arq.write_text("\n".join(md), encoding="utf-8")
    print(arq)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "P06")
