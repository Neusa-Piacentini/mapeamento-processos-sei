# Evidências — P01 Reajuste tarifário anual (saneamento e gás)

Processos SEI na carteira com este código: 29 (26 nativos do SEI). Casos do piloto: SEI-480002/001914/2024 (típico), SEI-220007/004053/2022 (crítico).

## Participação das unidades (todos os processos do código)

| Unidade | Processos em que juntou documento (%) | Posse mediana por passagem (du) | Posse total (du, nativos) |
|---|---|---|---|
| CONS-02 | 100 | 4 | 3676 |
| SCEXEC | 100 | 2 | 2627 |
| CAPET | 97 | 3 | 2325 |
| PROC | 97 | 5 | 2762 |
| CASAN | 24 | 0 | 104 |
| REG | 14 | 2 | 18 |
| CAENE | 10 | 0 | 0 |
| CHEGAB | 10 | 0 | 1 |
| CONS-01 | 10 | 0 | 72 |
| CODIR | 7 | 8 | 208 |
| CONS-04 | 7 | 0 | 35 |
| CONS-05 | 7 | 7 | 1188 |

## Transições entre unidades ativas, sem a Secretaria (todos os processos)

PROC → CONS-02: 35; CONS-02 → PROC: 27; CONS-02 → CAPET: 27; CAPET → CONS-02: 27; CONS-02 → CONS-02: 16; CAPET → PROC: 15; PROC → CAPET: 11; CONS-02 → CASAN: 4; CASAN → CAPET: 4; CAPET → CONS-05: 4; REG → CAPET: 4; CONS-01 → CAPET: 3; CAPET → CHEGAB: 3; CHEGAB → PROC: 3; CAPET → CASAN: 3

Retornos a unidade já visitada (média): 4.6; ofícios por processo (mediana): 5; vistas/razões finais (mediana): 1; aguardando terceiros (du, mediana): 13; lead time nativos (du, mediana): 398; com deliberação: 72%.

## Caso típico: SEI-480002/001914/2024

REAJUSTE TARIFÁRIO - IRC E ITS  - 2024

