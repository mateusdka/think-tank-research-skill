![Think Tank Research — Perspectivas distintas. Compreensão emergente.](assets/TTR-ptbr.png)

<div align="center">
    <h1>Think Tank Research</h1>
</div>

<div align="center">
  <img src="https://img.shields.io/badge/versão-0.2.1--beta-555555" alt="versão">
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/licença-MIT-555555" alt="licença MIT">
  </a>
  <img src="https://img.shields.io/badge/Python-3.9%2B-555555" alt="Python 3.9+">
  <img src="https://img.shields.io/badge/ChatGPT-validado-success" alt="ChatGPT validado">
  <img src="https://img.shields.io/badge/Claude.ai-validado-success" alt="Claude.ai validado">
  <img src="https://img.shields.io/badge/Hermes-validado-success" alt="Hermes validado">
  <div><p><strong>Pesquisa multi-perspectiva para decisões que não deveriam depender de uma única resposta de IA.</strong></p></div>
  </br>
  <a href="README.en.md">
      [ 🇺🇸 English ]
  </a>
  <a href="https://github.com/mateusdka/think-tank-research-skill/releases/download/v0.2.1/think-tank-research-portable.zip">
      [ 📦 Download ]
  </a>    
</div>
</br>

Think Tank Research é um método de pesquisa aberto, empacotado como Agent Skill, para decompor perguntas complexas em lentes analíticas com mandatos distintos, confrontar evidências e divergências e produzir uma síntese com incertezas explícitas.

Em vez de pedir a um único modelo que raciocine simultaneamente sobre mercado, público, viabilidade, risco e implementação, a skill separa esses critérios antes da síntese.

> **O objetivo não é produzir mais opiniões de IA. É tornar o processo de decisão mais inspecionável.**

<div></br></div>

## Índice

