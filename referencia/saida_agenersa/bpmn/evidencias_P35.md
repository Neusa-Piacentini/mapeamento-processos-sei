# Evidências — P35 Gestão de interrupções e crises de abastecimento

Processos SEI na carteira com este código: 20 (12 nativos do SEI). Casos do piloto: SEI-220007/002039/2022 (típico), SEI-220007/000992/2022 (crítico).

## Participação das unidades (todos os processos do código)

| Unidade | Processos em que juntou documento (%) | Posse mediana por passagem (du) | Posse total (du, nativos) |
|---|---|---|---|
| SCEXEC | 100 | 2 | 1649 |
| CONS-02 | 95 | 13 | 3634 |
| PROC | 95 | 9 | 1052 |
| CASAN | 60 | 6 | 1540 |
| CAPET | 45 | 0 | 315 |
| CAENE | 25 | 1 | 464 |
| CONS-05 | 25 | 8 | 752 |
| PRESI | 20 | 1 | 11 |
| PROT | 15 | 0 | 0 |
| CONS-04 | 10 | 26 | 946 |
| OUVI | 10 | 0 | 154 |
| ASSINF | 5 | 0 | 0 |

## Transições entre unidades ativas, sem a Secretaria (todos os processos)

CONS-02 → PROC: 29; PROC → CONS-02: 29; CASAN → CONS-02: 14; CONS-02 → CASAN: 9; CONS-02 → CAENE: 7; CONS-05 → PROC: 6; CAENE → CONS-02: 6; CONS-02 → CONS-02: 6; CAPET → CONS-02: 5; PROC → CASAN: 5; PROC → CONS-05: 4; CASAN → PROC: 4; CASAN → CASAN: 4; CAPET → PROC: 4; PROC → PRESI: 4

Retornos a unidade já visitada (média): 6.5; ofícios por processo (mediana): 5; vistas/razões finais (mediana): 2; aguardando terceiros (du, mediana): 74; lead time nativos (du, mediana): 930; com deliberação: 65%.

## Caso típico: SEI-220007/002039/2022

PLANO DE CONTINGÊNCIA 2023 E 2024

| # | Unidade | Tarefa (da ficha) | Natureza | du na passagem | Espera até 1ª juntada | Horas (teto) | Horas (piso) | Sinais de perda | Espera dominante |
|---|---|---|---|---|---|---|---|---|---|
| 1 | SCEXEC | Anexo | juntada | 4 | 0 | 0.6 | 0.6 |  |  |
| 2 | CAENE | E-mail | comunicacao | 13 | 9 | 7.0 | 7.0 |  |  |
| 3 | CHEGAB | Restituir processo à Secretaria Executiva | encaminhamento | 1 | 1 | 0.1 | 0.1 |  |  |
| 4 | SCEXEC | Notificar regulada sobre autuação de processo | comunicacao | 0 | 0 | 1.5 | 0.8 |  |  |
| 5 | SCEXEC | Encaminhar processo para análise jurídica da Procuradoria | encaminhamento | 0 | 0 | 0.1 | 0.1 |  |  |
| 6 | PROC | Despacho de Encaminhamento de Processo | tramitacao | 46 | 46 | 0.1 | 0.1 |  | sim |
| 7 | SCEXEC | Notificar concessionária sobre prazo para manifestação | comunicacao | 0 | 0 | 1.7 | 0.8 | prazo_concedido |  |
| 8 | SCEXEC | Encaminhar processo à Procuradoria | encaminhamento | 0 | 0 | 0.1 | 0.1 |  |  |
| 9 | PROC | Parecer 218 | analise | 26 | 26 | 6.0 | 6.0 |  | sim |
| 10 | CAENE | Despacho de Encaminhamento de Processo | tramitacao | 0 | 0 | 0.1 | 0.1 |  |  |
| 11 | SCEXEC | Encaminhar processo para ciência da CAENE | encaminhamento | 3 | 0 | 0.1 | 0.1 |  |  |
| 12 | SCEXEC | Encaminhar processo por prevenção ao relator designado | encaminhamento | 18 | 18 | 0.4 | 0.2 |  |  |
| 13 | CONS-02 | Relatar processo sobre Plano de Contingência | relatoria_decisao | 99 | 72 | 23.4 | 6.8 | prazo_concedido | sim |
| 14 | SCEXEC | Notificar concessionária sobre aprovação de Plano de Contingência | comunicacao | 2 | 0 | 1.5 | 0.8 | prazo_concedido |  |
| 15 | CAENE | Devolver processo à SECEX após ciência | encaminhamento | 1 | 1 | 0.1 | 0.1 |  |  |
| 16 | SCEXEC | Informar providências adotadas para cumprimento de deliberação | comunicacao | 0 | 0 | 2.6 | 0.8 |  |  |

Peças de maior complexidade: Relatório (CONS-02, 3 laudas, complexidade 3); Voto 13 (CONS-02, 4 laudas, complexidade 3)

## Caso crítico: SEI-220007/000992/2022

ROMPIMENTO DE ADUTORA EM NOVA IGUAÇU – ESQUINA ENTRE A RUA SANTA JOANA E ALAMEDA TOMÉ – 26/03/2022

