# Capacidades por ambiente

Esta matriz orienta a escolha de modo. Confirme as capacidades na sessão atual; planos e produtos mudam.

| Ambiente | Instalação | Arquivos | Execução independente | Modo recomendado |
|---|---|---|---|---|
| Hermes Agent | skill pessoal ou de perfil | workspace local | subagentes quando habilitados | workspace persistente |
| Codex | instalador de skills ou recurso equivalente | workspace local/projeto | conforme a superfície e configuração | workspace persistente |
| Claude Code | skill pessoal ou de projeto | workspace local/projeto | conforme as ferramentas habilitadas | workspace persistente |
| Claude.ai/Cowork | upload de `.zip`, quando elegível | sandbox ou pasta autorizada | conforme o produto | sandbox ou sessão única |
| ChatGPT | upload/criação de Skill, quando elegível | ambiente controlado pelo produto | conforme o produto | sandbox ou sessão única |
| Chat sem suporte a Skills | instruções anexadas | contexto e anexos | não garantido | sessão única |

## Princípios

- Instalação não garante ferramentas de pesquisa, arquivos ou subagentes.
- Acesso a um repositório não implica acesso às pastas locais do usuário.
- Arquivos de sandbox não devem ser descritos como persistentes sem confirmação.
- Um conector disponível não deve ser usado sem necessidade e autorização.
- Compatibilidade anunciada exige teste real naquele ambiente.

## Verificação de capacidade

Antes da pesquisa, responda internamente:

1. Posso criar tarefas ou agentes independentes?
2. Posso executar essas tarefas em paralelo?
3. Posso gravar e reler arquivos?
4. Esses arquivos persistem depois da sessão?
5. Posso consultar fontes externas ou somente anexos?
6. O usuário autorizou o uso das fontes e conectores disponíveis?

Escolha o modo de execução pelo conjunto confirmado de respostas.

## Fontes de compatibilidade

Consultadas em 2026-09-02:

- OpenAI, Skills in ChatGPT: https://help.openai.com/en/articles/20001066-skills-in-chatgpt
- OpenAI, Build skills for ChatGPT and Codex: https://learn.chatgpt.com/docs/build-skills
- Anthropic, Agent Skills: https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview
- Anthropic, Skills no Claude Code: https://code.claude.com/docs/en/skills
