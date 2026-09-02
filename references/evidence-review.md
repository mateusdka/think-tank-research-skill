# Revisão de evidências

Execute este gate depois da síntese e antes da revisão editorial.

## Objetivo

Confirmar que a força verbal do relatório corresponde à força das evidências. Repetição entre personas não transforma uma afirmação sem fonte em fato.

## Classificação das afirmações

- **Evidência:** sustentada diretamente por fonte inspecionada ou material fornecido.
- **Inferência:** conclusão raciocinada a partir de evidências identificadas.
- **Hipótese:** explicação plausível ainda não confirmada.
- **Opinião estratégica:** juízo ou recomendação para orientar uma decisão.

## Hierarquia prática de fontes

A força depende do problema, mas considere:

1. documento, dado ou registro primário pertinente;
2. documentação oficial e bases com método transparente;
3. pesquisa acadêmica ou técnica revisável;
4. fonte secundária especializada com autoria e data;
5. relato, opinião ou conteúdo sem método verificável.

Atualidade, independência, conflito de interesse e aderência geográfica também alteram o peso.

## Checklist

- [ ] Toda afirmação decisiva tem fonte, rótulo de inferência ou ressalva explícita.
- [ ] Toda fonte citada foi realmente inspecionada.
- [ ] Links, títulos, autores e datas correspondem ao material usado.
- [ ] Números preservam unidade, período, população e contexto.
- [ ] As personas não foram contadas como fontes independentes quando reutilizaram a mesma origem.
- [ ] Divergências relevantes continuam visíveis.
- [ ] Ausência de dados aparece como lacuna, não como confirmação.
- [ ] O grau de confiança tem justificativa.
- [ ] Recomendações indicam condições, dependências e riscos quando necessários.

## Correção

Se uma afirmação exceder a evidência disponível, escolha uma ação:

- localizar sustentação adequada;
- rebaixar para inferência ou hipótese;
- restringir o escopo;
- remover a afirmação;
- manter como pergunta em aberto.

Não aumente confiança apenas porque várias personas chegaram à mesma conclusão.

## Saída do gate

Registre um resultado:

- `EVIDENCE_REVIEW: PASS`
- `EVIDENCE_REVIEW: PASS_WITH_LIMITATIONS`, seguido das limitações
- `EVIDENCE_REVIEW: FAIL`, seguido dos bloqueios

Um relatório com `FAIL` não pode ser apresentado como conclusão validada.
