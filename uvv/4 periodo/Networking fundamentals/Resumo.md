
## 01 - Dispositivos e topologias de rede

### Dispositivos

Na rede, cada dispositivo tem um papel bem definido: quem gera/consome dados e quem apenas os encaminha. Confundir esses papéis é o erro mais comum neste tema.

- Hosts (dispositivos finais)
São a origem ou destino das mensagens 
Recebem um número para fins de comunicação que identificam o host dentro de uma rede especifica. (endereço IP)
ex.: computadores, smartphones, servidores

- Dispositivos intermediários
<strong>Encaminham</strong> os dados pela rede
==Intermediários não geram nem consomem o conteúdo das mensagens — apenas os repassam.==
ex.: switches, roteadores, access points
Um exemplo de software cliente é um navegador, como Chrome ou FireFox. Um único computador pode também executar vários tipos de software cliente. Por exemplo, um usuário pode verificar o e-mail e visualizar uma página da Web enquanto troca mensagens instantâneas e ouve um fluxo de áudio. A tabela lista três tipos comuns de software de servidor.

Uma rede só faz sentido se tiver dispositivos finais ligadas a ela. 

Se tem um endereço IP é um host.

Se utiliza um endereço de rede é um endpoint, e então um host.

Se um dispositivo desktop tiver uma função para ser um roteador ele será um dispositivo intermediário. 

Na aula trabalhamos com o Switch l2 (dispositivo intermediário)

#### Dispositivos finais

Um dispositivo final é a origem ou o destino de uma mensagem transmitida pela rede.

Os dados se originam em um dispositivo final, fluem pela rede e chegam a outro dispositivo final

![[Pasted image 20260929143001.png]]

#### Dispositivos intermediários

Dispositivos intermediários conectam os dispositivos finais individuais à rede. Eles podem conectar várias redes individuais para formar uma internetwork. Eles oferecem conectividade e asseguram que os dados fluam pela rede.

Esses dispositivos intermediários usam o endereço do dispositivo final de destino, em conjunto com as informações sobre as interconexões de rede, para determinar o caminho que as mensagens devem percorrer na rede. 

Exemplos dos dispositivos intermediários mais comuns e uma lista de funções são mostrados na figura.

![[Pasted image 20260929143103.png]]


### Tipos de Redes

==A distinção entre LAN e WAN é baseada na abrangência geográfica. A prova costuma trocar os conceitos — fique atento à definição de cada tipo.==

Os dois tipos mais comuns de infraestruturas de rede são as redes locais (LANs) e as redes de longa distância (WANs). Uma LAN é uma infraestrutura de rede que fornece acesso a usuários e dispositivos finais em uma pequena área geográfica. Normalmente, uma LAN é usada em um departamento dentro de uma empresa, uma casa ou uma rede de pequenas empresas. 

Uma WAN é uma infraestrutura de rede que fomece acesso a outras redes em uma ampla área geográfica, que normalmente pertence e é gerenciada por uma corporação maior ou por um provedor de serviços de telecomunicações. 

- LAN — Local Area Network
Conecta dispositivos em uma <strong>área geográfica pequena</strong>
Ex.: escritório, escola, casa

Rede local
Dentro de um prédio, de um campo, de uma cidade

Uma LAN é uma infraestrutura de rede que abrange uma pequena área geográfica. As LANs têm características específicas:
- LANs interconectam dispositivos finais em uma área limitada, como uma casa, uma escola, um edifício de escritórios ou um campus.
- Uma LAN é geralmente administrada por uma única organização ou pessoa. O controle administrativo é imposto no nível da rede e governa as políticas de segurança e controle de acesso.
- As LANs fornecem largura de banda de alta velocidade para dispositivos finais internos e dispositivos intermediários, conforme

- WAN — Wide Area Network
Conecta redes em <strong>áreas geograficamente distantes</strong>
Ex.: cidades, países, continentes

Rede de longo alcance
CIdades, países, continentes. 

Uma WAN é uma infraestrutura de rede que abrange uma ampla área geográfica. As WANs geralmente são gerenciadas por provedores de serviços (SPs) ou provedores de serviços de Internet (ISPs).

As WANs têm características especficas:
- As WANS interconectam as LANs em grandes áreas geográficas, como entre cidades, estados, províncias, países ou continentes.
- As WANs são geralmente administradas por vários prestadores de serviço.
- As WANs geralmente fomecem links de velocidade mais lenta entre as LANs.


