
## Cap 1 - Visão Geral

### Sistema operacional

*Definição*

é o responsável por controlar o computador e gerenciar os recursos de hardware e software, processador, memória, periféricos e dados.

==é o intermediário essencial==. Conecta o hardware ao usuário, tornando o uso do computador <strong>simples e seguro</strong> sem que o usuário precise conhecer os detalhes físico da máquina.

Sem o SO o usuário precisaria conhecer <strong>todos os detalhes do hardware</strong> para operar o computador.

O sistema operacional tem como objetivo funcionar como uma interface entre o usuário e o computador, tornando sua utilização mais simples, rápida e segura.

o So é o primeiro programa executado ao ligar o PC e permanece ativo gerenciando os recursos até o desligamento.

Funciona de forma contínuo e transparente, garantindo que os aplicativos acessem hardware de forma segura e organizada. 

![[Pasted image 20260913170347.png]]

A grande diferença entre um sistema operacional e aplicações convencionais é a maneira como suas rotinas são executadas em função do tempo. Um sistema operacional não é executado de forma linear como na maioria das aplicações, com início, meio e fim. Suas rotinas são executadas concorrentemente em função de eventos assíncronos, ou seja, eventos que podem ocorrer a qualquer momento.

#### Funções principais

- Estender a máquina (abstração) - Facilidade de acesso aos recursos do sistema
Esconde a complexidade do hardware do programador, apresentando uma interface amigável.


- Compartilhamento de recursos de forma organizada e protegida
Controla de forma <strong>ordenada e compartilhada</strong> o uso de memória do processador e dispositivos de E/S.

#### Máquina de Camadas

O computador pode ser compreendido como uma máquina de camadas ou máquina de níveis, em que inicialmente existem dois níveis: hardware (nível 0) e sistema operacional (nível 1). Desta forma, a aplicação do usuário interage diretamente com o sistema operacional, ou seja, como se o hardware não existisse. Esta visão modular e abstrata é chamada de máquina virtual. 

Na realidade, um computador não possui apenas dois níveis, e sim tantos níveis quantos foremnecessários para adequar o usuário às suas diversas aplicações. Quando o usuário está trabalhando emum desses níveis não necessita saber da existência das outras camadas, acima ou abaixo de sua máquina virtual.

![[Pasted image 20260927111102.png]]

#### Tipos de Sistemas Operacionais

![[Pasted image 20260927112625.png]]

##### Sistemas Monoprogramáveis/Monotarefa

execução de um único programa

Qualquer outra aplicação, para ser executada, deveria aguardar o término do programa corrente.

Os sistemas monoprogramáveis, se caracterizam por permitir que o processador, a memória e os periféricos permaneçam exclusivamente dedicados à execução de um único programa

Os sistemas monotarefa, como também são chamados, caracterizam-se por permitir que todos os recursos do sistema fiquem exclusivamente dedicados a uma única tarefa.

A memória é subutilizada caso o programa não a preencha totalmente, e os periféricos, como discos e impressoras, estão dedicados a um único usuário, nem sempre utilizados de forma integral.

==são de simples implementação, não existindo muita preocupação com problemas decorrentes do compartilhamento de recursos, como memória, processador e dispositivos de E/S.==
##### Sistemas Multiprogramáveis/Multitarefa

os recursos computacionais são compartilhados entre os diversos usuários e aplicações

Enquanto em sistemas monoprogramáveis existe apenas um programa utilizando os recursos disponíveis, nos multiprogramáveis várias aplicações compartilham esses mesmos recursos.

O sistema operacional se preocupa em gerenciar o acesso concorrente aos seus diversos recursos, como memória, processador e periféricos, de forma ordenada e protegida, entre os diversos programas.

A principal vantagem dos sistemas multiprogramáveis é a redução de custos em função da possibilidade do compartilhamento dos diversos recursos entre as diferentes aplicações. Além disso, sistemas multiprogramáveis possibilitam na média a redução total do tempo de execução das aplicações.

==são de implementação muito mais complexa.==

A partir do número de usuários que interagem com o sistema operacional, podemos classificar os sistemas multiprogramáveis como monousuário ou multiusuário

- monousuário
Sistemas multiprogramáveis monousuário são encontrados em computadores pessoais e estações de trabalho, onde há apenas um único usuário interagindo com o sistema.

- multiusuário
Sistemas multiprogramáveis multiusuário são ambientes interativos que possibilitam a diversos usuários conectarem-se ao sistema simultaneamente.

Os sistemas multiprogramáveis ou multitarefa podem ser classificados pela forma com que suas aplicações são gerenciadas, podendo ser divididos em sistemas batch, de tempo compartilhado ou de tempo real. Um sistema operacional pode suportar um ou mais desses tipos de processamento

###### Sistemas batch

O processamento batch tem a característica de não exigir a interação do usuário com a aplicação. Todas as entradas e saídas de dados da aplicação são implementadas por algum tipo de memória secundária, geralmente arquivos em disco.

Esses sistemas, quando bem projetados, podem ser bastante eficientes, devido à melhor utilização do processador, entretanto podem oferecer tempos de resposta longos

###### Sistemas de tempo compartilhado

Os sistemas de tempo compartilhado (time-sharing) permitem que diversos programas sejam executados a partir da divisão do tempo do processador em pequenos intervalos, denominados ==fatia de tempo (time-slice).==

Caso a fatia de tempo não seja suficiente para a conclusão do programa, ele é interrompido pelo sistema operacional e substituído por um outro, enquanto fica aguardando por uma nova fatia de tempo.

sistemas de tempo compartilhado permitem a interação dos usuários com o sistema através de terminais que incluem vídeo, teclado e mouse

==Devido a esse tipo de interação, os sistemas de tempo compartilhado também ficaram conhecidos como sistemas on-line.==

###### Sistemas de tempo real

Os sistemas de tempo real (real-time) são implementados de forma semelhante aos sistemas de tempo compartilhado. O que caracteriza a diferença entre os dois tipos de sistemas é o tempo exigido no processamento das aplicações.

Enquanto em sistemas de tempo compartilhado o tempo de processamento pode variar sem comprometer as aplicações em execução, nos sistemas de tempo real os tempos de processamento devem estar dentro de limites rígidos, que devem ser obedecidos, caso contrário poderão ocorrer problemas irreparáveis.

Nos sistemas de tempo real não existe a ideia de fatia de tempo, implementada nos sistemas de tempo compartilhado. Um programa utiliza o processador o tempo que for necessário ou até que apareça outro mais prioritário. A importância ou prioridade de execução de um programa é definida pela própria aplicação e não pelo sistema operacional.

Esses sistemas, normalmente, estão presentes em aplicações de controle de processos, como no monitoramento de refinarias de petróleo, controle de tráfego aéreo, de usinas termoelétricas e nucleares, ou em qualquer aplicação em que o tempo de processamento é fator fundamental.

##### Sistemas com Múltiplos Processadores

Os sistemas com múltiplos processadores caracterizam-se por possuir duas ou mais UCPs interligadas e trabalhando em conjunto.

==A vantagem deste tipo de sistema é permitir que vários programas sejam executados ao mesmo tempo ou que um mesmo programa seja subdividido em partes para serem executadas simultaneamente em mais de um processador.==

Os conceitos aplicados ao projeto de sistemas com múltiplos processadores incorporam os mesmos princípios básicos e benefícios apresentados na multiprogramação, além de outras características e vantagens específicas como escalabilidade, disponibilidade e balanceamento de carga.

-  Escalabilidade
Escalabilidade é a capacidade de ampliar o poder computacional do sistema apenas adicionando novos processadores.

- Disponibilidade
Disponibilidade é a capacidade de manter o sistema em operação mesmo em casos de falhas.

- Balanceamento de carga
Balanceamento de carga é a possibilidade de distribuir o processamento entre os diversos processadores da configuração a partir da carga de trabalho de cada processador, melhorando, assim, o desempenho do sistema como um todo


Um fator-chave no desenvolvimento de sistemas operacionais com múltiplos processadores é a forma de comunicação entre as UCPs e o grau de compartilhamento da memória e dos dispositivos de entrada e saída. Em função desses fatores, podemos classificar os sistemas com múltiplos processadores emfortemente acoplados ou fracamente acoplados.

