# Resultados da Fase 2 — do caso ao procedimento

Gerado por `scripts/resumo_fase2.py` a partir das saídas do pipeline. Tempos em dias úteis (du); horas são hipótese até a calibração com servidores.

## Coorte

117 processos em 12 códigos (92 com trilha nativa do SEI, 9 migrados com trilha parcial, 16 só com as peças, sem trâmite). 4 processos repetidos (cópia de processo físico migrado com número novo) foram retirados.

| Código | Processo | Situação | Casos (nativa/migrada/sem) | Lead time dos nativos encerrados | Concordância na auditoria (peças substantivas) |
|---|---|---|---|---|---|
| N01 | Acompanhamento ambiental e de mananciais das concessões | procedimento | 11 (5/3/3) | 362,5 du (q1 245,8–q3 601,5; n 4) | 93% (14 peças) |
| P01 | Reajuste tarifário anual | procedimento | 18 (18/0/0) | 327 du (q1 127,5–q3 407; n 11) | 100% (14 peças) |
| P04 | Homologação de planos de investimento e obras | procedimento | 19 (12/5/2) | 1028,5 du (q1 1009,2–q3 1109; n 4) | 100% (14 peças) |
| P06 | Fiscalização técnica de campo (programada e por demanda) | procedimento | 12 (12/0/0) | 317 du (q1 185,5–q3 503; n 7) | 100% (14 peças) |
| P07 | Processo sancionador (auto de infração à cobrança da multa) | estudo de caso | 3 (2/0/1) | — | 64% (14 peças) |
| P08 | Monitoramento de metas contratuais e do IDG (verificador independente) | procedimento | 6 (6/0/0) | 641 du (q1 546–q3 913,5; n 3) | 93% (14 peças) |
| P18 | Prorrogação, relicitação e alteração de concessões | procedimento | 10 (0/1/9) | — | 100% (10 peças) |
| P19 | Regulação do mercado livre de gás (CUSD e migração) | procedimento | 11 (11/0/0) | 516 du (q1 391–q3 641; n 2) | 86% (14 peças) |
| P21 | Apuração de ocorrência de usuário pelo Conselho-Diretor | procedimento | 11 (11/0/0) | 380 du (q1 281,8–q3 519,2; n 8) | 100% (14 peças) |
| P22 | Resposta a órgãos de controle e ao Ministério Público | procedimento | 8 (8/0/0) | 284,5 du (q1 274,8–q3 294,2; n 2) | 86% (14 peças) |
| P35 | Gestão de interrupções e crises de abastecimento | procedimento | 7 (7/0/0) | 930,5 du (q1 912,5–q3 975,2; n 4) | 93% (14 peças) |

Situação: *procedimento* = 5 casos ou mais e concordância ≥ 85% na auditoria às cegas; *indicativo* = abaixo do critério, números com ressalva; *estudo de caso* = menos de 5 casos.

## Controles de qualidade

- Classificador de atividade contra os vínculos auditados do piloto: 98% em 290 peças (otimista: as atividades foram descritas a partir desses mesmos casos).
- Auditoria às cegas fora do piloto: 216 peças de 11 códigos; concordância 88% no total e 92% nas 150 peças substantivas (critério 85%). Amostra de 14 substantivas por código: o percentual por código tem margem larga.
- Fichas de trabalho: 3183 peças; google/gemini-3.6-flash 2769; claude-haiku-5-5 414. As que faltavam quando o crédito do primeiro modelo acabou foram feitas com o segundo.
- Comparação dos dois modelos de ficha no mesmo documento (50 peças): natureza igual em 78%, complexidade igual em 76% (diferença de até 1 ponto em 98%); horas do segundo modelo = 1,42× as do primeiro (mediana). As horas-piso das peças do segundo modelo tendem, portanto, a ser maiores.

## Procedimento por código

### N01 — Acompanhamento ambiental e de mananciais das concessões (procedimento)

11 casos; 11 caminhos distintos (ordem da 1ª ocorrência de cada atividade). Peças substantivas fora do modelo por caso: mediana 0%.

Nenhum caminho se repete entre os casos. Núcleo comum (atividades em metade dos casos ou mais, na ordem do modelo): t1 → t5 → t9 → t10 → t11