==LAN não conecta cidades diferentes — isso é WAN. Não caia nessa troca!==

--- 
As redes domésticas simples permitem que você compartilhe recursos, como impressoras, documentos, imagens e música, entre alguns
dispositivos finais locais.

As redes de pequeno escritório e escritório doméstico (SOHO) permitem que as pessoas trabalhem em casa ou em um escritório remoto- Muitos trabalhadores independentes usam esses tipos de redes para anunciar e vender produtos, pedir suprimentos e se comunicar com os clientes.

Empresas e grandes organizações usam redes para fomecer consolidação, armazenamento e acesso a informações em servidores de rede. As redes fomecem e-mail, mensagens instantâneas e colaboração entre funcionários. Muitas organizações usam a conexão de sua rede à Internet para fomecer produtos e serviços aos chentes.

A intemet é a maior rede existente. Na verdade, o termo Internet significa uma «rede de redes". É uma coleção de redes públicas e privadas interconectadas.

Em pequenas empresas e residências, muitos computadores funcionam como servidores e clientes na rede. Esse tipo de rede é chamado de rede ponto a ponto.

---

### Topologia

- Topologia física 
descreve o mundo real (cabos, posição dos equipamentos); 
Na topologia fisica geralmente nao tem endereco ip. 

Os diagramas de topologia física ilustram a localização fisica dos dispositivos intermediários e a instalação dos cabos.


- topologia lógica 
descreve como os dados fluem. São camadas de abstração diferentes e independentes.
Na topologia logica se sabe o fluxo de dados

Diagramas de topologia lógica ilustram dispositivos, portas e o esquema de endereçamento da rede.


![[Pasted image 20260929101620.png]]


---
==Pontos-chave para a prova== 
- Topologia física → cabeamento e disposição real dos equipamentos 
- Topologia lógica → fluxo de dados e endereçamento lógico (ex.: IP)
- As duas são conceitos distintos e independentes

---

==Topologia física não é sobre endereçamento, não as confunda!==

### Tipos de portas

- Placa de interface de rede (MC) - Uma NIC conecta fisicamente o dispositivo final à rede.
- Porta fisica - Um conector ou tomada em um dispositivo de rede onde a mídia se conecta a um dispositivo final ou outro dispositivo de rede.
- Interface - Portas especializadas em um dispositivo de rede que se conectam a redes individuais. Como os roteadores conectam redes, as portas em um roteador são chamadas de interfaces de rede.

## 02 - Modos de configuração do Cisco IOS

O IOS possui uma hierarquia de modos de acesso. Cada modo oferece um conjunto diferente de comandos — é preciso subir de nível para ter mais permissões de configuração.

![[Pasted image 20260929101901.png]]

==O comando enable não leva direto ao config global — passa pelo modo privilegiado antes!==

Saber qual comando usar para subir ou descer de modo é essencial. Cada comando tem um comportamento diferente — use o correto para não se perder na hierarquia.

A hierarquia de modo de acesso siginifica que voce nao pode passar do modo usuario para o de configura interface tem que ir um por um. 4


==saber qual comando para subir e descer de módulo. ==

###  Acessando a CLI e Modos de Operação

- Switch>
EXEC do Usuário
Acesso limitado — apenas comandos básicos de visualização
O modo permite acesso a apenas um número limitado de comandos de monitoramento básico.
É geralmente chamado de modo "view-only".

- Switch#
EXEC Privilegiado
Acesso completo — entrar com ==enable==
O modo permite acesso a todos os comandos e recursos.
O usuário pode usar qualquer comando de monitoramento e executar a configuração e comandos de gerenciamento.
Para voltar para o modo EXEC do Usuário usar o comando ==disable==

- Switch(config)#
Configuração Global 
Configurar o dispositivo — entrar com ==configure terminal==

### Configurando Hostname e Senhas no S1

• Hostname: identifica o dispositivo na rede e na CLI 
• Senha de console: protege o acesso físico ao equipamento 
• Senha privilegiada: enable secret é criptografada — preferível ao enable password 
• Banner MOTD: exibe aviso legal a todos que acessarem o dispositivo

``` Cisco
Switch> enable 
Switch# configure terminal 
Switch(config)# hostname S1 
S1(config)# line console 0 
S1(config-line)# password cisco 
S1(config-line)# login 
S1(config-line)# exit 
S1(config)# enable secret class 
S1(config)# banner motd # 
Somente Acesso Autorizado. 
Infratores sujeitos às penalidades previstas em lei.
#
```

