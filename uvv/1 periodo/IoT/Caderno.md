# Aula - 10/02

## Introdução a IoT

Um computador conversa com outros através de um protocolo de rede 

- Protocolo de rede 
-> Um conjunto de regras que padronizam como um computador conversa com outro.

---
-> Ex:
- IP
- TCP 
- UDP
- ICMP
- DNS
- HTTP 
- DHCP
- POP
- IMAP
- IRC
- MQTT
- HTTPS
- FTPS
- SSH
- TELNET

------

## Protocolo IP

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

## Protocolo DNS

- Domain Name System

Para se conectar a um site o computador faz uma requisicao ao servidor DNS raiz da internet.

Há 13 servidores DNS raiz.

Quando vc digita um site, é feito uma conexao com um servidor DNS raiz perguntando qual o endereco IP do site, o servidor DNS raiz responde com o endereco do servidor DNS local. (no nosso caso o servidor DNS do Brasil), ai o computador vai no DNS do "Registro.br" e pergunta qual o endereco IP do site (uvv.br) que por sua vez vai responder o endereco do servidor DNS especifico (no caso o servidor DNS da UVV), que vai enviar o endereco IP.

O protocolo DNS faz a traducão de nomes para enderecos.


# Aula 17/02


há varios meios de conexos com rede

Ex: cabo de rede

![[Pasted image 20250217193914.png]]

Os cabos de redes sao conectados com os cabos de redes, que se conectam a outro aparelho.

Essa placa de rede tem um endereco MAC. Toda placa de rede tem um endereco especial chamado de MAC adress, messe endereco é único e exclusivo para as todas as placas de redes do mundo. Porque o endereco MAC é que identifica essa placa na rede.

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

# Aula 25/02

#### Configurar o modem

É preciso criar uma rede, e conectar esse rede a rede da operadora (no nosso caso a rede da uvv)

Para fazer isso, todo roteador wi-fi tem conexoes de cabo de rede, ha tres entradas de uma cor e outra de outra cor, o cabo de rede de marcado diferente é sempre o cabo de rede da operadora, as outras conexoes sao para a rede local.

Para configurar o modem você tem que conecta-lo a um cabo de rede local. 

Dentro do roteador tem um servidor DHCP que dá um endereco IP para o PC. Quando os PC precisam mandar uma mensagem, para isso o próprio roteador serve como gateway para a rede.

Para configurar o IP do roteador é necessário saber o IP do roteador. Para configurar basta ir no navegador e digitar o gateway.

Apos digitar a senha, e escolher "IP dinamico",  quando ligar o roteador a rede da uvv e o roteador da UVV vai, atraves do DHCP, dar o endereco IP da rede. O endereco gateway do rodetador será o gateway da uvv, o gateway do roteador da uvv será o gateway da internet.


# Aula 10/03


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

# Aula 11/03

==exercicio

# Aula 17/03 

==Aula no laboratorio

# Aula 25/03

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
- EEPROM(funciona como um HD) (não volátil) (variaveis)

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



# Aula 06/05

## histórico da IoT

### Percusores

- 1982: universidade de Carnegie Mellon:
	- máquina de coca cola
	- david nichols, mike kazar, john zsarnay
	- conectada na ARPANET e na LAN da Carnegie Mellon

### Termo IoT 

- 1985: surgiu o termo
	- Peter Lewis
	- publicou o termo em uma revista.

### 1 dispositivo IoT 
- 1990: torradeira
	- John Romkey
	- Conectou à internet 
	- ligava/desligava
- 1 Webcam
	- 1983: Cambridge Computer Lab
		- cafeteira monitorada por vídeo 
		- vídeo transmitido pela rede
- 2 Webcam
	- 1994: Wearcam
		- Steve Man
		- Câmara nos óculos
		- inspirada pela cafeteira de Cambridge
- Termo IoT
	- 1999: Surgiu o termo
		- Kevin Ashton
		- publicou o termo em uma revista cientifica conhecida
- RFID
	- a partir de 2004 o Wallmart resolveu utilizar dispositivos de rádio frequência em seus produtos
	- 2004: RFID no Walmart

 A partir de 2005, explosão de dispositios:
 - carros 
 - óculos
 - briquedos
 - TVs
 - Relógios
 - geladeiras
 - etc

### Por que a explosão

- tipos diferentes de sensores 
- formas para a identificacao
- computacao ficou barata
- criados diversos servicos de comunicacao


# Aula 12/05

## Tópico 002

---
autolab.compatucaoraiz.com.br

---

#### Conceitos básicos sobre IoT

IoT 
- basicamente significa conectar dispositivos na internet
	- sensores para monitoramento
	- atuadores para acoes
- Os dispositivos de IoT são geralmente fabricados por engenheiros de forma bem específica e personalizada;
	- tv
	- alexa
	- relógio de pontoo


---
==IMPORTANTE==

Microprocessador
- Unidade de controle 
- ULA

Microcontrolador
- Unidade de controle 
- ULA
- Memória RAM
- Memoria SRAM
- Memória ESFROM
- I/O
- AD

---

#### Arduino: hardware - microcontrolador
- é um pequeno ¨computador completo" em um único chip
- baseado em microcontroladores AVR de Atmel
- arquitetura Harvard modificada, 8-bits

Para o arduino conversar com o seu computador é necessário outro micro controlador "USB TO SERIAL CHIP"  


#### Memoria
- Geralmente 2 tipos de memória 
	- SRAM (memória de acesso randomico estatica): memoria volatil e temporaria, para uso nos programas, quantidade varia conforme o modelo:
		- UNO: 2KB
		- Nano: 32 KB
	- FLASH (armazena o programa, as intrucoes para o microcontrolador). Quantidade varia conforme o modelo:
		- UNO: 23kb
		- Nano: 256 KB
	- EEPROM (memória especial, memória permanente)