| Atividade | Casos | Com laço | Execução | Espera antes | Horas (piso) |
|---|---|---|---|---|---|
| t1 Solicitar informações à concessionária | 64% | 0 | 0 du (q1 0–q3 0; n 7) | 48 du (q1 8,5–q3 331,5; n 4) | 1,2 h (q1 1,1–q3 1,5; n 7) |
| t2 Requisitar informações à concessionária e à prefeitura | 45% | 1 | 0 du (q1 0–q3 16; n 9) | 13 du (q1 6–q3 30; n 9) | 0,8 h (q1 0,2–q3 1,2; n 9) |
| t3 Comunicar dilação de prazo à concessionária | 45% | 2 | 0 du (q1 0–q3 0; n 8) | 7 du (q1 2–q3 17; n 8) | 0,5 h (q1 0,4–q3 0,6; n 8) |
| t4 Reiterar ofício à concessionária | 18% | 1 | 0 du (q1 0–q3 0; n 3) | 11 du (q1 6,5–q3 49,5; n 3) | 0,8 h (q1 0,8–q3 1; n 3) |
| t5 Analisar o caso e emitir parecer técnico | 82% | 3 | 0 du (q1 0–q3 0; n 12) | 35,5 du (q1 12,2–q3 75; n 12) | 4,2 h (q1 3–q3 5; n 12) |
| t6 Oficiar concessionária com o parecer técnico | 45% | 1 | 0 du (q1 0–q3 1; n 7) | 1 du (q1 1–q3 5; n 7) | 0,8 h (q1 0,6–q3 1,1; n 7) |
| t7 Reiterar prazo de instrução à CASAN | 27% | 1 | 0 du (q1 0–q3 11; n 4) | 12 du (q1 8–q3 90,5; n 4) | 0,5 h (q1 0,4–q3 0,6; n 4) |
| t8 Avaliar a manifestação da concessionária | 36% | 0 | 0 du (q1 0–q3 0; n 4) | 9,5 du (q1 1,5–q3 171,8; n 4) | 1 h (q1 0,9–q3 1,2; n 4) |
| t9 Emitir parecer jurídico sobre o descumprimento | 82% | 2 | 0 du (q1 0–q3 0; n 11) | 49 du (q1 8–q3 82; n 11) | 3 h (q1 1,5–q3 5; n 11) |
| t10 Remeter ao gabinete do relator sorteado | 91% | 3 | 0 du (q1 0–q3 0; n 14) | 18,5 du (q1 12–q3 37; n 14) | 0,2 h (q1 0,2–q3 0,2; n 14) |
| t11 Notificar concessionária para razões finais | 64% | 0 | 0 du (q1 0–q3 0; n 7) | 30 du (q1 13–q3 33; n 7) | 1,2 h (q1 0,8–q3 1,2; n 7) |
| t12 Relatar, votar e deliberar o processo | 9% | 0 | 0 du (q1 0–q3 0; n 1) | 68 du (q1 68–q3 68; n 1) | 6,5 h (q1 6,5–q3 6,5; n 1) |
| t13 Publicar deliberação e comunicar a concessionária | 9% | 0 | 5 du (q1 5–q3 5; n 1) | 12 du (q1 12–q3 12; n 1) | 1,8 h (q1 1,8–q3 1,8; n 1) |
| t14 Informar cumprimento e encerrar o processo | 9% | 0 | 0 du (q1 0–q3 0; n 1) | 1 du (q1 1–q3 1; n 1) | 1,5 h (q1 1,5–q3 1,5; n 1) |

### P01 — Reajuste tarifário anual (procedimento)

18 casos; 17 caminhos distintos (ordem da 1ª ocorrência de cada atividade). Peças substantivas fora do modelo por caso: mediana 0%.

Caminho mais frequente (2 casos): t1 → t4 → t2 → t5 → t3 → t7 → t16 → t8 → t9 → t10 → t13

| Atividade | Casos | Com laço | Execução | Espera antes | Horas (piso) |
|---|---|---|---|---|---|
| t1 Acusar recebimento e sortear relator | 100% | 15 | 0 du (q1 0–q3 1,2; n 40) | 1 du (q1 0–q3 4; n 40) | 0,2 h (q1 0,2–q3 0,7; n 40) |
| t2 Calcular reajuste pela fórmula paramétrica | 100% | 13 | 0 du (q1 0–q3 0; n 35) | 3 du (q1 1–q3 7; n 35) | 4,1 h (q1 3,1–q3 7,2; n 35) |
| t3 Analisar legalidade do reajuste | 100% | 8 | 0 du (q1 0–q3 0; n 29) | 3 du (q1 2–q3 7; n 29) | 4 h (q1 4–q3 8; n 29) |
| t4 Diligenciar partes e verificador independente | 50% | 8 | 0 du (q1 0–q3 0; n 33) | 2 du (q1 0–q3 4; n 33) | 0,2 h (q1 0,1–q3 0,8; n 33) |
| t5 Reiterar ofício de diligência | 33% | 2 | 0 du (q1 0–q3 0; n 8) | 9,5 du (q1 4,5–q3 38; n 8) | 0,8 h (q1 0,6–q3 0,8; n 8) |
| t6 Conduzir conciliação entre as partes | 22% | 1 | 0 du (q1 0–q3 0; n 5) | 30 du (q1 7–q3 30; n 5) | 0,1 h (q1 0,1–q3 0,8; n 5) |
| t14 Diligenciar Poder Concedente e concessionária | 61% | 10 | 0 du (q1 0–q3 0; n 26) | 2 du (q1 0–q3 4; n 26) | 0,2 h (q1 0,1–q3 1,1; n 26) |
| t15 Lavrar decisão do Conselho em reunião interna | 44% | 2 | 0 du (q1 0–q3 0; n 11) | 5 du (q1 0–q3 5,5; n 11) | 0,2 h (q1 0,1–q3 0,3; n 11) |
| t16 Conceder acesso aos autos às partes | 50% | 2 | 0 du (q1 0–q3 0; n 11) | 2 du (q1 1–q3 5; n 11) | 0,8 h (q1 0,3–q3 0,8; n 11) |
| t7 Notificar partes para razões finais | 100% | 0 | 0 du (q1 0–q3 0; n 18) | 1 du (q1 0–q3 2; n 18) | 0,8 h (q1 0,8–q3 0,8; n 18) |
| t8 Relatar, votar e deliberar o reajuste | 94% | 7 | 0 du (q1 0–q3 6; n 25) | 5 du (q1 2–q3 22; n 25) | 5,5 h (q1 5–q3 8; n 25) |
| t9 Publicar deliberação e notificar concessionária | 94% | 8 | 0 du (q1 0–q3 5; n 25) | 2 du (q1 1–q3 5; n 25) | 0,5 h (q1 0,1–q3 0,8; n 25) |
| t10 Verificar aplicação das tarifas nas faturas | 67% | 0 | 16 du (q1 0–q3 23,2; n 12) | 5,5 du (q1 3,8–q3 128,5; n 12) | 3,4 h (q1 2,9–q3 4,3; n 12) |
| t11 Opinar sobre o arquivamento | 6% | 0 | 0 du (q1 0–q3 0; n 1) | 102 du (q1 102–q3 102; n 1) | 1 h (q1 1–q3 1; n 1) |
| t12 Certificar ausência de recurso | 17% | 1 | 0 du (q1 0–q3 0; n 4) | 51 du (q1 16,8–q3 85,5; n 4) | 0,4 h (q1 0,2–q3 0,6; n 4) |
| t13 Encerrar e arquivar o processo | 44% | 1 | 0 du (q1 0–q3 0; n 9) | 3 du (q1 1–q3 46; n 9) | 0,5 h (q1 0,5–q3 1; n 9) |

