# Fase 0 — trilhas, classificação e seleção do piloto

30/10/2026 · base: 251 processos SEI acompanhados pelo gabinete CONS-02, andamentos até 16/06/2026.
Planilha completa: `saida/Mapeamento_SEI_Fase0.xlsx`. Método: `docs/METODO.md`.

## 1. O que foi reconstruído

| Item | Quantidade |
|---|---|
| Processos | 251 (172 nativos do SEI, 79 físicos migrados com trilha parcial) |
| Andamentos lidos | 19.095 |
| Documentos atribuídos à unidade que os juntou | 12.986 (95% dentro da estadia, 4% na estadia mais próxima, 36 sem estadia) |
| Estadias (passagens por unidade) | 6.795, das quais 4.437 com documento juntado |
| Períodos de posse (partição do tempo sem sobreposição) | gerados para todos os processos (`saida/posse.csv`) |

Exemplo de leitura (SEI-220007/005630/2023, fiscalização da CEG): a CAENE abriu o processo e juntou o
relatório de fiscalização e o termo de notificação em 4 dias úteis; o processo ficou 382 dias úteis
na Procuradoria até o parecer; 31 na Secretaria até ir ao gabinete; 77 no gabinete até voto,
relatório e deliberação; depois publicação, ofício e encerramento. Lead time de 523 dias úteis
para cerca de 39 horas de trabalho estimado.

## 2. Primeiros achados (proxy por tipo de documento; esforço ainda não calibrado)

- **O tempo é espera, não trabalho.** Nos 85 processos nativos e encerrados, o lead time mediano é
  de 561 dias úteis (825 dias corridos) e, em média, 87% do tempo de posse está em períodos de
  espera dominante (≥ 20 dias úteis com trabalho estimado abaixo de 5% da capacidade). A eficiência
  do ciclo mediana é inferior a 1%. Mesmo que as horas-base estejam subestimadas em cinco vezes, a
  conclusão não muda.
- **Onde o processo espera.** Em média, a posse se divide entre gabinetes (41%), Secretaria
  Executiva (20%), câmaras técnicas (19%) e Procuradoria (14%). A Procuradoria tem a maior espera
  até a primeira juntada (mediana de 25 dias úteis; 75% das estadias até 76) e 164 filas longas
  com trabalho curto. O trecho gabinete → Procuradoria leva mediana de 41 dias úteis, contra 28
  quando a remessa vem da Secretaria.
- **Iteração é a regra.** Mediana de 4 retornos a unidades já visitadas por processo (sem contar a
  Secretaria); 76% dos processos nativos têm ao menos um pingue-pongue (A → B → A).
- **Passagens sem trabalho.** 34% das estadias em unidades da AGENERSA não juntam nenhum documento;
  nos gabinetes de outros conselheiros, de 50% a 67% (vistas e consultas).
- **Aguardando terceiros** (ofício ou notificação até a resposta juntada): mediana de 90 dias úteis
  por processo, cerca de 14% do lead time.

## 3. Classificação nos processos organizacionais do diagnóstico

Os 251 processos foram classificados pelo objeto de mérito no inventário P01–P36 (confiança alta
em 138, média em 104, baixa em 9; 209 passam pelo rito decisório, P15).

| Processo organizacional | Processos SEI | Lead time mediano (du, nativos) | Espera dominante (%) |
|---|---|---|---|
| P06 Fiscalização técnica de campo | 32 | 388 | 90 |
| P01 Reajuste tarifário anual | 29 | 398 | 85 |
| P21 Apuração de ocorrência de usuário | 24 | 493 | 87 |
| P04 Homologação de planos de investimento e obras | 23 | 1.049 | 95 |
| P35 Interrupções e crises de abastecimento | 20 | 931 | 90 |
| P08 Monitoramento de metas contratuais e IDG | 18 | 513 | 95 |
| P19 Mercado livre de gás | 16 | 685 | 95 |
| P22 Resposta a órgãos de controle e MP | 12 | 304 | 84 |
| Demais 11 processos do inventário | 49 | — | — |
| Sem correspondência no inventário (lacuna) | 28 | 1.026 | 94 |

**Lacunas do inventário** reveladas pela carteira real, para levar à oficina:
1. Acompanhamento ambiental e de mananciais das concessões (21 processos: crise do Guandu,
   autuações ambientais de INEA, ICMBio e municípios, recursos hídricos, CONAMA nas ETEs).
2. Gestão de bens reversíveis, bens vinculados e comodatos (4).
3. Acompanhamento da aquisição de gás pelas distribuidoras (3).

