

# Aula 12/08

#### Fundamentos de redes 

Redes sao classificadas de varias formas 

A mais comum é classificar por escopo geografico:
- PAN: Personal Area Network
Redes cujo escopa < 15m
Exemplo: bluetooth, infravermelho

- Lan: Local Area Network
Redes ondo o escopo <= 100m
Utilizam cabeamento metálico com cabos de pares trancados ou fibras opticas quando utilizam wi-fi, chama-se WLAN (wireless LAN)

- CAN: Campus Area Network
redes de mesmo proprietário que interliga varias LAN's em diferentes edificacoes (vários prédios em um mesmo terreno)
escopo: <= 3.000m

- MAN: Metropolitan Area Network
Redes que utilizam infraestrutura de interligacao (geralmente cabos de fibras opticas) em via pública
Escopo geografico: <= 15km
### Tipos de midias para redes locais(norma EIA/TIA 568-c)

Para redes locais sao permitidos os usos de:
- cabo de pares trancados nao blindados (UTP-unshielded twist pair)
- Cabos de pares trancados blindados 
	- FTP (Foiled twist pair (folha aluminizada))
	- SCTP (Screened twist pair(blindgem em malha))

Todos para distancias de até 100m entre a área de trabalho do usuário e o armário de telecomunicacoes 

Tambem é permitido o uso de cabo de fibras ópitcas para uso interno do armário até a área de trabalho desde que a distância nao exceda 100m e o cabo seja com fibras ópticas do tipo multimodo(Mmmf-multimode fiber)
	cabo obrigatoriamente do tipo tight(indoor)

Para interligacao de rede CAN entre prédios (interbuilding) são permitidos:

- Cabos com fibras ópticas do tipo multimodo (MMF) para distancias <= 2000m; e/ou 
- cabos com fibras ópticas do tipo monomodo(SMF) para dinstancias <= 3000m 
	todos os cabos do tipo Loose (outdoor)

#### Redes

TC: Tecommunication closed (armario de telecom) (rack)
HC: Horaizontal cabling (<= 100m)
WA: work Area (area de trabalho)

o Servidor de comunicacoes ffica na Equipament room (ER)(sala de equipamentos), ele leva o cabiamento vertical (back bone) para os outros Racks

O Rack principal é chamado me Main Cross Connect (MCC)

A norma permite que do MCC sai um HC para atender uma WA que está no mesmo andar

é no MCC quue chega o link da internet, ele entra por uma entrada de facilidades (entrance facilities)


# Aula 19/08

7 Subsistemas do cabeamento estruturado (Pode ser usado para uma ampla gama de finalidades)
- Work Area (WA)
- Horizontal Cablign (HC)
- Telecommunication room (TR)
	- Telecommonucation closet 
- Backbone Cabling 
- Equipament room(ER)
- Entrance Facilities (EF)
- Administration

a Rede externa pode ser de dois tipos:
- area 
- subterranea 



# Aula 26/08

#### Modelo OSP

HOSt A 
- Aplicacao (SW)
- apresentacao (SW)
- sessao (SW)
- transporte
- rede (HW)
- enlace (HW)
- fisica (HW)

Host B
- aplicacao 
- apresentacao
- sessao
- transpporte
- rede
- enlace
- fisica

Roteador Switch Hub (repetidor)

O host A se comunica com o B através do meio fisico, pode ser por cabeamento, wi-fi

O Hub so atua na camada fisica. O Switch trabalha na camada de enlace, ele faz isso usando o endereco MAC, atraveps do swtiching -> cadeamento, enlace, ponto -a-ponto, o switch é um equipamento de camada dois, o enlace feito pelo swtich é uma ligacao ponto-a-ponto, chaveando o mac adress.


o Switch encherga comunicao ponto-a-ponto, o switch nao consegue comunicar dispositivos em redes logicas distintas 

O roteador é um dispositivo de rede, atua na camada de rede, ele consegue roteador dados de um lado para o outro lado.

Quando o endereco IP destino nao existe dentro da rede, o pacote é encaminhado para o default gateway, ai o roteador verifica se há o endereco IP do outro lado e faz uma rota para os dados

A funcao do roteador é de fazer a interlegicao entre redes locais, ou com a web.

Para criar a comunicacao entre host autenticados/identificadas é a camada de sessao, que cria uma sessao identifica que tem um ID que tem a sessao que esta sendo feita.

As 3 camadas de cima (aplicacao, apresentacao e sessao) sao mais ligadas ao software, ja as tres ultimas sao ligadas ao hardware. A camada de transporte faz a ligacao entre as duas.

a camada de transporte separa a parte fisica, da parte do software, faz o disfarce de ambas as partes 

O protocolo IP incorpora as camadas de Rede, enlace, fisica. 

O TCP é capaz de fazer uma comunicao confiavel, ele tem um campo dados que é encapsulado dentro do IP.

Transmissoes de Streaming usando o UDP, que nao garante a entrega


