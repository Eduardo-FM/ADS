##### Oque é software

Software é um conjunto de instruções que um computador pode executar para realizar tarefas. Ele inclui programas, aplicativos e sistemas operacionais, além de dados e documentação necessários para seu funcionamento. Basicamente, o software diz ao hardware o que fazer e como fazer.

###### software x sistema

Sim, existe uma diferença entre sistema e software, embora os termos sejam frequentemente usados de forma intercambiável.

==**Software**: É um conjunto de programas e dados que executam tarefas específicas em um computador ou outro dispositivo. Exemplo: Windows, Microsoft Word, Google Chrome, aplicativos de celular.==

==**Sistema**: Um sistema é um conjunto de componentes interconectados que trabalham juntos para atingir um objetivo.==Exemplo: Um sistema bancário inclui não apenas os programas, mas também caixas eletrônicos, funcionários, regulamentos e procedimentos.


### A Crise dos desenvolvedores de Softwares menos preparados 

• "Crise de Software" 
• Expressão vem dos anos 1968
• Por Edsger Dijkstra 
• Problemas > Engenharia de Software era uma disciplina incipiente.

Com o aumento da demanda por softwares complexos, muitos sistemas são desenvolvidos sem estrutura adequada, resultando em falhas, custos elevados e baixa qualidade.

Problemas relatados por Dijkstra: 

==a) Projetos que estouram o cronograma 
b) Projetos que estouram o orçamento 
c) Produto final de baixa qualidade ou que não atenda aos requisitos 
d) Produtos não gerenciáveis e difíceis de manter ou evoluir==

### Importância do Software para a Sociedade

Os softwares estão em todos os lugares: na saúde, na educação, no comércio e no entretenimento. Eles automatizam tarefas, conectam pessoas e impulsionam a inovação
### Os eternos mitos 

São conhecidos os mitos do software identificados por Pressman (2005). 

==Pressman classifica os mitos em três grupos: administrativo, do cliente e do profissional.==

#### ==Administrativo==

a) A existência de um manual de procedimentos e padrões é suficiente para a equipe produzir com qualidade. 
b) A empresa deve produzir com qualidade, pois tem ferramentas e computadores de última geração. 
c) Se o projeto estiver atrasado, sempre é possível adicionar mais programadores para cumprir o cronograma. 
d) Um bom gerente pode gerenciar qualquer projeto.

#### ==Cliente==

a) Uma declaração geral dos objetivos é suficiente para iniciar a fase de programação. Os detalhes podem ser adicionados depois. 
b) Os requisitos mudam com frequência, mas sempre é possível acomodá-los, pois o software é flexível. 
c) "Eu sei do que preciso"
#### ==Profissional==

a) Assim que o programa for colocado em operação, nosso trabalho terminou. 
b) Enquanto o programa não estiver funcionando, não será possível avaliar sua qualidade. 
c) Se eu esquecer alguma coisa, posso arrumar depois. 
d) A única entrega importante em um projeto de software é o software funcionando.

### O que é Engenharia de software?

=="Engenharia de Software é a aplicação de abordagens sistemáticas, disciplinadas e quantificáveis ao desenvolvimento, operação e manutenção de software. "==

=="É a área da computação que aplica princípios da engenharia para projetar, desenvolver e manter softwares eficientes, confiáveis e escaláveis."==

### Sobre o Engenheiro de Software

"Segundo Wazlawick (2019), o engenheiro de software é responsável por viabilizar e monitorar o processo de desenvolvimento, selecionando e avaliando as ferramentas e técnicas mais adequadas para cada projeto ou organização"

Engenheiro de Software → Engenheiro Civil 
	==Ele projeta, planeja e define os requisitos do sistema, garantindo que a estrutura do software seja sólida, eficiente e sustentável a longo prazo.==

Desenvolvedor de Software → Pedreiro ou Mestre de Obras 
	==Ele implementa o projeto criado pelo engenheiro, codificando e construindo as funcionalidades do sistema, seguindo especificações previamente estabelecidas.==
### Tipos de Software

- Software de Sistema – Ex.: Sistemas operacionais (Windows, Linux). 
- Software de Aplicação – Ex.: Navegadores, editores de texto. 
- Software Embutido – Ex.: Sistemas de carros e eletrodomésticos. 
- Software de Desenvolvimento – Ex.: Compiladores, IDEs.

### Princípios da Engenharia de Software

- ==Modularidade== – Dividir o software em partes menores e independentes. 
- ==Reusabilidade== – Aproveitar códigos e componentes em diferentes projetos. 
- ==Manutenibilidade== – Criar softwares fáceis de atualizar e corrigir. 
- ==Eficiência== – Otimizar recursos e desempenho do sistema. 
- ==Confiabilidade== – Garantir que o software funcione corretamente e com segurança.


# Aula 08/08

### Engenharia de Requisitos

A Engenharia de Requisitos é uma das fases mais importantes do desenvolvimento de software porque:

==A) Define a arquitetura e a programação do sistema. 
B) Garante que o sistema funcione sem erros após a implementação. 
C) Determina o que o sistema deve fazer antes mesmo da implementação. 
D) Testa o software para verificar sua qualidade.==

A Engenharia de Requisitos é uma das fases mais importantes do desenvolvimento de software, pois define o que o sistema deve fazer antes mesmo da implementação.

==*Requisitos:* características e funcionalidade de sistemas, quem defini é o cliente.==

    funcionais: Defini o que o sistema deve fazer . ex: validação do usuário

    não funcional: defini restrições ou qualidades do sistemas. Ex: Identidade visual do sistema.

