# Mapeamento do processo SEI-480002/001314/2024

Estudo de caso único da metodologia do curso, aplicada ao processo **SEI-480002/001314/2024** (Agenersa: Fiscalização; interessada: Concessionária Iguá Rio de Janeiro S.A.), classificado como **P06 — Fiscalização técnica de campo (programada e por demanda)**. Fonte: Pesquisa Pública do SEI-RJ. Gerado por `scripts/relatorio_caso.py` a partir das saídas validadas.

> **Ressalvas.** Um caso só: medianas são o próprio caso, nada aqui é padrão do tipo de processo. Horas de trabalho são estimativa por peça (hipótese, a calibrar com os servidores). O volume anual do tipo não foi medido, então não há totais anuais, FTE nem R$. As paradas de validação humana do roteiro estão pendentes.

## 1. Base e trilha (fase 0)

| Indicador | Valor |
|---|---|
| Gerado em | 2024-02-07 |
| Último andamento (corte) | 2026-08-28 12:26:00 |
| Situação | aberto (sobrestado no último andamento) |
| Lead time | 636 du (933 dias corridos) |
| Documentos / processos anexados | 75 / 8 |
| Relatórios de fiscalização / pareceres / ofícios | 42 / 2 / 12 |
| Sequência de unidades ativas | CASAN → SCEXEC → CASAN → SCEXEC → PROC → SCEXEC |
| Espera entre atividades / execução | 552 du / 84 du |
| Espera de resposta da concessionária (confirmada) | 138 du |
| Indeterminado (não separável de processo parado) | 41 du |

Posse por unidade (du): CARES 0; CASAN 70; PROC 203; SCEXEC 57; SEM UNIDADE 306.

Estadias: 10 (8 com trabalho). Tabelas: `saida/estadias.csv`, `posse.csv`, `documentos.csv`, `janelas_terceiros.csv`, `processos_indicadores.csv`.

## 2. Conteúdo, esforço e modelo (fase 1)

- Fichas de trabalho: 60 peças próprias da agência (`saida/fichas_trabalho.jsonl`), evidência ancorada literalmente no texto.
- Auditoria automática: números sem âncora nas fichas 0,7% (critério ≤ 1%); posse sem lacuna nem sobreposição (0 casos com problema).
- Auditoria às cegas de 30 fichas (261 afirmações): sem lastro ou contradita 1,92% (≤ 2%), imprecisa 4,21% (≤ 10%).
- Trabalho estimado no caso: 297,7–480,3 h (hipótese).

**Modelo BPMN AS-IS** (`saida/bpmn/P06.bpmn`, visualizador em `docs/bpmn/index.html`): 14 elementos, raias CASAN, SCEXEC, PROC, EXT.

| Tarefa | Raia | Peças vinculadas | Gatilho → saída |
|---|---|---|---|
| t1 Agendar vistoria com a concessionária | CASAN | 8 | Unidades do município ou região incluídas no ciclo anual de vistorias → Ofício à concessionária com unidades, datas e ponto de encontro da vistoria |
| t2 Vistoriar unidade e emitir relatório de fiscalização | CASAN | 42 | Vistoria in loco realizada em estação de tratamento ou elevatória → Relatório de fiscalização com não conformidades, recomendações e checklist |
| t3 Encaminhar lote de relatórios à concessionária | CASAN | 14 | Conjunto de relatórios de fiscalização concluído → Ofício com os relatórios anexos e prazo para manifestação sobre as recomendações |
| t4 Analisar providências e emitir parecer técnico | CASAN | 2 | Respostas da concessionária a todos os lotes de relatórios do ciclo → Parecer técnico sobre o atendimento das recomendações das vistorias |
| t5 Dar ciência do parecer à concessionária | SCEXEC | 4 | Parecer técnico ou jurídico concluído e devolvido à Secretaria → Manifestação ou ofício à concessionária com o parecer anexo |
| t6 Responder contestação da concessionária | CASAN | 2 | Manifestação da concessionária contra o parecer técnico encaminhada pela Secretaria → Despacho técnico que reitera o parecer e rebate a tese da concessionária |
| t7 Emitir parecer jurídico sobre a fiscalização | PROC | 2 | Controvérsia sobre o alcance da fiscalização encaminhada pela Secretaria → Parecer jurídico sobre a regularidade e o alcance da atuação fiscalizatória |

## 3. Avaliação AS-IS

