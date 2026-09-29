
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
#### rede ponto a ponto

O software cliente e o servidor geralmente são executados em computadores separados, mas também é possível que um computador seja usado para ambas as funções ao mesmo tempo. Em pequenas empresas e em casas, muitos computadores funcionam como servidores e clientes na rede. Esse tipo de rede é chamado de rede ponto a ponto.

![[Pasted image 20260929142908.png]]

#### Dispositivos finais

Um dispositivo final é a origem ou o destino de uma mensagem transmitida pela rede.

Os dados se originam em um dispositivo final, fluem pela rede e chegam a outro dispositivo final

![[Pasted image 20260929143001.png]]

#### Dispositivos intermediários

Dispositivos intermediários conectam os dispositivos finais individuais à rede. Eles podem conectar várias redes individuais para formar uma internetwork. Eles oferecem conectividade e asseguram que os dados fluam pela rede.

Esses dispositivos intermediários usam o endereço do dispositivo final de destino, em conjunto com as informações sobre as interconexões de rede, para determinar o caminho que as mensagens devem percorrer na rede. 

Exemplos dos dispositivos intermediários mais comuns e uma lista de funções são mostrados na figura.

![[Pasted image 20260929143103.png]]

#### Meios de rede 

- Fios de metal dentro de cabos - Os dados são codificados em impulsos elétricos.
- Fibras de vidro ou plástico nos cabos (cabo de fibra óptica)- Os dados são codificados em pulsos de luz.
- Transmissão sem fio - Os dados são codificados através da modulação de frequências específicas de ondas eletromagnéticas.


### Tipos de Redes

==A distinção entre LAN e WAN é baseada na abrangência geográfica. A prova costuma trocar os conceitos — fique atento à definição de cada tipo.==

Os dois tipos mais comuns de infraestruturas de rede são as redes locais (LANs) e as redes de longa distância (WANs). Uma LAN é uma infraestrutura de rede que fornece acesso a usuários e dispositivos finais em uma pequena área geográfica. Normalmente, uma LAN é usada em um departamento dentro de uma empresa, uma casa ou uma rede de pequenas empresas. 

Uma WAN é uma infraestrutura de rede que fomece acesso a outras redes em uma ampla área geográfica, que normalmente pertence e é gerenciada por uma corporação maior ou por um provedor de serviços de telecomunicações. 

- LAN — Local Area Network
Conecta dispositivos em uma <strong>área geográfica pequena</strong>
Ex.: escritório, escola, casa

Uma LAN é uma infraestrutura de rede que abrange uma pequena área geográfica. As LANs têm características específicas:
- LANs interconectam dispositivos finais em uma área limitada, como uma casa, uma escola, um edifício de escritórios ou um campus.
- Uma LAN é geralmente administrada por uma única organização ou pessoa. O controle administrativo é imposto no nível da rede e governa as políticas de segurança e controle de acesso.
- As LANs fornecem largura de banda de alta velocidade para dispositivos finais internos e dispositivos intermediários, conforme

- WAN — Wide Area Network
Conecta redes em <strong>áreas geograficamente distantes</strong>
Ex.: cidades, países, continentes

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

#### A internet 

A intemet é uma coleção mundial de redes interconectadas (intemetworks, ou intemet para abreviar).

Algumas LANs do exemplo são conectados entre si por meio de uma WAN- As WANs estão conectadas entre si. As WANs podem se conectar através de fios de cobre, cabos de fibra ótica e transmissões sem fio (não mostradas).


##### Intranet e extranets

Existem outros dois termos semelhantes ao termo internet: intranet e extranet.

Intranet é um termo frequentemente usado para se referir a uma conexão privada de LANs e WANs que pertence a uma organização. Uma intranet é projetada para ser acessada apenas por membros da organização, funcionários ou outras pessoas autorizadas.

Uma organização pode usar uma extranet para fomecer acesso seguro e protegido a indivíduos que trabalham para uma organização diferente, mas exigem acesso aos dados da organização. 

Aqui estão alguns exemplos de extranets:
-  Uma empresa que fornece acesso a fornecedores e contratados extemos;
- Um hospital que fornece um sistema de reservas aos médicos para que eles possam marcar consultas para seus pacientes;
- Um escritório local de educação que está fornecendo informações sobre orçamento e pessoal às escolas de seu distrito.

