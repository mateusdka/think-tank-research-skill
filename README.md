# Think Tank Research

Uma skill para pesquisar perguntas que exigem mais de um critério de decisão. Lentes metodológicas independentes produzem pareceres; uma etapa de síntese compara evidências, preserva divergências e explicita incertezas antes de recomendar algo.

![Cinco robôs em uma sala de reunião debatendo uma pesquisa](assets/think-tank-research-robots-meeting.png)

## O problema que resolve

Uma resposta única costuma misturar mercado, tecnologia, público, risco e implementação no mesmo raciocínio. Isso dificulta perceber quais critérios sustentam a conclusão e quais objeções foram ignoradas.

A skill separa esses critérios em personas metodológicas. Elas não são personagens: cada uma recebe um mandato, uma lente, limites e um contrato de saída. O relatório final mostra onde os pareceres convergem, onde divergem e qual evidência sustenta cada decisão.

## O que entrega

- brief de pesquisa com escopo e limitações;
- três a sete pareceres especializados;
- mapa de evidências sem contagem duplicada de fontes;
- matriz de convergências e divergências;
- recomendação com condições, lacunas e grau de confiança;
- dois gates separados: evidência e revisão editorial anti-slop.

## Três modos de execução

| Modo | Quando usar | Limitação principal |
|---|---|---|
| Workspace persistente | agentes locais com arquivos e tarefas independentes | depende das ferramentas habilitadas |
| Sandbox | produtos web com arquivos temporários e tarefas | persistência e acesso externo podem ser limitados |
| Sessão única | chats sem subagentes ou filesystem | menor independência entre lentes |

A metodologia exige que o relatório declare qual modo foi usado. Consulte [os modos de execução](references/execution-modes.md).

## Compatibilidade

O núcleo não usa nomes de ferramentas de uma plataforma específica. Adapters traduzem o fluxo para:

- [Hermes Agent](adapters/hermes.md)
- [Codex](adapters/codex.md)
- [Claude Code](adapters/claude-code.md)
- [ChatGPT e Claude.ai](adapters/web-sandboxes.md)

O design é compatível com esses ambientes, mas a disponibilidade de Skills, subagentes, pesquisa externa e arquivos depende do produto, plano e configuração. O estado de homologação por ambiente está em [Estado de maturidade](#estado-de-maturidade).

## Instalação assistida

Copie o endereço deste repositório:

```text
https://github.com/mateusdka/think-tank-research-skill
```

Envie à sua IA com acesso a arquivos:

> Instale a skill Think Tank Research a partir deste repositório. Revise o conteúdo antes de copiar, use o mecanismo de Skills disponível nesta plataforma e valide a descoberta sem executar uma pesquisa completa.

Consulte o adapter da plataforma para definir escopo pessoal ou de projeto.

## Instalação por `.zip`

Para produtos web compatíveis com upload de Skills:

1. baixe `think-tank-research-portable.zip` nos artefatos da versão publicada;
2. confira o SHA-256 em `checksums.txt`;
3. revise os arquivos do pacote;
4. envie o `.zip` pela interface de Skills do produto;
5. valide o acionamento sem iniciar uma pesquisa real.

Se a conta não oferecer upload de Skills, anexe `SKILL.md`, os templates e as referências necessárias à conversa. Use o modo de sessão única.

## Uso básico

Exemplo:

> Use o Think Tank Research para avaliar se uma pequena consultoria deveria oferecer workshops de IA para equipes de marketing no Brasil. O relatório será lido pelos sócios e deve separar demanda, desenho da oferta, risco e teste de mercado.

Uma solicitação melhor informa pergunta, público, recorte geográfico e temporal, fontes disponíveis, profundidade, sensibilidades e formato desejado.

Veja:

- [exemplo de pergunta simples](examples/simple-question.md);
- [exemplo de relatório estratégico](examples/strategic-report.md).

## Anti-AI-slop sem perda factual

O gate editorial foi inspirado na skill pública [`anti-ai-slop`](https://github.com/Hermes-brasil/hermes-brasil/tree/main/skills/anti-ai-slop), do Hermes Brasil. Foram preservadas quatro lentes úteis: léxico, estrutura, tom e semântica.

A adaptação não usa listas de palavras como proibições automáticas. Em pesquisa, “humanizar” um texto não pode criar números, nomes, exemplos ou segurança que as fontes não sustentam. Por isso, a revisão editorial vem depois do gate de evidências e termina com uma comparação de integridade factual.

Leia o [protocolo editorial](references/editorial-review.md).

## Estrutura

```text
.
├── SKILL.md
├── adapters/
├── assets/
├── examples/
├── references/
├── scripts/
├── templates/
├── tests/
├── CHANGELOG.md
├── LICENSE
└── README.md
```

## Validação e pacote

Requer apenas Python 3.9 ou superior.

```bash
python3 scripts/validate_package.py
python3 -m unittest tests/test_package.py -v
python3 scripts/build_distributions.py
```

O último comando cria em `dist/`:

- `think-tank-research-portable.zip`;
- `MANIFEST.txt`, com hashes dos arquivos internos;
- `checksums.txt`, com o SHA-256 do pacote.

O build é determinístico: fontes idênticas produzem o mesmo hash. O pacote portátil contém apenas os arquivos de execução e leitura; scripts e testes permanecem no repositório de desenvolvimento.

Para validar o checksum gerado:

```bash
cd dist
shasum -a 256 -c checksums.txt
```

## Estado de maturidade

**Beta, versão 0.2.1.** Estado por ambiente:

- **ChatGPT web:** homologado ponta a ponta (instalação, descoberta, acionamento e relatório completo com os dois gates);
- **Claude.ai:** homologado ponta a ponta no plano Free, incluindo escolha autônoma do modo de sessão única e relatório conforme o template;
- **Hermes Agent:** instalado e em uso no ambiente do autor, com descoberta e acionamento verificados;
- **Codex e Claude Code:** arquitetura suportada, pendente de homologação ponta a ponta.

## Limites

- Personas simuladas não são especialistas humanos consultados.
- Convergência entre pareceres não substitui confirmação por fontes independentes.
- Sem acesso externo, fatos atuais permanecem não verificados.
- A skill não substitui avaliação profissional em temas médicos, jurídicos, financeiros ou de segurança.
- O modo sequencial tem maior risco de contaminação entre lentes.

## Licença e crédito

MIT. Consulte [LICENSE](LICENSE).

O protocolo editorial adapta princípios da skill `anti-ai-slop`, também publicada sob licença MIT pelo projeto Hermes Brasil. A implementação deste repositório acrescenta proteções específicas para evidências, dados estruturados e incerteza de pesquisa.