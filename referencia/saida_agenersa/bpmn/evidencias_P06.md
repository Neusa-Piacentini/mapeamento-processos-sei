# Evidências — P06 Fiscalização técnica de campo (programada e por demanda)

Processos SEI na carteira com este código: 32 (14 nativos do SEI). Casos do piloto: SEI-480002/007520/2025 (típico), SEI-480002/005546/2024 (crítico).

## Participação das unidades (todos os processos do código)

| Unidade | Processos em que juntou documento (%) | Posse mediana por passagem (du) | Posse total (du, nativos) |
|---|---|---|---|
| SCEXEC | 100 | 6 | 1809 |
| CONS-02 | 81 | 10 | 1786 |
| PROC | 75 | 23 | 1835 |
| CAENE | 66 | 4 | 1184 |
| CASAN | 22 | 4 | 199 |
| CONS-05 | 12 | 0 | 0 |
| CAPET | 9 | 0 | 8 |
| CONS-04 | 9 | nan | 0 |
| CONS-01 | 6 | 0 | 0 |
| ASSINF | 3 | 1 | 5 |
| CHEGAB | 3 | 0 | 1 |
| CONS-03 | 3 | 3 | 37 |

## Transições entre unidades ativas, sem a Secretaria (todos os processos)

PROC → CONS-02: 33; CONS-02 → PROC: 23; CAENE → PROC: 16; CONS-02 → CASAN: 11; CONS-02 → CAENE: 11; CASAN → CONS-02: 10; CAENE → CONS-02: 9; PROC → CAENE: 6; CONS-02 → CONS-02: 6; CAENE → CAENE: 6; CASAN → PROC: 4; CONS-05 → PROC: 3; CAENE → CONS-01: 3; CONS-01 → PROC: 3; CASAN → CASAN: 3

Retornos a unidade já visitada (média): 3.9; ofícios por processo (mediana): 3; vistas/razões finais (mediana): 1; aguardando terceiros (du, mediana): 0; lead time nativos (du, mediana): 388; com deliberação: 56%.

## Caso típico: SEI-480002/007520/2025

RELATÓRIO DE FISCALIZAÇÃO P-125/25 E TERMO DE NOTIFICAÇÃO 018/2025\n\n\nBombeiros não emitem certidão

| # | Unidade | Tarefa (da ficha) | Natureza | du na passagem | Espera até 1ª juntada | Horas (teto) | Horas (piso) | Sinais de perda | Espera dominante |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAENE | Realizar fiscalização de campo e emitir relatório | fiscalizacao_campo | 10 | 0 | 33.4 | 12.8 | prazo_concedido |  |
| 2 | SCEXEC | Encaminhar processo à Procuradoria para manifestação | encaminhamento | 32 | 32 | 0.6 | 0.2 |  | sim |
| 3 | PROC | Analisar processo sancionatório e emitir parecer jurídico | analise_juridica | 24 | 24 | 13.0 | 4.5 |  |  |
| 4 | SCEXEC | Encaminhar processo ao gabinete de conselheiro relator | encaminhamento | 23 | 23 | 0.1 | 0.1 |  | sim |
| 5 | CONS-02 | Notificar concessionária para apresentação de razões finais | comunicacao | 8 | 8 | 1.5 | 0.8 | prazo_concedido |  |
| 6 | CONS-02 | Relatar fiscalização e propor diligência ao CBMERJ | relatoria_decisao | 7 | 0 | 25.4 | 8.5 | diligencia_externa; prazo_concedido |  |
| 7 | SCEXEC | Solicitar ao CBMERJ informações sobre regularização documental | comunicacao | 2 | 0 | 3.9 | 2.4 | diligencia_externa; prazo_concedido |  |
| 8 | CAENE | Devolver processo à SECEX após ciência de deliberação | encaminhamento | 0 | 0 | 0.4 | 0.1 |  |  |
| 9 | SCEXEC | Registrar providências adotadas em cumprimento a Deliberação | instrucao_processual | 0 | 0 | 2.4 | 1.0 |  |  |