### Processo de engenharia de requisitos 

##### 1 - Levantamento(Elicitacao) de requisitos: 
Coleta das necessidades do cliente e usuários por meio de entrevistas, questionários, workshops, entre outras técnicas.

##### 2 - Analise e negociacao:
Avaliação da viabilidade técnica, econômica e organizacional dos requisitos, ajustando ou priorizando conforme necessário.

##### 3 - Especificacao
Documentação detalhada dos requisitos de forma clara e estruturada, geralmente em um Documento de Requisitos ou backlog.

##### 4 - Verificacao dos requisitos 
Revisão para garantir que os requisitos estão completos, consistentes e não contraditórios.

##### 5 - Validacao dos requisitos 
Confirmação de que os requisitos atendem às necessidades dos stakeholders e aos objetivos do sistema, garantindo que sejam corretos e úteis.

![[Pasted image 20250906195954.png]]
#### Tecnicas de levantamento de requisitos 

- entrevistas com clientes e usuarios 
- questionarios 
- observacao do ambiente de trabalho
- prototipacao 

### Modelos de ciclo de vida do software 

Vamos entender como construir software de forma estruturada e eficiente, utilizando o Modelo de ciclo de vida do software. Descubra as etapas essenciais para o sucesso do seu projeto. 

##### Modelo cascata (waterfall)

==Segue uma sequencia linear e rígida de fases==:
Requisitos -> projeto -> implementacao -> testes -> implementacao -> manutencao 

- Cada fase deve ser concluída antes da proxima comecar 
- indicado para projetos com requisitos bem definidos e pouca necessidade de mudancas

- *Desvantagem*: dificuldade em lidar com mudancas apos o inicio do projeto

![[Pasted image 20250823164916.png]]

O modelo em cascata funciona como uma linha de montagem: cada fase precisa ser concluída antes de passar para a próxima, sem voltar atrás.

• Modelo de desenvolvimento de software com etapas sequenciais e bem definidas. 
• Características: Cada fase só começa quando a anterior termina. 
• Vantagens: Simples, organizado, boa documentação.
• Desvantagens: Pouca flexibilidade, difícil lidar com mudanças.

#### Modelos incremental
- divide o desenvolvimento em pequenas partes(incremental)
- cada incremento entrega uma parte funcional do sistema, permitindo ajustes e melhorias ao longo do processo
• Vantagem: Feedback contínuo e maior flexibilidade para mudanças.
• Desafio/Desvantagem: Requer um bom planejamento para evitar desorganização. 
• Muito usado em sistemas que precisam de lançamentos rápidos e evolutivos
![[Pasted image 20250823170431.png]]

No modelo incremental, o projeto não é feito de forma aleatória. Ele é planejado desde o início, mas construído em partes.

O que evita bagunça? 
• Cada incremento segue um planejamento – Antes de programar qualquer funcionalidade, já se sabe onde ela se encaixa no sistema. 
• Feedback contínuo – O cliente e os usuários podem testar cada parte e sugerir ajustes sem precisar esperar o projeto todo ficar pronto. 
• Melhor adaptação a mudanças – Se algo novo for necessário, ele pode ser incorporado nos próximos incrementos sem precisar refazertudo.
#### Modelo espiral

O modelo espiral é como dar várias voltas ao redor de um problema, refinando a solução a cada ciclo. Ele combina o melhor do modelo cascata (planejamento estruturado) e do modelo incremental (desenvolvimento por partes), mas com um foco especial em análise de riscos

Cada ciclo da espiral passa por quatro fases e, a cada volta, o sistema fica mais completo:

1️⃣Planejamento – Define-se o que será feito no próximo ciclo (requisitos, objetivos e restrições). 
2️⃣Análise de Riscos – Identificam-se possíveis problemas (custo, segurança, tecnologia) e criam-se soluções para minimizá-los. 
3️⃣Desenvolvimento e Teste – A parte planejada é desenvolvida, testada e avaliada. 
4️⃣Avaliação e Decisão – Os stakeholders revisam o que foi feito e decidem se continuam para o próximo ciclo

Isso se repete até o sistema estar completo!

![[Pasted image 20250823170552.png]]
#### Modelo V (Validacao e verificacao)

Ele é uma evolução do modelo cascata, mas com um foco maior em testes e qualidade. Em vez de seguir apenas um fluxo linear, o Modelo V organiza o desenvolvimento e os testes em paralelo.

Imagine a letra V
- No lado esquedo, temos as etapas de desenvolvimento 
- No lado direito, cada fase tem uma etapa correspondente de teste
- no centro, o sistema é construido

![[Pasted image 20250823170642.png]]

Vantagens: 
• Qualidade elevada devido à forte validação e testes.
• Detecção de erros cedo, reduzindo custos de correção. 
• Ideal para sistemas críticos (exemplo: softwares médicos, aeroespaciais, bancários). 

Desvantagens • Exige documentação rigorosa.
• Pode ser mais lento devido ao grande número de testes.

#### Modelo Ágil (próximas aulas)

• Baseado em ciclos curtos chamados sprints, seguindo frameworks como Scrum ou Kanban. 
• O desenvolvimento é iterativo, colaborativo e adaptável a mudanças. 
• Prioriza entregas frequentes e a comunicação constante com o cliente. 
• Vantagem: Maior flexibilidade e entrega contínua de valor ao usuário.

