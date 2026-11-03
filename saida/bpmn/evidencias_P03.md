# Evidências — P03 Reequilíbrio econômico-financeiro e aditivos contratuais

Processos SEI na carteira com este código: 6 (6 nativos do SEI). Casos do piloto: SEI-220007/001749/2022 (típico).

## Participação das unidades (todos os processos do código)

| Unidade | Processos em que juntou documento (%) | Posse mediana por passagem (du) | Posse total (du, nativos) |
|---|---|---|---|
| CONS-02 | 100 | 55 | 3426 |
| PROC | 100 | 11 | 623 |
| SCEXEC | 100 | 3 | 1428 |
| CAPET | 67 | 2 | 389 |
| CASAN | 67 | 1 | 225 |
| CONS-01 | 50 | 8 | 626 |
| CONS-04 | 33 | 16 | 1272 |
| CAENE | 17 | 2 | 13 |
| CHEGAB | 17 | 0 | 1 |

## Transições entre unidades ativas, sem a Secretaria (todos os processos)

CONS-02 → CAPET: 8; PROC → CONS-02: 6; CAPET → CONS-02: 5; CAPET → PROC: 4; CASAN → PROC: 3; CONS-01 → CONS-02: 2; CONS-02 → CONS-02: 2; CONS-02 → CASAN: 2; CONS-04 → CASAN: 2; PROC → CAENE: 1; CAENE → CAPET: 1; PROC → CHEGAB: 1; CHEGAB → CAPET: 1; CAPET → CONS-01: 1; CONS-01 → CAENE: 1

Retornos a unidade já visitada (média): 4.7; ofícios por processo (mediana): 4; vistas/razões finais (mediana): 1; aguardando terceiros (du, mediana): 318; lead time nativos (du, mediana): 1330; com deliberação: 100%.

## Caso típico: SEI-220007/001749/2022

REEQUILÍBRIO ECONÔMICO-FINANCEIRO DA CONCESSÃO

