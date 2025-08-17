

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