### Qual Modelo Escolher?

A escolha do modelo de desenvolvimento depende do tipo de projeto, requisitos do cliente, grau de incerteza e necessidade de testes rigorosos.

![[Pasted image 20250823170734.png]]

### O que é o Ciclo de Vida do Software?
![[Pasted image 20250823170804.png]]

![[Pasted image 20250823170816.png]]
### Casos de Uso
Os casos de uso descrevem a interação entre os usuários e o sistema, ajudando a entender como as funcionalidades serão utilizadas.
![[Pasted image 20250823170838.png]]

### Elementos de um Caso de Uso

• Atores: Representam os usuários ou outros sistemas que interagem com o sistema. 
• Cenários: Sequência de ações entre ator e sistema. 
• Fluxo Principal: Caminho ideal da funcionalidade. 
• Fluxos Alternativos: Outras possibilidades, incluindo erros.

![[Pasted image 20250823170903.png]]
# Aula 15/08

![[Pasted image 20250815223359.png]]

### Ciclo de Vida do Software?

Cada modelo de desenvolvimento de software (como Cascata, Iterativo, Espiral e em V) pode aplicar o ciclo de vida de forma diferente. O ciclo de vida é contínuo, pois softwares frequentemente precisam de atualizações e melhorias ao longo do tempo.

Os estágios principais (requisitos, análise, projeto, implementação, testes, implantação e manutenção) geralmente são os mesmos, mas a forma como são organizados e executados varia.

### Stakeholders

"Stakeholders são todas as pessoas, grupos ou entidades que têm interesse ou são afetados pelas atividades e decisões de uma empresa ou projeto."

### Casos de Uso

Os casos de uso descrevem a interação entre os usuários e o sistema, ajudando a entender como as funcionalidades serão utilizadas.

Eles ajudam a responder perguntas como:
• Quem usa o sistema? 
• O que o usuário pode fazer no sistema? 
• Como o sistema responde a cada ação?


### Elementos de um Caso de Uso

• Sistema: Projeto que está sendo desenvolvimento 
• Atores: Representam os usuários ou outros sistemas que interagem com o sistema. 
• Ações: Funcionalidades 
• Cenários: Sequência de ações entre ator e sistema. 
• Fluxo Principal: Caminho ideal da funcionalidade. 
• Fluxos Alternativos: Outras possibilidades, incluindo erros.

Atores:
Dentro da modelagem de Casos de Uso, os atores representam pessoas, sistemas ou dispositivos que interagem com o sistema. Eles podem ser classificados em diferentes tipos dependendo do papel que desempenham.

![[Pasted image 20250823171203.png]]

Ator Primário 
• É aquele que inicia a interação com o sistema para alcançar um objetivo. 
• Representa um usuário principal do sistema.

Ator Secundário 
• Apoia a execução do caso de uso, mas não o inicia. 
• Pode ser outro sistema, um banco de dados ou um serviço externo.

![[Pasted image 20250823171213.png]]
![[Pasted image 20250823171219.png]]

Ações:
Referem-se às atividades ou operações realizadas pelo sistema e pelos atores durante a execução de um caso de uso. Essas ações são descritas para que todos os envolvidos no processo (analistas, desenvolvedores, usuários) possam entender o fluxo de interações e como o sistema deve responder a cada solicitação
![[Pasted image 20250823171235.png]]

![[Pasted image 20250823171242.png]]

Relacionamento:
São as interações entre os atores e os casos de uso, ou entre diferentes casos de uso dentro de um sistema. Eles são essenciais para descrever como as várias partes de um sistema se conectam e interagem. O entendimento desses relacionamentos ajuda a construir uma visão clara da dinâmica do sistema e das suas interações com os usuários e outros sistemas.

![[Pasted image 20250823171301.png]]

Tipos de Relacionamentos em Casos de Uso: 
• Relacionamento de Associação (ou Comunicação) 
• Relacionamento de Inclusão (Include) 
• Relacionamento de Extensão (Extend) 
• Generalização

![[Pasted image 20250823171438.png]]
![[Pasted image 20250823171453.png]]

# Aula 18/08

Imagine um sistema de caixa eletronico

Ator: Cliente

**Casos de Uso:**
- sacar dinheiro 
- depositar dinheiro
- consultar saldo
O cliente (ator) interage com o sistema para realizar essas ações.

### Documentacao do caso de uso

Para cada caso de uso, precisa de uma descricao detalhada, com as seguintes informacoes
- Nome do caso de uso
- ator(es) envolvidos(s)
- Objetivo do caso de uso
- Fluxo principal(passos principais que o ator e o sistema devem seguir)
- Fluxo alternativo(possiveis variacoes no processo)
- Pre-condicoes(o que precisar estar correto antes de executar o caso de uso)
- Pos-condicoes(o que deve ocorrer apos a execucao do caso de uso)

![[Pasted image 20250823171619.png]]
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

A principal motivacao foi a necessidade de maior flexibilidade, adaptacao as mudancas e foco na entrega contínua de valor ao cliente.

### Por que os Métodos Ágeis foram Criados?
Na década de 1990, o desenvolvimento de software enfrentava problemas como:
• Mudanças frequentes nos requisitos (clientes alteravam demandas no meio do projeto). 
• Longos prazos de entrega (modelos rígidos como o Cascata dificultavam adaptações).
• Baixa colaboração entre equipes (desenvolvedores, clientes e gestores trabalhavam isolados).
• Software final sem atender às expectativas (as entregas eram feitas apenas no final do projeto, sem validações constantes).