| # | Unidade | Tarefa (da ficha) | Natureza | du na passagem | Espera até 1ª juntada | Horas (teto) | Horas (piso) | Sinais de perda | Espera dominante |
|---|---|---|---|---|---|---|---|---|---|
| 1 | SCEXEC | Acusar recebimento de pleito e orientar peticionamento | comunicacao | 1 | 0 | 2.4 | 1.6 | prazo_concedido |  |
| 2 | PROC | Analisar legalidade do pleito de reajuste tarifário | analise_juridica | 37 | 37 | 13.2 | 4.0 |  |  |
| 3 | SCEXEC | Encaminhar processo ao Conselheiro Relator sorteado | encaminhamento | 5 | 0 | 0.2 | 0.2 |  |  |
| 4 | CAPET | Calcular reajuste tarifario anual e parametrico do Bloco II | analise_economico_financeira | 13 | 0 | 15.3 | 4.2 | refazimento |  |
| 5 | CONS-02 | Encaminhar processo à Procuradoria para análise jurídica | encaminhamento | 0 | 0 | 0.1 | 0.1 |  |  |
| 6 | CONS-02 | Encaminhar processo à SECEX para inclusão em pauta | encaminhamento | 0 | 0 | 0.2 | 0.3 |  |  |
| 7 | CONS-02 | Solicitar manifestação do Verificador Independente sobre ITS | comunicacao | 5 | 4 | 1.5 | 0.8 | diligencia_externa; prazo_concedido |  |
| 8 | SCEXEC | Notificar concessionária sobre decisão do Conselho Diretor | comunicacao | 0 | 0 | 1.9 | 1.0 |  |  |
| 9 | SCEXEC | Juntar Protocolo | tramitacao | 0 | 0 | 0.1 | 0.1 |  |  |
| 10 | CONS-02 | Reiterar solicitação de manifestação à FIPE | comunicacao | 32 | 28 | 1.6 | 0.8 | reiteracao | sim |
| 11 | CAPET | Analisar pleito de reajuste e recalcular IRC | analise_economico_financeira | 30 | 30 | 5.0 | 4.0 | aguardando_outra_unidade | sim |
| 12 | CONS-02 | Notificar concessionária sobre acesso aos autos | comunicacao | 0 | 0 | 1.5 | 0.8 |  |  |
| 13 | SCEXEC | Encaminhar processo ao Gabinete do Conselheiro Relator | encaminhamento | 3 | 0 | 0.6 | 0.3 |  |  |
| 14 | PROC | Analisar aspectos jurídicos de reajuste e fórmula paramétrica | analise_juridica | 5 | 5 | 44.8 | 12.0 | diligencia_externa |  |
| 15 | SCEXEC | Juntar Ofício IGUÁ OF-RJ 5260/2024 | comunicacao | 0 | 0 | 0.1 | 0.1 | refazimento |  |
| 16 | CAPET | Analisar e calcular reajuste tarifario e ITS | analise_economico_financeira | 0 | 0 | 19.0 | 12.1 |  |  |
| 17 | CONS-02 | Relatar e votar reajuste tarifário da concessionária | relatoria_decisao | 103 | 0 | 34.9 | 12.8 | aguardando_outra_unidade; diligencia_externa; prazo_concedido |  |
| 18 | SCEXEC | Juntar Protocolo - Recebimento | tramitacao | 11 | 0 | 0.1 | 0.1 |  |  |
| 19 | SCEXEC | Juntar Ofício IGUÁ_OFRJ 2024/6112 | comunicacao | 0 | 0 | 0.1 | 0.1 |  |  |
| 20 | SCEXEC | Juntar Publicação 13_12_2024 IGUA 4809__29 | comunicacao | 0 | 0 | 0.1 | 0.1 |  |  |
| 21 | SCEXEC | Informar ausência de recursos e encaminhar autos | encaminhamento | 23 | 23 | 0.7 | 0.3 |  | sim |
| 22 | CASAN | Encaminhar processo para arquivamento na SECEX | encaminhamento | 1 | 1 | 0.4 | 0.2 |  |  |
| 23 | CAPET | Devolver processo à SECEX registrando concordância com arquivamento | encaminhamento | 7 | 7 | 0.6 | 0.2 |  |  |
| 24 | SCEXEC | Declarar encerramento de processo administrativo | publicacao_registro | 7 | 7 | 0.4 | 0.1 |  |  |

Peças de maior complexidade: Parecer 562 (PROC, 56 laudas, complexidade 4); Parecer 289 (CAPET, 10 laudas, complexidade 4); Parecer 91 (CAPET, 5 laudas, complexidade 4); Voto 42 (CONS-02, 13 laudas, complexidade 4); Parecer 151 (PROC, 15 laudas, complexidade 3); Relatório (CONS-02, 11 laudas, complexidade 3); Despacho de Encaminhamento de Processo (CAPET, 5 laudas, complexidade 4)

## Caso crítico: SEI-220007/004053/2022

REAJUSTE TARIFÁRIO PARA VIGORAR A PARTIR DE JANEIRO DE 2023

