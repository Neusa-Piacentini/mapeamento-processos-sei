# Fase 1 — piloto de conteúdo (12 processos SEI, 8 processos organizacionais)

30/10/2026 · fluxos AS-IS por processo em `docs/ASIS_PILOTO.md` · planilha `saida/Mapeamento_SEI_Piloto.xlsx`.

## 1. O que foi feito

- **Texto e análises do relator.** Exportados do banco do relator: metadados de 25.781 documentos (398
  processos, 242 dos 251 da carteira), 25.390 análises por documento e o texto integral dos 12 processos-piloto.
- **Ajuste do piloto pela disponibilidade de texto.** Dois casos da seleção anterior não tinham texto: o
  acidente do Leblon (P06), com 49 documentos todos restritos, e o plano de contingência 2021–2022 (P35),
  nunca baixado. A elegibilidade passou a exigir que ao menos 60% das peças substantivas tenham texto.
  O caso típico de P06 passou a exigir relatório de fiscalização ou notificação, porque o primeiro escolhido
  era uma conferência de habilitação de empresas.
- **Autoria.** O editor do SEI gera HTML; PDF é peça de fora juntada (ofício da concessionária, publicação
  do DOERJ, deliberação ou ata copiadas). Exceção: relatórios técnicos e notificações, que as câmaras sobem
  em PDF. Dos 669 documentos do piloto, 155 são externos e só contam como juntada (0,1 h).
- **Ficha de trabalho.** 326 documentos produzidos pela AGENERSA receberam ficha: tarefa, natureza do
  trabalho, entregável, insumos, ferramentas, cálculos, testes, competências com nível, complexidade,
  fração autoral, horas e sinais de perda. Custo da rodada: cerca de US$ 3.

## 2. Esforço: uma faixa, ainda sem calibração

Há duas estimativas por peça, que ordenam os documentos do mesmo jeito (correlação 0,91) mas diferem em
escala:

| Estimativa | Como | Total no piloto | Mediana por processo |
|---|---|---|---|
| Piso | horas atribuídas peça a peça na leitura do documento | 588 h | 34 h |
| Teto | modelo por laudas autorais × complexidade + leitura de insumos + fontes externas | 1.421 h | 91 h |

Um parecer mediano (14 laudas) fica entre 4 h e 14 h; um relatório técnico de reequilíbrio com 47 laudas e
modelagem, entre 40 h e 62 h. O estudo de tempo com as unidades (Fase 2) decide os coeficientes. Mesmo no
teto, a eficiência do ciclo mediana é de 3,4% e 80% do tempo de posse é espera dominante: a conclusão da
Fase 0 se mantém com o esforço medido pelo conteúdo.

## 3. Onde está o trabalho

Pelo teto, 30% das horas são relatoria e decisão (relatórios, votos e deliberações do gabinete), 24% análise
econômico-financeira, 22% análise jurídica e 10% comunicação. Despachos de encaminhamento são 41% dos
documentos produzidos e menos de 5% das horas.

- **Insumos.** Das 79 peças de complexidade 3 ou mais, 68% usam só o próprio processo, contratos e normas, e
  documentos da regulada; 13% recorrem a base externa (índices, dados de sistemas, imprensa, jurisprudência).
- **Ferramentas.** Conferência documental e análise normativa dominam. 24% das peças substantivas fazem algum
  cálculo — concentrado na CAPET (fórmula paramétrica, TIR e fluxo de caixa do reequilíbrio) — e 66% aplicam
  algum teste de conformidade (prazo, cláusula, requisito normativo).
- **Competências por unidade** (planilha, abas de competências):
  - CAPET: econômico-financeira e tarifária em nível especialista; engenharia de saneamento e jurídico em
    nível intermediário.
  - Procuradoria: jurídico-regulatória especialista e redação oficial.
  - Gabinete CONS-02: jurídico-regulatória e econômico-financeira em nível especialista. O voto em reajuste e
    reequilíbrio exige ler e reavaliar o cálculo, não só o mérito jurídico.
  - CAENE e CASAN: engenharia de gás e de saneamento, com auditoria e conferência em nível intermediário.
  - Secretaria Executiva: gestão processual e redação oficial.

## 4. Perdas registradas nas próprias peças

| Sinal | Ocorrências |
|---|---|
| Prazo concedido a terceiros | 85 |
| Diligência externa | 22 |
| Pedido de complementação | 14 |
| Reiteração de pedido não atendido | 10 |
| Aguardando outra unidade | 9 |
| Refazimento | 3 |

Exemplos: o reajuste de 2024 (P01) reitera à FIPE a manifestação sobre o ITS e fica 32 dias úteis no gabinete
nisso; nos dois casos de ocorrência de usuário (P21), as peças registram 15 prazos concedidos.

## 5. O que o piloto mostrou sobre o método

1. **Funciona com conteúdo:** os fluxos reconstruídos têm tarefas nomeadas a partir do que a peça faz
   (por exemplo, "Calcular reajuste tarifário paramétrico do Bloco II", "Reiterar solicitação de manifestação
   à FIPE"), e não só a partir do tipo do documento.
2. **Disponibilidade de texto é critério de seleção:** processos de acidente e de sanção tendem a ser
   restritos. Para eles, o mapa sai da trilha e do tipo de peça, sem ficha.
3. **Autoria precisa do MIME:** sem ele, a Secretaria Executiva aparece produzindo cartas de concessionárias.
4. **Calibrar é o próximo passo:** a faixa de esforço é larga demais para dimensionar equipe; o estudo de
   tempo curto com ~20 peças-tipo (parecer, relatório técnico, voto, ofício, relatório de fiscalização)
   fecha os coeficientes.