| # | Unidade | Tarefa (da ficha) | Natureza | du na passagem | Espera até 1ª juntada | Horas (teto) | Horas (piso) | Sinais de perda | Espera dominante |
|---|---|---|---|---|---|---|---|---|---|
| 1 | SCEXEC | Autuar processo e encaminhar para a CAPET | encaminhamento | 0 | 0 | 1.7 | 0.8 |  |  |
| 2 | CAPET | Analisar pleito de reequilíbrio econômico-financeiro e aditivos | analise_economico_financeira | 162 | 1 | 38.6 | 27.1 | diligencia_externa; pedido_complementacao; prazo_concedido | sim |
| 3 | SCEXEC | Juntar Anexo | juntada | 0 | 0 | 0.1 | 0.1 |  |  |
| 4 | CONS-02 | Restituir processo à SECEX após juntada | encaminhamento | 50 | 50 | 0.1 | 0.2 |  | sim |
| 5 | CAPET | Analisar pleito de reequilíbrio econômico-financeiro e estudos | analise_economico_financeira | 0 | 0 | 27.9 | 20.2 | pedido_complementacao; refazimento |  |
| 6 | SCEXEC | Notificar concessionária sobre parecer e conceder acesso | comunicacao | 16 | 0 | 2.1 | 1.1 | prazo_concedido |  |
| 7 | CAPET | Analisar pleito de reequilíbrio econômico-financeiro e modelar fluxos de caixa | analise_economico_financeira | 10 | 10 | 13.4 | 12.0 | diligencia_externa |  |
| 8 | SCEXEC | Encaminhar processo à Procuradoria Geral para parecer | encaminhamento | 7 | 7 | 0.1 | 0.1 |  |  |
| 9 | PROC | Devolver processo para conclusão da instrução técnica | encaminhamento | 180 | 179 | 0.7 | 0.5 | aguardando_outra_unidade | sim |
| 10 | SCEXEC | Encaminhar processo ao Gabinete do Conselheiro Relator | encaminhamento | 0 | 0 | 0.2 | 0.3 |  |  |
| 11 | CONS-02 | Encaminhar processo para análise da CAPET | encaminhamento | 25 | 25 | 0.4 | 0.1 |  | sim |
| 12 | CAPET | Solicitar informações complementares para reequilíbrio econômico-financeiro | comunicacao | 82 | 5 | 3.4 | 3.2 | pedido_complementacao; prazo_concedido | sim |
| 13 | CONS-02 | Solicitar esclarecimentos e documentos à Prefeitura e Concessionária | comunicacao | 109 | 4 | 2.1 | 1.6 | diligencia_externa; prazo_concedido | sim |
| 14 | SCEXEC | Encaminhar autos ao gabinete do Conselheiro Relator | encaminhamento | 1 | 1 | 0.1 | 0.1 |  |  |
| 15 | CAPET | Analisar pleito de reequilíbrio e recalcular TIR | analise_economico_financeira | 48 | 48 | 62.0 | 40.1 |  |  |
| 16 | CONS-02 | Solicitar informações e documentos à concessionária | comunicacao | 64 | 28 | 10.6 | 6.5 | diligencia_externa; pedido_complementacao; prazo_concedido | sim |
| 17 | CAPET | Analisar revisão extraordinária e propor cenários de reequilíbrio | analise_economico_financeira | 8 | 1 | 71.6 | 26.6 | pedido_complementacao; prazo_concedido |  |
| 18 | CONS-02 | Encaminhar processo à CASAN para manifestação | encaminhamento | 1 | 0 | 0.1 | 0.1 |  |  |
| 19 | CASAN | Informar ausência de escopo técnico e devolver processo | encaminhamento | 14 | 14 | 0.6 | 0.5 |  |  |
| 20 | CONS-02 | Encaminhar processo à Procuradoria para análise jurídica | encaminhamento | 0 | 0 | 0.1 | 0.1 |  |  |
| 21 | PROC | Analisar viabilidade jurídica de reequilíbrio e prorrogação contratual | analise_juridica | 25 | 25 | 42.0 | 12.0 |  |  |
| 22 | CONS-02 | Notificar partes para apresentação de Razões Finais | comunicacao | 25 | 0 | 2.2 | 1.1 | aguardando_outra_unidade; prazo_concedido | sim |
| 23 | CAPET | Analisar reequilíbrio econômico-financeiro e modelar cenários tarifários | analise_economico_financeira | 1 | 1 | 67.8 | 33.6 |  |  |
| 24 | CONS-02 | Votar pleito de reequilíbrio econômico-financeiro da concessão | relatoria_decisao | 84 | 0 | 98.8 | 35.6 | aguardando_outra_unidade; prazo_concedido |  |
| 25 | SCEXEC | Juntar Publicação 13_12_2024 Deliberação 4830__31 | comunicacao | 0 | 0 | 0.1 | 0.1 |  |  |
| 26 | SCEXEC | Juntar Termo | juntada | 26 | 5 | 0.1 | 0.1 |  | sim |
| 27 | CAPET | Encaminhar processo à SECEX para ciência | encaminhamento | 0 | 0 | 0.1 | 0.1 |  |  |
| 28 | CASAN | Encaminhar processo para a SECEX | encaminhamento | 1 | 1 | 0.1 | 0.1 |  |  |
| 29 | SCEXEC | Encaminhar deliberação à CAPET e CASAN | encaminhamento | 0 | 0 | 0.4 | 0.5 |  |  |
| 30 | SCEXEC | Encerrar processo de reequilíbrio econômico-financeiro | publicacao_registro | 0 | 0 | 2.3 | 1.0 |  |  |

Peças de maior complexidade: Relatório (CAPET, 60 laudas, complexidade 5); Relatório (CAPET, 53 laudas, complexidade 5); Relatório Técnico (CAPET, 47 laudas, complexidade 5); Voto 46 (CONS-02, 57 laudas, complexidade 5); Parecer 497 (PROC, 53 laudas, complexidade 4); Relatório (CONS-02, 51 laudas, complexidade 4); Parecer 38 (CAPET, 27 laudas, complexidade 4); Parecer 20 (CAPET, 27 laudas, complexidade 4)