- Arquitetura Harvard
	- Diferente da arquitetura de Von Neumann (na arquitura os programas e os dados estão na mesma memória)
	- Na harvard a memoria do programa é separada da memoria dos dados



### Objetos de IoT x Objetos Inteligentes de IoT

Os objetos inteligentes de IoT pretendem tornar a interacao homem-maquina mais natural, gerando conexoes e servicos sem a necessidade de acoes humanas.


### C

Há linguagens de Alto nivel e linguagens de baixo nivel, a linguagem de mais baixo nível é a linguagem de máquina.

Em 1972 foi criado a linguagem em C (é uma linguagem de alto nivel)

Para ir do cógio fonte para o código de máquina é necessário um compilador:
- os principais sao:
	- GCC 
	- Clange


#### Comandos servidores linux 

- pwd (print work directory)
- ls 
- code 'nome_do_arquivo'.c

``` C

#include <stdio.h>

int main (void) 
{
 printf("Olá mundo! \n");
}

 //Para rodar precisa usar o comando
 make 'nome_do_arquivo'

//Para rodar 
./'nome_do_arquivo'


```

# Aula 13/05

### big data

- volume 
- velocidade 
- variedade 
- veracidade 
- + valor 


## C

todo programa C inicia pelo 'main'

o include serve para incluir bibliotecas

para formatar uma string é necessário utlizar um especificador de formato:

``` C

%s string 

%c caracter

%d inteiro

%f float ou double
```

```c

#include <cs50.h>

#include <stdio.h>

  

int main (void)

{

int idade = 50;

double pi = 3.14;

string nome = "Abrantes";

  
  

printf ("Olá, %s, você tem %d anos! \n", nome, idade);

}

```

```c
#include <cs50.h>

#include <stdio.h>

  

int main (void)

{

string nome = get_string("Qaul seu nome? ");

int idade = get_int("Sua idade é: ");

double numero = get_double("Qual seu número favorito? ");

  
  

printf ("Olá, %s, você tem %d anos! \n", nome, idade);

printf("Seu número favorito é %.2f.\n", numero);

}
```


# Aula 19/05

### IoT como um negócio 

- Area em franco crescimento 
- grande demanda profissional (redes, eletrônica, programacao)
- inovacao como diferencial competitivo


## C

``` c
#include <stdio.h>

#include <cs50.h>

  

int main(void)

{

//if/else

char letra = get_char("Você concorda com o nosso pacto? (S/N)");

  

if (letra == 'S')

{

printf("Sua alma é minha!!!\n");

}

else if (letra == 's')

{

printf("Sua alma é minha!!!\n");

}

else

{

printf("SNIF, SNIF, você é do time de Jesus\n");

}

}
```



#### OR ou AND

**Lógica matemática**

| nome      | Símero | Significado | C    |
| --------- | ------ | ----------- | ---- |
| CONJUNCAO | /\     | AND (E)     | &&   |
| DISJUNCAO | V      | OR (OU)     | \|\| |
| NEGACAO   | ~      | NOT (NAO)   | !    |

``` c
#include <stdio.h>

#include <cs50.h>

  

int main(void)

{

//OR e AND

char letra = get_char("Você concorda com o nosso pacto? (S/N)");

  

if (letra == 'S' || letra == 's')

{

printf("Sua alma é minha!!!\n");

}

else if (letra == 'N' || letra == 'n')

{

printf("SNIF, SNIF, você é do time de Jesus\n");

} else

{

printf("Não sei o que você quer!\n");

}

}

``` 

**Igualdade**

| nome      | C   |
| --------- | --- |
| Igual     | ==  |
| diferente | !=  |

**Relacao**


| nome           | C   |
| -------------- | --- |
| maior          | >   |
| mair ou igual  | >=  |
| menor          | <   |
| menor ou igual | <=  |


### Estrutura de repeticao

``` c
#include <cs50.h>

#include <stdio.h>

  

int main(void)

{

// FOR

string nome = get_string("Qual o seu nome?\n");

  

for (int i = 0; i < 10; i++)

{

printf("Olá, %s!\n", nome);

}

  

// WHILE

int numero = get_int("Digite um número:\n");

while (numero < 10)

{

printf("Número: %d\n", numero);

numero++;

}

  

// DO WHILE

int tabuada = get_int("Digite um número para a tabuada:\n");

int i = 1;

do

{

printf("%d x %d = %d\n", tabuada, i, tabuada * i);

i++;

} while (i <= 10);

  

return 0;

}
```


# Aula 20/05

### impressao

```c
#include <cs50.h>
#include <stdio.h>

int main(void)

{
	
	int linhas = get_int("Quantas linhas? \n");
	int colunas = get_int("Quantas colunas? \n");
	
	for (int l = 1; l <= linhas; l++)
	{
		for (int c = 1; c <= colunas; c++)
		{
			printf("#");
		}
		printf("\n");
	}
}
```

# Aula 26/05

### funcoes 

as variaveis dentro da funcao se chamam parametro

``` c
#include <stdio.h>
#include <cs50.h>

int potencia(int base, int expoente); //PROTÓTIPO DAS FUNCOES

int main(void)
{
	printf("Valor: %d \n", potencia(3, 2));
	
	return 0;
}

int potencia(int base, int expoente)
{
	int valor = 1;	
	for (int i = 1; i <= expoente; i++)	
	{
		valor *= base;
	}
	return valor;
}
```