==A grande diferença entre os dois tipos de sistemas é que em sistemas fortemente acoplados existe apenas uma memória principal sendo compartilhada por todos os processadores, enquanto nos fracamente acoplados cada sistema tem sua própria memória individual. Além disso, a taxa de transferência entre processadores e memória em sistemas fortemente acoplados é muito maior que nos fracamente acoplados.==

###### Sistemas fortemente acoplados

Nos sistemas fortemente acoplados (tightly coupled) existem vários processadores compartilhando uma única memória física (shared memory) e dispositivos de entrada/saída sendo gerenciados por apenas um sistema operacional. Em função destas características, os sistemas fortemente acoplados também são conhecidos como multiprocessadores

- SMP
Os sistemas SMP caracterizam-se pelo tempo uniforme de acesso à memória principal pelos diversos processadores

- NUMA
Os sistemas NUMA apresentam diversos conjuntos reunindo processadores e memória principal, sendo que cada conjunto é conectado aos outros através de uma rede de interconexão. O tempo de acesso à memória pelos processadores varia em função da sua localização física.

Nos sistemas SMP e NUMA todos os processadores têm as mesmas funções.

###### Sistemas fracamente acoplados

Os sistemas fracamente acoplados (loosely coupled) caracterizam-se por possuir dois ou mais sistemas computacionais conectados através de linhas de comunicação. Cada sistema funciona de forma independente, possuindo seu próprio sistema operacional e gerenciando seus próprios recursos, como UCP, memória e dispositivos de entrada/saída.

Em função destas características, os sistemas fracamente acoplados também são conhecidos como ==multicomputadores==.

Com base no grau de integração dos hosts da rede, podemos dividir os sistemas fracamente acoplados emsistemas operacionais de rede e sistemas distribuídos. A grande diferença entre os dois modelos é a capacidade do sistema operacional em criar uma imagem única dos serviços disponibilizados pela rede.

Os sistemas operacionais de rede (SOR) permitem que um host compartilhe seus recursos, como uma impressora ou diretório, com os demais hosts da rede.

Enquanto nos SORs os usuários têm o conhecimento dos hosts e seus serviços, nos sistemas distribuídos o sistema operacional esconde os detalhes dos hosts individuais e passa a tratá-los como um conjunto único, como se fosse um sistema fortemente acoplado.

Outro exemplo de sistema distribuído são os clusters. Em um cluster existem dois ou mais servidores ligados, normalmente, por algum tipo de conexão de alto desempenho


## Cap 2 - Conceitos de Hardware e software

Neste capítulo serão apresentados conceitos básicos de hardware e software relativos à arquitetura de computadores.

### Hardware

Um sistema computacional é um conjunto de circuitos eletrônicos interligados, formado por processadores, memórias, registradores, barramentos, monitores de vídeo, impressoras, mouse, discos magnéticos, além de outros dispositivos físicos (hardware).

Todos os componentes de um sistema computacional são agrupados em três subsistemas básicos, chamados unidades funcionais: processador ou unidade central de processamento, memória principal e dispositivos de entrada/saída.

![[Pasted image 20260927115434.png]]

#### Processador

O processador, também denominado unidade central de processamento (UCP), gerencia todo o sistema computacional controlando as operações realizadas por cada unidade funcional. A principal função do processador é controlar e executar instruções presentes na memória principal, por meio de operações básicas como somar, subtrair, comparar e movimentar dados.

é composto por unidade de controle, unidade lógica e aritmética, e registradores.

A unidade de controle (UC) é responsável por gerenciar as atividades de todos os componentes do computador, como a gravação de dados em discos ou a busca de instruções na memória. 

A unidade lógica e aritmética (ULA), como o nome indica, é responsável pela realização de operações lógicas (testes e comparações) e aritméticas (somas e subtrações).

A sincronização de todas as funções do processador é realizada através de um sinal de clock. Este sinal é um pulso gerado ciclicamente que altera variáveis de estado do processador.

Os registradores são dispositivos com a função principal de armazenar dados temporariamente. O conjunto de registradores funciona como uma memória de alta velocidade interna do processador, porémcom uma capacidade de armazenamento reduzida e custo maior que o da memória principal.

Alguns registradores podem ser manipulados diretamente por instruções (registradores de uso geral), enquanto outros são responsáveis por armazenar informações de controle do processador e do sistema operacional (registradores de uso específico), dos tipos: 

- o contador de instruções (CI) ou program counter (PC) contém o endereço da próxima instrução que o processador deve buscar e executar.
- o apontador da pilha (AP) ou stack pointer (SP) contém o endereço de memória do topo da pilha, que é a estrutura de dados onde o sistema mantém informações sobre programas que estão sendo executados;
- o registrador de instruções (RI) é responsável por armazenar a instrução que será decodificada e executada pelo processador;
- o registrador de status ou program status word (PSW) é responsável por armazenar informações sobre a execução de instruções, como a ocorrência de overflow.

O ciclo de busca e instrução é a maneira pela qual o processador executa os programas armazenados na memória principal segundo os passos descritos a seguir: O processador busca na memória principal a instrução armazenada no endereço indicado pelo CI e a armazena no RI. O processador incrementa o CI para que o registrado contenha o endereço da próxima instrução. O processador decodifica a instrução armazenada no RI. O processador busca os operandos na memória, se houver. O processador executa a instrução decodificada. Após este último passo, o ciclo é reiniciado do passo (a).

#### Memória Principal

A memória principal, primária ou real é o local onde são armazenados instruções e dados. A memória é composta por unidades de acesso chamadas células, sendo cada célula composta por um determinado número de bits. O bit é a unidade básica de memória, podendo assumir o valor lógico 0 ou 1.

O acesso ao conteúdo de uma célula é realizado através da especificação de um número chamado endereço. O endereço é uma referência única que podemos fazer a uma célula de memória.

A especificação do endereço é realizada por um registrador denominado registrador de endereço de memória (memory address register — MAR). Pelo conteúdo deste registrador, a unidade de controle sabe qual a célula de memória que será acessada.

Outro registrador usado em operações com a memória é o registrador de dados da memória (memory buffer register — MBR). Este registrador é utilizado para guardar o conteúdo de uma ou mais células de memória, após uma operação de leitura, ou para guardar o dado que será transferido para a memória em uma operação de gravação

A memória principal pode ser classificada em função de sua volatilidade, que é a capacidade de a memória preservar o seu conteúdo mesmo sem uma fonte de alimentação ativa. Memórias do tipo RAM(Random Access Memory) são voláteis, enquanto as memórias ROM (Read-Only Memory) e EPROM(Erasable Programmable ROM) são do tipo não voláteis.


#### Memória Cache

A memória cache é uma memória volátil de alta velocidade, porém com pequena capacidade de armazenamento.

O propósito do uso da memória cache é minimizar a disparidade existente entre a velocidade com que o processador executa instruções e a velocidade com que dados são lidos e gravados na memória principal

==Alto custo==

A memória cache armazena uma pequena parte do conteúdo da memória principal. Toda vez que o processador faz referência a um dado armazenado na memória, é verificado, primeiramente, se o mesmo encontra-se na memória cache. Caso o processador encontre o dado (cache hit), não há necessidade do acesso à memória principal, diminuindo assim o tempo de acesso.

A maioria dos processadores apresenta uma arquitetura de memória cache com múltiplos níveis. O funcionamento desta arquitetura tem como base o princípio de que quanto menor é a capacidade de armazenamento da memória cache, mais rápido é o acesso ao dado; contudo, a probabilidade da ocorrência de cache hits é menor.

A hierarquização da cache em múltiplos níveis é uma solução para aumentar o desempenho no funcionamento das memórias caches. O nível de cache mais alto é chamado de L1 (Level 1), com baixa capacidade de armazenamento e com altíssima velocidade de acesso. O segundo nível, L2 (Level 2), possui maior capacidade de armazenamento, porém com velocidade de acesso inferior a L1. Quando a UCP necessita acessar um dado na memória principal, primeiramente é verificado se o dado encontra-se na cache L1. Caso o dado seja encontrado, obtém-se um excelente desempenho no acesso à informação, porém, caso o dado não seja encontrado, a busca prossegue para a L2.

#### Memória Secundária

A memória secundária é um meio permanente, isto é, não volátil de armazenamento de programas e dados. Enquanto a memória principal precisa estar sempre energizada para manter suas informações, a memória secundária não precisa de alimentação.