| # | Unidade | Tarefa (da ficha) | Natureza | du na passagem | Espera até 1ª juntada | Horas (teto) | Horas (piso) | Sinais de perda | Espera dominante |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CASAN | Realizar vistoria técnica e elaborar relatório de fiscalização | fiscalizacao_campo | 33 | 0 | 17.6 | 9.7 | diligencia_externa; prazo_concedido |  |
| 2 | CASAN | Analisar justificativa e plano de ação sobre rompimento de adutora | analise_tecnica_engenharia | 153 | 0 | 9.1 | 3.5 |  | sim |
| 3 | SCEXEC | Encaminhar processo à Procuradoria para manifestação | encaminhamento | 1 | 1 | 0.1 | 0.1 |  |  |
| 4 | PROC | Analisar descumprimento contratual e orientar instrução regulatória | analise_juridica | 11 | 11 | 10.6 | 4.0 | aguardando_outra_unidade |  |
| 5 | SCEXEC | Encaminhar processo à CASAN para esclarecimentos | encaminhamento | 0 | 0 | 0.4 | 0.2 | aguardando_outra_unidade |  |
| 6 | CASAN | Analisar descumprimento contratual e impactos do desabastecimento | analise_tecnica_engenharia | 15 | 15 | 7.6 | 4.0 |  |  |
| 7 | SCEXEC | Encaminhar processo à CAPET para análise econômico-financeira | encaminhamento | 4 | 4 | 0.6 | 0.2 |  |  |
| 8 | CAPET | Analisar despesas de sinistro e classificar no OPEX | analise_economico_financeira | 235 | 1 | 20.0 | 14.7 | pedido_complementacao; prazo_concedido; reiteracao | sim |
| 9 | SCEXEC | Notificar concessionária sobre despacho e solicitar manifestação | comunicacao | 1 | 0 | 1.3 | 0.3 | prazo_concedido |  |
| 10 | SCEXEC | Reiterar ofício e solicitar manifestação à concessionária | comunicacao | 0 | 0 | 1.3 | 0.6 | prazo_concedido; reiteracao |  |
| 11 | SCEXEC | Reiterar solicitação de manifestação à concessionária | comunicacao | 1 | 0 | 1.6 | 0.7 | prazo_concedido; reiteracao |  |
| 12 | SCEXEC | Juntar Carta RIO4.JRG.2024.000044 | juntada | 1 | 0 | 0.2 | 0.2 |  |  |
| 13 | SCEXEC | Encaminhar autos ao gabinete do conselheiro relator | encaminhamento | 0 | 0 | 0.4 | 0.2 |  |  |
| 14 | CONS-02 | Encaminhar processo à Procuradoria para manifestação | encaminhamento | 17 | 17 | 0.1 | 0.2 |  |  |
| 15 | PROC | Analisar descumprimento contratual e recomendar aplicação de penalidade | analise_juridica | 9 | 9 | 18.2 | 4.0 |  |  |
| 16 | CONS-02 | Notificar concessionária para apresentar Razões Finais | comunicacao | 3 | 3 | 1.7 | 0.8 | prazo_concedido |  |
| 17 | CONS-02 | Relatar processo sobre rompimento de adutora | relatoria_decisao | 31 | 0 | 38.6 | 11.8 |  |  |
| 18 | SCEXEC | Juntar Deliberação | decisao | 0 | 0 | 0.1 | 0.1 |  |  |
| 19 | PROC | Analisar embargos de declaração e sugerir devolução de prazo | analise_juridica | 12 | 11 | 6.3 | 3.0 | prazo_concedido |  |
| 20 | CONS-02 | Notificar concessionária para ratificar ou substituir embargos | comunicacao | 0 | 0 | 1.8 | 0.8 | prazo_concedido |  |
| 21 | CONS-02 | Encaminhar processo à Procuradoria para manifestação | encaminhamento | 0 | 0 | 0.6 | 0.5 |  |  |
| 22 | PROC | Analisar embargos de declaração e recomendar improvimento | analise_juridica | 6 | 5 | 16.1 | 4.0 |  |  |
| 23 | CONS-02 | Notificar concessionária para apresentar razões finais | comunicacao | 8 | 8 | 1.2 | 0.8 | prazo_concedido |  |
| 24 | CONS-02 | Juntar Carta RIO4.JRG.2024.000506 | juntada | 0 | 0 | 0.2 | 0.2 |  |  |
| 25 | CONS-02 | Analisar embargos de declaração e propor voto ao Conselho Diretor | relatoria_decisao | 25 | 0 | 19.4 | 6.0 |  |  |
| 26 | SCEXEC | Juntar Publicação Deliberacao AGENERSA 4868 | comunicacao | 0 | 0 | 0.1 | 0.1 |  |  |
| 27 | SCEXEC | Notificar concessionária sobre decisão de embargos de declaração | comunicacao | 0 | 0 | 1.8 | 0.8 |  |  |
| 28 | CASAN | Registrar ciência e encaminhar processo à SECEX | encaminhamento | 0 | 0 | 0.4 | 0.1 |  |  |
| 29 | SCEXEC | Encaminhar processo à CASAN para ciência e anotações | encaminhamento | 1 | 0 | 2.3 | 1.0 |  |  |
| 30 | CONS-02 | Conceder vista dos autos e notificar concessionária | comunicacao | 37 | 0 | 1.7 | 0.8 | prazo_concedido | sim |

Peças de maior complexidade: Relatório (CONS-02, 14 laudas, complexidade 4); Parecer 282 (PROC, 20 laudas, complexidade 4); Parecer 452 (PROC, 20 laudas, complexidade 3); Voto 21 (CONS-02, 8 laudas, complexidade 4); Relatório de Fiscalização (CASAN, 3 laudas, complexidade 3); Parecer 11 (PROC, 12 laudas, complexidade 3); Voto 5 (CONS-02, 5 laudas, complexidade 3); Parecer 211 (CASAN, 5 laudas, complexidade 3)
