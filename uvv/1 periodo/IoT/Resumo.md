
# Historia da internet 

# Protocolos

##### o que é um protocolo?

Um protocolo, em geral, é um ==conjunto de regras e procedimentos que regulam uma interação ou um processo==.

- Protocolo de rede 
-> Um conjunto de regras que padronizam como um computador conversa com outro.

### IP

- Internet Protocol

Todo o computador precisa saber aonde o outro computador está para estabelecer comunicações. Para isso se utiliza o endereço IP.

O IP é um dos protocolos mais importantes.

Toda comunicação entre dispositivos em uma rede se dá através de endereços IPs.

O protocolo IP é feito através de 4 grupos de números.

O padrão é sempre:
	XXX.YYY.ZZZ.WWW

Cada grupo de número tem 256 possibilidades. (Pode ser do 0 ao 255) A combinação desses números formam o endereço IP. Esse endereço tem que ser diferente para todos os computadores conectados em uma rede.

Dá aproximadamente 4 bilhões de possibilidades.

O endereco IP são divididos em faixas entre enderecos públicos e enderecos privados.

Não é possível ter endereços IPs repetidos dentro da mesma rede, mas é possível ter endereços iguais em redes distintas. 

Os enderecos privados não são válidos dentro da Internet. 

O nome da rede dada a uma rede que está em um local especifico é "Rede local".

Todos os equipamentos de rede são configurados para que se voce está na internet e tenta utilizar um endereco privado ele mata a conecao.

Para se conectar a internet os roteadores de internet encaminham o trafico da internet para que a rede local utilize um IP público para a comunicao com a internet.

Todo equipamento tem um IP privado e um IP público.

Quando voce se conecta em uma rede o computador recebe o seu endereco IP privado, além disso ele recebe a máscara de rede, o endereco do Gateway, os enderecos do DNS e ETC.

Todo gateway tem 2 enderecos: o endereco da rede interna e o endereco externo.


---

Um endereço IP (Internet Protocol) ==é um identificador numérico exclusivo atribuído a cada dispositivo conectado à internet ou a uma rede de computadores==. É como um endereço postal para a internet, permitindo que os dispositivos comuniquem uns com os outros. 

Em detalhes:

- **Identificação:**
    O endereço IP serve para identificar um dispositivo específico em uma rede, garantindo que os dados sejam enviados para o destino correto. 

- **Comunicação:**
    Ele permite que os dispositivos se comuniquem entre si, enviando e recebendo dados pela internet ou por uma rede local. 

- **Protocolo da Internet:**
    O IP é parte do Protocolo de Internet, que é o conjunto de regras que define como os dados são enviados e recebidos na internet. 

- **Tipos de endereços IP:**
    Existem endereços IP públicos (visíveis para a internet) e privados (usados dentro de uma rede local). Também existem endereços IP estáticos (fixos) e dinâmicos (mudam com o tempo). 

- **Exemplo:**
    Um endereço IP pode ser algo como `192.168.1.100` (privado) ou `123.45.67.89` (público).

---

### DHCP 

DHCP, ou Dynamic Host Configuration Protocol, ==é um protocolo de rede que atribui automaticamente endereços IP a dispositivos em uma rede==. Isso significa que os dispositivos não precisam ser configurados manualmente com um endereço IP, tornando a configuração de rede mais fácil e eficiente. 

Em termos mais detalhados:
- **Atribuição Automática de Endereços IP:**
    O DHCP permite que um servidor central (servidor DHCP) distribua automaticamente endereços IP para dispositivos que se conectam à rede. 
    
- **Simplificação da Configuração:**
    Isso elimina a necessidade de configurar manualmente cada dispositivo com um endereço IP, economizando tempo e reduzindo erros. 
    

- **Gerenciamento Dinâmico:**
    Os endereços IP podem ser alocados temporariamente ou permanentemente, e o DHCP permite que os endereços IP sejam reatribuídos a outros dispositivos quando um dispositivo se desconecta ou se move para outro local na rede. 
    

- **Outras Configurações:**
    Além de endereços IP, o DHCP também pode fornecer outras informações de configuração, como a máscara de sub-rede, o gateway padrão e os endereços DNS, que são essenciais para que os dispositivos se comuniquem na rede e na internet. 


- **Uso Comum:**
    
    O DHCP é amplamente utilizado em redes domésticas, em redes corporativas e em ambientes de nuvem, facilitando a configuração e o gerenciamento de dispositivos conectados.

### DNS

- Domain Name System

Para se conectar a um site o computador faz uma requisicao ao servidor DNS raiz da internet.

Há 13 servidores DNS raiz.

