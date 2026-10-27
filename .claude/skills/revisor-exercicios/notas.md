# Notas de recorrência

Registro de erros e padrões que já apareceram em revisões anteriores deste repositório. Usado pela skill `revisor-exercicios` para identificar quando um erro se repete.

Formato de cada entrada: `- **<padrão>** — visto em: <arquivos>. <breve descrição>`

- **Comparar valor com tipo em vez de valor com valor** (ex: `variavel != int`) — visto em: `dicionarios.py`. A comparação deveria ser com o valor esperado, não com o tipo `int`/`str`/etc.
- **Condição de parada de loop não bate com o texto mostrado ao usuário** (case sensitivity) — visto em: `lista-frutas.py`. O texto pedia `'Ver tudo'` mas a comparação exigia minúsculas exatas; corrigido com `.lower()`.
- **`else`/lógica com indentação no nível errado** — visto em: `lista-frutas.py`. Um `else` alinhado com `while` em vez do `if` correspondente, fazendo parte do código nunca executar.