### P04 — Homologação de planos de investimento e obras (procedimento)

19 casos; 17 caminhos distintos (ordem da 1ª ocorrência de cada atividade). Peças substantivas fora do modelo por caso: mediana 0%.

Caminho mais frequente (2 casos): t1 → t3 → t2 → t4 → t5 → t6 → t8

| Atividade | Casos | Com laço | Execução | Espera antes | Horas (piso) |
|---|---|---|---|---|---|
| t1 Autuar pleito e comunicar a concessionária | 100% | 3 | 0 du (q1 0–q3 0,2; n 24) | 0 du (q1 0–q3 6,2; n 22) | 0,8 h (q1 0,4–q3 2,3; n 24) |
| t2 Solicitar documentos e complementações à concessionária | 63% | 10 | 0,5 du (q1 0–q3 39,8; n 28) | 19 du (q1 10–q3 22,5; n 28) | 1,5 h (q1 0,9–q3 2; n 28) |
| t3 Reiterar ofício ou prorrogar prazo | 47% | 6 | 0 du (q1 0–q3 0; n 20) | 9 du (q1 5–q3 14,8; n 20) | 0,8 h (q1 0,5–q3 1; n 20) |
| t4 Analisar projeto ou as built da obra | 74% | 10 | 0 du (q1 0–q3 0; n 31) | 16 du (q1 3,5–q3 39; n 31) | 4,1 h (q1 0,5–q3 5; n 31) |
| t5 Analisar orçamento e comprovação financeira | 74% | 8 | 0 du (q1 0–q3 0; n 24) | 5 du (q1 1,8–q3 20,5; n 24) | 3,5 h (q1 2–q3 4; n 24) |
| t6 Opinar sobre homologação e penalidade | 95% | 9 | 0 du (q1 0–q3 0; n 32) | 59 du (q1 18–q3 187; n 32) | 3 h (q1 0,9–q3 4; n 32) |
| t7 Notificar concessionária para manifestação e vista | 37% | 1 | 0 du (q1 0–q3 0; n 8) | 0 du (q1 0–q3 3; n 8) | 0,8 h (q1 0,8–q3 0,9; n 8) |
| t8 Distribuir processo ao relator sorteado | 89% | 4 | 0 du (q1 0–q3 0; n 21) | 14 du (q1 3–q3 20; n 21) | 0,2 h (q1 0,1–q3 0,3; n 21) |
| t9 Diligenciar concessionária e convocar reunião | 74% | 10 | 0 du (q1 0–q3 0; n 39) | 12 du (q1 1–q3 35; n 39) | 0,2 h (q1 0,1–q3 0,5; n 39) |
| t10 Notificar partes para razões finais | 63% | 3 | 0 du (q1 0–q3 16; n 15) | 22 du (q1 3–q3 95,5; n 15) | 1,5 h (q1 0,8–q3 2,4; n 15) |
| t11 Relatar, votar e deliberar o processo | 42% | 0 | 0 du (q1 0–q3 1,5; n 8) | 49,5 du (q1 19,2–q3 73; n 8) | 9,5 h (q1 7,8–q3 11,9; n 8) |
| t12 Publicar deliberação e notificar as partes | 42% | 2 | 3 du (q1 0,5–q3 4,8; n 10) | 4 du (q1 1,2–q3 7,2; n 10) | 1,4 h (q1 0,5–q3 2,4; n 10) |
| t13 Analisar recurso ou embargos de declaração | 11% | 0 | 0 du (q1 0–q3 0; n 2) | 127,5 du (q1 107,2–q3 147,8; n 2) | 4,5 h (q1 4,2–q3 4,8; n 2) |
| t15 Verificar cumprimento das determinações da deliberação | 42% | 0 | 0 du (q1 0–q3 0; n 8) | 17,5 du (q1 4,2–q3 75,8; n 8) | 0,2 h (q1 0,1–q3 0,8; n 8) |
| t14 Encerrar e arquivar o processo | 21% | 1 | 0 du (q1 0–q3 0; n 5) | 8 du (q1 1–q3 24; n 5) | 0,5 h (q1 0,5–q3 1; n 5) |

### P06 — Fiscalização técnica de campo (programada e por demanda) (procedimento)

12 casos; 9 caminhos distintos (ordem da 1ª ocorrência de cada atividade). Peças substantivas fora do modelo por caso: mediana 0%.

