# Evidências — P36 Regulação e fiscalização comercial (faturamento, medição, corte, religação e tarifa social)

Processos SEI na carteira com este código: 7 (4 nativos do SEI). Casos do piloto: SEI-480002/008679/2025 (típico).

## Participação das unidades (todos os processos do código)

| Unidade | Processos em que juntou documento (%) | Posse mediana por passagem (du) | Posse total (du, nativos) |
|---|---|---|---|
| CONS-02 | 100 | 40 | 1622 |
| SCEXEC | 100 | 2 | 245 |
| PROC | 86 | 30 | 1457 |
| CASAN | 57 | 7 | 181 |
| OUVI | 29 | 2 | 4 |
| PRESI | 29 | 2 | 10 |
| CAENE | 14 | nan | 0 |
| CAPET | 14 | 0 | 0 |
| CHEGAB | 14 | 3 | 3 |
| CONS-03 | 14 | 3 | 135 |
| PROT | 14 | 0 | 0 |
| REG | 14 | 3 | 60 |

## Transições entre unidades ativas, sem a Secretaria (todos os processos)

PROC → CONS-02: 6; CONS-02 → PROC: 5; CONS-02 → CASAN: 3; CONS-02 → CONS-02: 3; CASAN → PROC: 3; PROC → PRESI: 3; CONS-03 → PROC: 3; PROC → CONS-03: 3; CONS-03 → CASAN: 2; CASAN → CONS-03: 2; REG → PROC: 2; CAENE → OUVI: 1; OUVI → CONS-02: 1; CONS-02 → CAENE: 1; PROT → PRESI: 1

Retornos a unidade já visitada (média): 5.0; ofícios por processo (mediana): 3; vistas/razões finais (mediana): 1; aguardando terceiros (du, mediana): 0; lead time nativos (du, mediana): 1094; com deliberação: 71%.

## Caso típico: SEI-480002/008679/2025

CONTRATO DE CONDIÇÕES ESPECIAIS PARA A PRESTAÇÃO DE ABASTECIMENTO DE ÁGUA POTÁVEL A GRANDES USUÁRIOS. CONCESSIONÁRIA RIO + SANEAMENTO E TERNIUM BRASIL LITDA.

| # | Unidade | Tarefa (da ficha) | Natureza | du na passagem | Espera até 1ª juntada | Horas (teto) | Horas (piso) | Sinais de perda | Espera dominante |
|---|---|---|---|---|---|---|---|---|---|
| 1 | SCEXEC | Juntar Recibo Eletrônico de Protocolo | tramitacao | 2 | 0 | 0.2 | 0.2 |  |  |
| 2 | REG | Encaminhar pleito de contrato especial para análise jurídica | encaminhamento | 14 | 0 | 1.9 | 2.0 |  |  |
| 3 | PROC | Analisar minuta de contrato especial para grande usuário | analise_juridica | 25 | 25 | 46.8 | 8.0 |  |  |
| 4 | PRESI | Encaminhar processo à SECEX para providências | encaminhamento | 1 | 1 | 0.1 | 0.1 |  |  |
| 5 | REG | Encaminhar processo à SECEX para deliberação do Conselho Diretor | encaminhamento | 10 | 10 | 0.9 | 0.5 |  |  |
| 6 | SCEXEC | Encaminhar autos à Assessoria Regulatória | encaminhamento | 8 | 8 | 0.1 | 0.1 |  |  |
| 7 | REG | Encaminhar minuta contratual ajustada à Procuradoria | encaminhamento | 0 | 0 | 0.4 | 0.2 |  |  |
| 8 | PROC | Verificar incorporação de recomendações jurídicas em minuta | analise_juridica | 7 | 7 | 1.2 | 1.0 |  |  |
| 9 | SCEXEC | Encaminhar processo ao gabinete de conselheiro relator | encaminhamento | 0 | 0 | 0.4 | 0.1 |  |  |
| 10 | CONS-02 | Votar aprovação de minuta contratual de grande usuário | relatoria_decisao | 97 | 21 | 29.8 | 11.2 | prazo_concedido |  |
| 11 | SCEXEC | Juntar Publicação 11/03/2026 Deliberação 5012 | comunicacao | 1 | 0 | 0.1 | 0.1 |  |  |
| 12 | CASAN | Restituir processo à SECEX após ciência de deliberação | encaminhamento | 0 | 0 | 0.4 | 0.1 |  |  |
| 13 | SCEXEC | Informar cumprimento de determinações de Deliberação | instrucao_processual | 0 | 0 | 6.1 | 2.2 |  |  |
| 14 | SCEXEC | Registrar providências finais e encerrar processo regulatório | publicacao_registro | 2 | 2 | 1.6 | 0.5 |  |  |

Peças de maior complexidade: Parecer 673 (PROC, 47 laudas, complexidade 4); Voto 10 (CONS-02, 6 laudas, complexidade 4); Relatório (CONS-02, 9 laudas, complexidade 3); Deliberação (CONS-02, 3 laudas, complexidade 3); Despacho de Encaminhamento de Processo (PROC, 2 laudas, complexidade 3)
