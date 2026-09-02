# Revisão editorial anti-slop

Este protocolo adapta princípios da skill pública `anti-ai-slop`, do projeto Hermes Brasil, ao gênero específico de relatórios de pesquisa. A referência inspirou as quatro camadas de análise: léxico, estrutura, tom e semântica.

Execute esta revisão somente depois da revisão de evidências.

## Regra central

Melhore a prosa sem alterar o conteúdo analítico. Não invente nomes, datas, números, exemplos, fontes ou detalhes para fazer o texto parecer mais concreto. Especificidade só entra quando existe no material pesquisado.

## 1. Léxico

Procure sinais contextuais, não uma lista automática de palavras proibidas:

- verbos vagos que escondem a ação real;
- adjetivos promocionais sem critério observável;
- conectores usados como preenchimento;
- hedges repetidos que não correspondem a uma incerteza real;
- jargão que poderia ser substituído por uma descrição precisa.

Termos como “robusto”, “inovador”, “transformar”, “estratégico” ou “significativo” podem ser necessários. Mantenha-os apenas quando o texto disser em que sentido e com qual evidência.

## 2. Estrutura

- Mantenha headings, listas, matrizes e tabelas quando ajudam a consultar o relatório.
- Corte seções que apenas repetem títulos ou conclusões anteriores.
- Evite a mesma cadência em todos os pareceres.
- Não force variedade numérica em listas nem mudanças artificiais no comprimento das frases.
- Não transforme informação comparável em prosa apenas para parecer mais humana.

Relatório técnico não deve perder navegabilidade para satisfazer uma regra estética.

## 3. Tom

Remova:

- entusiasmo performático;
- elogios automáticos à pergunta ou ao usuário;
- otimismo obrigatório no encerramento;
- falsa segurança;
- ressalvas defensivas sem função;
- linguagem promocional disfarçada de análise.

Não substitua incerteza legítima por opinião categórica. O grau de compromisso verbal deve seguir o gate de evidências.

## 4. Semântica

Questione cada parágrafo:

- há um achado, argumento, contraste ou consequência identificável?
- a frase seria verdadeira em quase qualquer tema?
- uma abstração está escondendo a falta de exemplo ou evidência?
- a conclusão acrescenta algo à matriz de evidências?
- o texto confunde convergência entre personas com confirmação externa?

Corte truísmos, definições circulares e conclusões que apenas repetem o sumário.

## Proteções para dados e divergências

Não “humanize”:

- dados estruturados;
- valores, percentuais, datas ou unidades;
- nomes de fontes;
- citações;
- rótulos de evidência;
- níveis de confiança;
- divergências preservadas;
- condições e limitações da recomendação.

Se uma edição afetar qualquer item acima, volte ao material de origem e valide a mudança.

## Self-check

- [ ] O lead apresenta a pergunta ou o achado, sem introdução genérica.
- [ ] Cada seção desempenha uma função diferente.
- [ ] Adjetivos importantes têm critério ou evidência.
- [ ] As conclusões não prometem mais do que a pesquisa sustenta.
- [ ] A prosa diferencia fato, inferência, hipótese e recomendação.
- [ ] Nenhuma edição criou precisão inexistente.
- [ ] Nenhuma divergência foi apagada por conveniência narrativa.
- [ ] Tabelas e números permanecem idênticos às versões aprovadas no gate anterior.

## Extensão opcional

Se o ambiente tiver uma skill editorial confiável, ela pode ser carregada como segunda leitura. Trate suas regras como heurísticas subordinadas ao gênero do documento e às proteções deste protocolo.

## Saída do gate

Registre:

- `EDITORIAL_REVIEW: PASS`
- `EDITORIAL_REVIEW: PASS_WITH_NOTES`, seguido das notas
- `EDITORIAL_REVIEW: FAIL`, seguido dos trechos bloqueadores

Finalize com uma verificação de integridade factual comparando a versão editada à versão aprovada na revisão de evidências.

Fonte de referência consultada em 2026-09-02: https://github.com/Hermes-brasil/hermes-brasil/tree/main/skills/anti-ai-slop