Caminho mais frequente (3 casos): t1 → t3 → t4 → t5 → t6 → t7 → t8 → t9

| Atividade | Casos | Com laço | Execução | Espera antes | Horas (piso) |
|---|---|---|---|---|---|
| t1 Vistoriar instalação, relatar e notificar concessionária | 92% | 1 | 0 du (q1 0–q3 0,2; n 12) | 0 du (q1 0–q3 4,2; n 12) | 7,4 h (q1 5,7–q3 8,3; n 12) |
| t2 Requisitar documentos à concessionária e a órgãos | 33% | 2 | 3,5 du (q1 0–q3 10,5; n 8) | 11,5 du (q1 4,2–q3 26,8; n 8) | 1,4 h (q1 1,1–q3 2,6; n 8) |
| t3 Analisar defesa e emitir parecer técnico | 92% | 5 | 0 du (q1 0–q3 0; n 28) | 9,5 du (q1 1–q3 18,2; n 28) | 3 h (q1 1,8–q3 4,1; n 28) |
| t10 Notificar concessionária sobre o parecer | 42% | 1 | 0 du (q1 0–q3 0; n 6) | 1 du (q1 0,2–q3 3,2; n 6) | 0,7 h (q1 0,5–q3 1,5; n 6) |
| t11 Decidir pedido de dilação de prazo | 17% | 1 | 0 du (q1 0–q3 1; n 5) | 2 du (q1 0–q3 10; n 5) | 0,8 h (q1 0,4–q3 0,8; n 5) |
| t4 Analisar infração e emitir parecer jurídico | 92% | 3 | 0 du (q1 0–q3 0; n 16) | 36,5 du (q1 12,8–q3 75; n 16) | 4 h (q1 2–q3 4; n 16) |
| t5 Sortear relator e distribuir o processo | 100% | 5 | 0 du (q1 0–q3 0; n 17) | 15 du (q1 5–q3 31; n 17) | 0,1 h (q1 0,1–q3 0,2; n 17) |
| t6 Notificar concessionária para razões finais | 75% | 1 | 0 du (q1 0–q3 0; n 16) | 8 du (q1 8–q3 28,2; n 16) | 0,8 h (q1 0,4–q3 0,9; n 16) |
| t7 Relatar, votar e deliberar em sessão | 67% | 1 | 0 du (q1 0–q3 0; n 10) | 58,5 du (q1 20,2–q3 81,8; n 10) | 7 h (q1 6–q3 7,8; n 10) |
| t8 Publicar deliberação e oficiar concessionária e órgãos | 67% | 2 | 2 du (q1 1–q3 5; n 12) | 6 du (q1 2,8–q3 6; n 12) | 1,1 h (q1 0,8–q3 1,5; n 12) |
| t9 Registrar providências de cumprimento da deliberação | 75% | 3 | 0 du (q1 0–q3 0; n 14) | 0,5 du (q1 0–q3 2,8; n 14) | 0,5 h (q1 0,1–q3 0,9; n 14) |

### P07 — Processo sancionador (auto de infração à cobrança da multa) (estudo de caso)

3 casos; 3 caminhos distintos (ordem da 1ª ocorrência de cada atividade). Peças substantivas fora do modelo por caso: mediana 25%.

Nenhum caminho se repete entre os casos. Núcleo comum (atividades em metade dos casos ou mais, na ordem do modelo): t2 → t3 → t4 → t9 → t11 → t12 → t14 → t15 → t16 → t17

| Atividade | Casos | Com laço | Execução | Espera antes | Horas (piso) |
|---|---|---|---|---|---|
| t1 Calcular o valor da multa | 33% | 0 | 0 du (q1 0–q3 0; n 1) | 1 du (q1 1–q3 1; n 1) | 0,5 h (q1 0,5–q3 0,5; n 1) |
| t2 Lavrar minuta do auto de infração | 67% | 2 | 0 du (q1 0–q3 0; n 5) | 8 du (q1 4,5–q3 15,8; n 4) | 1,2 h (q1 1,2–q3 2; n 5) |
| t3 Conferir conformidade da minuta do auto | 67% | 1 | 0 du (q1 0–q3 0; n 3) | 5 du (q1 5–q3 7,5; n 3) | 3 h (q1 1,6–q3 4,5; n 3) |
| t4 Assinar o auto de infração | 67% | 0 | 0,5 du (q1 0,2–q3 0,8; n 2) | 0 du (q1 0–q3 0; n 2) | 0,2 h (q1 0,2–q3 0,2; n 2) |
| t5 Notificar concessionária do auto de infração | 33% | 0 | 0 du (q1 0–q3 0; n 1) | 1 du (q1 1–q3 1; n 1) | 1,2 h (q1 1,2–q3 1,2; n 1) |
| t6 Analisar impugnação ao auto de infração | 33% | 0 | 0 du (q1 0–q3 0; n 1) | 9 du (q1 9–q3 9; n 1) | 6 h (q1 6–q3 6; n 1) |
| t7 Comunicar resultado da impugnação à concessionária | 33% | 0 | 0 du (q1 0–q3 0; n 1) | 2 du (q1 2–q3 2; n 1) | 1,8 h (q1 1,8–q3 1,8; n 1) |
| t8 Recomendar submissão ao Conselho-Diretor | 33% | 0 | 0 du (q1 0–q3 0; n 1) | 12 du (q1 12–q3 12; n 1) | 4 h (q1 4–q3 4; n 1) |
| t9 Remeter ao gabinete do relator sorteado | 100% | 1 | 0 du (q1 0–q3 0; n 7) | 15 du (q1 7–q3 38,5; n 7) | 0,2 h (q1 0,2–q3 0,2; n 7) |
| t10 Acompanhar ação judicial e consultar a PGE | 33% | 1 | 0 du (q1 0–q3 0; n 5) | 26 du (q1 12–q3 48; n 5) | 0,2 h (q1 0,1–q3 0,8; n 5) |
| t11 Negociar acordo na câmara de mediação | 67% | 0 | 0 du (q1 0–q3 0; n 2) | 41,5 du (q1 35,2–q3 47,8; n 2) | 0,1 h (q1 0,1–q3 0,1; n 2) |
| t12 Propor processo de autocomposição ao Conselho-Diretor | 67% | 2 | 0 du (q1 0–q3 0,8; n 10) | 11 du (q1 0,2–q3 100,5; n 10) | 0,2 h (q1 0,1–q3 1; n 10) |
| t13 Registrar e publicar decisão de instauração | 33% | 0 | 1 du (q1 1–q3 1; n 1) | 9 du (q1 9–q3 9; n 1) | 0,2 h (q1 0,2–q3 0,2; n 1) |
| t14 Atualizar valores das multas aplicadas | 67% | 0 | 0 du (q1 0–q3 0; n 2) | 2 du (q1 2–q3 2; n 2) | 1,5 h (q1 1,2–q3 1,8; n 2) |
| t15 Emitir parecer sobre a minuta de autocomposição | 67% | 1 | 0 du (q1 0–q3 0; n 3) | 92 du (q1 46–q3 121; n 3) | 0,6 h (q1 0,4–q3 6,3; n 3) |
| t16 Informar resultado da mediação | 67% | 1 | 5 du (q1 2,5–q3 29,5; n 3) | 0 du (q1 0–q3 3; n 3) | 2 h (q1 1,6–q3 2,5; n 3) |
| t17 Notificar concessionária para razões finais | 67% | 0 | 0 du (q1 0–q3 0; n 2) | 7,5 du (q1 4,2–q3 10,8; n 2) | 0,8 h (q1 0,8–q3 0,8; n 2) |

### P08 — Monitoramento de metas contratuais e do IDG (verificador independente) (procedimento)

6 casos; 6 caminhos distintos (ordem da 1ª ocorrência de cada atividade). Peças substantivas fora do modelo por caso: mediana 0%.

Nenhum caminho se repete entre os casos. Núcleo comum (atividades em metade dos casos ou mais, na ordem do modelo): t1 → t2 → t3 → t5 → t4 → t6

| Atividade | Casos | Com laço | Execução | Espera antes | Horas (piso) |
|---|---|---|---|---|---|
| t1 Acusar recebimento e remeter à CASAN | 100% | 5 | 0,5 du (q1 0–q3 5,2; n 12) | 3,5 du (q1 0–q3 9; n 12) | 0,6 h (q1 0,2–q3 1; n 12) |
| t2 Analisar metas e indicadores e emitir parecer | 100% | 3 | 0 du (q1 0–q3 29; n 13) | 16 du (q1 3–q3 44; n 13) | 4,4 h (q1 2,2–q3 6,1; n 13) |
| t3 Notificar concessionária e conceder prazo | 100% | 2 | 0 du (q1 0–q3 0,8; n 10) | 1,5 du (q1 1–q3 8,8; n 10) | 0,8 h (q1 0,6–q3 0,8; n 10) |
| t5 Reanalisar após manifestação e emitir parecer final | 100% | 3 | 0 du (q1 0–q3 1; n 9) | 4 du (q1 0–q3 10; n 9) | 2,1 h (q1 1,8–q3 4,1; n 9) |
| t4 Emitir parecer jurídico ou restituir os autos | 83% | 3 | 0 du (q1 0–q3 0; n 13) | 13 du (q1 7–q3 26; n 13) | 2 h (q1 0,5–q3 4; n 13) |
| t6 Consolidar instrução e distribuir ao relator | 100% | 4 | 0 du (q1 0–q3 0; n 12) | 12 du (q1 7–q3 29,2; n 12) | 0,2 h (q1 0,1–q3 0,2; n 12) |
| t7 Instruir no gabinete e oficiar concessionária | 33% | 2 | 0 du (q1 0–q3 7; n 17) | 4 du (q1 2–q3 12; n 17) | 0,8 h (q1 0,5–q3 3; n 17) |
| t8 Relatar, votar e deliberar em sessão | 33% | 1 | 3 du (q1 2–q3 5; n 5) | 9 du (q1 0–q3 23; n 5) | 6,7 h (q1 4,2–q3 26,1; n 5) |
| t9 Publicar deliberação e comunicar concessionária | 33% | 1 | 0 du (q1 0–q3 0; n 5) | 1 du (q1 1–q3 2; n 5) | 0,6 h (q1 0,6–q3 1,4; n 5) |

### P18 — Prorrogação, relicitação e alteração de concessões (procedimento)

10 casos; 4 caminhos distintos (ordem da 1ª ocorrência de cada atividade). Peças substantivas fora do modelo por caso: mediana 0%.

Caminho mais frequente (5 casos): t1 → t2 → t3 → t4 → t7

