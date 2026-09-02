# Adapter para Codex

## Instalação assistida

Envie o endereço do repositório ao Codex e peça:

> Instale a skill `think-tank-research` para uso pessoal a partir deste repositório. Revise o conteúdo, use o instalador de skills disponível e valide a descoberta sem executar uma pesquisa real.

O Codex documenta o uso do `$skill-installer` para recursos locais e a instalação a partir de outros repositórios. Skills pessoais são descobertas em `$HOME/.agents/skills`; Skills de repositório, em `.agents/skills` do diretório atual ou de seus pais até a raiz. Se a superfície atual não oferecer o instalador, use o escopo local documentado pelo produto.

## Execução

- Traduza “parecer independente” para o mecanismo de agentes ou tarefas disponível na superfície atual.
- Grave os artefatos no workspace do projeto quando permitido.
- Se não houver agentes independentes, use o modo de sessão única e declare a limitação.
- Não procure comandos com nomes de outros agentes.

## Verificação

1. Confirme que a skill aparece no catálogo ou seletor do Codex.
2. Peça uma descrição breve de quando ela seria acionada.
3. Verifique se o `SKILL.md` e os arquivos em `references/` são acessíveis.
4. Não execute uma pesquisa completa durante a instalação.

Referência oficial consultada em 2026-09-02: https://learn.chatgpt.com/docs/build-skills
