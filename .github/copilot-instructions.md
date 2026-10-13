# Instruções do repositório

- Gere todas as mensagens de commit em português do Brasil, incluindo tipo, resumo e corpo. Não use prefixos nem frases em inglês; preserve nomes próprios e identificadores de código apenas quando necessários.
- Siga o formato "tipo: resumo", usando tipos em português: recurso, correção, documentação, refatoração, manutenção ou testes.
- O resumo deve identificar a mudança principal. Para alterações relevantes, inclua um corpo após uma linha em branco explicando o que mudou, por que mudou e o efeito esperado.
- Considere somente as alterações preparadas para o commit. Não invente contexto, motivos nem resultados de testes; mencione validações apenas quando tiverem sido executadas.

## Exemplos

- recurso: valida os dados antes de gerar o contrato

	Impede a criação do documento quando campos obrigatórios estão vazios e orienta a pessoa sobre o dado que precisa ser corrigido.
- correção: usa os parágrafos corretos nas células da tabela

	Evita erro ao preencher os dados das partes e permite concluir a geração do contrato.
- documentação: explica como executar os exercícios

	Acrescenta instruções de uso para facilitar a configuração e a execução dos exemplos.

## Regra principal

Toda mensagem de commit gerada neste projeto deve ser escrita somente em português do Brasil e explicar as alterações com detalhes proporcionais ao tamanho e ao impacto da mudança.