| Atividade | Casos | Com laço | Execução | Espera antes | Horas (piso) |
|---|---|---|---|---|---|
| t1 Juntar decisão do CODIR e abrir processo municipal | 100% | 0 | 0 du (q1 0–q3 0; n 10) | 815 du (q1 815–q3 815; n 1) | 0,8 h (q1 0,8–q3 0,8; n 10) |
| t2 Verificar pendências documentais do município | 90% | 0 | 0 du (q1 0–q3 0; n 9) | 3 du (q1 3–q3 3; n 9) | 1 h (q1 1–q3 1,5; n 9) |
| t3 Oficiar CEDAE sobre abertura dos processos | 90% | 0 | 0 du (q1 0–q3 0; n 9) | 6 du (q1 6–q3 6; n 9) | 0,1 h (q1 0,1–q3 0,1; n 9) |
| t4 Juntar termo aditivo e publicação no DOERJ | 50% | 0 | 0 du (q1 0–q3 0; n 5) | 19 du (q1 19–q3 19; n 5) | 1,1 h (q1 1–q3 1,1; n 5) |
| t5 Notificar município sobre urgência do aditivo | 40% | 0 | 0 du (q1 0–q3 4,2; n 4) | 43,5 du (q1 37–q3 50; n 4) | 2,1 h (q1 1,9–q3 2,2; n 4) |
| t6 Reiterar notificação ao município | 40% | 0 | 0 du (q1 0–q3 0; n 4) | 138 du (q1 137–q3 141,2; n 4) | 0,8 h (q1 0,8–q3 0,9; n 4) |
| t7 Encaminhar processo ao relator por prevenção | 100% | 0 | 0 du (q1 0–q3 0; n 10) | 120,5 du (q1 11–q3 180; n 10) | 0,2 h (q1 0,2–q3 0,2; n 10) |
| t8 Juntar resposta do município | 10% | 0 | 0 du (q1 0–q3 0; n 1) | 4 du (q1 4–q3 4; n 1) | 0,3 h (q1 0,3–q3 0,3; n 1) |

### P19 — Regulação do mercado livre de gás (CUSD e migração) (procedimento)

11 casos; 11 caminhos distintos (ordem da 1ª ocorrência de cada atividade). Peças substantivas fora do modelo por caso: mediana 0%.

Nenhum caminho se repete entre os casos. Núcleo comum (atividades em metade dos casos ou mais, na ordem do modelo): t1 → t2 → t3 → t4 → t5 → t6 → t7 → t9 → t12 → t13

| Atividade | Casos | Com laço | Execução | Espera antes | Horas (piso) |
|---|---|---|---|---|---|
| t1 Notificar concessionária e distribuir ao relator | 100% | 7 | 0 du (q1 0–q3 5; n 57) | 3 du (q1 1–q3 11; n 57) | 0,3 h (q1 0,2–q3 0,5; n 57) |
| t2 Requisitar documentos e convocar reuniões com partes | 91% | 9 | 0 du (q1 0–q3 2; n 69) | 4 du (q1 1–q3 11; n 69) | 0,8 h (q1 0,2–q3 1,4; n 69) |
| t3 Elaborar parecer técnico e minuta regulatória | 64% | 5 | 0 du (q1 0–q3 0; n 19) | 0 du (q1 0–q3 12; n 19) | 0,5 h (q1 0,2–q3 4,1; n 19) |
| t4 Publicar aviso de consulta ou audiência pública | 55% | 6 | 0 du (q1 0–q3 0; n 40) | 1 du (q1 0,8–q3 1; n 40) | 0,8 h (q1 0,2–q3 1,5; n 40) |
| t5 Divulgar peças no portal e na imprensa | 55% | 6 | 0 du (q1 0–q3 0; n 40) | 0 du (q1 0–q3 1; n 40) | 0,2 h (q1 0,1–q3 0,2; n 40) |
| t6 Convidar interessados e conceder acesso aos autos | 73% | 8 | 0 du (q1 0–q3 0; n 56) | 2 du (q1 0–q3 9,2; n 56) | 0,8 h (q1 0,6–q3 1,2; n 56) |
| t7 Realizar audiência e juntar contribuições | 55% | 5 | 0 du (q1 0–q3 2; n 33) | 0 du (q1 0–q3 1; n 33) | 0,8 h (q1 0,1–q3 1,2; n 33) |
| t8 Analisar contribuições e consolidar minuta | 45% | 2 | 0 du (q1 0–q3 0; n 9) | 1 du (q1 0–q3 3; n 9) | 0,4 h (q1 0,4–q3 1,6; n 9) |
| t9 Emitir parecer jurídico sobre a matéria | 64% | 2 | 0 du (q1 0–q3 0; n 9) | 0 du (q1 0–q3 3; n 9) | 4 h (q1 3–q3 16; n 9) |
| t10 Esclarecer dúvida técnica apontada na instrução | 45% | 2 | 0 du (q1 0–q3 0; n 8) | 1,5 du (q1 0–q3 12,5; n 8) | 1 h (q1 0,2–q3 2; n 8) |
| t11 Notificar partes para apresentar razões finais | 36% | 3 | 0 du (q1 0–q3 0; n 13) | 1 du (q1 0–q3 4; n 13) | 0,8 h (q1 0,8–q3 1,1; n 13) |
| t12 Relatar, votar e deliberar em sessão | 55% | 4 | 0 du (q1 0–q3 1; n 16) | 1,5 du (q1 0,8–q3 23,2; n 16) | 1,1 h (q1 0,5–q3 17,1; n 16) |
| t13 Publicar deliberação e notificar interessados | 73% | 5 | 0 du (q1 0–q3 0,5; n 19) | 2 du (q1 0,5–q3 4,5; n 19) | 0,1 h (q1 0,1–q3 0,3; n 19) |
| t14 Analisar embargos de declaração | 36% | 3 | 0 du (q1 0–q3 0; n 10) | 9 du (q1 0,2–q3 22,8; n 10) | 5,5 h (q1 4–q3 6; n 10) |
| t15 Decidir pedido de efeito suspensivo | 27% | 2 | 0 du (q1 0–q3 0; n 9) | 4 du (q1 1–q3 8; n 9) | 0,2 h (q1 0,2–q3 3,2; n 9) |

