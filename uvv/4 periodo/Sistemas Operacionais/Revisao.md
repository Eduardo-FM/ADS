
===Tem conceitos muitos similares==

*Se der fazer uma prática de comandos no Ubuntu*

Tudo é feito em funcao do acesso do usuario. O SO se nao tiver na camada zero, nao tem finalidade para o usuario. Quem interage pelo o SO é sempre o usuario. 

O aplicativos/compiladores usam os servicos do SO

O SO abstrai o hardware e oferece servicos controlados e seguros

O hardware é a ultima camada, é a base física da computacao.


## Mono x multi

*Monoprogamacao*
- apenas um programa ocupa memoria e processador por vez 
- apenas sistemas legados funcionam assim


*multi*

- varios programas residem na memoria de forma simutanea e nao concorrente.
- maximiza o uso do processador
- multitarefa (fala em fatiar o tempo em camadas, te da a sensacao de paralelismo, mas não são, é sequencial - paralelismo simulado)
- paralelismo real (processos executam simultaneamente )

==Hierarquia de memoira==

Registradores (maior) -> Cache -> Ram -> SSD / HDD (menor)

Quanto maior mais a taxa de processamento e mais caro, mas tem um melhor desempenho.

*Comando no linux para ver a memoria RAM disponivel ==free -h==*

## RISC x CISC e Pipeline

-> Tipos de processadores

*Risc*
processador especializado em algumas funcoes, nao precisa ter um clock( frequencia que ele realiza operacoes matematicas ) muito alto.

*Cisc*
Um processador que aceita varias funcoes, mas ele é mais lento.

-> Pipeline
aumenta a vazao de dados do processador. ele consegue armazenar e utilizar dados fora dos processadores, mas causa bolhas de ciclos desperdiçados e o processador precisa fazer o reprocessamento.

throughput -> taxa de evasao basica do processamento.

## Ferramentas 

- Compilador 
transforma o codigo fonte em um arquivo executado.

- interpretador 
executa o código fonte linha a linha.

- Linker
une módulos objeto e bibliotes em um único executável

- Loadres 

- Depurador


## Concorrencia

Significa multimos processos progridem, no tempo, disputando recursos compartilhados.

### Implicacoes

surgem naturalmente em sistemas multiprogramaveis.

### Interrupcao x Excecao

terminar um processo e comaçar outro a partir de um sinal que outro processo mudou de estado.

*Excecao*
Origem interna - gerada pela propria execucao de uma instrucao. 

Duas funcionalides tem o objetivo de interromper a execucao normal do processador

### buffering x Spooling

Ambos os mecanismos lidam com a diferenca de velocidade entre dispositivos, mas oprem de formas fundamentalmente distintas.

*Buffering*

Uso de area de RAM para armazenador dados temporariamente durante a transferencia entre dispositivos de velocidades diferentes.

- armazenamento temporario de RAM
- durante operacao de E/s
- compensa diferenca de velocidade em tempo real
- arquivos muito grandes nao se faz buffering (joga para RAM o possivel, depois passa para o disco pelo spooling)

*Spooling*

Ddaos sao gravados em disco antes de serem enviados ao dispositivo lento. 

- utiliza memoria de disco
- é uma fila

### Reentrancia

propriedade do codigo que permite seu compartilhamento seguro entre multiplos processos simultaneaos.

- nao altera seu proprio codigo se identificar que é uma reentrancia.

é importante para diminuir a quantidade de memoria utilizada. Para ter seguranca de execucao. e ser escalado.

## Esstrutura do SO

- modo usuario 
acesso restrio ao hardware

- modo kernel acesso total ao hardware

- SystemCall

uma aplicacao solicita servico ao kernel, transmitindo do modo usuario para o modo kernel de forma controlada, auditavel e segura. 

### arquitetura do nucledo

- monolitica
tudo em um unico bloco de kernel

- camadas
funcos divididas em niveis hierarquicos

- maquina virtual
Camada que simula hardware para multiplos SOs

- microkernel
Apenas funcoes essenciais no kernel; resto em modo usuario


## Processo

==Diferenca entre programa e processo==
Um programa é um artefato passivo; um processo é a instancia ativa de sua execucao, com recursos e estado próprios.

### Estados do processo

- Novo 
Processo criado, aguardando admissao pelo SO no sistema

- Pronto
Apto a executar, aguarda a CPU ser atribuida pelo escalonador (decide quem tem acesso a CPU)

- Executando
Usando a CPU neste exato instance.

- Bloqueado
Aguada evento externo (E/S, sinal). Nao pode usar a CPU mesmo que esteja disponivel.

- Encerrado
Execucao concluida, recursos sendo liberados pelo SO.

==Transmissao critica: bloqueado -> pronto (nao executando!). QUando a E/S termina, o processo volta à fila de prontos e aguarda o escalonador atribuir a CPU. 

### Bound x

Classificacao por uso de recursos

- CPU-bound
processo que passa a maior parte do tempo usando o processador.

- I/O - bound
Processo que passa a maior parte do tempo aguardando E/S.


Classificacao por interatividade
- Foreground
Processo que interga diretamente com o usuário em tempo real.

- Background
Processo sem interacao direta com o usuário  - executa em segundo plano. 

### Processo x Thread

Thread é a unidade em execucao dentro de um processo (é uma unidade básica). Processo é a unidade de alocacao de rurcos.

Nao necessariamente rodam juntos. Um processo pode chamar varias threads.

Thread é um "guarda chuva" que busca recursos de memoria e CPU.

Processo é especifico. Thread é algo compartilhando entre qualquer processo. 