O acesso à memória secundária é lento, se comparado com o acesso à memória principal, porém seu custo é baixo e sua capacidade de armazenamento é bem superior.

#### Dispositivos de Entrada e Saída

Os dispositivos de entrada e saída (E/S) são utilizados para permitir a comunicação entre o sistema computacional e o mundo externo, e podem ser divididos em duas categorias: os que são utilizados como memória secundária e os que servem para a interface usuário-máquina.


#### Barramento

O barramento ou bus é um meio de comunicação compartilhado que permite a comunicação entre as unidades funcionais de um sistema computacional. Através de condutores, informações como dados, endereços e sinais de controle trafegam entre processadores, memórias e dispositivos de E/S.

Em geral, um barramento possui linhas de controle e linhas de dados. Através das linhas de controle trafegam informações de sinalização como, por exemplo, o tipo de operação que está sendo realizada.

Os barramentos são classificados em três tipos: barramentos processador-memória, barramentos de E/S e barramentos de backplane. Os barramentos processador-memória são de curta extensão e alta velocidade para que seja otimizada a transferência de informação entre processadores e memórias. Diferentemente, os barramentos de E/S possuem maior extensão, são mais lentos e permitem a conexão de diferentes dispositivos.

#### Pipelining

Pipelining é uma técnica que permite ao processador executar múltiplas instruções paralelamente emestágios diferentes. O conceito de processamento pipeline se assemelha muito a uma linha de montagem, onde uma tarefa é dividida em uma sequência de subtarefas, executadas dentro da linha de produção.

Da mesma forma que em uma linha de montagem, a execução de uma instrução pode ser dividida em subtarefas, como as fases de busca da instrução e dos operandos, execução e armazenamento dos resultados. 

O processador, através de suas várias unidades funcionais pipeline, funciona de forma a permitir que, enquanto uma instrução se encontra na fase de execução, uma outra instrução possa estar na fase de busca simultaneamente.

#### ==Arquiteturas RISC e CISC==

A linguagem de máquina de um computador é a linguagem de programação que é realmente entendida pelo processador. Cada processador possui um conjunto definido de instruções de máquina, definido por seu fabricante. As instruções de máquina fazem referências a detalhes, como registradores, modos de endereçamento e tipos de dados, que caracterizam um processador e suas funcionalidades.

Um programa em linguagem de máquina pode ser diretamente executado pelo processador, não requerendo qualquer tipo de tradução ou relocação. Quando escrito em linguagem de máquina de umdeterminado processador, um programa não pode ser executado em outra máquina de arquitetura diferente, visto que o conjunto de instruções de um processador é característica específica de cada arquitetura.

- RISC
==Um processador com arquitetura RISC (Reduced Instruction Set Computer) caracteriza-se por possuir poucas instruções de máquina, em geral bastante simples, que são executadas diretamente pelo hardware.== 

Na sua maioria, estas instruções não acessam a memória principal, trabalhando principalmente comregistradores que, neste tipo de processador, se apresentam em grande número. 

Estas características, além de permitirem que as instruções sejam executadas rapidamente, facilitam a implementação do pipelining

- CISC
Os processadores com arquitetura CISC (Complex Instruction Set Computers) já possuem instruções complexas que são interpretadas por microprogramas. 

O número de registradores é pequeno, e qualquer instrução pode referenciar a memória principal. 

Neste tipo de arquitetura, a implementação do pipelining é mais difícil



Nos processadores RISC, um programa em linguagem de máquina é executado diretamente pelo hardware, porém isto não ocorre nos processadores CISC.

Os microprogramas definem a linguagem de máquina de um computador CISC. Apesar de cada computador possuir níveis de microprogramação diferentes, existem muitas semelhanças nessa camada se compararmos os diferentes equipamentos. Um computador possui, aproximadamente, 25 microinstruções básicas, que são interpretadas pelos circuitos eletrônicos. Na realidade, o código executável de um processador CISC é interpretado por microprogramas durante sua execução, gerando microinstruções, que, finalmente, são executadas pelo hardware. Para cada instrução em linguagem de máquina existe um microprograma associado.


### Software

Para que o hardware tenha utilidade prática, deve existir um conjunto de programas utilizado como interface entre as necessidades do usuário e as capacidades do hardware. A utilização de softwares adequados às diversas tarefas e aplicações torna o trabalho dos usuários muito mais simples e eficiente.

#### Tradutor

Com o surgimento das primeiras linguagens de montagem ou assembly e das linguagens de alto nível, o programador deixou de se preocupar com muitos aspectos pertinentes ao hardware, como em qual região da memória o programa deveria ser carregado ou quais endereços de memória seriam reservados para as variáveis. A utilização dessas linguagens facilitou a construção de programas, documentação e manutenção.

Apesar das inúmeras vantagens proporcionadas pelas linguagens de montagem e de alto nível, os programas escritos nessas linguagens não estão prontos para ser diretamente executados pelo processador (programas-fonte). Para isso, eles têm de passar por uma etapa de conversão, onde toda representação simbólica das instruções é traduzida para código de máquina. ==Esta conversão é realizada por um utilitário denominado tradutor.==

==O módulo gerado pelo tradutor é denominado módulo-objeto==, que, apesar de estar em código de máquina, na maioria das vezes não pode ser ainda executado. Isso ocorre em função de um programa poder chamar sub-rotinas externas, e, neste caso, o tradutor não tem como associar o programa principal às sub-rotinas chamadas. Esta função é realizada por outro utilitário denominado linker, e será apresentado adiante.

Dependendo do tipo do programa-fonte, existem dois tipos distintos de tradutores que geram módulosobjeto: montador e compilador.

![[Pasted image 20260927121503.png]]

O montador (assembler) é o utilitário responsável por traduzir um programa-fonte em linguagem de montagem em um programa-objeto não executável (módulo-objeto). A linguagem de montagem é particular para cada processador, assim como a linguagem de máquina, o que não permite que programas assembly possam ser portados entre máquinas diferentes.

O compilador é o utilitário responsável por gerar, a partir de um programa escrito em uma linguagem de alto nível, um programa em linguagem de máquina não executável.

Um compilador é um utilitário que opera de modo integrado aos componentes do sistema de programação disponíveis, sob a supervisão do sistema operacional.

#### Interpretador

O interpretador é considerado um tradutor que não gera módulo-objeto. A partir de um programa-fonte escrito em linguagem de alto nível, o interpretador, durante a execução do programa, traduz cada instrução e a executa imediatamente.

A maior desvantagem na utilização de interpretadores é o tempo gasto na tradução das instruções de umprograma toda vez que este for executado, já que não existe a geração de um código executável. A vantagem é permitir a implementação de tipos de dados dinâmicos, ou seja, que podem mudar de tipo durante a execução do programa, aumentando, assim, sua flexibilidade.

#### Linker

O linker ou editor de ligação é o utilitário responsável por gerar, a partir de um ou mais módulos-objeto, um único programa executável.

Suas funções básicas são resolver todas as referências simbólicas existentes entre os módulos e reservar memória para a execução do programa.

![[Pasted image 20260927121818.png]]

Outra função importante do linker é a relocação, que determina a região de memória na qual o programa será carregado para execução.

#### Loader

O loader ou carregador é o utilitário responsável por carregar na memória principal um programa para ser executado. . O procedimento de carga varia com o código gerado pelo linker e, em função deste, o loader é classificado como do tipo absoluto ou relocável.

Se o código executável for do tipo absoluto, o loader só necessita conhecer o endereço de memória inicial e o tamanho do módulo para realizar o carregamento. Então, o loader transfere o programa da memória secundária para a memória principal e inicia sua execução (loader absoluto).

No caso do código relocável, o programa pode ser carregado em qualquer posição de memória, e o loader é responsável pela relocação no momento do carregamento (loader relocável).

#### Depurador

O depurador (debugger) é o utilitário que permite ao usuário acompanhar toda a execução de um programa a fim de detectar erros na sua lógica.

Este utilitário oferece ao usuário recursos como: 
- acompanhar a execução de um programa instrução por instrução; 
- possibilitar a alteração e a visualização do conteúdo de variáveis; 
- implementar pontos de parada dentro do programa (breakpoint), de forma que, durante a execução, o programa pare nesses pontos;
- especificar que, toda vez que o conteúdo de uma variável for modificado, o programa envie uma mensagem (watchpoint).