### P21 — Apuração de ocorrência de usuário pelo Conselho-Diretor (procedimento)

11 casos; 11 caminhos distintos (ordem da 1ª ocorrência de cada atividade). Peças substantivas fora do modelo por caso: mediana 0%.

Nenhum caminho se repete entre os casos. Núcleo comum (atividades em metade dos casos ou mais, na ordem do modelo): t1 → t2 → t3 → t4 → t7 → t8 → t9 → t10

| Atividade | Casos | Com laço | Execução | Espera antes | Horas (piso) |
|---|---|---|---|---|---|
| t1 Relatar ocorrência e omissão da concessionária | 91% | 4 | 0 du (q1 0–q3 2; n 17) | 1 du (q1 0–q3 3; n 17) | 1,2 h (q1 0,3–q3 1,8; n 17) |
| t2 Apurar ocorrência e emitir manifestação técnica | 91% | 6 | 0 du (q1 0–q3 0; n 24) | 4 du (q1 1–q3 11; n 24) | 1 h (q1 0,2–q3 3,4; n 24) |
| t3 Notificar concessionária para manifestação | 82% | 4 | 0,5 du (q1 0–q3 10,8; n 22) | 1 du (q1 0–q3 3,8; n 22) | 0,9 h (q1 0,7–q3 1,2; n 22) |
| t4 Analisar descumprimento e opinar sobre sanção | 100% | 2 | 0 du (q1 0–q3 0; n 13) | 51 du (q1 14–q3 84; n 13) | 4 h (q1 4–q3 4; n 13) |
| t5 Solicitar razões finais e dar vista ao usuário | 18% | 0 | 48 du (q1 24–q3 72; n 2) | 69,5 du (q1 56,2–q3 82,8; n 2) | 1 h (q1 0,6–q3 1,5; n 2) |
| t6 Tomar ciência das razões finais | 45% | 2 | 0 du (q1 0–q3 1; n 15) | 4 du (q1 1–q3 35; n 15) | 0,3 h (q1 0,2–q3 0,5; n 15) |
| t7 Sortear relator e distribuir o processo | 100% | 4 | 0 du (q1 0–q3 0; n 20) | 20 du (q1 6,2–q3 30,2; n 20) | 0,2 h (q1 0,2–q3 0,3; n 20) |
| t13 Conceder acesso aos autos | 45% | 2 | 0 du (q1 0–q3 0; n 8) | 1,5 du (q1 0,8–q3 46,5; n 8) | 0,8 h (q1 0,8–q3 0,8; n 8) |
| t8 Notificar concessionária para razões finais | 100% | 3 | 0 du (q1 0–q3 0; n 17) | 24 du (q1 14–q3 43; n 17) | 0,8 h (q1 0,8–q3 0,8; n 17) |
| t9 Relatar, votar e deliberar em sessão | 73% | 4 | 0 du (q1 0–q3 3,5; n 19) | 12 du (q1 7,5–q3 36,5; n 19) | 5,5 h (q1 0,3–q3 6,2; n 19) |
| t10 Publicar deliberação e notificar concessionária | 73% | 3 | 0 du (q1 0–q3 2,8; n 14) | 6 du (q1 0–q3 8; n 14) | 0,3 h (q1 0,1–q3 0,8; n 14) |
| t14 Verificar cumprimento da deliberação | 36% | 2 | 0 du (q1 0–q3 0; n 6) | 0 du (q1 0–q3 0; n 6) | 1 h (q1 1–q3 1,4; n 6) |
| t11 Analisar recurso ou embargos de declaração | 45% | 2 | 0 du (q1 0–q3 0; n 8) | 18,5 du (q1 7,5–q3 34,8; n 8) | 3,5 h (q1 2,8–q3 4; n 8) |
| t12 Encerrar o processo administrativo | 27% | 0 | 0 du (q1 0–q3 0; n 3) | 5 du (q1 3–q3 8; n 3) | 1 h (q1 0,6–q3 1; n 3) |

### P22 — Resposta a órgãos de controle e ao Ministério Público (procedimento)

8 casos; 8 caminhos distintos (ordem da 1ª ocorrência de cada atividade). Peças substantivas fora do modelo por caso: mediana 0%.

Nenhum caminho se repete entre os casos. Núcleo comum (atividades em metade dos casos ou mais, na ordem do modelo): t1 → t2 → t3 → t4 → t5 → t6 → t7