Peças de maior complexidade: Relatório de Fiscalização (CAENE, 7 laudas, complexidade 3); Parecer 735 (PROC, 13 laudas, complexidade 3); Voto 31 (CONS-02, 8 laudas, complexidade 4); Relatório (CONS-02, 5 laudas, complexidade 3); Parecer 83 (CAENE, 6 laudas, complexidade 3)

## Caso crítico: SEI-480002/005546/2024

FISCALIZAÇÃO CAENE - ESTAÇÃO DE REGULAGEM E MEDIÇÃO - SANTA CRUZ

| # | Unidade | Tarefa (da ficha) | Natureza | du na passagem | Espera até 1ª juntada | Horas (teto) | Horas (piso) | Sinais de perda | Espera dominante |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAENE | Realizar vistoria em ERM e elaborar relatório de fiscalização | fiscalizacao_campo | 32 | 0 | 20.1 | 11.8 | diligencia_externa; pedido_complementacao; prazo_concedido |  |
| 2 | SCEXEC | E-mail | comunicacao | 0 | 0 | 0.2 | 0.2 |  |  |
| 3 | INEA/PRESI | Despacho de Encaminhamento de Processo | tramitacao | 0 | 0 | 0.1 | 0.1 |  |  |
| 4 | INEA/DIRLAM | Despacho de Encaminhamento de Processo | tramitacao | 1 | 1 | 0.1 | 0.1 |  |  |
| 5 | INEA/SERVARAT | Manifestação 1146 | juntada | 2 | 2 | 0.2 | 0.2 |  |  |
| 6 | INEA/GERLRAC | Despacho de Encaminhamento de Processo | tramitacao | 1 | 1 | 0.1 | 0.1 |  |  |
| 7 | INEA/DIRLAM | Despacho de Encaminhamento de Processo | tramitacao | 0 | 0 | 0.1 | 0.1 |  |  |
| 8 | INEA/PRESI | Ofício - NA 2015 | comunicacao | 5 | 5 | 0.8 | 0.8 |  |  |
| 9 | CAENE | Avaliar regularidade documental de estação de gás | analise_tecnica_engenharia | 0 | 0 | 10.0 | 3.0 |  |  |
| 10 | SCEXEC | Juntar Ofício .INEA/PRESI Nº2326 | comunicacao | 0 | 0 | 0.1 | 0.1 |  |  |
| 11 | SCEXEC | Encaminhar processo à Procuradoria para parecer jurídico | encaminhamento | 0 | 0 | 0.4 | 0.6 |  |  |
| 12 | PROC | Analisar infração fiscalizatória e opinar sobre aplicação de penalidade | analise_juridica | 17 | 17 | 15.8 | 4.0 |  |  |
| 13 | SCEXEC | Encaminhar processo para relatoria após sorteio | encaminhamento | 5 | 5 | 0.1 | 0.1 |  |  |
| 14 | CONS-02 | Notificar concessionária para apresentar Razões Finais | comunicacao | 106 | 106 | 1.5 | 0.8 | prazo_concedido | sim |
| 15 | CONS-02 | Votar aplicacao de advertencia e expedicao de oficio | relatoria_decisao | 7 | 0 | 34.5 | 9.0 | diligencia_externa; prazo_concedido |  |
| 16 | SCEXEC | Solicitar informações sobre regularização junto ao CBMERJ | comunicacao | 2 | 0 | 4.7 | 1.9 | diligencia_externa; prazo_concedido |  |
| 17 | CAENE | Devolver processo à SECEX após ciência de deliberação | encaminhamento | 0 | 0 | 0.4 | 0.1 |  |  |
| 18 | SCEXEC | Informar providências adotadas em cumprimento a deliberação | instrucao_processual | 0 | 0 | 2.5 | 1.0 |  |  |

Peças de maior complexidade: Voto 29 (CONS-02, 10 laudas, complexidade 4); Parecer 417 (PROC, 16 laudas, complexidade 3); Relatório (CONS-02, 7 laudas, complexidade 3); Parecer 86 (CAENE, 2 laudas, complexidade 3); Relatório (CAENE, 4 laudas, complexidade 3); Deliberação (CONS-02, 3 laudas, complexidade 3)
