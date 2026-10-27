---
name: atualizar-readme
description: Atualiza o README.md deste repositório com os exercícios e conceitos novos. Use quando o usuário pedir para atualizar, sincronizar ou revisar o README após adicionar exercícios .py novos.
---

# Atualizar README

Mantém o `README.md` deste repositório refletindo o estado real dos exercícios, sem expor isso como "acompanhamento de progresso" — o README deve parecer um README de repositório de prática normal, mas organizado de forma que quem olhar consiga perceber a evolução dos conceitos cobertos.

## Passos

1. Liste todos os arquivos `.py` na raiz do repositório (`Glob *.py`).
2. Compare com a tabela de exercícios já existente no README (seção `## Exercícios`). Identifique quais arquivos ainda não estão listados.
3. Para cada arquivo novo, leia o conteúdo e escreva uma descrição curta e objetiva do que o exercício faz (mesmo padrão das linhas já existentes na tabela: foco no que o script resolve, não em como).
4. Adicione uma linha por arquivo novo na tabela, na ordem em que os exercícios foram criados (use `git log` para arquivos sem data clara, ou a ordem em que aparecem no diretório se não houver histórico).
5. Releia a seção `## Conceitos praticados`. Se algum exercício novo introduzir um conceito que ainda não está na lista (ex: dicionários, try/except, recursão, funções, classes, manipulação de arquivos, etc.), adicione-o. Não remova conceitos existentes mesmo que pareçam básicos — a lista é cumulativa.
6. Não altere nenhuma outra seção do README (Objetivo, Como usar, Destaques, Requisitos) a menos que o usuário peça explicitamente.

## Regras

- Nunca descreva um exercício como "errado" ou "com bugs" no README — isso é assunto da skill `revisor-exercicios`, não desta. O README documenta o que o exercício *se propõe a fazer*, não a qualidade da implementação.
- Não insira linguagem de "nível", "dificuldade" ou "progresso do aluno" — a lista de conceitos cumulativa já comunica isso implicitamente.
- Mantenha a tabela e a lista de conceitos no mesmo estilo (tom direto, descrições curtas) já usado nas entradas anteriores.
- Se nenhum arquivo novo for encontrado, informe isso e não altere o README.

## Depois de atualizar

Pergunte ao usuário se deseja commitar e enviar (push) a alteração — não faça isso automaticamente, a menos que o pedido original já tenha incluído essa instrução.