### Salvando a Configuração

- running-config
Configuração ativa, armazenada na RAM — perdida ao desligar o equipamento

- startup-config 
Configuração salva na NVRAM — carregada automaticamente na inicialização


Comandos Essenciais
``` Cisco
! Salvar configuração 
S1# copy running-config 
startup-config 

! Verificar configuração atual 
S1# show running-config
```

==Sempre salve após qualquer alteração de configuração. Sem isso, todas as mudanças serão perdidas ao reiniciar==

### Configurando os PCs

![[Pasted image 20260929115831.png]]

Gateway padrão não é necessário — todos os dispositivos estão na mesma rede 192.168.1.0/24. A máscara 255.255.255.0 define que os primeiros 3 octetos identificam a rede — dispositivos com o mesmo prefixo se comunicam diretamente.

### Interface de Gerenciamento do Switch (SVI)

Por que configurar IP no switch? Para gerenciamento remoto via SSH — o switch encaminha quadros por MAC, mas precisa de IP para ser acessado remotamente.

Comandos no S1

``` Cisco
S1(config)# interface vlan 1 
S1(config-if)# ip address 192.168.1.253 255.255.255.0 
S1(config-if)# no shutdown 
S1(config-if)# exit
```

### Verificação e Teste de Conectividade

Comandos de Verificação

``` Cisco
! Verificar interfaces 
S1# show ip interface brief 

! Verificar VLANs e portas 
S1# show vlan brief 

! Teste de conectividade (a partir do PC1) 
C:\> ping 192.168.1.2 
C:\> ping 192.168.1.253 
C:\> ping 192.168.1.254
```

![[Pasted image 20260929120041.png]]


### Situação-Problema: Troubleshooting

![[Pasted image 20260929120100.png]]

### Navegando entre os Modos IOS

---

``` cisco
exit 
```

Volta um nível acima na hierarquia Ex.: de config-if → retorna ao config Ex.: de config → retorna ao modo privilegiado

---

``` cisco
end / Ctrl+Z 
```

Volta direto ao modo privilegiado de qualquer lugar 
Ex.: de config-if → pula direto ao modo enable, ignorando o config

---

==Use exit quando quiser recuar passo a passo. Use end ou Ctrl+Z quando quiser sair rapidamente de qualquer subconfiguração.==

## 03 - Modelos OSI e TCP/IP

### Modelo OSI

O modelo OSI é um <strong>padrão de referência</strong> que divide a comunicação em 7 camadas independentes. Cada camada tem responsabilidades específicas e se comunica apenas com as camadas adjacentes.

PDU da camada fisicia:
- bits
- bytes
- cabos (upt, stp, fu, MM, MN)
- conectores
- hub
- 2.4 ghz

Padrao EIA/TIA:
- 568A
- 568B
- cross e direto (saber quando utiliza e qual a relacao)

Padrao RJ45
cabos de par trançado blindado e nao blindado

Categorias dos cabos 5,6,7E (quando maior o cabo maior a largura de banda)
Quando mais retorcido o cabo, maior o cancelamento. 

==Mnemônico: “Até a sua tia ri enquanto fala"==

![[Pasted image 20260929102248.png]]

![[Pasted image 20260930120851.png]]
### Modelo TCP/IP — 4 Camadas

é reduzido 

tem 4 camadas apenas 

==saber quais camadas sao aglutinadas pelo TCP do modelo OSI==

O TCP/IP é o modelo prático usado na internet. Suas 4 camadas agrupam as 7 do OSI, entender essa correspondência é fundamental para compreender como a comunicação em rede funciona.

Esse tipo de modelo corresponde à estrutura de um conjunto de protocolos específico. O modelo TCP/IP é um modelo de protocolo porque descreve as funções que ocorrem em cada camada de protocolos dentro da suíte TCP/IP O TCP/IP também é usado como um modelo de referência. 

![[Pasted image 20260930121037.png]]


![[Pasted image 20260929104451.png]]


Correspondências entre TCP/IP e OSI 
• Aplicação → camadas 5, 6 e 7 do OSI 
• Transporte → camada 4 do OSI 
• Internet (Rede) → camada 3 do OSI 
• Acesso à Rede → camadas 1 e 2 do OSI (Física + Enlace)

==O TCP/IP simplifica o modelo OSI agrupando camadas com funções semelhantes em uma única camada mais abrangente.==