## Cap 3 - Concorrência 

Sistemas operacionais podem ser vistos como um conjunto de rotinas executadas de forma concorrente e ordenada. A possibilidade de o processador executar instruções ao mesmo tempo que outras operações, como, por exemplo, operações de E/S, permite que diversas tarefas sejam executadas concorrentemente pelo sistema. O conceito de concorrência é o princípio básico para o projeto e a implementação dos sistemas multiprogramáveis.


### Sistemas Monoprogramáveis × Multiprogramáveis

Os sistemas multiprogramáveis surgiram a partir de limitações existentes nos sistemas operacionais monoprogramáveis. 

Neste tipo de sistema, os recursos computacionais, como processador, memória e dispositivos de E/S, eram utilizados de maneira pouco eficiente, limitando o desempenho destas arquiteturas. Muitos destes recursos de alto custo permaneciam muitas vezes ociosos por longos períodos de tempo.

Nos sistemas monoprogramáveis somente um programa pode estar em execução por vez, permanecendo o processador dedicado, exclusivamente, a essa tarefa. 

Podemos observar que, nesse tipo de sistema, ocorre um desperdício na utilização do processador, pois enquanto uma leitura em disco é realizada, o processador permanece ocioso. 

O tempo de espera é relativamente longo, já que as operações com dispositivos de entrada e saída são muito lentas, se comparadas com a velocidade do processador em executar instruções.

Outro aspecto a ser considerado é a subutilização da memória principal. Um programa que não ocupe totalmente a memória ocasiona a existência de áreas livres sem utilização. Nos sistemas multiprogramáveis, vários programas podem estar residentes em memória, concorrendo pela utilização do processador.

Dessa forma, quando um programa solicita uma operação de E/S outros programas poderão utilizar o processador. Nesse caso, a UCP permanece menos tempo ociosa (Fig. 3.1b) e a memória principal é utilizada de forma mais eficiente, pois existem vários programas residentes se revezando na utilização do processador

A utilização concorrente da UCP deve ser implementada de maneira que, quando um programa perde o uso do processador e depois retorna para continuar o processamento, seu estado deve ser idêntico ao do momento em que foi interrompido. O programa deverá continuar sua execução exatamente na instrução seguinte àquela em que havia parado, aparentando ao usuário que nada aconteceu. Em sistemas de tempo compartilhado existe a impressão de que o computador está inteiramente dedicado ao usuário, ficando esse mecanismo totalmente transparente.

### Interrupções e Exceções

Durante a execução de um programa podem ocorrer alguns eventos inesperados, ocasionando um desvio forçado no seu fluxo de execução.

. Estes tipos de eventos são conhecidos por interrupção ou exceção e podem ser consequência da sinalização de algum dispositivo de hardware externo ao processador ou da execução de instruções do próprio programa.

==. A diferença entre interrupção e exceção é dada pelo tipo de evento ocorrido==

A interrupção é o mecanismo que tornou possível a implementação da concorrência nos computadores, sendo o fundamento básico dos sistemas multiprogramáveis. É em função desse mecanismo que o sistema operacional sincroniza a execução de todas as suas rotinas e dos programas dos usuários, além de controlar dispositivos.

==Uma interrupção é sempre gerada por algum evento externo ao programa e, nesse caso, independe da instrução que está sendo executada==

Um exemplo de interrupção ocorre quando um dispositivo avisa ao processador que alguma operação de E/S está completa. Nesse caso, o processador deve interromper o programa para tratar o término da operação.

![[Pasted image 20260927124106.png]]

Existem dois métodos para o tratamento de interrupções:  
- O primeiro método utiliza uma estrutura de dados chamada vetor de interrupção, que contém o endereço inicial de todas as rotinas de tratamento existentes associadas a cada tipo de evento. 

- Um segundo método utiliza um registrador de status que armazena o tipo do evento ocorrido. Neste método só existe uma única rotina de tratamento que, no seu início, testa o registrador para identificar o tipo de interrupção e tratá-la de maneira adequada.

==interrupções mascaráveis - São interrupções que são ignoradas e não recebem tratamento.==

Alguns processadores não permitem que interrupções sejam desabilitadas, fazendo com que exista umtratamento para a ocorrência de múltiplas interrupções. Nesse caso, o processador necessita saber qual a ordem de atendimento que deverá seguir. Para isso, as interrupções deverão possuir prioridades, emfunção da importância no atendimento de cada uma. Normalmente, existe um dispositivo denominado controlador de pedidos de interrupção, responsável por avaliar as interrupções geradas e suas prioridades de atendimento.

==Uma exceção é semelhante a uma interrupção, sendo a principal diferença o motivo pelo qual o evento é gerado. A exceção é resultado direto da execução de uma instrução do próprio programa, como a divisão de um número por zero ou a ocorrência de overflow em uma operação aritmética==


==A diferença fundamental entre exceção e interrupção é que a primeira é gerada por um evento síncrono, enquanto a segunda é gerada por eventos assíncronos. Um evento é síncrono quando é resultado direto da execução do programa corrente==

Da mesma forma que na interrupção, sempre que uma exceção é gerada o programa em execução é interrompido e o controle é desviado para uma rotina de tratamento de exceção.

#### Operações de Entrada/Saída

Nos primeiros computadores, o **processador controlava diretamente os periféricos**, usando instruções específicas para cada dispositivo. Isso criava uma forte dependência entre a CPU e os dispositivos de E/S.

Com o surgimento do **controlador de E/S**, o processador passou a se comunicar com os periféricos por meio desse controlador, que ficava responsável pelos detalhes da operação.

A evolução ocorreu em três etapas principais:

- **E/S controlada por programa:** o processador iniciava a operação e ficava verificando continuamente se ela havia terminado (**busy wait**), desperdiçando tempo de processamento.
- **Polling:** o processador podia executar outras tarefas, mas precisava verificar periodicamente o estado dos dispositivos. Isso permitiu o surgimento dos primeiros sistemas **multiprogramáveis**, porém muitos dispositivos causavam muitas interrupções para verificação.
- **E/S controlada por interrupção:** o controlador avisa o processador quando a operação termina por meio de uma **interrupção**. Assim, a CPU pode executar outras tarefas enquanto a E/S acontece, tornando o sistema mais eficiente.

**Em resumo:** a evolução passou de um modelo em que a CPU controlava e esperava pela E/S para um modelo em que o **controlador executa a operação e avisa a CPU quando necessário**, permitindo maior aproveitamento do processador.

- DMA
A técnica de DMA permite que um bloco de dados seja transferido entre a memória principal e dispositivos de E/S sem a intervenção do processador, exceto no início e no final da transferência

Quando o sistema deseja ler ou gravar um bloco de dados, o processador informa ao controlador sua localização, o dispositivo de E/S, a posição inicial da memória de onde os dados serão lidos ou gravados e o tamanho do bloco. Com estas informações, o controlador realiza a transferência entre o periférico e a memória principal, e o processador é somente interrompido no final da operação.

==A área de memória utilizada pelo controlador na técnica de DMA é chamada de buffer de entrada e saída.==

O canal de E/S realiza a transferência e, ao final, gera uma interrupção, avisando do término da operação. Um canal de E/S pode controlar múltiplos dispositivos através de diversos controladores.

Cada dispositivo, ou conjunto de dispositivos, é manipulado por umúnico controlador.

#### Buffering

A técnica de buffering consiste na utilização de uma área na memória principal, denominada buffer, para a transferência de dados entre os dispositivos de E/S e a memória.

Esta técnica permite que em uma operação de leitura o dado seja transferido primeiramente para o buffer, liberando imediatamente o dispositivo de entrada para realizar uma nova leitura. Nesse caso, enquanto o processador manipula o dado localizado no buffer, o dispositivo realiza outra operação de leitura no mesmo instante. Este mesmo mecanismo pode ser aplicado nas operações de gravação.

O buffering permite minimizar o problema da disparidade da velocidade de processamento existente entre o processador e os dispositivos de E/S. O objetivo principal desta técnica é manter, na maior parte do tempo, processador e dispositivos de E/S ocupados.

#### Spooling

aumentar o grau de concorrência e a eficiência dos sistemas operacionais

A técnica de spooling, semelhante à técnica de buffering já apresentada, utiliza uma área em disco como se fosse um grande buffer. Neste caso, dados podem ser lidos ou gravados em disco, enquanto programas são executados concorrentemente.