| # | Unidade | Tarefa (da ficha) | Natureza | du na passagem | Espera até 1ª juntada | Horas (teto) | Horas (piso) | Sinais de perda | Espera dominante |
|---|---|---|---|---|---|---|---|---|---|
| 1 | SCEXEC | Encaminhar pleito de reajuste à CAPET | encaminhamento | 0 | 0 | 1.3 | 1.0 |  |  |
| 2 | CAPET | Analisar pleito de reajuste tarifário da concessionária | analise_economico_financeira | 1 | 1 | 12.4 | 4.1 |  |  |
| 3 | SCEXEC | Encaminhar processo de reajuste à Procuradoria | encaminhamento | 0 | 0 | 0.1 | 0.1 |  |  |
| 4 | PROC | Analisar termo aditivo e solicitar manifestação municipal | analise_juridica | 15 | 13 | 2.5 | 3.5 | diligencia_externa |  |
| 5 | SCEXEC | Solicitar manifestação do Poder Concedente sobre contrato | comunicacao | 6 | 0 | 2.3 | 1.9 | diligencia_externa |  |
| 6 | SCEXEC | Encaminhar processo ao relator sorteado | encaminhamento | 0 | 0 | 0.5 | 0.2 |  |  |
| 7 | PROC | Solicitar reiteração de ofício ao Poder Concedente | encaminhamento | 0 | 0 | 0.4 | 0.2 | reiteracao |  |
| 8 | SCEXEC | Solicitar esclarecimentos ao Poder Concedente sobre aditivo | comunicacao | 0 | 0 | 2.1 | 1.3 | diligencia_externa |  |
| 9 | SCEXEC | Encaminhar processo ao Gabinete do Conselheiro Relator | encaminhamento | 0 | 0 | 0.8 | 0.5 |  |  |
| 10 | PROC | Encaminhar processo para nova análise técnica da CAPET | encaminhamento | 0 | 0 | 1.9 | 1.5 |  |  |
| 11 | CONS-02 | Encaminhar processo à Procuradoria para manifestação | encaminhamento | 0 | 0 | 1.0 | 0.3 | aguardando_outra_unidade |  |
| 12 | CAPET | Analisar manifestação municipal e propor cenários tarifários | analise_economico_financeira | 3 | 3 | 11.3 | 6.1 |  |  |
| 13 | CONS-02 | Encaminhar processo à Procuradoria para manifestação | encaminhamento | 1 | 1 | 0.4 | 0.1 |  |  |
| 14 | PROC | Sintetizar controvérsia e sugerir diligência à Relatoria | instrucao_processual | 7 | 7 | 3.3 | 3.0 | diligencia_externa |  |
| 15 | CONS-02 | Solicitar documentos e esclarecimentos à concessionária | comunicacao | 11 | 4 | 4.4 | 2.8 | pedido_complementacao; prazo_concedido |  |
| 16 | CAPET | Analisar documentação complementar e recomendar condicionante tarifária | analise_economico_financeira | 2 | 1 | 8.5 | 4.2 |  |  |
| 17 | CONS-02 | Encaminhar ata de reunião para assinatura | comunicacao | 1 | 1 | 1.6 | 0.8 |  |  |
| 18 | PROC | Analisar legalidade do reajuste e realinhamento tarifário | analise_juridica | 25 | 12 | 36.4 | 19.0 |  |  |
| 19 | CONS-02 | Relatar processo de reajuste tarifário e realinhamento | relatoria_decisao | 15 | 1 | 32.0 | 12.4 | prazo_concedido |  |
| 20 | SCEXEC | Notificar concessionária sobre Deliberação de reajuste tarifário | comunicacao | 0 | 0 | 1.4 | 0.7 |  |  |
| 21 | CONS-02 | Relatar e votar homologação de reajuste tarifário | relatoria_decisao | 0 | 0 | 11.7 | 4.0 |  |  |
| 22 | SCEXEC | Encaminhar processo à CAPET para ciência e providências | encaminhamento | 0 | 0 | 0.1 | 0.5 |  |  |
| 23 | CONS-02 | Encaminhar processo à Procuradoria para parecer | encaminhamento | 232 | 232 | 0.4 | 0.2 |  |  |
| 24 | CAPET | Verificar aplicação das novas tarifas em faturas | auditoria_conferencia | 21 | 2 | 6.9 | 6.0 | prazo_concedido; reiteracao |  |
| 25 | PROC | Opinar sobre arquivamento de processo de reajuste | analise_juridica | 43 | 43 | 2.6 | 2.0 |  | sim |
| 26 | CONS-02 | Solicitar encerramento e arquivamento de processo | encaminhamento | 82 | 82 | 0.6 | 0.2 |  |  |
| 27 | SCEXEC | Encerrar processo de reajuste tarifário | publicacao_registro | 93 | 93 | 1.9 | 0.5 |  | sim |

Peças de maior complexidade: Parecer 110 (PROC, 45 laudas, complexidade 4); Relatório (CONS-02, 56 laudas, complexidade 4); Parecer 221 (CAPET, 7 laudas, complexidade 4); Voto 9 (CONS-02, 8 laudas, complexidade 4); Parecer 10 (CAPET, 4 laudas, complexidade 4); Parecer 39 (CAPET, 4 laudas, complexidade 3); Ata de Reunião (PROC, 8 laudas, complexidade 3); Despacho (CAPET, 4 laudas, complexidade 4)
