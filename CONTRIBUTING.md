# Como Contribuir?

Este livro esta sendo desenvolvido de forma colaborativa e aberta, aqui no
GitHub. Nós aceitamos comentários, contribuições e correções em geral.

Nós utilizamos o
[asciidoc](https://asciidoctor.org/docs/asciidoc-writers-guide/) para formatar
e compilar o documento. Recomendamos que você entenda o básico de sua sintaxe.

Por se tratar de um projeto colaborativo e desenvolvido no GitHub, seria
interessante que você se familiarizar-se com o Git e seus principais workflows
de trabalho. Neste projeto utilizamos o [Forking
Workflow](https://br.atlassian.com/git/tutorials/comparing-workflows/forking-workflow).

## Contribuindo com um pull-request

Nós aceitamos pull-requests desde que seu PR venha licenciado e com autoria. Se
você está contribuindo com um trabalho original seu, então você concorda
automaticamente em oferecê-lo sob a licenca deste livro (CC-BY-SA). Se você
estiver fazendo referências a trabalhos de terceiros, também precisa vir com
uma licenca compatível com CC-BY-SA, neste caso você precisa indicar onde está
o documento original bem como sua a licenca original, incluindo um comentário
no início de sua contribuicão. Ex:

```
////
Source: https://github.com/foo/bar/blob/master/test.md
License: MIT
Added by: John Example (@johnexample)
////
```

## Contribuindo com uma *issue*

Se você encontrou algum erro e não tem certeza de como corrigir ou você não
sabe como funcionam os Pull-Requests então você pode abrir ou comentar em uma
[*issue*](https://github.com/computer-music-book/book/issues).


## Contribuindo com notas, referencias e dicas

Caso sua contribuicão seja uma nota, uma referência ou um dica solta e você não
sabe onde colocar, você pode enviar um PR para um novo arquivo na pasta
`src/drafts`.

Esta área funciona como um *sandbox*, e poderá sofrer alteracões mais
livremente.

# Padronizacão de estilos no livro

*{precisa de mais informacões aqui}*

## Final de linha

Todas as submissões devem usar o padrão de fim de linhas dos sistemas
Unix-like: LF (não utilizar CR, não utilizar CR/LF). Todo o processo de
compilacão e pós-processamento será feito em sistemas Unix-like e fim de linhas
diferentes de LF irão causar confusão nas ferramentas de diff. Verifique e
altere nas configuracões de seu editor de textos qual final de linha usar.

## Largura máxima

Configure também o seu editor de textos para o máximo de **80 colunas**. Isso
facilitará o trabalho de revisão e merge.