##### Conexões com a internet 

- Cabo - Normalmente oferecido por provedores de serviços de televisão a cabo, o sinal de dados da internet transmite no mesmo cabo que fornece televisão a cabo. Ele fornece alta largura de banda, alta disponibilidade e uma conexão sempre ativa à Internet.

- DSL - As linhas de assinante digital também fornece alta largura de banda, alta disponibilidade e uma conexão sempre ativa à Internet. O DSL funciona utilizando a linha telefônica. Em geral, usuários de pequenos escritórios e escritórios domésticos se conectam com o uso de DSL Assimétrico (ADSL), o que significa que a velocidade de download é maior que a de upload.

- Celular - O acesso celular à Internet usa uma rede de telefonia celular para se conectar. Onde quer que você possa obter um sinal de celular, você pode obter acesso à Internet por celular. O desempenho é limitado pelos recursos do telefone e da torre de celular à qual está conectado.

- Satélite - A disponibilidade do acesso à internet via satélite é um benefício nas áreas que, de outra forma, não teriam conectividade com a internet. As antenas parabólicas exigem uma linha de visão clara para o satélite.

- Conexão Discada (Dial-up) - Uma opção de baixo custo que usa qualquer linha telefônica e um modem. A baixa largura de banda fornecida por uma conexão de modem dial-up não é suficiente para grandes transferências de dados, embora seja útil para acesso móvel durante a viagem.

- Fibra óptica — Uma forma de conexão de banda larga que utiliza cabos de fibra óptica para fornecer acesso à internet de alta velocidade com velocidades de upload e download simétricas.


###### Conexões corporativas
Linha Alugada Dedicada - As linhas alugadas são circuitos reservados na rede do provedor de serviços que conectam escritórios geograficamente separados para redes privadas de voz e / ou dados. Os circuitos são alugados a uma taxa mensal ou anual.

Metro Ethernet - Isso às vezes é conhecido como Ethernet WAN- Neste módulo, vamos nos referir a ele como Metro Ethernet. As Ethernet metropolitanas estendem a tecnologia de acesso à LAN na WAN. Ethernet é uma tecnologia de LAN que você aprenderá em um módulo posterior.

DSL de negócios - O DSL comercial está disponível em vários formatos. Uma escolha popular é a linha de assinante digital simétrica (SDSL), que é semelhante à versão DSL do consumidor, mas fornece uploads e downloads nas mesmas velocidades altas

Satélite - O serviço de satélite pode fornecer uma conexão quando uma solução com fio não está disponível.

Fibra óptica — Uma forma de conexão de banda larga que utiliza cabos de fibra óptica para fornecer acesso à internet de alta velocidade com velocidades de upload e download simétricas.

##### A Rede Convergente

- Redes Separadas Tradicionais
Cada rede possuía seu próprio conjunto de regras e padrões para assegurar a comunicação bem-sucedida. Vários serviços foram executados em várias redes.

![[Pasted image 20260929144815.png]]


- **Redes convergentes**
Diferentemente das redes dedicadas, as redes convergentes são capazes de fornecer dados, voz e vídeo entre muitos tipos diferentes de dispositivos na mesma infraestrutura de rede. Essa infraestrutura de rede usa o mesmo conjunto de regras, os mesmos contratos e normas de implementação. As redes de dados convergentes transportam vários serviços em uma rede.

![[Pasted image 20260929144856.png]]

#### Redes confiáveis

- Tolerância a falhas;
Uma rede tolerante a falhas é aquela que limita o número de dispositivos afetados durante uma falha.

- Escalabilidade;
Uma rede escalável se expande rapidamente para oferecer suporte a novos usuários e aplicativos.

- Qualidade de serviço (QOS); 
- Segurança.

#### Segurança 

Vírus, worms e cavalos de Tróia - Eles contêm software ou código malicioso em execução no dispositivo do usuário.

Spyware e adware - Estes são tipos de software que são instalados no dispositivo de um usuário. O software, em seguida, coleta secretamente informações sobre o usuário.

Ataques de dia zero - Também chamados de ataques de hora zero, ocorrem no primeiro dia em que uma vulnerabilidade se toma conhecida.

