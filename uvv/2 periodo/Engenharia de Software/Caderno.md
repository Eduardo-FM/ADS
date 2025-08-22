##### Oque é software
um conjunto de ordens para o computador executar determinada funcao 

###### software x sistema

Sim, existe uma diferença entre sistema e software, embora os termos sejam frequentemente usados de forma intercambiável.

**Software**: É um conjunto de programas e dados que executam tarefas específicas em um computador ou outro dispositivo. Exemplo: Windows, Microsoft Word, Google Chrome, aplicativos de celular. 

**Sistema**: Um sistema é um conjunto de componentes interconectados que trabalham juntos para atingir um objetivo. Exemplo: Um sistema bancário inclui não apenas os programas, mas também caixas eletrônicos, funcionários, regulamentos e procedimentos.


### A Crise dos desenvolvedores de Softwares menos preparados 

Problemas relatados por Dijkstra: 

a) Projetos que estouram o cronograma 
b) Projetos que estouram o orçamento 
c) Produto final de baixa qualidade ou que não atenda aos requisitos 
d) Produtos não gerenciáveis e difíceis de manter ou evoluir

### Os eternos mitos 

São conhecidos os mitos do software identificados por Pressman (2005). 

Pressman classifica os mitos em três grupos: administrativo, do cliente e do profissional.

#### Administrativo

a) A existência de um manual de procedimentos e padrões é suficiente para a equipe produzir com qualidade. 
b) A empresa deve produzir com qualidade, pois tem ferramentas e computadores de última geração. 
c) Se o projeto estiver atrasado, sempre é possível adicionar mais programadores para cumprir o cronograma. 
d) Um bom gerente pode gerenciar qualquer projeto.


#### Cliente

a) Uma declaração geral dos objetivos é suficiente para iniciar a fase de programação. Os detalhes podem ser adicionados depois. 
b) Os requisitos mudam com frequência, mas sempre é possível acomodá-los, pois o software é flexível. 
c) "Eu sei do que preciso"
#### Profissional

a) Assim que o programa for colocado em operação, nosso trabalho terminou. 
b) Enquanto o programa não estiver funcionando, não será possível avaliar sua qualidade. 
c) Se eu esquecer alguma coisa, posso arrumar depois. 
d) A única entrega importante em um projeto de software é o software funcionando.

### O que é Engenharia de software?

"É a área da computação que aplica princípios da engenharia para projetar, desenvolver e manter softwares eficientes, confiáveis e escaláveis."

### Tipos de Software

- Software de Sistema – Ex.: Sistemas operacionais (Windows, Linux). 
- Software de Aplicação – Ex.: Navegadores, editores de texto. 
- Software Embutido – Ex.: Sistemas de carros e eletrodomésticos. 
- Software de Desenvolvimento – Ex.: Compiladores, IDEs.

### Princípios da Engenharia de Software

- Modularidade – Dividir o software em partes menores e independentes. 
- Reusabilidade – Aproveitar códigos e componentes em diferentes projetos. 
- Manutenibilidade – Criar softwares fáceis de atualizar e corrigir. 
- Eficiência – Otimizar recursos e desempenho do sistema. 
- Confiabilidade – Garantir que o software funcione corretamente e com segurança.


# Aula 08/08

*Requisitos:* características e funcionalidade de sistemas, quem defini é o cliente.

    funcionais: Defini o que o sistema deve fazer . ex: validação do usuário

    não funcional: defini restrições ou qualidades do sistemas. Ex: Identidade visual do sistema.

### Processo de engenharia de requisitos 

##### 1 - Levantamento(Elicitacao) de requisitos: 
Coleta das necessidades do cliente e usuarios por meio de entrevistas,, questionários, workshops, entre outrsa tecnicas

##### 2 - Analise e negociacao:

Avaliacao da viabilidade tecnica, economica e organizacional dos requisitos, ajustando ou priorizando conforme necessario

##### 3 - Especificacao
Documentacao detalhada dos requisitos de forma clara e estruturada, geralmente em um Documento de requisitos ou backlog

##### 4 - Verificacao dos requisitos 
Revisao para garantir que os requisitos estao completos, consistentes e nao contraditorios

##### 5 - Validacao dos requisitos 
Confirmacao de que os requisitos atendem as necessidades dos stakeholders e aos objetivos do sistema, garantindo que sejam corretos e uteis. 

#### Tecnicas de levantamento de requisitos 

- entrevistas com clientes e usuarios 
- questionarios 
- observacao do ambiente de trabalho
- prototipacao 

### Modelos de ciclo de vida do software 

Vamos entender como construir software de forma estruturada e eficiente, utilizando o Modelo de ciclo de vida do software. Descubra as etapas essenciais para o sucesso do seu projeto. 

##### Modelo cascata (waterfall)

Segue uma sequencia linear e rígida de fases:
Requisitos -> projeto -> implementacao -> testes -> implementacao -> manutencao 

- Cada fase deve ser concluida antes da proxima comecar 
- indicado para projetos com requisitos bem definidos e pouca necessidade de mudancas

- *Desvantagem*: dificuldade em lidar com mudancas apos o inicio do projeto

#### Modelos incremental
- divide o desenvolvimento em pequenas partes(incremental)
- cada incremento entrega uma parte funcional do sistema, permitindo ajustes e melhorias ao longo do processo
- vantagem: feedback continuo
- desvantagem: ==...==

#### Modelo espiral

O modelo espiral é como dar varias voltas ==...==


#### Modelo V (Validacao e verificacao)

Ele é uma evolucao do modelo cascatas, mas com u foco maior em testes e qualidade. Em vez de seguir apenas um fluxo linear, o Modelo V organiza o desenvolvimento e os testes em paralelo

Imagine a letra V
- No lado esquedo, temos as etapas de desenvolvimento 
- No lado direito, cada fase tem uma etapa correspondente de teste
- no centro, o sistema é construido



# Aula 15/08

![[Pasted image 20250815223359.png]]

# Aula 18/08

Imagine um sistema de caixa eletronico

Ator: Cliente

**Casos de Uso:**
- sacar dinheiro 
- depositar dinheiro
- consultar saldo

### Documentacao do caso de uso

Para cada caso de uso, precisa de uma descricao detalhada, com as seguintes informacoes
- Nome do caso de uso
- ator(es) envolvidos(s)
- Objetivo do caso de uso
- Fluxo principal(passos principais que o ator e o sistema devem seguir)
- Fluxo alternativo(possiveis variacoes no processo)
- Pre-condicoes(o que precisar estar correto antes de executar o caso de uso)
- Pos-condicoes(o que deve ocorrer apos a execucao do caso de uso)


### Desenvolvimento agil

Sao abordagens flexiveis e iterativas para o desenvolvimento de software, focadas na entrega continua de valor ao cliente. Diferente dos modelos tradicionais, como o Cascata, que seguem uma sequencia rigida de etapas, os metodos ageis promovem adaptacao as mudancas, colaboracao entre equipes e entregas incrementais. 


- SCRUM
- KANBAM
- XP

#### Vantagens dos metodos ageis

- Flexibilidade para mudancas 
- Entrega continua e incremental
- Maior colaboracao entre equipe e cliente 
- Identificaco rapida de problemas 
- Maior satisfacao do usuario final. 

#### Metodos ageis em engenharia de software\

Os metodos ageis surgiram como uma resposta as limitacoes dos modelos tradicionais de desenvolvimento de software, como o Cascata, Incremental, Espiral e V.

A principal motivacao foi a necessidade de maior flexibilidade, adaptacao as mudancas e ==...==

### Scrum

O Scrum é um dos métodos ageis ==...==

