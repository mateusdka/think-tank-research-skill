# Adapter para ChatGPT e Claude.ai

## Instalação por pacote

1. Obtenha `think-tank-research-portable.zip` de uma distribuição publicada pelo mantenedor. Se ainda não houver uma Release, clone o repositório e execute `python3 scripts/build_distributions.py` para gerar o pacote em `dist/`.
2. Revise o conteúdo antes do upload.
3. Abra a área de Skills ou Recursos do produto.
4. Faça o upload do `.zip` quando a conta e o workspace forem elegíveis.
5. Aguarde a análise de segurança da plataforma.
6. Faça um teste de descoberta sem rodar uma pesquisa completa.

A disponibilidade varia por plano, produto e configuração administrativa. Se o upload não existir na conta, anexe o `SKILL.md` e os templates à conversa e use o modo de sessão única.

## Limites

- O ambiente web não recebe acesso automático às pastas locais do computador.
- Arquivos anexados, conectores e fontes externas dependem das permissões da conversa.
- Arquivos criados em sandbox podem ser temporários.
- A plataforma pode não oferecer subagentes independentes.

## Execução

- Use sandbox quando houver arquivos e tarefas independentes.
- Exporte os pareceres e o relatório quando a plataforma permitir.
- Use sessão única quando não houver isolamento.
- Registre o modo e as limitações no relatório.

## Verificação

- a plataforma aceitou o pacote;
- a skill aparece como instalada ou disponível;
- o agente consegue resumir seu gatilho e os três modos de execução;
- nenhuma pesquisa real foi iniciada durante o teste.

Fontes oficiais consultadas em 2026-09-02:

- https://help.openai.com/en/articles/20001066-skills-in-chatgpt
- https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview
