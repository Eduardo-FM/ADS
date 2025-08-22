
#### O QUE É BANCO DE DADOS?

Um banco de dados é uma coleção organizada de informações - ou dados - estruturadas, normalmente armazenadas eletronicamente em um sistema de computador.

##### Dado

Para Pulga, França e Goya (2013) dado representa uma unidade básica de informação, reconhecido apenas como uma valoração de qualquer objeto. O mesmo autor define que Informação como um conjunto de dados associados a um mesmo contexto. Desta forma, um conglomerado de dados, tornam-se informações promovendo o conhecimento para um indivíduo a respeito de um determinado assunto.

### Informação

A Informação nada mais é que o processo de interpretação dos dados associados dentro de um mesmo contexto. A interpretação dos dados, em sua grande maioria é realizada por pessoas, pois, apenas as pessoas destreza de transformar grupos de dados em informações que possam ser utilizadas pela sociedade para a execução de determinada ação (MATTOS, 2005).

#### Conhecimento
Mattos (2005) defende que o conhecimento é a forma mais completa do processo, pois se vale da junção de um ou vários conjuntos de informações que estão relacionadas dentro de um mesma conjuntura. Considerando um hierarquia, o conhecimento está alocado em um nível acima das informações e dois níveis acima dos dados, pois, se tratam desses, trabalhados e associados. Assim, a junção de dados apresenta como resultado informações e dos conjuntos de informações emanam conhecimento.

Valdemar W.Setzer Conhecimento é uma abstração interior, pessoal, de alguma coisa que foi experimentada por alguém. Assim, alguém tem algum conhecimento de Paris somente se a visitou.

![[Pasted image 20250817190958.png]]

### Sistemas de recuperacao de informacao

Classificação de Informações; 

Recuperação de informações; 
Uso de informações recuperadas; 

Classificação dessas, em geral leva a erros básicos;
● Dados estruturados; 
● Dados não estruturados;

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

---
##### Revisão

Um banco de dados pode ser definido como um conjunto de dados devidamente relacionados. Podemos compreender como os dados os objetos conhecidos que podem ser armazenados e que possuem um significado implícito, porém o significado do termo banco de dados é mais restrito, logo apresenta como propriedades:

• É uma coleção de dados logicamente coerente que possui um significado implícito cuja interpretação é dada por uma determinada aplicação. 

• Representa abstratamente uma parte do mundo real, conhecida como Mini-Mundo ou Universo de Discurso (UD) que é de interesse de uma certa aplicação. 

• Mantido em dispositivos de armazenamento secundário de um sistema de computação.

• É uma coleção lógica coerente de dados com um significado inerente; uma disposição desordenada dos dados não pode ser referenciada como banco de dados. 

• Ele é projetado, construído e preenchido com valores de dados para um propósito específico, um banco de dados possui um conjunto predefinido de usuários e de aplicações. 

• Ele representa algum aspecto do mundo real, o qual é chamado de mini mundo, qualquer alteração efetuada no minimundo é automaticamente refletida no banco de dados. 

• Banco de Dados 

• Sistema de gerenciamento de banco de dados (SGBD)  

• Sistema de banco de dados

---

### Sistema de gerenciamento de banco de dados 

Um sistema de gerenciamento de banco de dados (SGBD) é um software que possui recursos capazes de manipular as informações do banco de dados e interagir com o usuário. Exemplos de SGBDs são: Oracle, SQL Server, DB2, PostgreSQL, MySQL, o próprio Access ou Paradox, entre outros. 

Software construído para facilitar as atividades de definição, construção e manipulação de banco de dados.
### Sistema de Banco de dados

SISTEMA DE BANCO DE DADOS: BANCO DE DADOS + SOFTWARE QUE O MANIPULA

Um conjunto de quatro componentes básicos: dados, hardware, software e usuários. Date conceituou que “sistema de bancos de dados pode ser considerado como uma sala de arquivos eletrônica”.

![[Pasted image 20250817191531.png]]

![[Pasted image 20250817191536.png]]

![[Pasted image 20250817191542.png]]

![[Pasted image 20250817191547.png]]

![[Pasted image 20250817191551.png]]

#### ELIMINAÇÃO DA INCONSISTÊNCIA DOS DADOS

Nos sistemas de arquivos, os dados ficam armazenados em locais isolados e só acessados pela linguagem que lhes deu origem

#### FACILIDADE DE ACESSO AOS DADOS.

• Devido ao fato dos dados estarem centralizados