Em 2001, um grupo de especialistas criou o Manifesto Ágil, estabelecendo 4 valores e 12 princípios para um desenvolvimento mais eficiente e flexível.

![[Pasted image 20250823172741.png]]
![[Pasted image 20250823172749.png]]

### Características dos Métodos Ágeis

Os métodos ágeis possuem algumas características essenciais que os diferenciam dos modelos tradicionais:
1. Iterativo e Incremental – O software é desenvolvido em pequenos ciclos (iterações), entregando partes funcionais em cada ciclo. 
2. Flexível a Mudanças – Requisitos podem ser alterados conforme novas necessidades surgem. 
3. Colaboração e Comunicação – Equipes trabalham juntas e em contato frequente com o cliente. 
4. Entrega Contínua de Valor – Versões utilizáveis do software são entregues frequentemente, garantindo feedback constante. 
5. Melhoria Contínua – Após cada ciclo, há uma retrospectiva para aprimorar processos e evitar erros repetidos. 
6. Simplicidade – Busca-se desenvolver apenas o necessário, sem desperdícios. 
7. Foco no Cliente – O cliente participa ativamente, validando entregas e garantindo que suas expectativas sejam atendidas.
### Scrum

O Scrum é um dos métodos ágeis mais populares e estruturados para o desenvolvimento de software e gerenciamento de projetos. Ele organiza o trabalho em ciclos curtos chamados sprints, permitindo entregas rápidas e adaptáveis.

![[Pasted image 20250823172828.png]]


#### Papéis no Scrum

##### Product Owner (PO)

Representa os interesses do cliente. 
Define e prioriza as tarefas no Product Backlog.

##### Scrum Master
Garante que o time siga as práticas do Scrum. Remove impedimentos e facilita a comunicação.

##### Time de Desenvolvimento
Autogerenciado e multidisciplinar. 
Trabalha para entregar incrementos de software no final de cada sprint.

#### Eventos no Scrum

##### Sprints
O Scrum organiza o trabalho em ciclos chamados sprints, que duram entre 1 e 4 semanas.

##### Sprint Planning (Planejamento da Sprint)
O time define as tarefas a serem realizadas na sprint.

##### Daily Scrum (Reunião diária)
Duração de 15 minutos. 
Cada membro responde: O que fiz ontem? O que farei hoje? Há algum impedimento?

##### Sprint Review (Revisão da Sprint)
Apresentação do que foi concluído.
Feedback do Product Owner e stakeholders

##### Sprint Retrospective (Retrospectiva da Sprint)
Reflexão sobre o que pode ser melhorado no processo


#### Artefatos do Scrum

##### Product Backlog
Lista de todas as funcionalidades e melhorias do projeto, priorizadas pelo Product Owner

##### Sprint Backlog
Conjunto de tarefas selecionadas para a sprint atual.

##### Incremento
Parte funcional do produto entregue ao final da sprint.

### Como Funciona na Prática?
1. O Product Owner prioriza as tarefas no Product Backlog. 
2. No Sprint Planning, o time escolhe tarefas para o Sprint Backlog. 
3. Durante a Sprint (1-4 semanas), o time trabalha no desenvolvimento. 
4. Todos os dias, há a Daily Scrum para acompanhar o progresso. 
5. No final da sprint, ocorre a Sprint Review, onde o incremento é apresentado. 
6. A equipe realiza a Sprint Retrospective para aprender com a experiência e melhorar.

## Nem todo programa é um software

![[Pasted image 20250906204442.png]]![[Pasted image 20250906204447.png]]
![[Pasted image 20250906204456.png]]

## O que é Elicitação de Requisitos?


![[Pasted image 20250906204521.png]]
![[Pasted image 20250906204527.png]]![[Pasted image 20250906204538.png]]

## Entrevista

A entrevista é uma conversa planejada entre o analista de requisitos (P.O.) e as partes interessadas (cliente, usuários, gestores), com o objetivo de entender necessidades, expectativas, problemas e desejos em relação ao sistema a ser desenvolvido.


#### Por que usar entrevistas?

![[Pasted image 20250906204607.png]]

#### Etapas para realizar uma entrevista com o cliente

![[Pasted image 20250906204612.png]]

##### Planejamento
![[Pasted image 20250906204643.png]]
![[Pasted image 20250906204656.png]]

##### Abertura da entrevista
![[Pasted image 20250906204710.png]]

##### Condução da Entrevista
![[Pasted image 20250906204723.png]]

##### Encerramento

![[Pasted image 20250906204733.png]]

### Tipos de Perguntas

![[Pasted image 20250906204756.png]]

### Estrutura de um Roteiro de Entrevista 

![[Pasted image 20250906204817.png]]

### Questões Éticas e Proteção de Dados
![[Pasted image 20250906205717.png]]
![[Pasted image 20250906205723.png]]

### Dicas Práticas

![[Pasted image 20250906205740.png]]

### Documento de Visão

![[Pasted image 20250906210122.png]]
![[Pasted image 20250906205759.png]]

Ele não entra em detalhes técnicos profundos, mas serve como um guia estratégico e uma referência durante todo o projeto

![[Pasted image 20250906205812.png]]

![[Pasted image 20250906205825.png]]

#### Escopo do Projeto

O escopo é como o contrato de expectativas entre a equipe e o cliente. Ele mostra o que vamos desenvolver neste projeto e o que vai ficar para depois. Isso ajuda a equipe a manter o foco, evita retrabalho e garante que todos estejam de acordo com o que será entregue.

