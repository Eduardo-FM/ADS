
...

#### Sistemas que pensam como humanos
- foca na capacidade de entender, aprender e raciocinar de forma semelhante à maneria como os seres humanos fazer.

Exemplo: 
- Sistemas de visao computacional para detectar tumores

#### Sistemas que agem como humanos:
- Sistemas de IA que possam realizar tarefas de maneira que seriam consideradas "inteligentes" se um ser humano estivesse realizando.
- O foco não é a inteligência cognitiva interna, e sim a simulacao do comportamento humano

##### Sistemas que pensam x agem como humanos:

#### Sistemas que pensam logicamente: 
- Sistemas que possam tomar decisões lógicas, resolver problemas e fazer inferências de maneira semelhante à lógica humana, mas de forma explícita e formalizada

Baseado em lógica simbolica 
Precisos e deterministicos
Nao se adaptam sozinhos

#### Sistemas que agem logicamente 

==...==
88


## Metrica de classificacao

### Metricas de avaliacao:

Sao metodos ou criterios usados para medir o desempenho de um modelo de aprendizado de maquina, particulamente em tarefas de classificacao.

Em problemas de classificacao, as metricas mais comuns sao:
- Accuracy;
- Precision
- Recall
- F1-score

Definicao:
- Verdadeiros positivos (TP): O número de casos que o modelo previu como positivos e sao realmente positivos.
- Falsos positivos(FP): O numero de casos que o modelo previu como positivos, mas sao realmente negativos.
- Verdadeiros negativos (TN): O número de casos que o modelo previu como negativos e sao realmente negativos
- Falsos negativos (FN): O numero de casos que o modelo que previu como negativos, mas sao realmente positivos.

#### Accuracy: 
mede a proporcao de previsoes corretas (tanto verdadeiros positivos, quanto verdadeiros negativos) em relacao ao total de previsoes feitas. É dado nessa formúla:

===...===

Limitacoes:
A Acracia pode ser enganosa em conjuntos de dados desbalanceados.
A Acuracia nao diferencia entre os tipos de erros (falsos positivos e falsos negativos), o que pode ser critivo em muitos problemas. 

#### Precision: 
Mede a proporcao de verdadeiros positivos em relacao ao total de previsoes positivas feitas pelo modelo.
- Ou seja, avalia a seguinte pergunta: "De todas as previsoes que o modelo classificou como positivo, quantas ele acertou?"
- Percebe que a métrica leva em consideracao os FP< mas os FN ficam de fora. Isso pode ser ruim dependendo do tipo de problema que esta sendo analisado.

#### Recall:
Tambem pode ser chamada de sentividade.
===...====