Quando vc digita um site, é feito uma conexao com um servidor DNS raiz perguntando qual o endereco IP do site, o servidor DNS raiz responde com o endereco do servidor DNS local. (no nosso caso o servidor DNS do Brasil), ai o computador vai no DNS do "Registro.br" e pergunta qual o endereco IP do site (uvv.br) que por sua vez vai responder o endereco do servidor DNS especifico (no caso o servidor DNS da UVV), que vai enviar o endereco IP.

O protocolo DNS faz a traducão de nomes para enderecos.

---
O protocolo DNS (Domain Name System) ==é um sistema que traduz nomes de domínio (como google.com) em endereços IP (como 172.217.160.142), que são os endereços numéricos que os computadores usam para se comunicar==. Em resumo, é como a agenda telefônica da internet, permitindo que os usuários naveguem usando nomes fáceis de lembrar, em vez de endereços IP complexos. 

Função:
- **Tradução de Domínio para IP:**
    O DNS converte os nomes de domínio em endereços IP, que são necessários para que os computadores se conectem a outros dispositivos na internet. 

- **Facilidade de Uso:**
    Simplifica a navegação na web, permitindo que os usuários digitem nomes de domínio em vez de endereços IP. 

- **Mapeamento de Nomes:**
    O DNS mantém um banco de dados distribuído com os mapeamentos entre nomes de domínio e endereços IP. 

Como funciona:
- **1.** **Solicitação:**
    Quando você digita um nome de domínio em um navegador, a solicitação é enviada a um servidor DNS.
    

- **2.** **Resolução:**
    O servidor DNS procura no seu banco de dados o endereço IP correspondente ao nome de domínio solicitado.
    

- **3.** **Envio do IP:**
    O servidor DNS envia o endereço IP para o navegador.
    

- **4.** **Conexão:**
    O navegador utiliza o endereço IP para se conectar ao servidor do site desejado. 
    

Importância:
- **Indispensável para a internet:**
    O DNS é essencial para que a internet funcione, pois permite que os computadores se comuniquem usando nomes de domínio. 
    

- **Facilidade de uso para os usuários:**
    Permite que os usuários naveguem na internet com nomes de domínio fáceis de lembrar, em vez de endereços IP numéricos. 
    

- **Redução de complexidade:**
    Simplifica o processo de navegação na web, reduzindo a necessidade de lembrar endereços IP complexos.
---

### TCP/UDP

TCP (Transmission Control Protocol) e UDP (User Datagram Protocol) são ==dois protocolos usados para a transferência de dados na camada de transporte da Internet==. O TCP é orientado à conexão, garantindo a entrega confiável e ordenada dos dados, enquanto o UDP é um protocolo sem conexão, focado em velocidade e eficiência, mesmo que a entrega não seja garantida. 

TCP (Transmission Control Protocol):

- **Orientado à conexão:**
    O TCP estabelece uma conexão entre o remetente e o destinatário antes de enviar os dados, garantindo a entrega confiável e ordenada.

- **Confiabilidade:**
    O TCP garante que todos os dados sejam entregues corretamente, na ordem correta e sem erros, através de um processo de controle de erros e retransmissão.

- **Uso:**
    É usado em aplicações onde a confiabilidade é essencial, como acesso a páginas da web (HTTP), transferência de ficheiros (FTP), e-mail (SMTP) e acesso remoto (SSH). 

UDP (User Datagram Protocol):
- **Sem conexão:**
    O UDP não estabelece uma conexão antes de enviar os dados, o que o torna mais rápido, mas menos confiável.

- **Velocidade e eficiência:**
    O UDP é mais rápido porque não há sobrecarga de estabelecer e manter uma conexão, sendo ideal para aplicações onde a velocidade é mais importante que a garantia da entrega, como streaming de vídeo, jogos online e chamadas de voz.

- **Uso:**
    É usado em aplicações onde a velocidade é mais importante que a confiabilidade, como jogos online, streaming de vídeo, VoIP e pesquisas de DNS.
    
### GATEWAY

Um gateway, em redes de computadores, ==é um dispositivo ou sistema que facilita a comunicação entre diferentes redes, sistemas ou dispositivos que usam protocolos, linguagens ou arquiteturas distintas==. Pode ser visto como uma "porta" que permite que os dados fluam entre esses ambientes. 

Em resumo:

- **Função:** Atua como intermediário na comunicação entre redes diferentes. 
- **Exemplos:** Roteadores, firewalls e modems podem atuar como gateways. 
- **Importância:** Garante que dados possam ser transmitidos entre sistemas com diferentes protocolos, como redes locais e a internet. 

- **Tipos:** Existem gateways de rede, de API e gateways de pagamento, entre outros. 

Explicação mais detalhada:

- **Gateway de Rede:**
    
    Permite a comunicação entre diferentes redes, traduzindo protocolos e endereços. 
    

- **Gateway de API:**
    
    Gerencia o tráfego de APIs, facilitando a comunicação entre diferentes sistemas sem expô-los diretamente. 
    

- **Gateway de Pagamento:**
    
    Facilita transações online, permitindo que consumidores paguem por produtos ou serviços. 
    

O conceito de gateway é fundamental para a interoperabilidade de sistemas e redes, garantindo que diferentes tecnologias possam interagir entre si.

# Cabo de rede

há varios meios de conexos com rede

Ex: cabo de rede

![[Pasted image 20250217193914.png]]

Os cabos de redes sao conectados com os cabos de redes, que se conectam a outro aparelho.

Essa placa de rede tem um endereco MAC. Toda placa de rede tem um endereco especial chamado de MAC adress, esse endereco é único e exclusivo para as todas as placas de redes do mundo. Porque o endereco MAC é que identifica essa placa na rede.

Há duas maneiras de se identificar um computador na rede, o endereco IP e o endereco MAC da placa de rede. 


A placa de rede pode vir sozinha (off board) ou embutida na placa mae do computador (on board). 

Cada placa de rede tem um endereco MAC unico e exclusivo.

Os computadores se comunicam através do endereco IP e do endereco MAC.

O indereco IP é dado pelo DHCP e o endereco MAC é pelo fabricante.


O endereco é dessa forma:
> ether dc:21:5c:b0:9c:85

Ela segue o padrao "Ethernet" (padrao de redes com cabo).

O endereco MAC está no padrao Hexidecimal.

Em um switch os computadores conversam entre em si através do endereco MAC.

Um tipo de cabo de rede é o cabo de par trançado.


Para conseguir utilizar o cabo é necessário colocar um conector, precisa colocar os 8 fios e colocar no conector (RJ45 ou 8P8C).

Os fios seguem uma ordem especifica, há dois padroes:

- Europeu (568B)
- Americano (568A)

O Brasil usa o Americano.

## *ORDEM DOS FIOS*

- branco verde
- verde 
- branco azul
- laranja 
- branco laranja
- azul
- branco marrom
- marrom

#### Configurar o modem

É preciso criar uma rede, e conectar esse rede a rede da operadora (no nosso caso a rede da uvv)

Para fazer isso, todo roteador wi-fi tem conexoes de cabo de rede, ha tres entradas de uma cor e outra de outra cor, o cabo de rede de marcado diferente é sempre o cabo de rede da operadora, as outras conexoes sao para a rede local.

Para configurar o modem você tem que conecta-lo a um cabo de rede local. 

Dentro do roteador tem um servidor DHCP que dá um endereco IP para o PC. Quando os PC precisam mandar uma mensagem, para isso o próprio roteador serve como gateway para a rede.

Para configurar o IP do roteador é necessário saber o IP do roteador. Para configurar basta ir no navegador e digitar o gateway.

Apos digitar a senha, e escolher "IP dinamico",  quando ligar o roteador a rede da uvv e o roteador da UVV vai, atraves do DHCP, dar o endereco IP da rede. O endereco gateway do rodetador será o gateway da uvv, o gateway do roteador da uvv será o gateway da internet.

# Wifi

# Circuito elétrico

## Fundamentos físicos da computação

### circuitos elétricos 

Para entender circuitos eletricos é necessários entender alguns circuitos fisicos
#### Carga elétrica

- é uma propriedade intriseca da matéria 
- faz com que a matéria experimente uma força de atracão ou repulsão 
- medida em Coulombs (C)
- Analogia: a carga elétrica é a ÁGUA

==Vamos usar uma analogia com um circuito de água para entender os circuitos elétricos==

#### Corrente elétrica

- é a carga elétrica em movimento
- é o movimento da carga életrica  (representa uma taxa que mede a intensidade do fluxo elétrico)
- medida em Amperes (A)
- Em equacoes costuma-se utilizar o I
- 1 A = 1 C/s
- Analogia: Fluxo da água em um ponto especifico / s

#### Tensão (Vontagem)

- aquilo que impulsiona a carga elétrica, ela faz a carga elétrica andar e cria a corrente.
- imagine uma fonte de energia (uma BOMBA DÁGUA). Essa bomba aumenta a PRESSÃO DA ÁGUA e aumenta a velecidade do fluxo. Essa pressão é a TENSÃO.
- A tensão influencia a taxa com a qual uma carga flui através de um circuito, e corresponde à diferenca de potencial elétrico entre dois pontos. É medida em Volts(V)
- A tensão é a diferença entre o potencial elétrico entre dois pontos.
- Potencial elétrico é a energia potencial por unidade de carga, em J/C, para mover uma carga de um ponto à outro.
- A tensão é uma diferenca entre o positivo e o negativo da eletricidade

#### Resisência 

- É uma medida da dificuldade da corrente fluir através de um condutor
- dificulta a passagem da corrente elétrica
- Medida em Ohms(Ω)
- Analogia: diâmetro do cano


### Lei de Ohm

- A corrente que flui entre dois pontos é igual à voltagem dividida pela resistência 

							I = V /R

==macete para decorar 

- cuidado: ACxDC

Corrente continua: o polo do fluxo da corrente continua o mesmo (oque é positivo é sempre positivo, e oque é negativo é sempre negativo)

Corrente alternada:  polo do fluxo da corrente alterna com o tempo (o positivo e o negativo ficam se invertendo com o tempo)

==não vamos trabalhar com corrente alternada, apenas com corrente continua==

### Circuitos elétricos

- é um conjunto de componentes conectados de forma a permitir que a corrente possa fluir em um loop, a partir da fonte de energia, passando pelos elementos do circuito, e de volta à fonte ==TEM MAIS COISA==
- comeca e termina no mesmo lugar
- para que um circuito funcione ele tem que estar fechado
- ==tem mais coisa==

### Lei de Kirchhoff

- A soma das voltagens em um circuito é zero.
- Isso significa que se uma bateria fornece 9v para um circuito, os vários elementos do circuito devem "consumir' esses 9v.
- ==tem mais coisa aqui==

# Arduino

#### Arduino

Com o arduino se faz prototipos de dispositivos de Iot

o Arduino é uma placa para criar prototipos

---

Para trabalhar com IoT é necessário aprender sobre:
- circuitos eletricos
- circuitos analogico
- circuitos digitais 

Depois vamos criar os primeiros dispositivos não conectados a internet.

Depois iremos aprender a usar shields de internet, que fazem o arduino a conectar a internet.

Depois vamos utilizar o ESP32

---

#### Arduíno 

O arduino é uma placa para facilitar a criacao de prototipos de dispositivos eletronicos


ele é open hardware 

o Componente grande da placa é o microcontrolador (como se fosse a CPU, mas não é realmente uma CPU)

o arduino tem um micro controlador, ao contrário da CPU que é um microprocessador

o Microprocessador tem uma unidade de controle e uma unidade lógica aritimética. O microcontrolador tem além da UC e ULA, ele tem memória flash, memória SRAM, entrada, saída e outras coisas. 

O microcontrolador funcioná sozinho, náo precisa de placa mãe, HD e etc.

As desvantagens são: falta velocidade, pouco armazenamento.

O microcontrolador tem 3 tipos de memória:
- memória flash (aonde guarda o programa)
- SRAM (memória aonde fica as variaveis do programa) (memória volátil)
- EEPRUM (funciona como um HD) (não volátil) (variaveis)

para alimentar o arduino há 3 opcoes:
- cabo USB ligado ao computador (fornece 5V)
- fonte de alimentacao (pode usar fonte de 5V até 20V, o recomendável é até 12V)
- pelo VIN (input de voltagem) e o GND (GROUND)


OBS para alimentar outros dispositivos com o arduino tem que usar os pinos de (3V e 5V do arduíno)

Os pinos do arduinos servem para conectar os dispositivos que você irá utilizar 

na parte de baixo tem 6 pinos (A0 até A5) servem para entrada analógica (um dado não binário), mas não servem para saída analógica. Também servem para entrada analógica, também servem para saída digital. 

na parte de cima tem 14 pinos (0 ao 13) servem para entrada digital (dados binários) funcionam para: entrada digital, saída digital, os que tem os "~" (PWM) funcionam para simular saída analógica. Os pinos 0(RX, recepcao de dados) e 1 (TX, transmissao de dados), esses dois pinos são usados para comunicacão do arduino com outros dispositivos, para fazer essa comunicacao os cabos precisam ficar invertidos entre os dois dispositivos


A  lógica de programacao no arduíno é rodar em loop infinito (configura oque quer fazer, e comeca um loop infinito)

Os pinos de saída do arduino entregam até 5V.


Para programar o arduino precisa colocar o SETUP, configuracao do arduino

``` C arduino 

void setup() {
 pinMode(10, OUTPUT);
}

void loop() {
 digitalWrite(10, HIGH);
 delay(1000);
 digitalWrite(10, LOW);
 delay(1000);
}

```