![[Pasted image 20250906205843.png]]
![[Pasted image 20250906205849.png]]

![[Pasted image 20250906205941.png]]

#### Contextualização

![[Pasted image 20250906205953.png]]![[Pasted image 20250906210002.png]]

#### Visão do Produto

![[Pasted image 20250906210013.png]]
![[Pasted image 20250906210027.png]]

#### Valor para o Cliente

![[Pasted image 20250906210042.png]]

![[Pasted image 20250906210048.png]]

#### Objetivos de Negócio

![[Pasted image 20250906210157.png]]

#### Objetivos Técnicos

![[Pasted image 20250906210209.png]]

#### Funcionalidades (Características-Chave)

![[Pasted image 20250906210241.png]]
![[Pasted image 20250906210252.png]]
![[Pasted image 20250906210311.png]]

#### Restrições

![[Pasted image 20250906210323.png]]![[Pasted image 20250906210333.png]]

#### Partes Interessadas (Stakeholders)

![[Pasted image 20250906210347.png]]
#### Requisitos Funcionais

![[Pasted image 20250906210359.png]]

#### Requisitos Não Funcionais

![[Pasted image 20250906210412.png]]

#### Interface do Usuário

![[Pasted image 20250906210425.png]]


#### Protótipos e Wireframes

![[Pasted image 20250906210439.png]]

####   Metodologia de Desenvolvimento
![[Pasted image 20250906211658.png]]

#### Anexos do Projeto

![[Pasted image 20250906211707.png]]


## Modelo de Classes na Análise Orientada a Objetos

### Diagrama de Casos de Uso x Diagrama de Classes
![[Pasted image 20250906211751.png]]

![[Pasted image 20250906211804.png]]
![[Pasted image 20250906211820.png]]


#### Modelo de Classes na Análise Orientada a Objetos

![[Pasted image 20250906211915.png]]

### O que são objetos em um Diagrama de Classes?

![[Pasted image 20250906211928.png]]![[Pasted image 20250906211935.png]]

Uma classe é como uma receita de bolo – ela define os ingredientes (atributos) e o modo de preparo (métodos). Um objeto é um bolo real, feito a partir da receita, com ingredientes específicos.

![[Pasted image 20250906211945.png]]

### Estágios do Modelo de Classes na Análise Orientada a Objetos
![[Pasted image 20250906212007.png]]

#### Elementos Principais de um Diagrama de Classes

![[Pasted image 20250906212034.png]]

### Técnicas para Identificação de Classes e Construção do Modelo de Classes
![[Pasted image 20250906215755.png]]

### Relação Entre o Modelo de Classes e o Desenvolvimento de Software

![[Pasted image 20250906215810.png]]

### Diagrama de classes

![[Pasted image 20250906215825.png]]


### Tipos de relacionamento

![[Pasted image 20250906215838.png]]

![[Pasted image 20250906215847.png]]


#### Associação

![[Pasted image 20250906215903.png]]![[Pasted image 20250906215909.png]]

#### Herança ou Generalização

![[Pasted image 20250906215921.png]]![[Pasted image 20250906215927.png]]
![[Pasted image 20250906215935.png]]![[Pasted image 20250906215941.png]]

#### Dependência
![[Pasted image 20250906220042.png]]![[Pasted image 20250906220050.png]]![[Pasted image 20250906220101.png]]

#### Agregação

![[Pasted image 20250906220115.png]]![[Pasted image 20250906220121.png]]
![[Pasted image 20250906220127.png]]![[Pasted image 20250906220137.png]]

#### Composição
![[Pasted image 20250906220155.png]]
![[Pasted image 20250906220202.png]]
![[Pasted image 20250906220209.png]]

### Principais Tipos de Multiplicidade

![[Pasted image 20250906220236.png]]

#### Um para Um

![[Pasted image 20250906220251.png]]

#### Um para Muitos

![[Pasted image 20250906220303.png]]

#### Muitos para Muitos

![[Pasted image 20250906220312.png]]

![[Pasted image 20250906220319.png]]![[Pasted image 20250906220345.png]]

### Relacionamentos Ternários

![[Pasted image 20250906220402.png]]

### Auto relacionamento / Relacionamento Reflexivo

![[Pasted image 20250906220412.png]]

### Visibilidade
![[Pasted image 20250906220422.png]]![[Pasted image 20250906220429.png]]

## Diagrama de objetos

O Diagrama de Objetos faz parte da UML (Unified Modeling Language) e serve para representar instâncias concretas das classes em um determinado momento da execução do sistema.

![[Pasted image 20250927184512.png]]

Se o Diagrama de Classes mostra a estrutura e os relacionamentos de forma genérica, o Diagrama de Objetos mostra exemplos reais desses relacionamentos, com dados específicos.

### Principais características

![[Pasted image 20250927184531.png]]

![[Pasted image 20250927184539.png]]

### Notação do Diagrama de Objetos

Os objetos no diagrama são representados por retângulos, assim como as classes, mas com algumas diferenças na notação:

• O nome do objeto segue este formato: nomeObjeto : NomeClasse 
• Os atributos do objeto mostram valores reais. 
•O sublinhado indica que estamos falando de um objeto e não de uma classe

![[Pasted image 20250927184630.png]]
![[Pasted image 20250927184636.png]]
![[Pasted image 20250927184640.png]]

### Apoio na Análise de Requisitos

![[Pasted image 20250927184657.png]]