| Atividade | Casos | Com laço | Execução | Espera antes | Horas (piso) |
|---|---|---|---|---|---|
| t1 Atestar descumprimento de prazo da concessionária | 88% | 4 | 1,5 du (q1 1–q3 3; n 12) | 6,5 du (q1 3,5–q3 8,5; n 12) | 0,3 h (q1 0,2–q3 1,3; n 12) |
| t2 Oficiar concessionária com prazo de resposta | 75% | 4 | 0 du (q1 0–q3 3; n 11) | 3 du (q1 2–q3 8; n 11) | 1,2 h (q1 0,8–q3 1,9; n 11) |
| t3 Reiterar prazo de instrução à CASAN | 75% | 4 | 0 du (q1 0–q3 2,5; n 16) | 2,5 du (q1 1–q3 12,2; n 16) | 0,5 h (q1 0,2–q3 1,1; n 16) |
| t4 Analisar denúncia e apurar descumprimento | 75% | 3 | 0 du (q1 0–q3 0; n 11) | 4 du (q1 3–q3 10,5; n 11) | 3,1 h (q1 0,5–q3 4; n 11) |
| t5 Opinar sobre descumprimento e penalidade | 100% | 1 | 0 du (q1 0–q3 0; n 9) | 31 du (q1 14–q3 96; n 9) | 4 h (q1 4–q3 6; n 9) |
| t6 Notificar concessionária para razões finais | 88% | 1 | 0 du (q1 0–q3 0; n 8) | 73 du (q1 39–q3 96,5; n 8) | 0,8 h (q1 0,8–q3 0,8; n 8) |
| t7 Relatar, votar e aplicar penalidade | 50% | 0 | 0 du (q1 0–q3 0; n 4) | 55,5 du (q1 41,2–q3 59,8; n 4) | 7,2 h (q1 5–q3 8,8; n 4) |
| t8 Publicar deliberação e notificar concessionária | 38% | 0 | 6 du (q1 5,5–q3 9,5; n 3) | 6 du (q1 5–q3 6; n 3) | 2,6 h (q1 1,7–q3 3; n 3) |
| t9 Certificar ausência de recurso e encerrar | 12% | 0 | 1 du (q1 1–q3 1; n 1) | 88 du (q1 88–q3 88; n 1) | 1 h (q1 1–q3 1; n 1) |

### P35 — Gestão de interrupções e crises de abastecimento (procedimento)

7 casos; 7 caminhos distintos (ordem da 1ª ocorrência de cada atividade). Peças substantivas fora do modelo por caso: mediana 0%.

Nenhum caminho se repete entre os casos. Núcleo comum (atividades em metade dos casos ou mais, na ordem do modelo): t1 → t2 → t3 → t6 → t7 → t8 → t9 → t10 → t12

| Atividade | Casos | Com laço | Execução | Espera antes | Horas (piso) |
|---|---|---|---|---|---|
| t1 Oficiar concessionária e vistoriar a ocorrência | 71% | 1 | 3,5 du (q1 0–q3 28,8; n 6) | 2 du (q1 1,2–q3 7,2; n 6) | 5,3 h (q1 0,5–q3 13,6; n 6) |
| t2 Analisar justificativa e emitir parecer técnico | 100% | 2 | 0 du (q1 0–q3 0; n 10) | 39,5 du (q1 22,2–q3 104,8; n 10) | 3,6 h (q1 1,5–q3 4,1; n 10) |
| t3 Analisar descumprimento e emitir parecer jurídico | 86% | 3 | 0 du (q1 0–q3 0; n 9) | 29 du (q1 16–q3 85; n 9) | 2 h (q1 1–q3 4; n 9) |
| t4 Complementar análise técnica do descumprimento | 29% | 0 | 0 du (q1 0–q3 0; n 2) | 8 du (q1 4,5–q3 11,5; n 2) | 2 h (q1 1,1–q3 3; n 2) |
| t5 Apurar despesas do sinistro junto à concessionária | 43% | 0 | 0 du (q1 0–q3 117; n 3) | 3 du (q1 2–q3 4; n 3) | 0,1 h (q1 0,1–q3 7,6; n 3) |
| t6 Notificar concessionária para manifestação | 71% | 3 | 0 du (q1 0–q3 3,8; n 12) | 0,5 du (q1 0–q3 3,2; n 12) | 0,8 h (q1 0,4–q3 0,9; n 12) |
| t7 Distribuir ao relator (sorteio ou prevenção) | 86% | 2 | 0 du (q1 0–q3 32; n 9) | 6 du (q1 4–q3 51; n 9) | 0,2 h (q1 0,2–q3 0,4; n 9) |
| t8 Notificar concessionária para razões finais | 71% | 3 | 0 du (q1 0–q3 11,2; n 8) | 3,5 du (q1 0,8–q3 24,8; n 8) | 0,8 h (q1 0,7–q3 1,1; n 8) |
| t9 Relatar, votar e deliberar em sessão | 71% | 1 | 0 du (q1 0–q3 0; n 6) | 58,5 du (q1 14,2–q3 87; n 6) | 6 h (q1 4,6–q3 7,8; n 6) |
| t10 Publicar deliberação e notificar concessionária | 71% | 3 | 1 du (q1 0–q3 2,2; n 8) | 6 du (q1 0,8–q3 7,2; n 8) | 0,6 h (q1 0,2–q3 0,9; n 8) |
| t11 Analisar embargos de declaração | 14% | 0 | 13 du (q1 13–q3 13; n 1) | 24 du (q1 24–q3 24; n 1) | 6 h (q1 6–q3 6; n 1) |
| t12 Registrar cumprimento e encerrar o processo | 71% | 1 | 0 du (q1 0–q3 0,8; n 6) | 0 du (q1 0–q3 0,8; n 6) | 0,6 h (q1 0,5–q3 0,9; n 6) |