Os protocolos que compõem a suíte de protocolos TCP/IP também podem ser descritos em termos do modelo de referência OSI.

No modelo OSI, a camada de acesso à rede e a camada de aplicação do modelo TCP/IP são, divididas para descrever funções discretas que devem ocorrer nessas camadas.

Na camada de acesso à rede, o suíte de protocolos TCP/IP não especifica que protocolos usar ao transmitir por um meio físico; ele descreve somente a transmissão da camada de Internet aos protocolos da rede física. As Camadas 1 e 2 do modelo OSI discutem os procedimentos necessários para acessar a mídia e o meio físico para enviar dados por uma rede.

![[Pasted image 20260930121152.png]]
## 04 - Encapsulamento e PDUs

Cada camada do modelo TCP/IP "embrulha" os dados com suas próprias informações de controle, gerando uma unidade de dados (PDU) com nome específico. Memorize o nome de cada PDU.


![[Pasted image 20260929105200.png]]

==Cada camada adiciona um cabeçalho (header) ao descer — esse processo é chamado de encapsulamento.==

### Encapsulamento e desencapsulamento

Encapsulamento e desencapsulamento são processos simétricos e opostos: um ocorre no emissor (descendo as camadas) e o outro no receptor (subindo as camadas). A prova testa se você sabe diferenciá-los.

![[Pasted image 20260929105252.png]]

- Encapsulamento (Emissor)
Dados descem pelas camadas → cada camada adiciona informações de controle

- Desencapsulamento (Receptor)
Dados sobem pelas camadas → cada camada remove seu cabeçalho

À medida que os dados da aplicação são passados pela pilha de protocolos em seu caminho para serem transmitidos pelo meio físico de várias informações de protocolos são adicionadas em cada nível- Isso é conhecido como o processo de encapsulamento.

O formato que uma parte de assume em qualquer camada é chamado de unidade de dados de (PDU)- Durante o encapsulamento a PDU que recebe da camada superior de acordo com o protocolo sendo usado.

Em cada etapa do processo, uma PDU possui um nome diferente para refletir suas novas funções Embora não haja uma convenção de nomenclatura universal para PDUs, neste curso, as PDUs são de acordo com os protocolos do conjunto TCP / IP. As PDUs para cada forrna de dados são mostradas na figura.

![[Pasted image 20260930121537.png]]


Quando as mensagens estão sendo enviadas em uma rede, o processo de encapsulamento  funciona de cima para baixo. Em cada camada, as informações da camada superior são consideradas dados encapsulados no protocolo. Por exemplo, o segmento TCP é considerado dados dentro do pacote IP.

Esse processo é revertido no host de recebimento e é conhecido como desencapsulamento. O desencapsulamento é o processo usado um dispositivo receptor para remover um ou mais cabeçalhos de protocolo. Os dados são desencapsulados à medida que se movem na pilha em direção à aplicação do usuário final.


==São processos opostos — não são sinônimos. E o encapsulamento ocorre em todas as camadas, não só na Aplicação!==

#### Sentido 

Tem que ver o sentido de quem envia e de quem recebe. 

Quando desce a o descapsulamento, Quando sobe ha o encapsulamento. 
## 05 - Meios de transmissão físicos

Cada meio físico tem características próprias de velocidade, distância, custo e imunidade a interferências. A prova compara esses meios — saiba os pontos fortes e fracos de cada um.

![[Pasted image 20260929105842.png]]

==Wireless não dispensa meio físico — o ar é o meio! Nunca escreva "sem meio físico".==

### Cabos de cobre - UTP

![[Pasted image 20260930123851.png]]
![[Pasted image 20260930123923.png]]
![[Pasted image 20260930123938.png]]

![[Pasted image 20260930123956.png]]

![[Pasted image 20260930124008.png]]

![[Pasted image 20260930124015.png]]


![[Pasted image 20260930124058.png]]

![[Pasted image 20260930124125.png]]

![[Pasted image 20260930124303.png]]

![[Pasted image 20260930124340.png]]