**Fronteiras a discutir:** P06 × P07 × P21 × P35 (quase toda fiscalização e ocorrência termina em
deliberação que pode sancionar; a sanção decidida no próprio processo de origem não tem etapa
própria); acidentes com gás (hoje em P06; P09 cobre só a inspeção periódica); P22 mistura "responder
ao MP" com "apurar o mérito"; P08 virou "obrigações contratuais em geral" (educação ambiental,
perdas, fraudes); P19 é mais amplo que CUSD e migração; tarifa social dividida entre P01 e P36.

## 4. Processos selecionados para testar o modelo

> **Atualização (30/10/2026, Fase 1):** a seleção abaixo é a primeira versão. Com o texto do relator,
> passou-se a exigir texto em ao menos 60% das peças substantivas e peça de fiscalização no caso típico de
> P06. O piloto final tem 12 processos (`saida/piloto.csv`, `docs/RESULTADOS_PILOTO.md`).

Critérios: nativo do SEI, encerrado, 10 a 150 documentos, ao menos 3 unidades ativas, ao menos uma
peça de análise, nenhum documento sem estadia e classificação de confiança alta ou média (56
elegíveis). Prioridade para a Onda 1 do diagnóstico. Por processo organizacional, um caso
**típico** (lead time mais próximo da mediana do grupo) e, onde há ao menos 4 elegíveis, um caso
**crítico** (mais espera dominante, retornos e espera de terceiros).

| Processo SEI | Processo organizacional | Onda | Caso | Lead time (du) | Docs | Assunto |
|---|---|---|---|---|---|---|
| SEI-480002/001914/2024 | P01 Reajuste tarifário | 1 | típico | 327 | 63 | Reajuste tarifário — IRC e ITS 2024 |
| SEI-220007/004053/2022 | P01 Reajuste tarifário | 1 | crítico | 698 | 66 | Reajuste para vigorar em janeiro de 2023 |
| SEI-480002/005546/2024 | P06 Fiscalização | 1 | típico | 483 | 38 | Fiscalização CAENE — estação de regulagem e medição de Santa Cruz |
| SEI-220007/002058/2021 | P06 Fiscalização | 1 | crítico | 1.026 | 42 | Acidente com duas vítimas fatais no Leblon (monóxido de carbono) |
| SEI-480002/008679/2025 | P36 Regulação comercial | 1 | típico | 166 | 28 | Contrato de grandes usuários Rio+ Saneamento × Ternium |
| SEI-220007/000992/2022 | P35 Crises de abastecimento | 1 | típico | 939 | 128 | Rompimento de adutora em Nova Iguaçu |
| SEI-220007/000856/2020 | P35 Crises de abastecimento | 1 | crítico | 1.315 | 111 | Plano de contingência 2021–2022 |
| SEI-480002/001574/2024 | P21 Ocorrência de usuário | 1 | típico | 469 | 44 | Atraso na análise de tarifa social |
| SEI-220007/001831/2021 | P21 Ocorrência de usuário | 1 | crítico | 964 | 90 | Ocorrência da Ouvidoria em face da CEG |
| SEI-220007/003644/2021 | P08 Metas contratuais | 2 | típico | 910 | 40 | Programa de Educação Ambiental |
| E-22/007.17/2020 | P08 Metas contratuais | 2 | crítico | 1.589 | 31 | Índice de controle de perdas 2019 |
| SEI-220007/001749/2022 | P03 Reequilíbrio | 3 | típico | 710 | 97 | Reequilíbrio econômico-financeiro da concessão |
| SEI-480002/003768/2024 | P22 Órgãos de controle e MP | 3 | típico | 304 | 38 | Abastecimento em Campo Grande — vazamento com reparo moroso |

Todos passam pelo rito decisório, então o piloto também cobre P15. Da Onda 1 ficam de fora P20
(Ouvidoria: os 3 processos da carteira são relatórios semestrais da Ouvidoria ainda em aberto) e
P07 (sanção: dos 4 processos, os encerrados ou têm classificação de confiança baixa ou não têm peça
de análise juntada; os demais seguem abertos). Os dois pedem uma base SEI de outras unidades,
porque o atendimento ao usuário e a cobrança de multa raramente chegam à relatoria.

## 5. Próximo passo: piloto de conteúdo

1. Exportar do banco do relator os metadados por documento (MIME, nº de caracteres, restrição), as
   análises map-v3 e o texto integral dos 13 processos (`scripts/exportar_relator.py
   --texto-piloto`). Depende da URL pública do Postgres.
2. Gerar a ficha de trabalho das peças substantivas (insumos, ferramentas, competências,
   complexidade, fração autoral, sinais de perda) e recalcular o esforço por laudas.
3. Montar o AS-IS dos 8 processos organizacionais do piloto (variantes, grafo de sucessão, BPMN com
   tempos e perdas) e levar às unidades para validação e para o estudo de tempo curto que calibra
   as horas.