### Validação de Cenários

![[Pasted image 20250927184713.png]]

### Comunicação entre Stakeholders

![[Pasted image 20250927184751.png]]

### Suporte ao Design do Sistema

![[Pasted image 20250927184807.png]]

### Ferramenta CASE

![[Pasted image 20250927184819.png]]

#### Principais funções das ferramentas CASE:

![[Pasted image 20250927185034.png]]

# Diagrama de classes
## Tipos de variáveis

![[Pasted image 20251004193838.png]]
![[Pasted image 20251004193844.png]]![[Pasted image 20251004193850.png]]

### int (inteiro)
![[Pasted image 20251004193900.png]]

### float ou double (ponto flutuante)
![[Pasted image 20251004193918.png]]

### char (caractere)

![[Pasted image 20251004193928.png]]

### string (texto)

![[Pasted image 20251004193938.png]]

### bool ou boolean (lógico)

![[Pasted image 20251004193949.png]]

### data / Date (data)
![[Pasted image 20251004194001.png]]

### long

![[Pasted image 20251004194013.png]]

### Retorno dos métodos

![[Pasted image 20251004194027.png]]

## Onde estão as variáveis? Qual sua classificação?

![[Pasted image 20251004194035.png]]

### Variáveis de Instância

![[Pasted image 20251004194043.png]]

### Variáveis de Classe (ou Estáticas)

![[Pasted image 20251004194055.png]]
![[Pasted image 20251004194104.png]]

### Variáveis locais

![[Pasted image 20251004194113.png]]

### Variáveis de Parâmetro

![[Pasted image 20251004194122.png]]

## Visibilidade de Atributos e Métodos

![[Pasted image 20251004194136.png]]
![[Pasted image 20251004194141.png]]
![[Pasted image 20251004194156.png]]
![[Pasted image 20251004194201.png]]


### Tipos de Visibilidade

![[Pasted image 20251004194210.png]]

### Pública (+)

![[Pasted image 20251004194223.png]]
![[Pasted image 20251004194229.png]]


### Privada (-)

![[Pasted image 20251004194240.png]]
![[Pasted image 20251004194245.png]]

### Protegida (#)
![[Pasted image 20251004194256.png]]
![[Pasted image 20251004194302.png]]

## Por que construir diagramas de classes consistentes é importante na engenharia de software?

![[Pasted image 20251004194316.png]]
![[Pasted image 20251004194324.png]]

## O forma de construir o diagrama de classes tem a ver o tipo de desenvolvimento escolhido no ciclo de vida do software?

![[Pasted image 20251004194336.png]]

### Modelo em Cascata

![[Pasted image 20251004194343.png]]

## Modelo Incremental

![[Pasted image 20251004194350.png]]

## Modelo Espiral

![[Pasted image 20251004194357.png]]

## Modelo V

![[Pasted image 20251004194407.png]]

# Modelos de Desenvolvimento de Software

![[Pasted image 20251120165228.png]]

![[Pasted image 20251120165244.png]]


## Modelo de Prototipação

![[Pasted image 20251120165257.png]]

## Modelo RAD (Desenvolvimento Rápido de Aplicações

![[Pasted image 20251120165311.png]]

## Modelo RUP (Processo Unificado da Rational)

![[Pasted image 20251120165324.png]]

## Modelo DevOps

![[Pasted image 20251120165338.png]]
## Qual a diferença entre Modelo de Prototipação e Incremental ?

![[Pasted image 20251120165359.png]]

## Diferença entre Modelo de RUP x RAD ?

![[Pasted image 20251120165415.png]]
![[Pasted image 20251120165422.png]]

## Esses modelos são considerados ágeis?

![[Pasted image 20251120165438.png]]

# Kanban


![[Pasted image 20251120170404.png]]

## Princípios básicos

![[Pasted image 20251120170422.png]]

## Quadro Kanban

![[Pasted image 20251120170433.png]]
![[Pasted image 20251120170440.png]]

## Vantagens

![[Pasted image 20251120170500.png]]

## Desafios / Desvantagens

![[Pasted image 20251120170516.png]]

## Comparação com o Scrum

![[Pasted image 20251120170528.png]]

![[Pasted image 20251120170538.png]]

### Evidência acadêmica

![[Pasted image 20251120170549.png]]

![[Pasted image 20251120170557.png]]
### Estudo de Caso

![[Pasted image 20251120170607.png]]
## Conclusão

![[Pasted image 20251120170619.png]]
# Modelagem de interações

![[Pasted image 20251109194205.png]]

## Principais Diagramas de Interação na UML

![[Pasted image 20251109194213.png]]

## Características da Modelagem de Interações
![[Pasted image 20251109194237.png]]

## Vantagens de modelagens de interação

![[Pasted image 20251109194258.png]]

## Relação com o Diagrama de Casos de Uso

![[Pasted image 20251109194314.png]]

## Por que fazer Diagramas de Interação?
![[Pasted image 20251109194325.png]]

## Diagrama de Sequência (UML)

![[Pasted image 20251109194340.png]]

![[Pasted image 20251109195910.png]]

### Como funciona?
![[Pasted image 20251109195925.png]]

![[Pasted image 20251109195932.png]]

### Principais elementos do Diagrama de Sequência

![[Pasted image 20251109195944.png]]

#### Principais elementos do Diagrama de Sequência

![[Pasted image 20251109195957.png]]

![[Pasted image 20251109200002.png]]