#### PROVÊ EFICIENTE SEGURANÇA AOS DADOS.
• Critérios de permissões definidos pelo administrador.  
• permissões de consulta 
• permissões de manipulação

#### PROVÊ RESTRIÇÕES DE INTEGRIDADE
• Nos SGDB‟s você pode definir regras de integridade sobre os campos de uma tabela, com isso qualquer valor inserido naquela coluna deverá respeitar esta regra. 
• Exemplo: Salário >= 151,00 (CHECK CONSTRAINTS) UF Pertence a tabela de ESTADOS (Integridade Referencial – FOREIGN KEY)

#### PROVÊ FERRAMENTAS EFICIENTES PARA BACKUP E RESTORE

#### VANTAGENS DO USO DO SGBD

• Dados armazenados em um único local
	• evita-se redefinições;
	• minimiza-se redundância.
• Dados compartilhados pelas aplicações
	• facilita integração de aplicações;
	• evita redefinição de dados
• Dados mais independentes das aplicações
	• novas operações de manipulação de 43dos não requerem modificação "pesada" no código da
	aplicação
	aplicações não se preocupam mais com o gerenciamento dos dados
• Maior flexibilidade de acesso
	• linguagens para BD

#### QUANDO NÃO USAR UM SGBD?

• Quando minha aplicação é simples
	• lida com poucos dados operacionais que podem ser mantidos em um ou poucos arquivos.
• Quando minha aplicação faz processamento pesado mas não requer
gerenciamento de dados operacionais.
• Quando o custo para instalação e administração de um SGBD é muito alto
	- equipamento, pessoal, treinamento.

### TIPOS DE BANCO DE DADOS
• Banco de Dados Relacional
• Banco de dados Hierárquico
• Banco de dados de rede
• Banco de dados Objeto-Relacional

### Banco de Dados Relacional

Um banco de dados relacional consiste em uma coleção de tabelas, cada uma das quais com um nome único. Os dados de um banco de dados relacional (BDR) são armazenados em tabelas, que por sua vez, nada mais são do que estruturas de linhas e colunas. Uma linha em uma tabela representa um relacionamento entre um conjunto de valores.

A linguagem padrão dos Bancos de Dados Relacionais é a Structured Query Language, ou simplesmente SQL como é mais conhecida.

![[Pasted image 20250817195013.png]]

### BANCO DE DADOS HIERÁRQUICO

Trabalha com os dados e relacionamentos como uma coleção de registros relacionados por ligações. As ligações entre os registros podem ser chamadas links. Nesse tipo de banco de dados os dados estão agrupados sob a forma de árvores. Cada registro é uma coleção de atributos campos), cada um dos quais contendo somente uma informação; uma ligação é a associação entre dois registros

![[Pasted image 20250817195107.png]]

### BANCO DE DADOS DE REDE

Enquanto no modelo relacional os dados e os relacionamentos entre dados são representados por uma coleção de tabelas, o modelo de rede representa os dados por coleções de registros e os relacionamentos entre dados são representados por links. O banco de dados de rede é uma coleção de registros que são conectados uns aos outros por meio de links. Cada registro é uma coleção de campos. Um link é uma associação entre exatamente dois registros.

![[Pasted image 20250817195126.png]]

### BANCO DE DADOS OBJETO-RELACIONAL

Os bancos de dados tradicionais como os bancos relacionais, de rede e hierárquicos foram bem sucedidos na maioria das aplicações comerciais de banco de dados.

Porém, bancos de dados para projetos de:
• engenharia e manufatura
• experimentos científicos
• telecomunicações,
• entre outros, podem ser mais complexos.


• Os bancos de dados orientados a objeto foram propostos para atender a
essas necessidades de aplicações mais complexas.
Banco de dados orientados a objeto suportam tipos de dados complexos.

Bancos de dados relacionais suportam grandes volumes de dados e  consultas complexas

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

### Independência de dados

o conceito de independencia de dados e similar em muitos aspectos ao conceito de tipos abstratos de dados em modernas linguaguens de programacao.

Ambos esconcem detalhes de implementacao do usuario

Isto permite ao usuario concentra-se na estrutura geral em vez de detalhes de baixo nivel de implementacao

A habilidade de modificar a definição de um esquema em um nível sem afetar a definição de esquema num nível mais alto é chamada de independência de dados. Existem dois níveis de independência dos dados:

### independencia fisica de dados

É a habilidade de modificar o esquema fisico sem a necessidade de reescrever os programas aplicativos