Ataques de ator de ameaça - Uma pessoa mal-intencionada ataca dispositivos de usuário ou recursos de rede.

Ataques de negação de serviço - Esses ataques atrasam ou travam aplicativos e processos em um dispositivo de rede.

Interceptação de dados e roubo - Esse ataque captura informações privadas da rede de uma organização.

Roubo de identidade - Esse ataque rouba as credenciais de login de um usuário para acessar informações privadas.
##### Soluções

Estes são os componentes básicos de segurança para uma rede doméstica ou de pequeno escritório:

Antivirus e antispyware - Esses aplicativos ajudam a proteger os dispositivos finais contra a infecção por software malicioso.

Filtragem por firewall - A filtragem por firewall bloqueia o acesso não autorizado dentro e fora da rede. Isso pode incluir um sistema de firewall baseado em host que impede o acesso não autorizado ao dispositivo final ou um serviço básico de filtragem no roteador doméstico para impedir o acesso não autorizado do mundo externo à rede.


### Topologia

- Topologia física 
descreve o mundo real (cabos, posição dos equipamentos); 

Os diagramas de topologia física ilustram a localização fisica dos dispositivos intermediários e a instalação dos cabos.


- topologia lógica 
descreve como os dados fluem. São camadas de abstração diferentes e independentes.

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

###  Acessando a CLI e Modos de Operação

- Switch>
EXEC do Usuário
Acesso limitado — apenas comandos básicos de visualização

- Switch#
EXEC Privilegiado
Acesso completo — entrar com ==enable==

- Switch(config)#
Configuração Global 
Configurar o dispositivo — entrar com configure terminal

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

==Mnemônico: “Até a sua tia ri enquanto fala"==

![[Pasted image 20260929102248.png]]

### Modelo TCP/IP — 4 Camadas

O TCP/IP é o modelo prático usado na internet. Suas 4 camadas agrupam as 7 do OSI, entender essa correspondência é fundamental para compreender como a comunicação em rede funciona.

![[Pasted image 20260929104451.png]]


Correspondências entre TCP/IP e OSI 
• Aplicação → camadas 5, 6 e 7 do OSI 
• Transporte → camada 4 do OSI 
• Internet (Rede) → camada 3 do OSI 
• Acesso à Rede → camadas 1 e 2 do OSI (Física + Enlace)

==O TCP/IP simplifica o modelo OSI agrupando camadas com funções semelhantes em uma única camada mais abrangente.==


## 04 - Encapsulamento e PDUs

Cada camada do modelo TCP/IP "embrulha" os dados com suas próprias informações de controle, gerando uma unidade de dados (PDU) com nome específico. Memorize o nome de cada PDU.


![[Pasted image 20260929105200.png]]

==Cada camada adiciona um cabeçalho (header) ao descer — esse processo é chamado de encapsulamento.==

### Encapsulamento

Encapsulamento e desencapsulamento são processos simétricos e opostos: um ocorre no emissor (descendo as camadas) e o outro no receptor (subindo as camadas). A prova testa se você sabe diferenciá-los.

![[Pasted image 20260929105252.png]]

- Encapsulamento (Emissor)
Dados descem pelas camadas → cada camada adiciona informações de controle

- Desencapsulamento (Receptor)
Dados sobem pelas camadas → cada camada remove seu cabeçalho

==São processos opostos — não são sinônimos. E o encapsulamento ocorre em todas as camadas, não só na Aplicação!==
## 05 - Meios de transmissão físicos

Cada meio físico tem características próprias de velocidade, distância, custo e imunidade a interferências. A prova compara esses meios — saiba os pontos fortes e fracos de cada um.

![[Pasted image 20260929105842.png]]

==Wireless não dispensa meio físico — o ar é o meio! Nunca escreva "sem meio físico".==


## 06 - Conversão binário/decimal/hex

Em endereçamento IPv4, cada octeto é um número de 8 bits. Saber converter binário para decimal é indispensável — cada bit tem um valor posicional fixo, e a conversão é feita somando os valores dos bits que valem 1.

![[Pasted image 20260929110410.png]]

![[Pasted image 20260929110415.png]]

Identifique quais bits são 1, some seus valores posicionais e obtenha o decimal correspondente.
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
