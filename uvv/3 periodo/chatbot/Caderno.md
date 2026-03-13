
# Introdução

## O QUE É Inteligência Artificial?

Definições de IA, encontradas na literatura científica, podem ser agrupadas em quatro categorias principais:
- sistemas que pensam como humanos
- sistemas que agem como humanos
- sistemas que pensam logicamente
- sistemas que agem logicamente
#### Sistemas que pensam como humanos
Foca na capacidade de entender, aprender e raciocinar de forma semelhante à maneira como os seres humanos fazem. 

Exemplo: 
- Sistemas de visao computacional para detectar tumores
- Redes Neurais Convolucionais (CNNs) tentam replicar o pensamento humano no sentido de aprender padrões visuais em imagens médicas, assim como um médico treinado faria.
- Seu objetivo não é agir como um médico interagindo com pacientes, mas pensar como um médico.
- GPTchat , DeepSeek

#### Sistemas que agem como humanos:

Sistemas de IA que possam realizar tarefas de maneira que seriam consideradas "inteligentes" se um ser humano estivesse realizando.

O foco não é a inteligência cognitiva interna, e sim a simulação do comportamento humano.

Exemplo: Chatbots e Assistente Virtuais:
##### Sistemas que pensam x agem como humanos:
- Ele é projetado para imitar conversas humanas, não para desenvolver um pensamento autônomo e criativo.

- Ele aprende com interações anteriores, mas esse aprendizado é apenas um refinamento da comunicação, não um processo cognitivo profundo.

- Ele não tem autonomia para tomar decisões complexas como um humano, apenas responde com base no que foi programado ou aprendido superficialmente.

##### Sistemas que pensam x agem como humanos:

![[Pasted image 20260308115204.png]]

#### Sistemas que pensam logicamente: 

Sistemas que possam tomar decisões lógicas, resolver problemas e fazer inferências de maneira semelhante à lógica humana, mas de forma explícita e formalizada.

Esses sistemas usam lógica formal e regras explícitas para tomar decisões. Eles não aprendem padrões como humanos, mas aplicam regras bem definidas para chegar a uma resposta correta.

- Exemplo: Sistemas Especialistas: Programados com conhecimento de especialistas em uma área (ex: análise de crédito).

- O Prolog (Programming in Logic) é uma linguagem de programação associada à IA que se concentra em lógica formal.

Baseados em lógica simbólica: Tomam decisões com base em regras predefinidas, sem aprendizado adaptativo.

 Precisos e determinísticos: Sempre chegam a uma resposta específica com base na lógica estabelecida.
 
Não se adaptam sozinhos: Precisam de ajustes manuais para incorporar novos conhecimentos.

##### Sistemas que Pensam como humanos x Pensam logicamente :

Exemplo: Diagnóstico Médico

IA que pensa como humano: Uma rede neural treinada em imagens de raio-X aprende padrões de doenças e consegue identificar câncer de pulmão baseando-se em exemplos anteriores, como um médico faria.

IA que pensa logicamente: Segue regras como "Se o tamanho da massa for maior que 5 mm e houver calcificação irregular, então é provável que seja câncer". Ele não aprende sozinho, apenas aplica regras.

#### Sistemas que agem logicamente 

Os sistemas nesta categoria são projetados para agir de maneira a alcançar objetivos específicos, com base em raciocínio lógico e dedutivo. 

Eles não tentam imitar o pensamento humano, apenas escolhem a melhor ação possível com base em otimização matemática e regras definidas.

A diferença crucial aqui é o foco na ação, em vez de apenas no processo de pensamento.

Exemplo:
- Carro Autônomo: Um carro autônomo não pensa como um humano e não segue regras fixas, mas age de forma lógica e racional.
- Ele analisa sensores, previsão de tráfego e variáveis ambientais para escolher a melhor ação possível em tempo real.
- Ele não precisa pensar como um humano, mas age escolhendo a melhor ação com base em otimização matemática.

![[Pasted image 20260308120632.png]]

![[Pasted image 20260308120640.png]]

## ==Resto== 
# Metrica de classificacao

## Metricas de avaliacao:

São métodos ou critérios usados para medir o desempenho de um modelo de aprendizado de máquina, particularmente em tarefas de classificação.

Em problemas de classificacao, as metricas mais comuns sao:
- Accuracy, 
- Precision, 
- Recall, 
- F1-score, 
- Average Precision (AP)
- Mean Average Precision (mAP), 
- Matriz confusão

Definicao:
- Verdadeiros positivos (TP): O número de casos que o modelo previu como positivos e sao realmente positivos.
- Falsos positivos(FP): O numero de casos que o modelo previu como positivos, mas sao realmente negativos.
- Verdadeiros negativos (TN): O número de casos que o modelo previu como negativos e sao realmente negativos
- Falsos negativos (FN): O numero de casos que o modelo que previu como negativos, mas sao realmente positivos.

### Threshold (limiar)

é um valor crítico predefinido que serve como um ponto de decisão em muitos sistemas, especialmente em classificação e detecção em Inteligência Artificial (IA) e aprendizado de máquina.

Em um problema de classificação binária, o modelo de IA gera uma probabilidade de que uma instância pertença a uma determinada classe. Essa probabilidade é um valor contínuo entre 0 e 1.

O threshold é o valor que define a partir de qual ponto a classe prevista muda.
- Abaixo do Threshold: A instância é classificada como uma classe (por exemplo, "negativa").
- Acima do Threshold: A instância é classificada como outra classe (por exemplo, "positiva" ou "classe 1").
### Accuracy: 

Mede a proporção de previsões corretas (tanto verdadeiros positivos quanto verdadeiros 
negativos) em relação ao total de previsões feitas. 

Ë dado pela formula:
![[Pasted image 20260308125344.png]]

Ou seja, o número de acertos dividido pelo total de exemplos avaliados

Limitacoes:
A acurácia pode ser enganosa em conjuntos de dados desbalanceados. 

A acurácia não diferencia entre os tipos de erros (falsos positivos e falsos negativos), o que pode ser crítico em muitos problemas.

Quando usar:
Quando as classes estão bem balanceadas e o valor dos acertos de cada classe são parecidos.
Em problemas onde não há preferência por minimizar um tipo específico de erro..

### Precision: 

A precisão mede a proporção de verdadeiros positivos em relação ao total de previsões positivas feitas pelo modelo.

Ou seja, avalia a seguinte perguntar: “De todas as previsões que o modelo classificou como Positivo, quantas ele acertou?”

![[Pasted image 20260308132611.png]]

Perceba que a métrica leva em consideração os FP, mas os FN ficam de fora. Isso pode ser ruim dependendo do tipo de problema que está sendo analisado

Limitações: 
A Precisão foca apenas nas previsões positivas. Portanto, não informa sobre quantos casos positivos reais estão sendo ignorados (falsos negativos).

Quando Usar:
Quando é crucial minimizar o número de falsos positivos, por exemplo, na classificação de e-mails como spam (para evitar que e-mails legítimos sejam bloqueados).
### Recall:

Também pode ser chamada de sensitividade. O Recall mede a proporção de verdadeiros positivos em relação ao total de casos positivos reais.

Responde a pergunta: “De todos os casos que são realmente positivos, quantos o modelo acertou?”

![[Pasted image 20260308132656.png]]

Perceba que a métrica leva em consideração os FP, mas os FN ficam de fora. Isso pode ser ruim dependendo do tipo de problema que está sendo analisado

Quando usar:
Quando é crítico identificar todos os exemplos positivos, como em testes de triagem de doenças (para garantir que nenhum caso doente seja perdido).

Limitações:
O Recall ignora falsos positivos, o que pode ser problemático em situações onde esses erros também têm um custo alto.
- 100 e-mails Spam
- 10 e-maill NÃO spam
- O modelo diz que TODOS os e-mails são Spam. Pela formula:
 ![[Pasted image 20260308132733.png]]
 Segundo esta métrica, o modelo seria perfeito, apesar de ser muito ruim na pratica!!!!

### F1-score
É uma média harmônica entre o Precision e o Recall, sendo bastante útil quando busca-se avaliar tanto os FP quanto os FN do modelo.
![[Pasted image 20260308132812.png]]