![[Pasted image 20251109200007.png]]
![[Pasted image 20251109200011.png]]
![[Pasted image 20251109200016.png]]
![[Pasted image 20251109200021.png]]

#### Como modelar um Diagrama de Sequência?

![[Pasted image 20251109200033.png]]
![[Pasted image 20251109200038.png]]

### O que são estereótipos em UML?

![[Pasted image 20251109200055.png]]

![[Pasted image 20251109200111.png]]
![[Pasted image 20251109200116.png]]
![[Pasted image 20251109200120.png]]

![[Pasted image 20251109200125.png]]

![[Pasted image 20251109200129.png]]
![[Pasted image 20251109200133.png]]
![[Pasted image 20251109200137.png]]
![[Pasted image 20251109200142.png]]
![[Pasted image 20251109200148.png]]


# Diagrama de Comunicação (UML)

![[Pasted image 20251109202419.png]]
![[Pasted image 20251109202429.png]]

![[Pasted image 20251109202441.png]]

### Quando usar o Diagrama de Comunicação?

![[Pasted image 20251109202446.png]]

![[Pasted image 20251109202459.png]]

![[Pasted image 20251109202506.png]]

![[Pasted image 20251109202513.png]]

![[Pasted image 20251109202519.png]]
![[Pasted image 20251109202525.png]]
![[Pasted image 20251109202530.png]]


# Qualidade de Software

![[Pasted image 20251109202659.png]]
![[Pasted image 20251109202705.png]]
![[Pasted image 20251109202711.png]]


## Qualidade de software
![[Pasted image 20251109202727.png]]

### Mas o que seria arquitetura de software?

![[Pasted image 20251109202734.png]]

![[Pasted image 20251109204020.png]]

### Boas práticas

![[Pasted image 20251109204032.png]]
![[Pasted image 20251109204037.png]]

### Definições sobre Qualidade

![[Pasted image 20251109204047.png]]
![[Pasted image 20251109204052.png]]

### Qualidade x Confiança

![[Pasted image 20251109204107.png]]
![[Pasted image 20251109204112.png]]
![[Pasted image 20251109204119.png]]

![[Pasted image 20251109204132.png]]

### Órgãos padronizadores e reguladores

![[Pasted image 20251109204152.png]]
![[Pasted image 20251109204158.png]]

####  ISO 

![[Pasted image 20251109204220.png]]

####  IEEE (Institute of Electrical and Electronics Engineers)
![[Pasted image 20251109204328.png]]

#### OMG (Object Management Group)

![[Pasted image 20251109204338.png]]

#### W3C (World Wide Web Consortium)
![[Pasted image 20251109204353.png]]
#### NIST (National Institute of Standards and Technology - EUA)

![[Pasted image 20251109204406.png]]

#### ABNT (Associação Brasileira de Normas Técnicas)
![[Pasted image 20251109204427.png]]



## O que é Qualidade em Arquitetura de Software? 

![[Pasted image 20251109204445.png]]

![[Pasted image 20251109204458.png]]

![[Pasted image 20251109204503.png]]

### Características de uma Arquitetura de Qualidade
![[Pasted image 20251109204518.png]]
![[Pasted image 20251109204523.png]]
![[Pasted image 20251109204527.png]]
![[Pasted image 20251109204533.png]]
![[Pasted image 20251109204541.png]]
![[Pasted image 20251109204546.png]]
![[Pasted image 20251109204551.png]]
![[Pasted image 20251109204556.png]]
![[Pasted image 20251109204603.png]]

### Como Garantir Qualidade na Arquitetura?

![[Pasted image 20251109204609.png]]

### Técnicas para Avaliar e Melhorar os Atributos de Qualidade

![[Pasted image 20251109204704.png]]

### Trade-offs e Decisões Arquiteturais
![[Pasted image 20251109204717.png]]
![[Pasted image 20251109204723.png]]
![[Pasted image 20251109204729.png]]
![[Pasted image 20251109204737.png]]
![[Pasted image 20251109204742.png]]

### Quem está envolvido na escolha da Arquitetura?

![[Pasted image 20251109204753.png]]
![[Pasted image 20251109204759.png]]

### Boas Práticas para Garantir Qualidade na Arquitetura

![[Pasted image 20251109204810.png]]
![[Pasted image 20251109204815.png]]
![[Pasted image 20251109204821.png]]
![[Pasted image 20251109204832.png]]


# O que é um Diagrama de Transição de Estados?

![[Pasted image 20251109205142.png]]

![[Pasted image 20251109205147.png]]

![[Pasted image 20251109205151.png]]

![[Pasted image 20251109205155.png]]

## Por que usar o Diagrama de Estados?

![[Pasted image 20251109205211.png]]
![[Pasted image 20251109205217.png]]

![[Pasted image 20251109205221.png]]

![[Pasted image 20251109205225.png]]
![[Pasted image 20251109205229.png]]
![[Pasted image 20251109205235.png]]
![[Pasted image 20251109205239.png]]
![[Pasted image 20251109205244.png]]
![[Pasted image 20251109205248.png]]
![[Pasted image 20251109205252.png]]
![[Pasted image 20251109205258.png]]
![[Pasted image 20251109205306.png]]
![[Pasted image 20251109205311.png]]
![[Pasted image 20251109205315.png]]
![[Pasted image 20251109205321.png]]
![[Pasted image 20251109205325.png]]
![[Pasted image 20251109205329.png]]
![[Pasted image 20251109205333.png]]
![[Pasted image 20251109205338.png]]
![[Pasted image 20251109205343.png]]
![[Pasted image 20251109205350.png]]
![[Pasted image 20251109205355.png]]
![[Pasted image 20251109205402.png]]
![[Pasted image 20251109205406.png]]
![[Pasted image 20251109205410.png]]
![[Pasted image 20251109205415.png]]
![[Pasted image 20251109205419.png]]
![[Pasted image 20251109205423.png]]
![[Pasted image 20251109205429.png]]
![[Pasted image 20251109205432.png]]
![[Pasted image 20251109205436.png]]
![[Pasted image 20251109205441.png]]
![[Pasted image 20251109205445.png]]