Situação do código: estudo de caso. A coorte tem um único processo, nativo do SEI (SEI-480002/001314/2024, fiscalizações programadas de 2024 nas unidades da Águas do Rio – Bloco 1), com um só caminho e sem auditoria de classificador; a mediana de um caso nativo é o próprio caso, e nada aqui autoriza generalizar para o tipo de processo. O trabalho é pequeno diante do tempo: 297,7–480,3 h de trabalho estimado (hipótese, a calibrar com servidores) para um lead time de 636 du, dos quais 552 du são espera entre atividades e 84 du, execução das atividades. Dois blocos concentram a espera: 306 du sem nenhuma unidade com o processo aberto, que não se separam de processo parado (e incluem prazos dados à concessionária, que não são desperdício), e 203 du com a Procuradoria antes do Parecer 759/2025, assinado em 28/08/2026 (a data no corpo da peça é 25/06/2026), no mesmo dia em que o processo foi sobrestado. A concessionária contestou o alcance da fiscalização, e o processo terminou sobrestado, sem encerramento. A IA ajuda na conferência e na redação das peças e no controle de prazos; reduzir a espera depende de dar dono, marco e prazo-alvo a cada etapa, sobretudo à fila da Procuradoria.

**Gargalo.** A fila na Procuradoria antes do Parecer 759/2025: é a maior posse por unidade do caso e a maior espera antes de uma atividade, e vem depois de esperas sem nenhuma unidade com o processo antes do parecer técnico e antes da resposta à contestação, e de uma espera com a Secretaria antes da primeira ciência. Não há como saber, só pela linha do tempo, se foi fila de carga, pendência de diligência ou parecer pronto aguardando assinatura.

A espera antes da ciência do parecer jurídico é de 205 du, das quais 203 du com a Procuradoria e 2 du com a Secretaria; o Parecer 759/2025 e a ciência saem em 28/08/2026, de modo que a espera aparece antes da ciência (antes do parecer, o fato registra 0 du). A data no corpo do parecer é 25/06/2026, diferente da assinatura, o que sugere intervalo de assinatura ou de juntada a confirmar com a Procuradoria. A segunda maior espera é de 106 du sem nenhuma unidade com o processo aberto, entre a última remessa de relatórios à concessionária, em 30/01/2025, e o Parecer CASAN 250/2025, de 08/07/2025: não se separa processo parado de prazo dado à concessionária. Entre as esperas ligadas a este trecho do fluxo há ainda 55 du com a Secretaria antes da ciência do parecer técnico e 24 du sem unidade antes da resposta à contestação (a lista não inclui as esperas entre vistorias).

| Desperdício | Severidade | Evidência |
|---|---|---|
| Espera | alta | Quatro esperas concentram o tempo antes de atividades decisórias: 203 du com a Procuradoria antes da ciência do parecer jurídico, 106 du sem unidade antes do parecer técnico, 55 du com a Secretaria antes da ciência do parecer técnico e 24 du sem unidade antes da resposta à contestação. A parte sem unidade não se separa de processo parado e contém prazo dado à concessionária (30 dias nos ofícios de lote), que não é desperdício; a parte com a Procuradoria e com a Secretaria é fila interna. |
| Estoque | alta | Foram 306 du sem nenhuma unidade com o processo aberto, quase metade do lead time de 636 du, e o processo terminou sobrestado, sem ato final. Parte desse tempo é o intervalo programado entre vistorias do ciclo anual (planejamento, não desperdício) e parte é o prazo dado à concessionária; o registro não separa essas partes de processo parado. Os blocos mais longos sem dono são os 28 du antes de uma vistoria e os 27 du antes de outra, no ciclo, e os 106 du antes do parecer técnico. |
| Defeitos/retrabalho | média | Os relatórios de fiscalização têm defeitos de conteúdo que exigem conferência e podem exigir correção: trechos de outro caso no texto-padrão (município de Pomerode, a CEDAE, Bloco 04) e divergências entre o corpo e o checklist anexo nas peças SEI 74334571, SEI 79900134, SEI 80656240, SEI 79901118, SEI 74882333, SEI 72975320, SEI 86826664, SEI 86827856, SEI 82895573, SEI 79575319 e SEI 79573103; a peça SEI 89901514 indica outro número de processo (SEI-480002/001547/2024); e a peça SEI 68285969, juntada como Deliberação, é a compilação do Diário Oficial com a Deliberação 4.216/2021. A ficha registra sinal de pedido de complementação, de prazo concedido e de reiteração na vistoria e o impacto sobre o prazo é a medir. |
| Transporte | média | O processo teve 6 passagens entre unidades, e a Secretaria ficou 57 du com ele, inclusive 55 du antes de dar ciência do parecer técnico, em despacho de 0,6–0,8 h por ocorrência nos casos nativos. Houve ainda uma passagem pela CARES, em 20/05/2024, sem peça, com 0 du de posse: passagem sem trabalho visível. |
| Movimentação | média | As respostas da concessionária entram como processos anexados, sem peça própria na árvore: para saber quando e o que a concessionária respondeu a cada lote, é preciso abrir esses processos. A espera de resposta da concessionária só é medida pela data de juntada desses processos (138 du no caso), e 41 du ficam indeterminados, não separáveis de processo parado. |
| Superprocessamento | baixa | Cada relatório de fiscalização traz corpo e checklist anexo, e as divergências entre os dois (peças citadas no desperdício de defeitos) sugerem preenchimento em duplicidade, hipótese a confirmar. O total de 272 laudas de relatórios em 8 ocorrências de vistoria tem mediana de 30,5–49,2 h por ocorrência nos casos nativos, e a ciência do parecer, por ocorrência, mobiliza peça de 4 laudas no total. A fração do esforço que é duplicidade é a medir. |
| Talento não aproveitado | baixa | Os ofícios de lote, de redação padronizada, ficam com gerente: mediana de 0,8–1,1 h por ocorrência nos casos nativos, em 7 ocorrências, assinados por gerentes (7 assinaturas na ficha). Um modelo de ofício liberaria o gerente para a análise técnica, hipótese a confirmar. |

