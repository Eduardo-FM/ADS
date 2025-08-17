Um banco de dados é uma colecao organizada de informacoes - ou dados - estruturadas, normalmente armazenadas eletronicamente em um sistema de computador

Informacoes e dados são diferentes.


##### Dado

###### Pulga, Franca e Loyola
dado representa uma unidade basica de informacao, reconhecido apenas com uma valoracao de qualquer objeto. 

Informacao como um conjunto de dados associados a um mesmo contexto. 

Desta forma, um conglomerado de dados, tornam-se informacoes promovendo o conhecimento para um individuo a respeito de um determinado assunto. 


#### Conhecimento
É a juncao de varios conjuntos de informacoes.

(Setzer) Conhecimento é uma abstracao interior, pessoal, de alguma coisa que foi experimentada por alguem. 


### Sistemas de recuperacao de informacao

Classificacao de informacoes;
Recuperacao de informacoes;
Uso de informacoes recuperados;
Classificacao dessa, em geral leva a erros basicos;
- dados estruturados
- dados nao estruturados 

#### Nao estruturados

Os bancos de dados em geral nao contem todas as informacoes possiveis sobre algo la guardado.

Um dado é uma forma organizada de informacao, mas ela ocorre desde que campos especificos sejam preenchidos para que a recuperacao deles se de de forma automatizada. 

mas documentos de texto, por exemplo, 

Seria inviavel classificar cada palavra do texto e relacioná-las com contextos. 

#### Estruturados
Sao dados que contem uma organizacao para serem recuperados
É como se fosssem etiquetas, linhas e colunas que identificam diversos pontos sobre aquela informacao e tornam o trabalho da tecnologia bem simplificado
A maioria das empresas trabalha com eles ha decadas. Embora nao sejam a maior fatia do conteudo produzido, eles sao o que existe - ou exista - de melhor para tirar conclusoes e fazer processos fluirem.

### Ontologias 
uma ontologia é um modelo de dados que representa um conjunto de conceios dentro de um dominio e os relacionamentos entre estes.


### Entidades 
Entidades continuantes - as quais existem totalmente durante todo dempo de sua existencia, persistem atraves do tempo mantendo identidade.

- Continuantes independentes: entidades portadoras de qualidades, das quais outra entidade pode depender.
- Continuantes dependentes: é uma entidade que mantem inerencia de outras entidades 


### Sistema de gerenciamento de banco de dados 

Um sistema de gerenciamento de banco de dados(SGBD) é um software que possui recrusos capazes

==...==

### Sistema de Banco de dados



# Aula 08/08

### Abstracao de dados

Um SGBD é composto de uma colecao de arquivos inter-relacionados e de um conjunto de programas que permitem aos usuarios fazer o acesso a estes arquivos e modificar os mesmos

O grande objetivo de um sistema de banco de dados é prover os usuários com uma visao abstrata dos dados. 

Isto é. o sistema omite certos detalhes de como os dados sao armazenados e mantidos 

#### Nivel externo 

A mais alto nivel de abstracao descreve apenas parte do banco de dados 

Apesar do uso de estruturas mais simples do que no nivel conceitual, alguma complexidade perdura devido ao grande tamanho do banco de dados. Muitos usuarios do sistema de banco de dados nao estarao interessados em todas as informacoes

Em vez disso precisam de apenas uma parte do banco de dados. O nivel de abstracao das visoes de dados é definido para simplificar esta interacao com o sistema, que pode fornecer muitas visoes para o mesmo banco de dados. 

#### Nivel fisico

O nivel mais baixo de abstracao descreve como os dados estao realmente armazenados.

No nivel fisico, complexas estruturas de dados de baixo nivel sao descritas em detalhes. 


##### Nivel conceitual

O descreve quais dados estao armazenados de fato no banco de dados e as relacoes que existem entre eles,

Aqui o banco de dados inteiro é descrito em termos de um pequeno numero de estruturas relativamente simples

Embora as implementacoes de estruturas simples no nivel conceitual possa envolver complexas estruturas de nivel fisico, o usuario do nivel conceitual nao precisa preocupar-se com isso

O nivel conceitual de abstracao é usado por administradores do banco de dados, que podem decidir quais informacoes devem ser mantidas no DB.

### Independen6icas de dados 

o conceito de independencia de dados e similar em muitos aspectos ao conceito de tipos abstratos de dados em modernas linguaguens de programacao.

Ambos esconcem detalhes de implementacao do usuario

Isto permite ao usuario concentra-se na estrutura geral em vez de detalhes de baixo nivel de implementacao

### independencia fisica de dados

É a habilidade de modificar o esquema fisico sem a necessidade de reescrever os programas aplicativos

As modificacoes no nivel fisico sao ocasionalmente necessarias para melhorar o desempehno;


# Aula 13/08

## Conceitos do Modelo entidade-relacionamento

Entidades e Atrabitutos
O objeto básico que o MER representa é a entidade. Uma entidade é algo do mundo real que possui uma existencia independente. Uma entidade pode ser um objeto com uma existencia fisic. ==...==

Cada entidade tem propriedades particulares, chamadas atributos, que a descrevem.

Por exemplo, uma entidade EMPREGADO pode ser descrita pelo seu nome, o trabalho que realiza, idade, endereco e salário. Uma entidade em particular tera um valor para cada um de seus atributos. 

Os valores de atributos que descrevem cada entidade ocupam a maior parte dos dados armazenados na base de dados. 

### Exemplo de entidades e seus respectivos atributos 

Alguns atributos podem ser divididos em subpartes com significados ==...==

### Tipos de entidades 

Uma base de dados irá conter normalmente grupos de entidades que sao similares.

Uma companhia com centenas de empregados pode querer agrupar as informacoes similares com respeito a emrpegados. 

Estas entidades, empregados compartilham os mesmos atributos, mas cada entidade terá seus próprias valores para cada atributo. 