#### Reentrância

Reentrância é a capacidade de um código executável (código reentrante) ser compartilhado por diversos usuários, exigindo que apenas uma cópia do programa esteja na memória. A reentrância permite que cada usuário possa estar em um ponto diferente do código reentrante, manipulando dados próprios, exclusivos de cada usuário.

## Cap 4 - Estrutura do SO

O sistema operacional é formado por um conjunto de rotinas que oferece serviços aos usuários e às suas aplicações. Esse conjunto de rotinas é denominado núcleo do sistema, ou kernel.

Há três maneiras distintas de os usuários se comunicarem com o kernel do sistema operacional. Uma delas é por intermédio das chamadas rotinas do sistema realizadas por aplicações. Além disso, os usuários podem interagir com o núcleo mais amigavelmente por meio de utilitários ou linguagem de comandos. Cada sistema operacional oferece seus próprios utilitários, como compiladores e editores de texto. A linguagem de comandos também é particular de cada sistema, com estruturas e sintaxe próprias.

O capítulo pode ser resumido nesta sequência:

**Kernel → proteção → System Calls → comandos → boot/shutdown → arquiteturas do núcleo**

E as quatro arquiteturas principais são:

**Monolítica → Camadas → Máquina Virtual → Microkernel**

A ideia central do capítulo é entender **como o sistema operacional é estruturado internamente e como ele controla o acesso das aplicações aos recursos do computador**.

### Funções do Núcleo

O **kernel** é o conjunto de rotinas responsável por fornecer os principais serviços do sistema operacional. Ele trabalha de forma concorrente e reage a eventos, como interrupções e solicitações das aplicações.

Entre suas principais funções estão:

- Tratamento de interrupções e exceções;
- Criação e eliminação de processos e threads;
- Sincronização e comunicação entre processos;
- Escalonamento de processos e threads;
- Gerenciamento de memória;
- Gerenciamento do sistema de arquivos;
- Gerenciamento dos dispositivos de entrada e saída;
- Suporte a redes;
- Contabilização do uso dos recursos;
- Auditoria e segurança.

### Modo de Acesso

O sistema operacional precisa proteger seus recursos contra acessos indevidos. Por isso, existem diferentes **modos de acesso**, principalmente:

- **Modo usuário:** possui acesso limitado aos recursos do sistema. uma aplicação só pode executar instruções conhecidas como não privilegiadas, tendo acesso a um número reduzido de instruções.
- **Modo kernel:** possui privilégios para executar operações que podem alterar diretamente o funcionamento do computador. A aplicação pode ter acesso ao conjunto total de instruções do processador.

Essa separação aumenta a **proteção e segurança** do sistema, impedindo que uma aplicação comum execute diretamente operações críticas.


### Rotinas do Sistema Operacional e System Calls

As rotinas do sistema operacional compõem o núcleo do sistema, oferecendo serviços aos usuários e suas aplicações. Todas as funções do núcleo são implementadas por rotinas do sistema que necessariamente possuem em seu código instruções privilegiadas. A partir desta condição, para que estas rotinas possam ser executadas o processador deve estar obrigatoriamente em modo kernel, o que exige a implementação de mecanismos de proteção para garantir a confiabilidade do sistema.

As aplicações não acessam diretamente todos os recursos do hardware. Para solicitar serviços ao sistema operacional, utilizam as **System Calls**.

Por exemplo, quando um programa precisa:

- criar ou eliminar um arquivo;
- ler ou gravar dados;
- criar um processo;
- utilizar determinado dispositivo;

ele pode solicitar esse serviço ao sistema operacional por meio de uma chamada de sistema.

Assim, a **System Call funciona como uma interface entre a aplicação e o kernel**.

Todo o controle de execução de rotinas do sistema operacional é realizado pelo mecanismo conhecido como system call. Toda vez que uma aplicação desejar chamar uma rotina do sistema operacional, o mecanismo de system call é ativado. Inicialmente, o sistema operacional verificará se a aplicação possui privilégios necessários para executar a rotina desejada. Em caso negativo, o sistema operacional impedirá o desvio para a rotina do sistema, sinalizando ao programa chamador que a operação não é possível

Os mecanismos de system call e de proteção por hardware garantem a segurança e a integridade do sistema. Com isso, as aplicações estão impedidas de excutarem instruções privilegiadas sem a autorização e a supervisão do sistema operacional.

### Chamada a Rotinas do Sistema Operacional

As rotinas do sistema e o mecanismo de system call podem ser entendidos como uma porta de entrada para o núcleo do sistema operacional e a seus serviços. Sempre que uma aplicação desejar algum serviço do sistema, deve ser realizada uma chamada a uma de suas rotinas através de uma system call

O mecanismo de ativação e comunicação entre o programa e o sistema operacional é semelhante ao mecanismo implementado quando um programa chama uma sub-rotina.

Na realidade existem duas maneiras distintas de chamada a uma rotina do sistema operacional: explícita e implícita. A chamada explícita é a descrita anteriormente, em que no código do programa há uma função explicitando a chamada a rotina do sistema com passagem de parâmetro. Já a chamada implícita é realizada por intermédio de um comando da própria linguagem de programação. Quando este comando é traduzido para uma instrução de mais baixo nível, há uma conversão do comando em uma chamada da função.

### Linguagem de Comandos

A **linguagem de comandos** permite que o usuário execute tarefas do sistema por meio de comandos.

Exemplos apresentados no livro para o Windows incluem:

- `dir` → lista o conteúdo de um diretório;
- `cd` → altera o diretório;
- `del` → elimina arquivos;
- `mkdir` → cria um diretório;
- `ver` → mostra a versão do sistema.

O **shell** ou interpretador de comandos recebe o comando, verifica sua sintaxe, solicita os serviços necessários ao sistema operacional e apresenta o resultado ao usuário.

Os comandos também podem ser armazenados em arquivos para automatizar tarefas, como acontece com **shell scripts** e arquivos batch.

### Ativação/Desativação do Sistema

Quando o computador é ligado, o sistema operacional ainda precisa ser carregado na memória. Esse processo é chamado de **boot**.

O procedimento de ativação se inicia com a execução de um programa chamado boot loader, que se localiza em um endereço fixo de uma memória ROM da máquina. Este programa chama a execução de outro programa conhecido como POST (Power-On Self Test), que identifica possíveis problemas de hardware no equipamento. Após esta fase, o procedimento de ativação verifica se há no sistema computacional algum dispositivo de armazenamento onde haja um sistema operacional residente. Caso nenhum dispositivo seja encontrado, uma mensagem de erro é apresentada e o procedimento de ativação é interrompido. Se um dispositivo com o sistema operacional é encontrado, um conjunto de instruções é carregado para memória e localizado em um bloco específico do dispositivo conhecido como setor de boot (boot sector). A partir da execução deste código, o sistema operacional é finalmente carregado para a memória principal. Além da carga, a ativação do sistema também consiste na execução de arquivos de inicialização onde são especificados procedimentos de customização e configuração de hardware e software específicos para cada ambiente.


De forma simplificada:

**Ligação → boot loader → verificação do hardware → localização do sistema operacional → carregamento na memória → inicialização do sistema**

O **shutdown** é o processo contrário: ele encerra ordenadamente as aplicações e os componentes do sistema operacional, ajudando a preservar sua integridade.

### Arquiteturas do Núcleo

A estrutura do núcleo do sistema operacional, ou seja, a maneira como o código do sistema é organizado e o inter-relacionamento de seus diversos componentes, pode variar conforme a concepção do projeto. A seguir serão abordadas as principais arquiteturas dos sistemas operacionais: arquitetura monolítica, arquitetura de camadas, máquina virtual e arquitetura microkernel.

| Arquitetura         | Característica principal                                                                 |
| ------------------- | ---------------------------------------------------------------------------------------- |
| **Monolítica**      | Todos os componentes formam um grande núcleo, com comunicação direta entre eles          |
| **Camadas**         | O sistema é dividido em níveis, onde cada camada utiliza serviços das camadas inferiores |
| **Máquina Virtual** | Cria ambientes virtuais independentes sobre o hardware                                   |
| **Microkernel**     | Mantém no núcleo apenas os serviços essenciais, deixando outros serviços fora dele       |