| Oportunidade | Categoria | Impacto | Esforço |
|---|---|---|---|
| Fila de pareceres da Procuradoria com marco de entrada, prazo-alvo e alerta de idade | IA + Lean | alto | baixo |
| Dono e marco para o processo entre as etapas, com alerta de processo sem unidade e sem ato final | IA + Lean | alto | baixo |
| Registro e vínculo da resposta da concessionária no processo principal no dia em que chega | Lean | médio | baixo |
| Ciência do parecer no dia da assinatura, sem passagem da Secretaria só para encaminhar | Lean | médio | baixo |
| Conferência automática do relatório de fiscalização antes da assinatura | IA | médio | médio |
| Quadro de atendimento das recomendações e minutas de parecer técnico e jurídico a partir dos autos | IA | médio | médio |
| Calendário do ciclo anual com ofícios de agendamento e de lote por modelo | Lean | baixo | baixo |

Verificação independente da avaliação: 76 afirmações, 73 corretas, 3 imprecisas (corrigidas antes do carimbo), 0 alucinações. Avaliação carimbada contra os fatos (4a6b7823ce862213).

## 4. Conformidade legal (fase 3)

| Requisito | Exigência | Teste | Resultado |
|---|---|---|---|
| R-P06-01 | A concessionária é vistoriada em suas estações de tratamento ao menos uma vez por ano, conforme cronograma. | manual | manual (não computado) |
| R-P06-02 | Antes da vistoria programada, a concessionária recebe Aviso de Fiscalização com antecedência mínima de 48 horas. | manual | manual (não computado) |
| R-P06-03 | Toda vistoria concluída gera Relatório de Fiscalização com determinações e recomendações à concessionária. | manual | manual (não computado) |
| R-P06-04 | O Relatório de Fiscalização chega ao Gerente da Câmara Técnica em até 5 dias úteis da lavratura. | manual | manual (não computado) |
| R-P06-05 | O ofício que encaminha o lote de relatórios concede à concessionária ao menos 30 dias para manifestação sobre as recomendações. | prazo_concedido_min | 100% conforme |
| R-P06-06 | Entre o último ofício de lote e o parecer técnico decorrem ao menos 30 dias, que são o prazo de manifestação da concessionária. | prazo_min | 100% conforme |
| R-P06-07 | A concessionária é cientificada do parecer técnico depois da sua emissão, para poder contestar. | precede | 100% conforme |
| R-P06-08 | Todo parecer técnico é seguido de ciência à concessionária. | exige | 100% conforme |
| R-P06-09 | O parecer jurídico é emitido em até 15 dias da resposta técnica que o motivou. | prazo_max | 0% conforme |
| R-P06-10 | Os prazos para falar nos autos e cumprir providência processual são contados em dias úteis. | manual | manual (não computado) |
| R-P06-11 | Se houver Notificação de Infração, a concessionária tem 30 dias para defesa prévia, e o Gerente da Câmara Técnica analisa a defesa em até 15 dias, prorrogáveis por igual período. | manual | manual (não computado) |

