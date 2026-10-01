

Imagine um estrutura de dados que possibilite o armazenamento de uma tabela onde o acesso a um de seus registros seja efetuado diretamente.

Esta estrutura representa um modelo ideal, contudo em aplicações reais este ideal pode ser aproximado.

A tabela hash serve para retorna os dados de forma O(1)

Ela tem que ter duas coisas essenciais:
- a propria tabela, com um array com numero finito de entradas 
- e uma funcao hash que faz a traducao da chave para a posicao

Nao existe ordem entre os elementos. A ordem da entrada dos dados quem determina é a função Hash

Mas pode ter um problema na funcao hash, a funcao hash pode retornar a mesma posicao para duas chaves diferentes (colisao). 


A capacidade de carga como boa pratica, deve ser manter em menos de 0.75. Para ter alguma posicao vaga para a insercao de elementos.

Tambem é possivel fazer um hash encadeado, aonde se utiliza uma lista encadeada para inserir elementos.

---

*Tabela hash com endereçamento aberto*

Toda vez que acontecer uma colisão, se procura uma outra posicao livre. 

- tentativa linear 
Pula de um em um, a passada para evitar a colisão.

Implementa uma nova funcao para achar uma posicao livre quando ocorrer uma colisao.

o problema desse tipo de sondagem, é pq criar cluster, então ao tentar achar uma posicao livre, a possibilidade é grande de ele encontrar uma posicao ocupada. 

- tentativa quadrática

Na tentativa quadrática,, a taxa de busca cresce de forma quadrática. Se faz isso para sair das posiçoes ocupadas de memória mais rápido. 