# Diagrama de atividades

![[Pasted image 20251109205507.png]]
![[Pasted image 20251109205511.png]]
![[Pasted image 20251109205515.png]]
![[Pasted image 20251109205520.png]]

![[Pasted image 20251109205524.png]]
![[Pasted image 20251109205530.png]]
![[Pasted image 20251109205536.png]]
![[Pasted image 20251109205540.png]]
![[Pasted image 20251109205545.png]]
![[Pasted image 20251109205548.png]]
![[Pasted image 20251109205555.png]]
![[Pasted image 20251109205600.png]]
![[Pasted image 20251109205607.png]]
![[Pasted image 20251109205612.png]]
![[Pasted image 20251109205619.png]]
![[Pasted image 20251109205624.png]]
![[Pasted image 20251109205628.png]]
![[Pasted image 20251109205632.png]]
![[Pasted image 20251109205635.png]]
![[Pasted image 20251109205639.png]]
![[Pasted image 20251109205644.png]]


# Modelo de interacao:

### Principais diagramas 

1 - Diagrama de Sequência
2 - Diagrama de Comunicacao(anteriormente chamado de colaboracao)
3 - Diagrama de tempo (Timing Diagram6
4 - Diagrama de interacao Geral

#### Caracteristicas

- baseada na troca de mensagens entre objetos
- representa eventos temporais (quem faz o que e quando)
- complementa os diagramas de classe e caos e casos de uso com detalhamento de comportamento
- pode mostrar criacao e destruicao de objetos 
- é focada em cenários especificos (como os descritos nos casos de uso)

##### Vantagens 
- ajuda a entender comos os componentes do sistema se comunicam
- facilita a deteccao de erros de logica ou de responsabilidade entre classes
- suporte à análise e validacao de requisitos
- facilita o trabalho em equipe com uma visualizacao clara do comportamento dos sistema
- util na documentacao do sistema e comunicacao entre analistas, desenvolvedores e clientes 

#### Relacao com o diagrama de casos de uso

- o caso de uso mostra  oque o sistema deve fazer 
- o diagrama de interacao mostra como os objetos interagem para executar um caso de uso especifico

Exemplo:
==Casp de uso: Realizar login==
Diagrama de sequencia: mostra o passo a passo entre usuario, tela de login, controlador e banco de dados durante o processo de login. 


Não é um gabarito,  há formas diferentes de serem feitos

#### Porque faszer os diagrams de interacao

- ==....==

### Diagrama de sequencia (UML)

o dagrama de sequencia mostara quem faz o que e a sequencia 

##### Como funciona

- o diagrama é lido de cima para baixo, representando a ordem das mensagens no tempo
- cada objeto envolvido é representado horizontalmente, e o tempo (a sequencia dos eventos) é representado verticalmente 
- as mensagens trocadas sao representadas por setas horizontais 
- o foco é no comportamento do sistema durante a execucao de uma operacao ou caso de uso


### Principais elementos 

==...==

### Como modelar m diagrama de sequencia 

- escolha um cenário (geralemnte com base em um caso de uso)
- identifique os obejtos ==...==


### O que sao estereotipos em UML?

estereotipos sao rotulos que colocamos nos elementos da UML (Como objetos, classes, ou participantes do diagrama) para indicar o papel que aquele elementos exerce emm uma interecao

#### boundary: fronteira

- representa a interface que interagem com o mundo exterior (usuario ou outro sistema)
- pode ser uma tela, formulario, API, etc
- é onde a cao comeca no sistema
#### Control - controle
- representa o "cerebro" que cordena as acoes, valida dados, chama as entidades, decide oque fazer 
- geralmente é uma classe responsavel por controlar um caso de uso

#### entity - entidade

- representa os dados do sistema ou objetos de nefocio
- sao geralmente classes persistentes, ligadas a banco de dados ou modelo de negocio


# Diagrama de comunicacao (UML)

O ==diagrama de comunicacao== mostra como os objetos interagem entre si por meio de mensagens, como foco na estrutura da comunicacao entre eles e menos foco na ordem temporal (embora a ordem aidna exista)

ele é util para representar a estrutura das interacoes em um cenario espeifico, destacando os relacionamentos entre os objetos e as mensagens trocadas entre eles. 

- sequencia = "quando" as mensagens acontecem
- comunicacao = "quem fala com quem"

### quando usar o diagrama de comiunicacao 

- quando quiser mostrar a estrutura dos relacionamentos entre objetos durante um cenário específico
- quando o layout dem rede é facil ==...==

### Palavra-chave: vínculo


### Vantagens

- oferece uma visao compacta e estruturada da interacao entre objetos 
- util para visualizar quem pode quem
- ==..==

### Condicoes

- indica quem uma mensagem so sera enviada quando uma determinada condicao for satisfeita 
- a condicao vem entre colchetes antes da mensagem