Normas: 11 (4 de fonte externa, a conferir à mão: Lei estadual nº 4.556/2005 art. 4º, IV; Lei estadual nº 5.427/2009 (processo administrativo do Estado do Rio de Janeiro) art. 69; Regimento Interno da AGENERSA (Resolução CODIR nº 394/2013, texto consolidado) art. 17, VI; Lei estadual nº 9.789/2022 art. 4º (nova redação do art. 67, § 2º, I, da Lei nº 5.427/2009)). Trechos literais conferidos por `verificar_normas.py`. Interpretações a validar com a Procuradoria em `normas_P06.json` → `interpretacao`.

## 5. TO-BE e simulação (fase 3)

| Melhoria | Fase | Título | Hipótese |
|---|---|---|---|
| M-P06-01 | 1 | Prazo-alvo e fila por idade na Procuradoria para o parecer jurídico e ciência do parecer no dia da assinatura | sim |
| M-P06-02 | 1 | Dono e marco para o processo entre o último ofício de lote e o parecer técnico, com início da análise contado do fim do prazo da concessionária | sim |
| M-P06-03 | 1 | Prazo-alvo para a resposta à contestação, com alerta de chegada da manifestação | sim |
| M-P06-04 | 1 | Ofício de lote expedido em prazo interno depois do último relatório, com o prazo de 30 dias da concessionária mantido | sim |
| M-P06-05 | 1 | Modelo único de relatório de fiscalização e checklist como fonte única, com lista de conferência antes da assinatura | sim |
| M-P06-06 | 2 | Painel de idade do processo por unidade, de processo sem unidade e sem ato final e de prazos dados à concessionária, com alerta de vencimento | sim |
| M-P06-07 | 2 | Ciência do parecer disparada na assinatura por modelo, com alerta de parecer assinado sem ciência | sim |
| M-P06-08 | 2 | Calendário do ciclo anual de vistorias com alerta de unidade sem agendamento e de vistoria fora da janela | sim |
| M-P06-09 | 2 | Ofícios de agendamento, de lote e de ciência por modelo, com campos preenchidos dos dados do processo e prazo calculado em dias úteis | sim |
| M-P06-10 | 2 | Conferência por regra do relatório de fiscalização antes da assinatura (termos de outro caso, número de processo e campos obrigatórios) | sim |
| M-P06-11 | 3 | Minuta do relatório de fiscalização a partir do checklist e conferência assistida do corpo contra o checklist e o processo | sim |
| M-P06-12 | 3 | Quadro de atendimento das recomendações e minuta do parecer técnico e do despacho de resposta à contestação a partir dos autos | sim |
| M-P06-13 | 3 | Minuta do parecer jurídico com linha do tempo dos atos do ciclo e dispositivos citados verificados contra a base | sim |

| Fase | Lead (du), conservador / esperado / otimista | Horas piso–teto (esperado) | Ganho de lead (esperado) |
|---|---|---|---|
| AS-IS | 636 | 297,1–479,9 | — |
| 1 | 452 / 360 / 301 | 276,2–445,1 | 43,4% |
| 2 | 408 / 320 / 269 | 267,8–432,9 | 49,7% |
| 3 | 408 / 320 / 269 | 235,2–380,3 | 49,7% |

Maior peso na sensibilidade (piora do lead mediano sem a melhoria, fase 3, esperado): M-P06-01 +100 du; M-P06-07 +30 du; M-P06-04 +11 du. São as que mais precisam de validação com a unidade dona (PARADA 8).

## 6. Controles e metas

| Indicador | Linha de base | Metas por fase |
|---|---|---|
| I-P06-01 Lead time do primeiro relatório de fiscalização do ciclo à última atividade registrada | 636.0 du | f1: 360.0 (simulacao); f2: 320.0 (simulacao); f3: 320.0 (simulacao) |
| I-P06-02 Parecer jurídico em até 15 dias úteis da resposta técnica | 0.0 % conforme | f1: 0.0 (simulacao); f2: 100.0 (simulacao); f3: 100.0 (simulacao) |
| I-P06-03 Espera antes da ciência do parecer à concessionária | 205.0 du (ocorrência de maior espera) | f2: 15.0 (norma) |
| I-P06-04 Espera antes do parecer técnico depois do prazo dado à concessionária | 106.0 du (inclui o prazo da concessionária) | f3: 30.0 (norma) |
| I-P06-05 Prazo de manifestação do ofício de lote: mínimo de 30 dias à concessionária | 100.0 % conforme | f1: 100.0 (norma); f2: 100.0 (norma); f3: 100.0 (norma) |
| I-P06-06 Parecer técnico só depois do prazo da concessionária e ciência de todo parecer técnico | 100.0 % conforme | f1: 100.0 (norma); f2: 100.0 (norma); f3: 100.0 (norma) |
| I-P06-07 Qualidade do relatório de fiscalização: texto de outro caso, divergência entre corpo e checklist e retrabalho na vistoria | 1 casos com sinal de reiteração na vistoria (em 1) | f2: 1 (benchmark); f3: 1 (benchmark) |
| I-P06-08 Horas de trabalho por processo | 297.0 h por processo (piso) | f1: 276.2 (simulacao); f2: 267.8 (simulacao); f3: 235.2 (simulacao) |