**Método** · [Por que construí este projeto](#por-que-construí-este-projeto) · [Como funciona](#como-funciona) · [O que diferencia o método](#o-que-diferencia-o-método) · [Controles de qualidade](#controles-de-qualidade)

**Evidências** · [Teste real em duas plataformas](#teste-real-em-duas-plataformas) · [Compatibilidade e maturidade](#compatibilidade-e-maturidade)

**Implementação** · [Engineering highlights](#engineering-highlights) · [Modos de execução](#modos-de-execução) · [Experimente](#experimente) · [Instalação](#instalação-por-zip) · [Estrutura](#estrutura-do-repositório) · [Validação e pacote](#validação-e-pacote)

**Projeto** · [Limites](#limites) · [Roadmap](#roadmap) · [Contribuições](#contribuições) · [Licença e crédito](#licença-e-crédito)

<div></br></div>

## Por que construí este projeto

Uma resposta única costuma misturar coleta de evidências, interpretação, objeções e recomendação no mesmo raciocínio. Isso dificulta perceber quais critérios sustentam a conclusão, quais perspectivas ficaram de fora, quando repetição está sendo confundida com consenso e quais lacunas deveriam permanecer abertas em vez de serem preenchidas pela IA.

O Think Tank Research experimenta outra arquitetura: cada lente recebe um mandato explícito e um contrato de saída; os pareceres são produzidos antes da síntese; divergências são preservadas; e a revisão factual é separada da revisão editorial.

A hipótese de design é simples: **uma decisão fica mais auditável quando perspectivas diferentes são obrigadas a mostrar seu raciocínio separadamente antes que alguém tente conciliá-las.**

<div></br></div>

## Como funciona

```mermaid
flowchart LR
    A[Pergunta] --> B[Brief]
    B --> C{Lentes}
    C --> C1[A]
    C --> C2[B]
    C --> C3[C]
    C --> C4[D]
    C --> C5[E]
    C1 --> D[Pareceres]
    C2 --> D
    C3 --> D
    C4 --> D
    C5 --> D
    D --> E[Evidências]
    E --> F[Convergências e divergências]
    F --> G[Síntese]
    G --> H[Evidence review]
    H --> I[Editorial review]
```

As personas não são personagens ou vozes fictícias. Cada uma representa uma **lente metodológica** com escopo, responsabilidades, limites e critérios próprios.

A skill entrega brief de pesquisa, três a sete pareceres especializados, mapa de evidências, matriz de convergências e divergências, recomendação condicionada e dois gates de qualidade separados.

<div></br></div>

## Teste real em duas plataformas

Para verificar portabilidade comportamental, a mesma pergunta estratégica foi executada no ChatGPT web e no Claude.ai:

```text
Use o Think Tank Research para avaliar se uma pequena consultoria deveria
oferecer workshops de IA para equipes de marketing no Brasil.

O relatório será lido pelos sócios e deve separar demanda, desenho da oferta,
risco e teste de mercado.
```

```mermaid
flowchart LR
    Q[Pergunta] --> M[Mercado]
    Q --> P[Comprador]
    Q --> O[Oferta]
    Q --> V[Viabilidade]
    Q --> R[Risco]
    M --> S[Síntese]
    P --> S
    O --> S
    V --> S
    R --> S
```

Os relatórios não foram usados para perguntar qual modelo "venceu". O teste observou se runtimes diferentes preservavam os comportamentos centrais do método.

| Comportamento observado | ChatGPT web | Claude.ai |
|---|---|---|
| Skill descoberta e acionada | Sim | Sim |
| Lentes com mandatos distintos | Sim | Sim |
| Limitações do ambiente declaradas | Sim | Sim |
| Evidência separada de inferência | Sim | Sim |
| Divergências preservadas | Sim | Sim |
| Lacunas mantidas como lacunas | Sim | Sim |
| Evidence review | `PASS_WITH_LIMITATIONS` | `PASS_WITH_LIMITATIONS` |
| Editorial review | `PASS` | `PASS` |
| Recomendação condicionada | Sim | Sim |

As duas execuções produziram respostas diferentes, mas preservaram os invariantes centrais. O ChatGPT tornou o teste comercial mais operacional e marcou seus critérios numéricos como hipóteses de gestão, não benchmarks. O Claude formalizou mais o mapa de evidências e descartou explicitamente números incompatíveis de tamanho de mercado. Em ambos os casos, incertezas relevantes permaneceram abertas e a recomendação foi condicionada.

<div></br></div>

**Evidências do teste:**

- [caso de validação e comparação entre ambientes](examples/validation-workshops-ia.md);
- [relatório completo gerado no ChatGPT web](examples/report-chatgpt-workshops-ia.md);
- [relatório gerado no Claude.ai](examples/report-claude-workshops-ia.md);
- [exemplo de pergunta simples](examples/simple-question.md);
- [exemplo de relatório estratégico](examples/strategic-report.md).

<div></br></div>

## O que diferencia o método

| Princípio | Implementação |
|---|---|
| **Lentes com mandatos distintos** | cada parecer recebe escopo e contrato de saída próprios |
| **Divergência é informação** | conflitos relevantes são preservados antes da recomendação |
| **Evidência não é inferência** | o relatório distingue sustentação factual, interpretação, hipótese e opinião estratégica |
| **Síntese não é votação** | convergência entre lentes não é tratada automaticamente como verdade |
| **Escrita não é validação** | revisão de evidências ocorre antes da revisão editorial |
| **Limitações são parte do resultado** | ausência de fonte, baixa confiança e restrições do ambiente são declaradas |
| **Degradação controlada** | ambientes sem subagentes continuam utilizáveis, mas a perda de independência é explicitada |

<div></br></div>

## Controles de qualidade

O método separa dois trabalhos que frequentemente aparecem misturados em fluxos de IA:

```mermaid
flowchart LR
    A[Pareceres] --> B[Síntese] --> C[Evidence review] --> D[Editorial review] --> E[Integridade factual]
```

**Evidence review** verifica sustentação, classificação das afirmações, citações, lacunas, conflitos entre fontes e grau de confiança.

**Editorial review** melhora clareza, concisão, consistência de idioma e legibilidade **sem alterar fatos, números, tabelas ou grau de certeza**.

O protocolo editorial foi inspirado na skill pública [`anti-ai-slop`](https://github.com/Hermes-brasil/hermes-brasil/tree/main/skills/anti-ai-slop), do Hermes Brasil, e adaptado para pesquisa. Leia o [protocolo de evidências](references/evidence-review.md) e o [protocolo editorial](references/editorial-review.md).

<div></br></div>

## Engineering highlights

A entrega principal é uma Agent Skill baseada em instruções e contratos, mas o repositório foi tratado como um pacote de software distribuível e verificável.

- núcleo baseado em **capacidades**, sem nomes de ferramentas proprietárias no método canônico;
- adapters específicos por ambiente;
- três modos de execução e um modo limitado às fontes fornecidas;
- degradação explícita quando subagentes ou filesystem não estão disponíveis;
- templates reutilizáveis para brief, pareceres e relatório final;
- validação estrutural e de privacidade do pacote;
- testes unitários e de contrato;
- build determinístico;
- manifesto interno e checksum SHA-256 do artefato distribuído;
- separação entre fontes de desenvolvimento e pacote portátil.

<div></br></div>

## Modos de execução

| Modo | Quando usar | Limitação principal |
|---|---|---|
| **Workspace persistente** | agentes locais com arquivos e tarefas independentes | depende das ferramentas habilitadas |
| **Sandbox** | produtos web com arquivos temporários e tarefas | persistência e acesso externo podem ser limitados |
| **Sessão única** | chats sem subagentes ou filesystem | menor independência entre lentes |

A metodologia exige que o relatório declare qual modo foi usado. Consulte [os modos de execução](references/execution-modes.md).

<div></br></div>

## Compatibilidade e maturidade

O núcleo não depende de uma plataforma específica. Adapters traduzem capacidades para [Hermes Agent](adapters/hermes.md), [Codex](adapters/codex.md), [Claude Code](adapters/claude-code.md), [ChatGPT e Claude.ai](adapters/web-sandboxes.md).

**Estado atual, versão `0.2.1-beta`:**

| Ambiente | Estado |
|---|---|
| **ChatGPT web** | homologado ponta a ponta: instalação, descoberta, acionamento e relatório completo |
| **Claude.ai (Free)** | homologado ponta a ponta, incluindo escolha autônoma do modo de sessão única |
| **Hermes Agent** | instalado e validado localmente, com descoberta e acionamento verificados |
| **Codex** | arquitetura suportada; homologação ponta a ponta pendente |
| **Claude Code** | arquitetura suportada; homologação ponta a ponta pendente |

Compatibilidade arquitetural não significa que todas as capacidades estejam disponíveis em qualquer conta. Skills, subagentes, pesquisa externa, arquivos e persistência dependem do produto, plano, workspace e configuração.

<div></br></div>

## Experimente

Se sua IA tiver acesso ao GitHub e permissão para instalar Skills, copie o prompt abaixo:

```text
Instale a skill Think Tank Research a partir deste repositório:
https://github.com/mateusdka/think-tank-research-skill

Revise o conteúdo antes de copiar, use o mecanismo de Skills disponível
nesta plataforma e valide a descoberta sem executar uma pesquisa completa.
```

Depois, experimente uma pergunta que realmente exija critérios conflitantes. Por exemplo:

```text
Use o Think Tank Research para avaliar se uma pequena consultoria deveria oferecer
workshops de IA para equipes de marketing no Brasil. O relatório será lido pelos sócios
e deve separar demanda, desenho da oferta, risco e teste de mercado.
```

Uma solicitação melhor informa pergunta, público, recorte geográfico e temporal, fontes disponíveis, profundidade, sensibilidades e formato desejado.

<div></br></div>

## Instalação por `.zip`

Para produtos web compatíveis com upload de Skills:

1. baixe `think-tank-research-portable.zip` nos artefatos da versão publicada;
2. confira o SHA-256 em `checksums.txt`;
3. revise os arquivos do pacote;
4. envie o `.zip` pela interface de Skills do produto;
5. valide o acionamento sem iniciar uma pesquisa real.

Se a conta não oferecer upload de Skills, anexe `SKILL.md`, os templates e as referências necessárias à conversa e use o modo de sessão única. Consulte o adapter da plataforma para instruções específicas.

<div></br></div>

## Estrutura do repositório

```text
.
├── SKILL.md        
├── adapters/        #
├── assets/          #
├── examples/        #
├── references/
├── scripts/
├── templates/
├── tests/
├── CHANGELOG.md
├── LICENSE
└── README.md
```

O `SKILL.md` contém o núcleo portátil. Os adapters traduzem capacidades para ambientes específicos; referências guardam protocolos metodológicos; templates definem contratos reutilizáveis; scripts e testes verificam a distribuição.

<div></br></div>

## Validação e pacote

Requer apenas Python 3.9 ou superior.

```bash
python3 scripts/validate_package.py
python3 -m unittest tests/test_package.py -v
python3 scripts/build_distributions.py
```

O último comando cria em `dist/` o pacote portátil, `MANIFEST.txt` com hashes internos e `checksums.txt` com o SHA-256 do pacote. O build é determinístico: fontes idênticas produzem o mesmo hash.

<div></br></div>

## Limites

- Personas simuladas não são especialistas humanos consultados.
- Convergência entre pareceres não substitui confirmação por fontes independentes.
- Sem acesso externo, fatos atuais permanecem não verificados.
- A skill não substitui avaliação profissional em temas médicos, jurídicos, financeiros ou de segurança.
- O modo sequencial tem maior risco de contaminação entre lentes.
- O método organiza pesquisa e decisão; ele não transforma ausência de evidência em certeza.

<div></br></div>

## Roadmap

- [x] núcleo portátil baseado em capacidades;
- [x] adapters para diferentes ambientes;
- [x] gates separados de evidência e revisão editorial;
- [x] build determinístico e pacote verificável;
- [x] homologação no ChatGPT web;
- [x] homologação no Claude.ai;
- [x] validação no Hermes Agent;
- [ ] homologação ponta a ponta no Codex;
- [ ] homologação ponta a ponta no Claude Code;
- [ ] promoção para versão estável após os gates de compatibilidade.

<div></br></div>

## Contribuições

Contribuições são bem-vindas. O projeto ainda está em beta e há espaço tanto para melhorias metodológicas quanto para validação em novos ambientes.

Alguns pontos especialmente úteis neste momento:

- homologação ponta a ponta no **Codex**, registrando instalação, descoberta, acionamento, modo de execução escolhido e relatório final;
- homologação ponta a ponta no **Claude Code**, com o mesmo protocolo de validação usado nos demais ambientes;
- repetição do caso de workshops no ChatGPT e Claude.ai após mudanças relevantes dos runtimes, para identificar regressões comportamentais;
- novos casos de teste em domínios diferentes, especialmente perguntas com conflito real entre mercado, risco, implementação e evidência;
- testes em **workspaces persistentes com subagentes estruturalmente independentes**, comparados ao modo sequencial;
- automação de CI para validação estrutural, privacidade, build determinístico e integridade do pacote a cada mudança;
- atualização dos adapters quando as plataformas alterarem seus mecanismos de Skills, arquivos, subagentes ou permissões;
- refinamentos de templates e protocolos que reduzam ambiguidades sem tornar o método dependente de um modelo ou provedor;
- documentação de falhas e contraexemplos: casos em que a skill apaga divergências, mistura evidência com inferência ou exagera certeza são tão úteis quanto execuções bem-sucedidas.

Pull requests podem propor código, documentação, adapters, casos de teste ou mudanças metodológicas. Para alterações de comportamento, prefira incluir um exemplo reproduzível ou evidência de validação que demonstre o problema e o resultado esperado.

<div></br></div>

## Licença e crédito

MIT. Consulte [LICENSE](LICENSE).

O protocolo editorial adapta princípios da skill `anti-ai-slop`, também publicada sob licença MIT pelo projeto Hermes Brasil. A implementação deste repositório acrescenta proteções específicas para evidências, dados estruturados e incerteza de pesquisa.