#### Arquitetura Monolítica

A arquitetura monolítica pode ser comparada com uma aplicação formada por vários módulos que são compilados separadamente e depois linkados, formando um grande e único programa executável, onde os módulos podem interagir livremente.

Desenvolvimento e manutenção difíceis.

Simples e bom desempenho.
#### Arquitetura de Camada

Na arquitetura de camadas, o sistema é dividido em níveis sobrepostos. Cada camada oferece um conjunto de funções que podem ser utilizadas apenas pelas camadas superiores.

Neste tipo de implementação, as camadas mais internas são mais privilegiadas que as mais externas.

A vantagem da estruturação em camadas é isolar as funções do sistema operacional, facilitando sua manutenção e depuração, além de criar uma hierarquia de níveis de modos de acesso, protegendo as camadas mais internas. Uma desvantagem para o modelo de camadas é o desempenho. Cada nova camada implica uma mudança no modo de acesso.

#### Máquina Virtual

Um sistema computacional é formado por níveis, onde a camada de nível mais baixo é o hardware. Acima desta camada encontramos o sistema operacional que oferece suporte para as aplicações. O modelo de máquina virtual, ou virtual machine (VM), cria um nível intermediário entre o hardware e o sistema operacional, denominado gerência de máquinas virtuais. Este nível cria diversas máquinas virtuais independentes, onde cada uma oferece uma cópia virtual do hardware, incluindo os modos de acesso, interrupções, dispositivos de E/S etc.

Como cada máquina virtual é independente das demais, é possível que cada VM tenha seu próprio sistema operacional e que seus usuários executem suas aplicações como se todo o computador estivesse dedicado a cada um deles.

Este modelo cria o isolamento total entre cada VM, oferecendo grande segurança para cada máquina virtual. Se, por exemplo, uma VM executar uma aplicação que comprometa o funcionamento do seu sistema operacional, as demais máquinas virtuais não sofrerão qualquer problema. 

Apesar do isolamento das aplicações, as máquinas virtuais não estão livres de problemas, como, por exemplo, vírus e erros de software do sistema operacional ou aplicações da VM. 

Além dessas vantagens, existem diversas aplicações para a utilização de máquinas virtuais:
- Portabilidade de código
- Consolidação de servidores
- Aumento da disponibilidade
- Facilidade de escalabilidade e balanceamento de carga
- Facilidade no desenvolvimento de software

#### Arquitetura Microkernel


Uma tendência nos sistemas operacionais modernos é tornar o núcleo do sistema operacional o menor e mais simples possível. Para implementar esta ideia, os serviços do sistema são disponibilizados através de processos, onde cada um é responsável por oferecer um conjunto específico de funções, como gerência de arquivos, gerência de processos, gerência de memória e escalonamento.

Sempre que uma aplicação deseja algum serviço, é realizada uma solicitação ao processo responsável

Neste caso, a aplicação que solicita o serviço é chamada de cliente, enquanto o processo que responde à solicitação é chamado de servidor

Um cliente, que pode ser uma aplicação de um usuário ou um outro componente do sistema operacional, solicita um serviço enviando uma mensagem para o servidor. O servidor responde ao cliente através de uma outra mensagem. A principal função do núcleo é realizar a comunicação, ou seja, a troca de mensagens entre cliente e servidor.

Além disso, a arquitetura microkernel permite isolar as funções do sistema operacional por diversos processos servidores pequenos e dedicados a serviços específicos, tornando o núcleo menor, mais fácil de depurar e, consequentemente, aumentando sua confiabilidade. Na arquitetura microkernel, o sistema operacional passa a ser de mais fácil manutenção, flexível e de maior portabilidade.

Apesar de todas as vantagens deste modelo, sua implementação, na prática, é muito difícil. Primeiro existe o problema de desempenho, devido à necessidade de mudança de modo de acesso a cada comunicação entre clientes e servidores. Outro problema é que certas funções do sistema operacional exigem acesso direto ao hardware, como operações de E/S. Na realidade, o que é implementado mais usualmente é uma combinação do modelo de camadas com a arquitetura microkernel. O núcleo do sistema, além de ser responsável pela comunicação entre cliente e servidor, passa a incorporar outras funções críticas do sistema, como escalonamento, tratamento de interrupções e gerência de dispositivos.

## Cap 5 - Processo 

**processo é a principal estrutura utilizada pelo sistema operacional para controlar a execução concorrente de programas**, mantendo informações sobre seu estado, recursos, memória e execução.

|Conceito|Ideia principal|
|---|---|
|**Processo**|Programa em execução + informações necessárias para seu controle|
|**Contexto de hardware**|Estado dos registradores da CPU|
|**Contexto de software**|PID, prioridades, quotas e privilégios|
|**Espaço de endereçamento**|Memória usada pelo processo|
|**PCB**|Estrutura usada pelo SO para controlar o processo|
|**Execução**|Processo está usando a CPU|
|**Pronto**|Aguarda a CPU|
|**Espera**|Aguarda um evento/E/S|
|**Criação**|Processo está sendo criado|
|**Terminado**|Processo encerrou sua execução|
|**CPU-bound**|Forte utilização da CPU|
|**I/O-bound**|Forte utilização de E/S|
|**Foreground**|Interage diretamente com o usuário|
|**Background**|Executa sem interação direta|
|**Subprocesso**|Processo-filho ligado a um processo-pai|
|**Thread**|Unidade de execução dentro de um processo|
|**Sinal**|Notificação de um evento para um processo|

==Um **processo** pode ser entendido como um programa em execução==, mas o conceito é mais amplo. Ele reúne todas as informações necessárias para que o sistema operacional consiga executar e controlar um programa, incluindo os recursos que ele pode utilizar.

O processo é fundamental em sistemas **multiprogramáveis**, pois permite que vários programas compartilhem o processador. Quando um processo deixa de utilizar a CPU, suas informações são armazenadas para que posteriormente ele possa continuar exatamente de onde parou. Essa troca entre processos é chamada de **mudança de contexto**.
### Estrutura do Processo

O conceito de processo pode ser definido como sendo o conjunto necessário de informações para que o sistema operacional implemente a concorrência de programas.

Um processo também pode ser definido como o ambiente onde um programa é executado. Este ambiente, além das informações sobre a execução, possui também a quantidade de recursos do sistema que cada programa pode utilizar, como o espaço de endereçamento da memória principal, tempo de processador e área em disco.

Um processo é formado por três partes principais:

- **Contexto de hardware:** contém os valores dos registradores da CPU, como **PC (Program Counter)**, **SP (Stack Pointer)** e registrador de status. Essas informações são salvas quando o processo deixa de utilizar a CPU.
- **Contexto de software:** contém características e limites do processo, como identificação, prioridade, quotas de recursos e privilégios. O processo possui um **PID**, que permite identificá-lo no sistema.
- **Espaço de endereçamento:** região da memória onde ficam as instruções e os dados utilizados pelo processo. Cada processo possui seu próprio espaço, que deve ser protegido contra acesso indevido de outros processos.

#### Contexto de Hardware

O contexto de hardware de um processo armazena o conteúdo dos registradores gerais da UCP, além dos registradores de uso específico, como program counter (PC), stack pointer (SP) e registrador de status.

Quando um processo está em execução, o seu contexto de hardware está armazenado nos registradores do processador. No momento em que o processo perde a utilização da UCP, o sistema salva as informações no contexto de hardware do processo.

#### Contexto de software

No contexto de software de um processo são especificados limites e características dos recursos que podem ser alocados pelo processo, como o número máximo de arquivos abertos simultaneamente, prioridade de execução e tamanho do buffer para operações de E/S. Muitas destas características são determinadas no momento da criação do processo, enquanto outras podem ser alteradas durante sua existência.

A maior parte das informações do contexto de software do processo provém de um arquivo do sistema operacional, conhecido como arquivo de usuários. Neste arquivo são especificados os limites dos  recursos que cada processo pode alocar, sendo gerenciado pelo administrador do sistema. Outras informações presentes no contexto de software são geradas dinamicamente ao longo da execução do processo.

O contexto de software é composto por três grupos de informações sobre o processo: identificação, quotas e privilégios.

##### Identificação