As modificacoes no nivel fisico sao ocasionalmente necessarias para melhorar o desempehno;

### Independência lógica de dados

É a habilidade de modificar o esquema conceitual sem a necessidade de reescrever os programas aplicativos.

As modificações no nível conceitual são necessárias quando a estrutura lógica do banco de dados é alterada (por exemplo, a adição de contas de bolsas de mercado num sistema bancário).


A independência lógica dos dados é mais difícil de ser alcançada do que a independência física, porém os programas são bastante dependentes da estrutura lógica dos dados que eles acessam.

### Linguagem de Manipulação de Dados

Os níveis de abstração discutidos anteriormente (níveis físico, conceitual e de visão) não se aplicam somente à definição ou estrutura de dados, mas também à sua manipulação.

A manipulação de dados significa:
● a busca da informação armazenada no BD; 
● a inserção de novas informações nos BD; 
● a eliminação de informações no BD; 
● a modificação de dados armazenados no BD.

# Aula 13/08

## Conceitos do Modelo entidade-relacionamento

Entidades e Atrabitutos
O objeto básico que o MER representa é a entidade. Uma entidade é algo do mundo real que possui uma existência independente. Uma entidade pode ser um objeto com uma existência física - uma pessoa, carro ou empregado - ou pode ser um objeto com existência conceitual - uma companhia, um trabalho ou um curso universitário.

Cada entidade tem propriedades particulares, chamadas atributos, que a descrevem.

Por exemplo, uma entidade EMPREGADO pode ser descrita pelo seu nome, o trabalho que realiza, idade, endereco e salário. Uma entidade em particular tera um valor para cada um de seus atributos. 

Os valores de atributos que descrevem cada entidade ocupam a maior parte dos dados armazenados na base de dados. 

### Exemplo de entidades e seus respectivos atributos 

Alguns atributos podem ser divididos em subpartes com significados independentes. Por exemplo, Endereço da entidade e1 pode ser dividido em Endereço da Rua, Cidade, Estado e CEP. Um atributo que é composto de outros atributos mais básicos é chamado composto.

Já, atributos que não são divisíveis são chamados simples ou atômicos. Atributos compostos podem formar uma hierarquia, conforme pode ser observado no exemplo da

### Tipos de entidades 

Uma base de dados irá conter normalmente grupos de entidades que sao similares.

Uma companhia com centenas de empregados pode querer agrupar as informacoes similares com respeito a emrpegados. 

Estas entidades, empregados compartilham os mesmos atributos, mas cada entidade terá seus próprias valores para cada atributo. 

### Atributos-Chaves

Atributo-Chave de um Tipo de Entidade: Uma restrição importante sobre entidades de um tipo de entidade é a restrição de atributo-chave ou unicidade.

Um tipo de entidade tem, normalmente, atributos cujos valores são distintos para cada entidade. 

Tal atributo é chamado atributo-chave, e o seu valor pode ser usado para identificar cada entidade unicamente. Algumas vezes, um conjunto de atributos pode formar uma chave. 

Nestes casos, os atributos podem ser agrupados em um atributo composto, que virá a ser um atributo-chave do tipo de entidade.

### Relacionamentos, Papéis e Restrições Estruturais

Por exemplo, considere-se que um tipo de relacionamento TRABALHA-PARA exista entre tipos de entidades EMPREGADO e DEPARTAMENTO.

Este relacionamento associa cada empregado com o departamento em que este trabalha.

Cada instância de relacionamento em TRABALHA-PARA associa uma entidade empregado e uma entidade departamento

### Tipo de Entidade-Fraca

Alguns tipos de entidades podem não ter quaisquer atributos-chaves. Isto implica que não se pode distinguir as entidades porque a combinação dos valores de atributos podem ser idênticas. 

Tais tipos de entidades são chamadas tipos de entidades-fracas. 

Entidades que pertencem a um tipo de entidade-fraca são identificadas por estarem associadas a entidades específicas de um outro tipo de entidade em combinação com alguns de seus valores de atributos.

![[Pasted image 20250817200244.png]]

![[Pasted image 20250817200249.png]]

Note-se que é possível ter um tipo de entidade-fraca com um tipo de relacionamento de identificação ternário (ou n-ário)

Neste caso, o tipo de entidade-fraca pode ter muitos tipos de entidades proprietárias da identificação. As razões de cardinalidade também são aplicáveis em tipos de relacionamentos n-ários


### Atributos