Quando Usar:

O F1-score é útil quando há uma necessidade de balancear entre precisão e recall. Por exemplo, em diagnósticos médicos, um bom F1-score indica que o modelo está mantendo um equilíbrio entre não deixar de detectar casos de doença (alto recall) e não ter um número excessivo de alarmes falsos (alta precision).
Se tanto falsos positivos quanto falsos negativos tiverem consequências significativas, o F1-score ajuda a encontrar um meio-termo, mas geralmente, o recall é priorizado

Limitações:
Em base desbalanceadas, o f1-score também pode apresentar distorções.

### Matriz de Confusão:

É uma ferramenta essencial para avaliar o desempenho de um modelo de classificação. 

- Ela fornece uma representação tabular das previsões do modelo, comparando os resultados reais com os resultados previstos. 

- Para um problema de classificação, a matriz de confusão é organizada em uma tabela n X n, onde n é a quantidade de classes.

![[Pasted image 20260308133806.png]]

![[Pasted image 20260308133912.png]]
![[Pasted image 20260308133921.png]]
![[Pasted image 20260308133927.png]]
![[Pasted image 20260308133933.png]]
![[Pasted image 20260308133940.png]]

Limitações: 
À medida que o número de classes aumenta, a matriz de confusão torna-se maior e mais complexa. Para problemas de classificação com muitas classes, a matriz pode se tornar difícil de interpretar e analisar, pois haverá muitas células para considerar


Quanto maior a precisão, mais confiante o modelo está ao classificar uma amostra como Positiva. 

Quanto maior o recall, mais amostras positivas o modelo classificou corretamente como Positivas.

A métrica f1 mede o equilíbrio entre precisão e recall. Quando o valor de f1 é alto, isso significa que tanto a precisão quanto o recall são altos. Uma pontuação f1 menor significa um desequilíbrio maior entre precisão e recall.

Todas estas métricas variam de acordo com o LIMIAR (threshold) escolhido.

### Average Precision

Combina as métricas de Precision  e Recall  em diferentes pontos do threshold para fornecer uma única métrica de desempenho do modelo.

- Ele é particularmente útil em problemas onde queremos avaliar como o modelo se comporta em diferentes níveis de confiança.
- Utiliza gráfico (Precision-Recall Curve) que mostra a relação entre Precision e Recall para diferentes thresholds. 
- Precision-Recall Curve: Primeiramente, traçamos uma curva de Precision-Recall para a classe ou problema de interesse. Isso é feito calculando o precision e a recall em vários pontos diferentes (thresholds).
![[Pasted image 20260308142628.png]]
![[Pasted image 20260308142631.png]]

Cálculo

![[Pasted image 20260308142650.png]]
![[Pasted image 20260308142709.png]]
![[Pasted image 20260308142718.png]]


### mAP (Mean Average Precision):


É a média do Average Precision (AP) calculado para cada classe em um problema de classificação ou detecção de objetos.

Em problemas de múltiplas classes, a mAP dá uma visão geral do desempenho do modelo ao avaliar a precisão média em todas as classes.

Após calcular o Avarege Precision para cada classe, basta somar os valores e dividir pelo numero de classes.

![[Pasted image 20260308142758.png]]

![[Pasted image 20260308142803.png]]
![[Pasted image 20260308142807.png]]
![[Pasted image 20260308142813.png]]

# Aprendizado supervisionado

![[Pasted image 20260309183947.png]]
![[Pasted image 20260309184000.png]]

## Dados Rotulados:
![[Pasted image 20260309184251.png]]
![[Pasted image 20260309184303.png]]
![[Pasted image 20260309184329.png]]
![[Pasted image 20260309184352.png]]

###  Sobreajuste (Overfitting)

![[Pasted image 20260309184417.png]]

### Subajuste (Underfitting)

![[Pasted image 20260309184925.png]]

### Por Regressão:
![[Pasted image 20260309185056.png]]
![[Pasted image 20260309185107.png]]

## Redes Neurais CNN
![[Pasted image 20260309185136.png]]
![[Pasted image 20260309185209.png]]
![[Pasted image 20260309185225.png]]
![[Pasted image 20260309185244.png]]