Cada processo criado pelo sistema recebe uma identificação única (PID — process identification) representada por um número. Através do PID, o sistema operacional e outros processos podem fazer referência a qualquer processo existente, consultando seu contexto ou alterando uma de suas características. Alguns sistemas, além do PID, identificam o processo através de um nome. O processo também possui a identificação do usuário ou processo que o criou (owner). Cada usuário possui uma identificação única no sistema (UID — user identification), atribuída ao processo no momento de sua criação. A UID permite implementar um modelo de segurança, onde apenas os objetos (processos, arquivos, áreas de memória etc.) que possuem a mesma UID do usuário (processo) podemser acessados.

##### Quotas

As quotas são os limites de cada recurso do sistema que um processo pode alocar. Caso uma quota seja insuficiente, o processo poderá ser executado lentamente, interrompido durante seu processamento ou mesmo não ser executado. Alguns exemplos de quotas presentes na maioria dos sistemas operacionais são: 
- número máximo de arquivos abertos simultaneamente;
- tamanho máximo de memória principal e secundária que o processo pode alocar; 
- número máximo de operações de E/S pendentes; 
- tamanho máximo do buffer para operações de E/S;
- número máximo de processos, subprocessos e threads que podem ser criados.

##### Privilégios

Os privilégios ou direitos definem as ações que um processo pode fazer em relação a ele mesmo, aos demais processos e ao sistema operacional

Privilégios que afetam o próprio processo permitem que suas características possam ser alteradas, como prioridade de execução, limites alocados na memória principal e secundária etc. Já os privilégios que afetam os demais processos permitem, além da alteração de suas próprias características, alterar as de outros processos.


Privilégios que afetam o sistema são os mais amplos e poderosos, pois estão relacionados à operação e à gerência do ambiente, como a desativação do sistema, alteração de regras de segurança, criação de outros processos privilegiados, modificação de parâmetros de configuração do sistema, entre outros. 

A maioria dos sistemas operacionais disponibiliza uma conta de acesso com todos estes privilégios disponíveis, com o propósito de o administrador gerenciar o sistema operacional. No sistema Unix existe a conta “root”, no MS Windows a conta “administrator” e no OpenVMS existe a conta “system” com este mesmo perfil.

#### Espaço de endereçamento

O espaço de endereçamento é a área de memória pertencente ao processo onde instruções e dados do programa são armazenados para execução. Cada processo possui seu próprio espaço de endereçamento, que deve ser devidamente protegido do acesso dos demais processos.

#### Bloco de Controle do Processo

O processo é implementado pelo sistema operacional através de uma estrutura de dados chamada bloco de controle do processo (Process Control Block — PCB). A partir do PCB, o sistema operacional mantém todas as informações sobre o contexto de hardware, contexto de software e espaço de endereçamento de cada processo.

O sistema operacional utiliza uma estrutura chamada **PCB (Process Control Block)** para representar e controlar cada processo.

O PCB armazena informações relacionadas ao:
- contexto de hardware;
- contexto de software;
- espaço de endereçamento.

Os PCBs dos processos ativos ficam em uma área da memória principal reservada ao sistema operacional. Por meio deles, o sistema consegue criar, alterar, consultar, suspender, sincronizar e eliminar processos.

### Estados do Processo

Durante sua execução, um processo pode passar por diferentes estados:

- **Execução (running):** o processo está utilizando a CPU.
- **Pronto (ready):** o processo está preparado para executar, mas aguarda a CPU.
- **Espera (wait):** o processo aguarda algum evento, normalmente relacionado a uma operação de E/S.
- **Criação (new):** o processo está sendo criado pelo sistema.
- **Terminado (exit):** a execução terminou, embora algumas informações do processo ainda possam permanecer no sistema para contabilização e finalização.

As mudanças de estado acontecem em consequência de eventos como solicitação de E/S, término de uma operação, escalonamento ou encerramento do processo.

### Mudanças de Estado do Processo

Um processo muda de estado durante seu processamento em função de eventos originados por ele próprio (eventos voluntários) ou pelo sistema operacional (eventos involuntários). Basicamente, existem quatro mudanças de estado que podem ocorrer a um processo:

Pronto → Execução
Após a criação de um processo, o sistema o coloca em uma lista de processos no estado de pronto, onde aguarda por uma oportunidade para ser executado (Fig. 5.8a). Cada sistema operacional temseus próprios critérios e algoritmos para a escolha da ordem em que os processos serão executados (política de escalonamento). No Capítulo 8 — Gerência do Processador, esses critérios e seus algoritmos serão analisados com detalhes. 

Execução → Espera 
Um processo em execução passa para o estado de espera por eventos gerados pelo próprio processo, como uma operação de E/S, ou por eventos externos (Fig. 5.8b). Um evento externo é gerado, por exemplo, quando o sistema operacional suspende por um período de tempo a execução de umprocesso.

Espera → Pronto
Um processo no estado de espera passa para o estado de pronto quando a operação solicitada é atendida ou o recurso esperado é concedido. Um processo no estado de espera sempre terá de passar pelo estado de pronto antes de poder ser novamente selecionado para execução. Não existe a mudança do estado de espera para o estado de execução diretamente (Fig. 5.8c).

Execução → Pronto
Um processo em execução passa para o estado de pronto por eventos gerados pelo sistema, como o término da fatia de tempo que o processo possui para sua exe-cução (Fig. 5.8d). Nesse caso, o processo volta para a fila de pronto, onde aguarda por uma nova oportunidade para continuar seu processamento.

==Um processo em estado de pronto ou de espera pode não se encontrar na memória principal. Esta condição ocorre quando não existe espaço suficiente para todos os processos na memória principal e parte do contexto do processo é levado para memória secundária. A técnica conhecida como swapping, na condição citada, retira processos da memória principal (swap out) e os traz de volta (swap in) seguindo critérios de cada sistema operacional. Neste caso, os processos em estados de espera e pronto podem estar residentes ou não residentes (outswapped) na memória principal (Fig. 5.9).==

### Criação e Eliminação de Processos

A criação de um processo ocorre a partir do momento em que o sistema operacional adiciona um novo PCB à sua estrutura e aloca um espaço de endereçamento na memória para uso. A partir da criação do PCB, o sistema operacional já reconhece a existência do processo, podendo gerenciá-lo e associar programas ao seu contexto para seremexecutados. No caso da eliminação de um processo, todos os recursos associados ao processo são desalocados e o PCB eliminado pelo sistema operacional.

- Criação (new)
Um processo é dito no estado de criação quando o sistema operacional já criou um novo PCB, porém ainda não pode colocá-lo na lista de processos do estado de pronto. Alguns sistemas operacionais limitam o número de processos ativos em função dos recursos disponíveis ou de desempenho. Esta limitação pode ocasionar que processos criados permaneçam no estado de criação até que possam passar para ativos. No item 5.8 são descritas diferentes maneiras de criação de processos.

- Terminado (exit)
Um processo no estado de terminado não poderá ter mais nenhum programa executado no seu contexto, porém o sistema operacional ainda mantém suas informações de controle presentes emmemória. 

Um processo neste estado não é considerado mais ativo, mas como o PCB ainda existe, o sistema operacional pode recuperar informações sobre a contabilização de uso de recursos do processo, como o tempo total do processador. Após as informações serem extraídas, o processo pode deixar de existir. 

O término de processo pode ocorrer por motivos como: 
- término normal de execução; 
- eliminação por um outro processo;
- eliminação forçada por ausência de recursos disponíveis no sistema.

Um processo pode ser criado de diferentes maneiras. Uma delas ocorre por meio de **rotinas do sistema operacional**, que recebem informações como o programa a ser executado, prioridade e características do novo processo.

O capítulo apresenta exemplos como:

- `fork` no Unix;
- `CreateProcess` no Windows;
- `sys$createprocess` no OpenVMS.

Um processo pode ser eliminado quando termina normalmente, quando outro processo solicita sua eliminação ou quando ocorre falta de recursos.

### Processos CPU-bound e I/O-bound

Os processos podem ser classificados de acordo com a forma como utilizam a CPU e os dispositivos de entrada e saída:

**CPU-bound:** passa a maior parte do tempo executando ou aguardando para executar, realizando muitas operações de processamento e poucas operações de E/S. É comum em aplicações que realizam muitos cálculos.

**I/O-bound:** passa grande parte do tempo esperando operações de entrada e saída. É comum em aplicações que realizam muitas leituras e gravações, além de aplicações interativas