São propriedades (características) que identificam as entidades. Uma entidade é representada por um conjunto de atributos. Os atributos podem ser simples, composto, multivalorado ou determinante.

### Atributo simples

Não possui qualquer característica especial. A maioria dos atributos serão simples. Quando um atributo não é composto, recebe um valor único como nome, por exemplo e não é um atributo chave, então ele será atributo simples.

### Atributo composto

O seu conteúdo é formado por vários itens menores. Exemplo: Endereço. Seu conteúdo poderá ser dividido em vários outros atributos, como: Rua, Número, Complemento, Bairro, Cep e Cidade. Este tipo de atributo é chamado de atributo composto. Veremos mais de sua aplicação no post sobre normalização de dados.

### Atributo multivalorado

O seu conteúdo é formado por mais de um valor.

Exemplo: Telefone. Uma pessoa poderá ter mais de um número de telefone. É indicado colocando-se um asterisco precedendo o nome do atributo. O atributo multivalorado serão tratados com mais detalhes na normalização de dados

### Atributo determinante

Identifica de forma única uma entidade, ou seja, não pode haver dados repetidos.

É indicado sublinhando-se o nome do atributo.

Exemplo: CNPJ, CPF, Código do fornecedor, Número da matrícula, etc. Os atributos determinantes serão as chaves primárias no banco de dados e seu uso tem implicações na normalização de dados


### Projeto de chaves e Regras de Integridade

Chave primária: é o conjunto de atributos que identificam unicamente uma entidade.

Chave alternativa: também conhecida como chave secundária, é aquela chave candidata que não é primária. De acordo com as regras do negócio, às vezes pode ser conveniente identificar entidades por atributos que não são únicos dentre todas as instâncias.

Chave estrangeira: são atributos de uma entidade cujos valores aparecem como chave primária em outra entidade.

### Relacionamentos

Um relacionamento é uma conexão entre itens. Em uma modelagem orientada a objetos, os três relacionamentos mais importantes são as dependências, as generalizações e as associações.

### Tipo de Relacionamento

Tipo de Relacionamento: 

Define um conjunto de associações entre n tipos de entidade E1 , E2 ,...,En 

Exemplo: Trabalha-para entre Empregado e Departamento

![[Pasted image 20250817200651.png]]

### Tipos de Relacionamento

Matematicamente, um tipo de relacionamento R é um conjunto de (instâncias de) relacionamentos ri , onde cada ri associa n (instâncias de) entidades (e1 ,...,en ) e cada ej pertence a um tipo de entidade Ej

R ⊆ E1 x E2 x ... x E


### Restrições sobre tipos de relacionamento

Cardinalidade: Especifica o número de instâncias de um tipo de relacionamento do qual uma entidade pode participar

Participação: Especifica se a existência de uma entidade depende de seu relacionamento com outra entidade através de um tipo de relacionamento parcial ou total

### Especialização e Generalização: Subclasses e Superclasses

Especialização: Processo de definição de um conjunto de subclasses (sub-tipos) de um tipo de entidade

Generalização: Processo de definição de um tipo de entidade genérico (super-classe ou super-tipo) a partir de um conjunto de tipos de entidade

![[Pasted image 20250820213826.png]]

![[Pasted image 20250820213845.png]]
![[Pasted image 20250820214515.png]]
![[Pasted image 20250820214558.png]]
![[Pasted image 20250820214735.png]]

### Especialização e Generalização

Toda instância de uma sub-classe (ou subtipo) é também uma instância de sua superclasse (ou super-tipo)

● Ex.: “John Smith” é um engenheiro e também um empregado

Herança de atributos e relacionamentos:
- Uma entidade de uma sub-classe possui todos os atributos e relacionamentos de sua super-classe, ou seja, ela herda todos os atributos e relacionamentos da super-classe
- Além disso, uma entidade de uma sub-classe pode possuir seus próprios atributos e relacionamentos locais ou específicos

### Especialização

O processo de especialização permite: 
- Definir um conjunto de sub-classes (subtipos) de um determinado tipo de entidade 
- Estabelecer atributos específicos adicionais para cada sub-classe (sub-tipo) 
- Estabelecer tipos de relacionamento específicos adicionais entre cada sub-classe (sub-tipo) e outros tipos de entidade ou sub-classes (sub-tipos)

# Aula 22/08

Disjunta: no maximo uma ocorrencia (d)

Sobreposta: pode uma ou mais (o)

Total: deve (obrigatório)

Parcial: pode (opcional)