==O **cabo direto** (ou _straight-through_) serve para conectar **dispositivos diferentes**, como um computador a um [switch](https://www.youtube.com/watch?v=xAbJf1cVn2A) ou roteador, enquanto o **cabo crossover** (cruzado) serve para ligar **dispositivos iguais** diretamente entre si, como um computador a outro computador==


### Cabos Fibra óptica

![[Pasted image 20260930124456.png]]

![[Pasted image 20260930124510.png]]

![[Pasted image 20260930124522.png]]

![[Pasted image 20260930124528.png]]

### Sem fio 

![[Pasted image 20260930124604.png]]

![[Pasted image 20260930124612.png]]


### Meios de rede 

- Fios de metal dentro de cabos - Os dados são codificados em impulsos elétricos.
- Fibras de vidro ou plástico nos cabos (cabo de fibra óptica)- Os dados são codificados em pulsos de luz.
- Transmissão sem fio - Os dados são codificados através da modulação de frequências específicas de ondas eletromagnéticas.

## 06 - Conversão binário/decimal/hex

Em endereçamento IPv4, cada octeto é um número de 8 bits. Saber converter binário para decimal é indispensável — cada bit tem um valor posicional fixo, e a conversão é feita somando os valores dos bits que valem 1.

![[Pasted image 20260929110410.png]]

![[Pasted image 20260929110415.png]]

Identifique quais bits são 1, some seus valores posicionais e obtenha o decimal correspondente.

Para converter um número binário para decimal, você deve ==multiplicar cada dígito do binário por uma potência de 2, começando com 2⁰ no dígito mais à direita e aumentando o expoente em 1 para cada posição à esquerda, e depois somar todos os resultados==.

## 07 - Quadro ethernet e comutação

O quadro Ethernet é a unidade de dados da camada de Enlace. Cada campo tem uma função específica a prova testa se você sabe o papel do preâmbulo, dos endereços MAC, do payload e do FCS.

![[Pasted image 20260929112402.png]]

- Preâmbulo 
Sincronização— não faz parte dos dados úteis

- MAC Destino / Origem 
Endereços físicos dos dispositivos

- Dados (Payload) 
Mín. 46 bytes — Máx. 1500 bytes

- FCS 
Verifica se o quadro foi corrompido

![[Pasted image 20260930125405.png]]

---
Endereço MAC
Identificador físico gravado na placa de rede — usado pelo switch para encaminhar quadros na camada 2

---
Endereço IP
Identificador lógico configurado pelo administrador — necessário para comunicação entre redes e gerenciamento remoto

---
Por que o switch precisa de IP?
Não é para encaminhar tráfego — é para permitir acesso remoto via SSH/Telnet

---

### FCS

Verificação de Erros no Quadro

O FCS é o mecanismo de integridade do quadro Ethernet. Ele não corrige erros, apenas os detecta. Se o quadro chegou corrompido, é simplesmente descartado.

• FCS = Frame Check Sequence, campo no final do quadro Ethernet 
• O receptor recalcula o FCS e compara com o valor recebido 
• Se diferente → quadro é descartado (não corrigido!)

==O MAC de destino fica no início do quadro, não no final. E o campo de dados tem tamanho mínimo (46 B) e máximo (1500 B) definidos.==

### Comutação de Switches — Dois Métodos

O switch pode usar estratégias diferentes para encaminhar quadros. A escolha impacta diretamente a latência e a confiabilidade da transmissão.

- Store-and-Forward
Armazena o quadro inteiro antes de encaminhar 
Verifica o FCS — quadros corrompidos são descartados 
Maior confiabilidade e controle de erros 
Latência ligeiramente maior

- Cut-Through
Encaminha assim que lê o MAC de destino
Menor latência — mais rápido
Não verifica FCS — pode propagar quadros corrompidos
Não elimina completamente quadros com erro

![[Pasted image 20260930125518.png]]

![[Pasted image 20260930125626.png]]
![[Pasted image 20260930125631.png]]



### Domínio de Colisão vs. Domínio de Broadcast

Esses dois conceitos definem os limites de propagação de tráfego na rede. Switches controlam colisões; roteadores controlam broadcasts — confundir os dois é erro clássico de prova.

- Domínio de Colisão
Segmento onde dois dispositivos podem transmitir simultaneamente e causar colisão 
Cada porta de um switch é um domínio separado 
Switches segmentam domínios de colisão

- Domínio de Broadcast
Conjunto de dispositivos que recebem o mesmo broadcast 
Delimitado por roteadores
Switches não limitam broadcasts



==Switches segmentam domínios de colisão, mas não domínios de broadcast — só roteadores fazem isso!==


## Para prova

![[Pasted image 20260929114053.png]]

![[Pasted image 20260929114059.png]]

![[Pasted image 20260929114108.png]]

![[Pasted image 20260929114115.png]]