### Processos Foreground e Background

Os processos também podem ser classificados de acordo com a forma como interagem com o usuário:

- **Foreground:** possui interação direta com o usuário, normalmente utilizando entrada e saída associadas a um terminal.
- **Background:** executa sem interação direta com o usuário, podendo continuar trabalhando enquanto o usuário realiza outras atividades.

### Formas de Criação de Processos

Um processo pode ser criado de diversas maneiras.

#### Logon Interativo

No logon interativo o usuário, por intermédio de um terminal, fornece ao sistema um nome de identificação (username ou logon) e uma senha (password). O sistema operacional autentica estas informações verificando se estão corretamente cadastradas no arquivo de usuários. Em caso positivo, um processo foreground é criado, possibilitando ao usuário interagir com o sistema utilizando uma linguagem de comandos

#### Via Linguagem de Comandos

Um usuário pode, a partir do seu processo, criar novos processos por intermédio de comandos da linguagem de comandos. O principal objetivo para que um usuário crie diversos processos é a possibilidade de execução de programas concorrentemente. Por exemplo, no sistema OpenVMS o comando spawn permite executar uma outra tarefa de forma concorrente. Esta é uma maneira de criar um processo a partir de outro processo já existente. O processo criado pode ser foreground ou background, dependendo do comando de criação utilizado.

#### Via Rotina do Sistema Operacional

Um processo pode ser criado a partir de qualquer programa executável com o uso de rotinas do sistema operacional. A criação deste processo possibilita a execução de outros programas concorrentemente ao programa chamador. A rotina de criação de processos depende do sistema operacional e possui diversos parâmetros, como nome do processo a ser criado, nome do programa executável que será executado dentro do contexto do processo, prioridade de execução, estado do processo, se o processo é do tipo foreground ou background etc.

### Processos Independentes, Subprocessos e Threads

O capítulo apresenta três formas de implementar concorrência:

**Processos independentes:** não possuem vínculo com o processo que os criou e possuem seus próprios recursos e espaço de endereçamento.

**Subprocessos:** possuem uma relação hierárquica entre processo-pai e processo-filho. O subprocesso possui seu próprio PCB e espaço de endereçamento, mas existe uma relação de dependência com o processo-pai.

**Threads:** permitem dividir um processo em várias unidades de execução. Os threads de um mesmo processo compartilham o contexto de software e o espaço de endereçamento, mas cada thread possui seu próprio contexto de hardware. Isso reduz o custo de criação e troca de contexto em comparação com vários processos.

### Processos do sistema operacional

O conceito de processo também pode ser utilizado para implementar serviços internos do sistema operacional. Isso é especialmente importante em arquiteturas **microkernel**, nas quais diversos serviços podem ser executados como processos.

Entre os exemplos citados estão:

- serviços de rede;
- segurança;
- gerenciamento de impressão;
- contabilização de recursos;
- gerenciamento de jobs;
- temporização;
- comunicação de eventos;
- interface de comandos.

### Sinais

**Sinais** são mecanismos utilizados para informar a um processo que determinado evento ocorreu. Eles podem ser gerados pelo sistema operacional ou por outros processos.

Um exemplo é pressionar **Ctrl+C** para interromper um programa. O sistema operacional gera um sinal que informa ao processo sobre o evento. O processo pode possuir um tratador específico para lidar com esse sinal.

## Cap 6 - Thread


Uma **thread** é uma unidade de execução dentro de um processo. Um processo pode possuir uma ou várias threads executando partes diferentes de uma aplicação de forma concorrente.

==A principal diferença em relação aos processos é que **threads de um mesmo processo compartilham o espaço de endereçamento e outros recursos**, tornando a comunicação entre elas mais simples e rápida.==

Thread = unidade de execução dentro de um processo.

**Processo = unidade de alocação de recursos**  
**Thread = unidade de execução/escalonamento**

|Conceito|Característica principal|
|---|---|
|**Monothread**|Um processo possui uma thread|
|**Multithread**|Um processo possui várias threads|
|**Thread de usuário (TMU)**|Gerenciada por biblioteca em modo usuário|
|**Thread de kernel (TMK)**|Gerenciada pelo sistema operacional|
|**Modo híbrido**|Combina TMU e TMK|
|**Scheduler activations**|Kernel e biblioteca cooperam no gerenciamento|
|**Principal vantagem**|Concorrência com menor custo que vários processos|
|**Principal cuidado**|Threads compartilham memória e precisam de sincronização|

==o capítulo mostra como as **threads permitem dividir um processo em várias unidades de execução concorrente**, proporcionando melhor utilização dos recursos e menor overhead, mas exigindo cuidado com o compartilhamento de memória e a sincronização.==
### Ambiente monothread

No **ambiente monothread**, cada processo possui apenas uma thread de execução.

Assim, o processo executa suas tarefas de forma sequencial. Para realizar concorrência, podem ser utilizados vários processos, mas isso gera maior custo de criação, comunicação e troca de contexto.

Uma limitação importante é que, quando o processo precisa esperar por uma operação de E/S, sua execução fica bloqueada até que essa operação termine.

### Ambiente multithread

No **ambiente multithread**, um único processo pode possuir várias threads.

As threads compartilham:

- espaço de endereçamento;
- arquivos;
- sinais;
- temporizadores;
- outros recursos do processo.

Isso reduz o custo em relação à utilização de vários processos. O livro apresenta, inclusive, tempos de criação e sincronização menores para threads do que para processos.

Por outro lado, como as threads compartilham a memória, é necessário utilizar mecanismos de **comunicação e sincronização** para evitar que uma thread altere dados utilizados incorretamente por outra.

#### Vantagens das threads
O uso de threads pode:

- diminuir o overhead de criação e troca de contexto;
- facilitar a comunicação entre partes de uma aplicação;
- permitir a execução concorrente de diferentes tarefas;
- melhorar a utilização do processador e dos dispositivos de E/S;
- permitir que uma aplicação continue trabalhando enquanto outra tarefa está bloqueada;
- aproveitar melhor sistemas com múltiplos processadores.

O livro cita como exemplos **editores de texto, planilhas, aplicativos gráficos e processadores de imagens**. Em sistemas cliente-servidor, várias threads também podem atender diferentes solicitações simultaneamente.


### Programação multithread

A programação multithread permite dividir uma aplicação em várias tarefas que podem ser executadas concorrentemente.

Em um processador único, as threads são alternadas pelo sistema ou pela biblioteca de threads, dando a impressão de execução simultânea. Em sistemas com múltiplos processadores, diferentes threads podem realmente executar **em paralelo**

### Arquiteturas de implementação

**Pthreads**. O padrão facilitou a implementação de aplicações multithread e é amplamente utilizado em ambientes Unix.

O capítulo apresenta quatro formas principais de implementação de threads:


#### Threads em modo usuário — TMU

São gerenciadas por uma **biblioteca em modo usuário**, sem que o sistema operacional precise conhecer individualmente cada thread.

**Vantagens:**

- maior rapidez;
- menor overhead;
- não exige suporte direto do sistema operacional;
- evita várias mudanças entre modo usuário e kernel.

**Desvantagens:**

- se uma thread realizar uma operação bloqueante, todo o processo pode ficar bloqueado;
- o sistema operacional não consegue escalonar as threads individualmente;
- em sistemas multiprocessadores, threads do mesmo processo não podem ser executadas simultaneamente em diferentes CPUs.

#### Threads em modo kernel — TMK

São gerenciadas diretamente pelo **núcleo do sistema operacional**.

O sistema conhece cada thread e pode escaloná-las individualmente. Em máquinas com múltiplos processadores, threads de um mesmo processo podem executar simultaneamente em diferentes processadores.

#### Modo híbrido

Combina threads em modo usuário e modo kernel. As threads de usuário são associadas às threads de kernel.

Apesar da flexibilidade, possui problemas herdados dos dois modelos. Por exemplo, uma chamada bloqueante realizada por uma thread de kernel pode colocar as threads de usuário associadas em espera.

#### Scheduler Activations

O modelo **scheduler activations** busca combinar as vantagens dos modos usuário e kernel.

Nesse modelo, a biblioteca de threads em modo usuário e o kernel **trocam informações e trabalham de forma cooperativa**. Assim, procura-se evitar mudanças desnecessárias entre os modos usuário e kernel e melhorar o desempenho.