Controles de qualidade da IA: Q-P06-01, Q-P06-02, Q-P06-03. Auditoria contínua: A-P06-01, A-P06-03, A-P06-04.

## 7. Priorização da automação (fase 4)

Prioridade na matriz: **reavaliar com dados** — com um caso e sem volume medido, os portões volume_medido, nota_volume, casos_coorte não passam. Capacidades de IA aplicáveis: automação de tramitação (RPA no SEI), busca de precedentes e normas, extração de dados de documentos, monitoramento de prazos e alertas, redação assistida de minuta, sumarização e linha do tempo, verificação de conformidade. A escolha do piloto do sistema é da gestão (PARADA 10).

## 8. Perguntas de validação (paradas pendentes)

1. Nos 203 du com a Procuradoria, houve diligência, fila de carga ou parecer pronto aguardando assinatura (a data no corpo do Parecer 759 é 25/06/2026 e a assinatura é 28/08/2026)?
2. O que o processo aguardava entre a última remessa de relatórios (30/01/2025) e o Parecer CASAN 250/2025 (08/07/2025): prazo dado à concessionária, análise ou nada? Quem era o dono do processo nesse intervalo?
3. Dos 306 du sem unidade, quanto é intervalo programado do ciclo anual e quanto é processo parado?
4. Onde se vê a data de cada resposta da concessionária (processos anexados sem peça própria) e o que ela respondeu a cada lote?
5. Como os trechos de outro caso (Pomerode, CEDAE, Bloco 04) entraram nos relatórios, quem confere o texto antes da assinatura e os relatórios foram corrigidos? A peça SEI 89901514, com outro número de processo (SEI-480002/001547/2024), foi juntada por engano?
6. A peça SEI 68285969, juntada como Deliberação, é a compilação do Diário Oficial de 2021: qual é o ato que fundamenta o ciclo de fiscalização e deve constar do processo?
7. Os 55 du com a Secretaria antes da ciência do parecer técnico correspondem a alguma conferência ou são só fila?
8. Por que o processo passou pela CARES em 20/05/2024 sem peça?
9. A contestação sobre o alcance da fiscalização é frequente? Há posição institucional ou modelo de resposta?
10. Qual é o critério de sobrestamento (28/08/2026), quem acompanha as providências depois e o que dispara a retomada?
11. As horas estimadas (inclusive o piso acima do teto no parecer técnico) conferem com a experiência dos servidores? Calibrar antes de qualquer estimativa de ganho.

## 9. Mapa das saídas

| Fase | Arquivos |
|---|---|
| 0 | `saida/estadias.csv`, `posse.csv`, `documentos.csv`, `janelas_terceiros.csv`, `processos_indicadores.csv`, `classificacao_processos.csv`, `Mapeamento_SEI_Fase0.xlsx` |
| 1 | `saida/fichas_trabalho.{csv,jsonl}`, `esforco_documentos.csv`, `Mapeamento_SEI_Piloto.xlsx`, `bpmn/{evidencias,modelo,vinculos,fatos,fichas,avaliacao}_P06.*`, `bpmn/P06.bpmn`, `docs/ASIS_PILOTO.md`, `docs/AVALIACAO_ASIS.md` |
| 2 | `saida/coorte_fase2.csv`, `fase2/{atribuicoes,procedimento,casos}_P06.*`, `docs/RESULTADOS_FASE2.md` |
| 3 | `saida/fase3/{normas,conformidade,linha_base,insumo_tobe,melhorias,resultado_tobe,controles}_P06.*`, `fase3/benchmark/`, `docs/BENCHMARKING.md` |
| 4 | `saida/fase4/matriz_automacao.*`, `capacidades_transversais.csv`, `Priorizacao_Automacao.xlsx`, `docs/PRIORIZACAO_AUTOMACAO.md` |
| Auditoria | `saida/auditoria/auditoria_automatica.json`, `auditoria_fichas.json`, `verificacao_avaliacao_P06.json`, `saida/pipeline_execucao.json` |
| Site | `docs/site/index.html` |
