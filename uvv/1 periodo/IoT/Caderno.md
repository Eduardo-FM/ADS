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

