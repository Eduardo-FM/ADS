## Processo de desenvolvimento de software

### 1. Modelo Cascata (_Waterfall_)

O **Modelo Cascata**, criado em 1970 por Winston W. Royce, é uma abordagem linear e sequencial (_top-down_) para a Gestão de Projetos de desenvolvimento de software. As suas etapas seguem a mesma lógica das fases descritas no guia PMBOK (iniciação, planejamento, execução, monitoramento/controle e encerramento).

#### As 5 Fases do Modelo

1. **Análise e Requisitos**: Coleta inicial de todas as especificações, serviços inclusos, limitações e objetivos do projeto. Inclui o estudo de viabilidade e a documentação inicial, permitindo que as fases subsequentes sejam planejadas de forma independente.
2. **Projeto (_Design_)**: Tradução dos requisitos definidos em um conjunto de modelos e representações abstratas para avaliar a qualidade da arquitetura antes do início da codificação.
3. **Implementação**: Tradução das representações do projeto em código de programação executável por computador.
4. **Verificação**: Focado na realização de testes estruturais (lógica interna do código) e testes funcionais (entradas e saídas esperadas). Após os testes, o produto é liberado para análise e validação do cliente.
5. **Manutenção**: Etapa em que o produto está em uso regular. Envolve a correção de _bugs_, adaptações para mudanças no ambiente externo, adequação a novas leis ou inclusão de novos requisitos de desempenho. Pode ser realizada pela equipe original ou por terceiros, reforçando a importância de manter a documentação atualizada.

#### Limitações e o Modelo Cascata Revisto

- **Rigidez de fluxo**: Projetos reais raramente seguem um fluxo puramente sequencial, e é extremamente difícil definir todos os requisitos em detalhes no início devido à incerteza natural.
- **Disponibilização tardia**: O cliente só tem acesso a uma versão executável do software em etapas muito avançadas do projeto.
- **Retorno oneroso**: No modelo tradicional, regredir a uma etapa anterior exige reiniciar todo o projeto a partir do começo. Para contornar essa fragilidade, foi criado o **Modelo Cascata Revisto**, que permite retroceder e fazer alterações com base em ocorrências durante o andamento do projeto.

#### Contribuições e Benefícios

- Serviu de fundação para diversos modelos modernos e impôs disciplina, planejamento rigoroso e gestão ao processo de desenvolvimento.
- Proporciona estabilidade no desenvolvimento, facilidade na inspeção/controle e alta facilidade administrativa por ser um modelo orientado à documentação.

---

### 2. Manifesto Ágil

A **agilidade** no desenvolvimento de software é definida como uma filosofia, ou seja, um conjunto de crenças, valores e princípios que orientam a tomada de decisões. Criado em 2001 por um grupo de 17 profissionais, o **Manifesto Ágil** surgiu para estabelecer formas mais colaborativas e eficientes de criação de software.

- Agilidade é um conjunto de crenças que guiam a tomada de decisão.
- Agilidade é uma filosofia, ou seja, um conjunto de valores e princípios.

#### Os 4 Valores do Manifesto Ágil

1. **Indivíduos e interações mais que processos e ferramentas**: Reconhece que são as pessoas que geram valor e executam estratégias, priorizando a comunicação e o alinhamento constante entre a equipe e os _stakeholders_.
2. **Software em funcionamento mais que documentação abrangente**: Prioriza o planejamento e a entrega contínua de um produto funcional dentro da janela de oportunidade do mercado, sem desperdiçar tempo em documentações excessivas.
3. **Colaboração com o cliente mais que negociação de contratos**: Foca na participação ativa do cliente ao longo de todo o desenvolvimento por meio de ciclos curtos de _feedback_.
4. **Responder a mudanças mais que seguir um plano**: Defende o uso de uma estratégia dinâmica em que o _backlog_ do produto é mantido vivo e constantemente reavaliado e repriorizado.

#### Princípios do Manifesto Ágil

- A maior prioridade é satisfazer o cliente por meio da entrega contínua e adiantada de software com valor.

- **Mudanças são bem-vindas:** Aceitar mudanças nos requisitos, mesmo tardiamente no desenvolvimento, para gerar vantagem competitiva ao cliente.

- **Frequência de entrega:** Entregar software funcionando com frequência, de poucas semanas a poucos meses, com preferência para períodos mais curtos.

- **Colaboração diária:** Pessoas de negócio e desenvolvedores devem trabalhar em conjunto diariamente durante todo o projeto.

- **Indivíduos motivados:** Construir projetos ao redor de indivíduos motivados, dando a eles o ambiente, o suporte necessário e confiança para a execução do trabalho.

- **Conversa face a face:** O método mais eficiente e eficaz de transmitir informações para e entre uma equipe de desenvolvimento é a conversa face a face.

- **Software funcionando:** Software em funcionamento é a medida primária de progresso.

- **Desenvolvimento sustentável:** Os processos ágeis promovam um ritmo sustentável, onde patrocinadores, desenvolvedores e usuários conseguem manter um ritmo constante indefinidamente.

- **Excelência técnica:** A atenção contínua à excelência técnica e ao bom design aumenta a agilidade.

- **Simplicidade:** A simplicidade — a arte de maximizar a quantidade de trabalho que não precisou ser feito — é essencial.

- **Times auto-organizáveis:** As melhores arquiteturas, requisitos e designs emergem de equipes que se auto-organizam.

- **Reflexão e ajuste:** Em intervalos regulares, a equipe reflete sobre como se tornar mais efetiva, ajustando e otimizando seu comportamento de acordo.
#### Benefícios dos Modelos Ágeis

- Aumento do desempenho da empresa e foco em resultados.
- Maior satisfação dos clientes e geração de valor progressivo.
- Redução de erros por meio da melhoria contínua e maior adaptabilidade a mudanças e inovações.

---

### 3. Framework Scrum

O **Scrum** é um framework leve e adaptativo projetado para ajudar times e organizações a gerarem valor ao resolverem problemas complexos. 

É gerencial e NÃO dita COMO o time de desenvolvimento deve realizar suas atividades, tampouco O QUE FAZER em todas as situações, pois parte do princípio de que o time tem autonomia e é auto-gerenciável.

Não garante o sucesso completo do projeto, pois depende de maior administração do projeto em suas etapas, mas garante que o trabalho é focado aos resultados de maior valor agregado. 

Requisitos importantes não ficam para o final, pois caso o projeto não seja concluído por motivos de tempo ou custo, o mais importante (prioritário) está pronto e entregue.

#### Teoria e Pilares Empíricos

Scrum emprega uma abordagem iterativa e incremental para otimizar a previsibilidade e controlar o risco. Scrum envolve grupos de pessoas que, coletivamente, possuem todas as habilidades e conhecimentos necessários para fazer o trabalho e compartilhar ou adquirir essas habilidades conforme necessário.

O Scrum fundamenta-se no **Empirismo** (o conhecimento vem da experiência) e no _**Lean thinking**_ (redução de desperdícios). Baseia-se em três pilares fundamentais:

- **Transparência**: O processo e o trabalho devem ser visíveis tanto para quem o executa quanto para quem recebe o produto.
- **Inspeção**: Avaliação constante dos artefatos e do progresso rumo às metas estabelecidas.
- **Adaptação**: Ajustes imediatos no processo ou produto quando são identificados desvios ou problemas.

#### Valores do Scrum

Compromisso, Foco, Abertura, Respeito e Coragem

O Scrum Team se compromete a atingir seus objetivos e suportar uns aos outros. Seu foco principal é o trabalho da Sprint para fazer o melhor progresso possível em direção a essas metas. O Scrum Team e seus stakeholders são abertos quanto ao trabalho e os desafios. Os membros do Scrum Team se respeitam quanto a serem pessoas capazes e independentes, e são respeitados como tal pelas pessoas com quem trabalham. Os membros do Scrum Team têm a coragem de, fazer a coisa certa e trabalhar em problemas difíceis

Esses valores orientam o Scrum Team em relação ao seu trabalho, ações e comportamento. As decisões que são tomadas, os passos dados e a forma como o Scrum é usado devem reforçar esses valores, não diminuí-los ou miná-los. Os membros do Scrum Team aprendem e exploram os valores à medida que trabalham com os eventos e artefatos do Scrum. Quando esses valores são incorporados pelo Scrum Team e pelas pessoas com quem trabalham, os pilares empíricos do Scrum de transparência, inspeção e adaptação ganham vida, construindo confiança.

#### Papéis e Responsabilidades

- **Product Owner (PO)**: Responsável por definir, ordenar e atualizar continuamente o _Product Backlog_ conforme as necessidades do cliente. Garantir que o Product Backlog seja transparente, visível e compreensível.
- **Scrum Master**: Facilitador encarregado de catalogar respostas, remover impedimentos e criar um ambiente seguro e transparente para a equipe.
- **Developers / Dev Team**: Equipe multidisciplinar, autogerenciada e responsável pela construção do incremento de software.

#### Cerimônias e Eventos Formais

- **Sprint**: O evento contêiner com duração fixa de um mês ou menos (geralmente de 2 a 4 semanas) no qual o trabalho é realizado.
- **Sprint Planning**: Reunião de planejamento (com até 4 horas de duração em Sprints de 2 semanas) para selecionar e detalhar os itens do _Product Backlog_ que comporão o _Sprint Backlog_.
- **Daily Scrum**: Reunião diária de até 15 minutos para os desenvolvedores inspecionarem o progresso em direção à Meta da Sprint e definirem o plano de ação para o dia seguinte.
- **Sprint Review**: Encontro realizado ao final da Sprint (até 4 horas para Sprints de 1 mês) para apresentar o incremento pronto aos _stakeholders_ e coletar _feedbacks_.
- **Sprint Retrospective**: Reunião de encerramento (com até 3 horas em Sprints de 1 mês ou 1 hora em Sprints de 2 semanas) para inspecionar o comportamento da equipe em relação a pessoas, processos e ferramentas, criando um plano de ação para melhorias contínuas.

#### Artefatos e seus Compromissos

- **Product Backlog**: Lista contínua e priorizada com todos os requisitos e necessidades do produto. (Compromisso: **Meta do Produto**).
- **Sprint Backlog**: Conjunto de itens selecionados do _Product Backlog_ detalhados em tarefas específicas para a execução durante a Sprint. (Compromisso: **Meta da Sprint**).
- **Incremento**: Soma de todas as funcionalidades concluídas durante a Sprint que atingiram a **Definição de Pronto** (testado, código bem escrito, executável e documentado). (Compromisso: **Definição de Pronto**).
- **Burndown Chart**: Gráfico de acompanhamento que compara visualmente o trabalho planejado com o executado ao longo do tempo.

## Qualidade de Software

Qualidade é um conceito relativo.

Diversos aspectos são levados em conta. No caso de um automóvel, fatores como conforto, segurança, desempenho, beleza e custo têm estreita relação com a qualidade.

Qualidade está fortemente relacionada à conformidade com os requisitos.

O que é “conformidade em relação a requisitos”? observado x especificado. Pode haver problemas na observação. Pode haver problemas na especificação.

Qualidade diz respeito à satisfação do cliente. Requisitos são especificados por pessoas e com o objetivo de satisfazer outras pessoas. Uma especificação depende das escolhas feitas (clientes alvo). Pode haver problemas na especificação.

### 1. Conceitos Fundamentais e Definições de Qualidade

- **Natureza Subjetiva e Relativa**: A palavra qualidade diz respeito às percepções individuais sobre um produto ou serviço, sendo fortemente influenciada por fatores culturais, necessidades e expectativas individuais.
- **Definições Formais de Autores e Normas**:
    - **NBR 8402**: É a totalidade das características de uma entidade que lhe confere a capacidade de satisfazer necessidades explícitas e implícitas.
    - **Philip B. Crosby**: Qualidade é a "conformidade com os requisitos", os quais devem ser claramente especificados sem margem para más interpretações (Foca no ==como==.
    - **Joseph Moses Juran**:  Conveniência para uso. Considera os requisitos e a expectativa do cliente. Um produto deve ter elementos que satisfaçam as diversas maneiras com que os clientes o utilizarão. (Foca no uso ==Resultado==)
    - **Roger S. Pressman**: Conformidade com requisitos funcionais e de desempenho especificados, padrões e convenções de desenvolvimento pré-estabelecidos e características implícitas esperadas em softwares profissionais.
- **Conformidade vs. Satisfação**: A conformidade avalia a relação entre o _observado vs. especificado_. Além disso, a qualidade está atrelada à satisfação das pessoas para as quais o sistema foi projetado.
- **Propósito e Prejuízos de Falhas**: A gestão da qualidade busca prevenir o retrabalho, eliminar falhas e assegurar entregas de alto valor. Estima-se que códigos mal escritos gerem perdas de US$ 85 bilhões por ano e que as equipes gastem até 40% do seu tempo corrigindo erros. Exemplos históricos de falhas incluem o HSBC (2016), TSB Bank (2018), Hospital NHS (2018), o Bug do Milênio (2000), o foguete Ariane 5 (1996) e o contador do YouTube com o vídeo Gangnam Style (2014).

---

### 2. Garantida de Qualidade

É um conjunto de atividades técnicas aplicadas durante todo o processo de desenvolvimento. 

O objetivo é garantir que tanto o processo de desenvolvimento quanto o produto de software gerado atinjam níveis de qualidade especificados.

==V & V==

Verificação: assegurar consistência, completude e corretude do produto em cada fase e entre fases consecutivas do ciclo de vida do software.
- “Estamos construindo corretamente o produto?” -> COMO

Validação: assegurar que o produto final corresponda aos requisitos do software.
- “Estamos construindo o produto certo?” -> O QUÊ

---

### 3. Ciclo de Vida de Desenvolvimento

![[Pasted image 20261005151709.png]]

---

### 4. Atividades de Garantia da Qualidade

![[Pasted image 20261005151729.png]]

---

### 5. Convertendo ideias em sonhos

Empresas nascem de uma boa ideia e da coragem de colocá-la em prática.

A partir dessa premissa, desenvolvem-se: 
- Tecnologias 
- Serviços 
- Produtos que visam transformar a vida das pessoas 
- Processos que mudam e movem o mundo


Para isso, é imprescindível formar uma cultura organizacional que preza pela ==excelência durante todo o ciclo de desenvolvimento de software.==

Além de adotar novos modelos de desenvolvimento, é preciso ==desconstruir== a ideia de que a qualidade está atrelada exclusivamente ao final do processo e a um departamento exclusivo.

==qualidade desde== o início e ao ==longo de todo o processo== de desenvolvimento de software.

- Prevenir retrabalho 
- Garantir aderência às necessidades 
- Reportar erros e verificar se foram corrigidos corretamente 
- Eliminar possíveis falhas no sistema - Garantir maior qualidade na entrega final do produto

---
### 6. Impactos Negativos

Falhas de software geram prejuízos para usuários e organizações.

---

### 7. As 5 Eras da Evolução da Qualidade

1. **1ª Era – A Era da Inspeção (Década de 1920)**: Com a produção em massa do Taylorismo e Fordismo, surge o papel do Inspetor de Qualidade. A verificação ocorria apenas _após_ o produto estar pronto, visando a uniformidade, sem foco na causa raiz dos defeitos.
2. **2ª Era – Controle Estatístico da Qualidade (Década de 1930)**: Liderada por Walter Shewhart e Joseph Juran, introduziu o uso de técnicas estatísticas, amostragem de lotes e gráficos de controle (LSC, LM, LIC) para inspecionar peças _durante_ a fabricação e estabilizar o processo.
3. **3ª Era – A Era da Garantia da Qualidade (Década de 1940 / 1954 em diante)**: Marcada pela visita de Juran ao Japão em 1954, que expandiu o controle tecnológico para uma gestão sistêmica e holística da organização. Incorporou 4 novos pilares:
    - **Quantificação dos Custos da Qualidade**: Custos de Processo (conformidade vs. não conformidade) e Custos de Produto (prevenção, avaliação, falhas internas e externas).
    - **Controle da Qualidade Total (TQC)**: Proposto por Feigenbaum em 1961, estabeleceu o foco no cliente e definiu que a qualidade é responsabilidade de todos os departamentos.
    - **Engenharia da Confiabilidade**: Identificação antecipada de falhas no ciclo de vida e envolvimento ativo do cliente.
    - **Defeito Zero**: Preconizado por Philip Crosby, defende a padronização e o esforço contínuo das pessoas para minimizar erros.
4. **4ª Era – Gestão da Qualidade Total (TQM - Década de 1980)**: A qualidade assumiu um papel **estratégico**, integrando o planejamento das empresas para garantir a sobrevivência frente à concorrência global (como o avanço japonês). Foco em melhoria contínua, atendimento a todos os _stakeholders_ e adoção de normas internacionais como a ISO.
5. **5ª Era – A Era da Indústria 4.0 (Atualidade)**: Integra a qualidade estratégica às tecnologias da Indústria 4.0, potencializando a produtividade, a flexibilidade, a redução de custos e a otimização do capital humano nas organizações.
---

### 8. As 5 Principais Abordagens da Qualidade

1. **Transcendental**: Associa qualidade à beleza, atratividade e excelência inata do produto.
2. **Baseada no Produto**: Foca na adequação ao uso (Juran, 1974) e na presença de características que agregam valor e satisfazem necessidades.
3. **Baseada na Produção**: Entende a qualidade como a conformidade rigorosa com as normas e especificações do processo produtivo.
4. **Baseada no Consumidor**: Centrada na satisfação e nas preferências individuais do usuário final.
5. **Baseada no Valor**: Avalia o equilíbrio entre desempenho, satisfação e um preço aceitável para o cliente.

---

### 9. Elementos da Gestão da Qualidade

![[Pasted image 20261005152229.png]]

---
### 10. Processo, Atividades e Papéis na Garantia da Qualidade de Software (GQS)

- **Conceito de GQS**: Conjunto de atividades técnicas aplicadas ao longo de _todo_ o ciclo de desenvolvimento para garantir a qualidade do processo e do produto final.
- **Verificação e Validação (V&V)**:
    - **Verificação**: Pergunta _"Estamos construindo corretamente o produto?"_ (foco no COMO), garantindo a consistência, completude e corretude técnica entre as fases.
    - **Validação**: Pergunta _"Estamos construindo o produto certo?"_ (foco no O QUÊ), garantindo que o software atenda às reais necessidades do cliente.
- **Atividades da Esteira de Desenvolvimento**:
    - **Documentação / Análise**: Planejamento de testes, inspeções formais, escrita em BDD + Gherkin e criação de cenários de teste.
    - **Codificação**: Suíte de testes, revisão de código-fonte, DevBox e automação de rotinas.
    - **Teste**: Execução de testes, monitoramento contínuo e análise de métricas de código e de qualidade.
    - **Homologação**: Testes de ponta a ponta (_End-to-End_ / E2E), testes de regressão e testes de aceitação do usuário.
- **Atores Envolvidos**: O processo de qualidade envolve de forma integrada o **Product Owner (PO)**, **Scrum Master**, **QA (Quality Assurance)**, **Designer**, **Dev Frontend** e **Dev Backend**.


## Qualidade do Código e Análise Estática

Qualidade vai além de “funcionar”

Um código de qualidade é compreensível, seguro e sustentável ao longo do tempo.

Um programa pode funcionar hoje e ainda ter código duplicado, lógica confusa e credenciais expostas

![[Pasted image 20261005153122.png]]

A análise estática encontra problemas antes da execução

Ela examina o código-fonte sem executar a aplicação: uma revisão automatizada e repetível.

![[Pasted image 20261005154634.png]]

O problema pode ser encontrado antes que a aplicação seja executada.


### FERRAMENTA

SonarQube transforma regras em feedback acionável

Uma plataforma de revisão automática e análise estática que ajuda equipes a acompanhar qualidade e segurança do código.

O resultado não é apenas um alerta: é uma prioridade clara para a próxima melhoria.

![[Pasted image 20261005154717.png]]

### FLUXO DE TRABALHO

O ciclo é contínuo: analisar, corrigir e repetir

![[Pasted image 20261005161515.png]]

### DEMONSTRAÇÃO

![[Pasted image 20261005161548.png]]

![[Pasted image 20261005161554.png]]

### MANUTENÇÃO

Débito técnico é o custo das escolhas adiadas

Débito técnico é o acúmulo de atalhos, bugs e code smells que torna cada mudança futura mais cara e arriscada.

O papel do SonarQube: tornar esse custo visível e ajudar a priorizar sua redução.

### Benefícios

Benefícios: qualidade incorporada ao processo

![[Pasted image 20261005161655.png]]

### 09 · CASO REAL

![[Pasted image 20261005161708.png]]

### Perguntas

### **1. Se um código funciona, por que ele ainda pode ser considerado de baixa qualidade?**

**Resposta:** Porque a qualidade de software vai muito além de apenas "funcionar". Um código pode executar suas tarefas hoje, mas ser considerado de baixa qualidade se contiver **código duplicado, lógica confusa, falta de padronização ou credenciais expostas**. Esses fatores comprometem a **legibilidade, a manutenibilidade, a segurança e a sustentabilidade** do sistema ao longo do tempo.

---

### **2. Por que é melhor identificar um problema no código antes de executar a aplicação?**

**Resposta:** Porque a **detecção antecipada** (feita via análise estática no código-fonte) permite identificar _bugs_, riscos de segurança e falhas antes que o programa seja executado ou entregue ao usuário. Quanto mais cedo o problema é encontrado no fluxo de trabalho, mais fácil, rápido e seguro é corrigi-lo.

---

### **3. Se duas funções possuem a mesma lógica, qual problema isso pode causar no futuro?**

**Resposta:** A duplicação de código torna a **manutenção mais difícil e onerosa**. Caso a regra de negócio precise ser alterada futuramente, os desenvolvedores terão que localizar e modificar múltiplos trechos. Se algum ponto for esquecido, as funções passarão a **divergir**, gerando inconsistências e _bugs_ no sistema.

---

### **4. Por que corrigir um problema hoje pode ser mais barato do que deixá-lo para depois?**

**Resposta:** Porque adiar a correção gera o chamado **débito técnico** — o acúmulo de atalhos, _code smells_ e falhas que tornam alterações futuras mais complexas. Resolver o problema imediatamente pode levar apenas **poucos minutos** enquanto ele é isolado. Deixá-lo para depois faz com que outras partes do software passem a depender daquela estrutura incorreta, exigindo **horas ou dias** de refatoração no futuro.

---

### **5. O SonarQube encontra um problema. Isso significa que o código está necessariamente “errado”? Por quê?**

**Resposta:** **Não necessariamente**. O SonarQube evidencia diferentes tipos de achados: _bugs_, _vulnerabilidades_, _duplicações_, _débito técnico_ e _code smells_. Um alerta de _code smell_ ou de padrão estilístico não significa que o programa vai falhar ao ser executado ou que esteja incorreto, mas sim que aquele trecho pode dificultar a manutenção futura ou violar boas práticas de engenharia de software.

---

### **ISO/IEC 25000**.

### **1. A Família de Normas ISO/IEC 25000 (SQuaRE)**

A **ISO/IEC 25000**, também conhecida como **SQuaRE** (_System and Software Quality Requirements and Evaluation_), fornece uma estrutura unificada para **especificar, medir e avaliar a qualidade** de produtos de software e sistemas.

Ela está estruturada em cinco divisões:

- **ISO/IEC 2500n (Gestão da Qualidade)**: Normas ISO/IEC 25000 e 25001.
- **ISO/IEC 2501n (Modelo de Qualidade)**: Normas ISO/IEC 25010 e 25012.
- **ISO/IEC 2502n (Medição de Qualidade)**: Normas ISO/IEC 25020, 25021, 25022, 25023 e 25024.
- **ISO/IEC 2503n (Requisitos de Qualidade)**: Norma ISO/IEC 25030.
- **ISO/IEC 2504n (Avaliação de Qualidade)**: Normas ISO/IEC 25040, 25041 e 25045.

---

### **2. A Norma ISO/IEC 25010**

A **ISO/IEC 25010** é a norma substituta da antiga ISO/IEC 9126. Ela define o **Modelo de Qualidade do Produto** para engenharia de software e sistemas, funcionando como modelo de referência para especificar, medir e avaliar requisitos não funcionais em todo o ciclo de vida do software.

---

### **3. As 9 Características de Qualidade na Prática**

O seminário exemplifica na prática como identificar e avaliar as características de qualidade de software:

- **Adequação Funcional**: Verifica se o sistema executa o que foi proposto a fazer (ex.: um aplicativo bancário permitir ver saldo, realizar transferências e fazer Pix).
- **Eficiência de Desempenho**: Capacidade do sistema de responder rapidamente sem consumo excessivo de recursos (ex.: carregar telas em até 2 segundos e não sobrecarregar a memória RAM/CPU).
- **Compatibilidade**: Capacidade do software de trocar informações e interagir de forma correta com outros sistemas (ex.: integração fluida entre o sistema de vendas e o de estoque).
- **Usabilidade**: Facilidade de operação e navegação sem a necessidade de treinamento prévio (ex.: achar facilmente onde realizar pagamentos ou Pix).
- **Confiabilidade**: Capacidade do sistema de se manter estável (sem quedas constantes) e de não perder dados quando ocorrem falhas.
- **Segurança**: Proteção de dados e controle de acesso para impedir que pessoas não autorizadas visualizem informações confidenciais.
- **Manutenibilidade**: Facilidade de encontrar e corrigir erros no código de forma simples e organizada, sem afetar outras partes do sistema.
- **Portabilidade**: Capacidade do software de ser executado em diferentes ambientes e dispositivos (celulares, notebooks, Windows, Linux, etc.).
- **Segurança Operacional**: Garantia de que uma falha de software durante a operação não resultará em danos físicos ou riscos materiais (ex.: a falha em um sistema de câmera de ré que não detecta um obstáculo).

---

## AUDITORIAS, INSPEÇÕES E REVISÕES DE CÓDIGO

### **1. Auditorias de Software (_Software Audits_)**

- **Base Normativa**: Baseia-se na norma **IEEE Std 1028**, referência internacional que define auditoria como uma avaliação independente da conformidade de produtos e processos em relação a regulamentos, padrões, diretrizes, planos e procedimentos.
- **Independência e Foco**: A palavra-chave é **independência**, pois a auditoria é conduzida por auditores externos à equipe de desenvolvimento. O foco reside estritamente na **conformidade** (com normas e processos) e não na qualidade técnica ou conteúdo do software.
- **O que pode ser auditado**: O padrão IEEE 1028 lista 32 exemplos de itens auditáveis, incluindo especificações, contratos, planos, projetos, relatórios, dados de testes e mídias de entrega.
- **Tipos de Auditoria**:
    - **1ª Parte**: Processo interno realizado pela própria empresa.
    - **2ª Parte**: Auditoria realizada no contexto comercial (cliente auditando o fornecedor).
    - **3ª Parte**: Auditoria conduzida por uma organização independente, focada em certificações formais (como ISO 9001).
- **Relatório de Auditoria**: O padrão exige um conteúdo mínimo no relatório, composto por propósito/escopo, organização e produtos auditados, critérios de avaliação, lista de observações (classificadas em maiores ou menores) e resumo de não conformidades.

---

### **2. Inspeções (_Fagan Inspection_)**

- **Origem Histórica**: O método foi criado por Michael Fagan (engenheiro da IBM) em 1976.
- **Definição e Papéis**: É um processo de revisão por pares formal e gerenciado, guiado por critérios inequívocos e metas quantitativas. É conduzido por papéis bem definidos: **Moderador (líder), Autor, Leitor, Revisor(es)/Inspetor(es) e Anotador/Registrador**.
- **Regra Fundamental**: Durante a reunião de inspeção, a determinação da ação corretiva para uma anomalia é obrigatória, porém **as soluções não devem ser debatidas na reunião** — o objetivo é detectar defeitos, não resolvê-los na hora.
- **Impacto**: A implementação de inspeções gera um aumento de produtividade entre **20% e 40%** ao longo do ciclo de vida do projeto. Como o retrabalho representa **44% do esforço de desenvolvimento** (decorrente principalmente de erros de requisitos, projeto e código), a detecção precoce reduz custos significativamente.

---

### **3. Revisão de Código (_Peer Review / Code Review_)**

- **Evolução**: Enquanto a Teoria de Fagan propõe um processo formal, as ferramentas modernas (GitHub, GitLab, Bitbucket) tornaram a revisão mais ágil e integrada através de _Pull Requests_ (PRs).
- **Eficácia Comprovada**:
    - Pesquisas do Google apontam a revisão de código como o **método mais eficaz para detectar defeitos**, superando testes e análise estática quando medidos isoladamente.
    - Captura entre **60% e 90% dos defeitos** antes de irem para produção.
    - Atua como uma ferramenta contínua de **mentoria e disseminação de conhecimento** para desenvolvedores juniores.
- **Boas Práticas Modernas**:
    - **Tamanho do PR**: PRs com menos de 400 linhas alteradas têm revisões de melhor qualidade, enquanto PRs com mais de 1.000 linhas acabam sendo aprovados sem revisão cuidadosa ("carimbados") em mais de 50% dos casos.
    - **Velocidade do Time**: Prioriza-se a velocidade da equipe em conjunto sobre a produtividade de um desenvolvedor isolado.
    - **Jargões do Mercado**: No ambiente de engenharia do Google, utiliza-se a sigla **CL** (_Changelist_) para Pull Request e **LGTM** (_"Looks good to me"_) para indicar aprovação.

---

### **4. Quadro Comparativo**

|Critério|Auditoria|Inspeção|Peer Review / Code Review|
|:--|:--|:--|:--|
|**Quem faz**|Auditor independente / externo|Equipe com papéis definidos|Colegas de equipe|
|**Foco**|Conformidade com normas|Detecção formal de defeitos|Qualidade do código e disseminação de conhecimento|
|**Formalidade**|Muito alta|Alta|Varia (informal a formal)|
|**Base / Origem**|IEEE 1028 / ISO 12207 / ISO 9001|Método de Fagan (1976)|Práticas de mercado (Google, GitHub)|

---


### Métricas de Qualidade de Software e Análise de Defeitos

### **1. Conceitos Fundamentais e Objetivos**

- **Métricas de Qualidade**: São medidas quantitativas que ajudam a identificar se o sistema funciona bem, onde existem falhas e quais pontos exigem melhorias.
- **Análise de Defeitos**: É o processo de identificar, investigar e analisar erros no software para entender suas causas raízes e prevenir sua reincidência.
- **Importância de Medir**: Medir permite acompanhar resultados e identificar falhas precocemente; quanto mais cedo um defeito é encontrado, menor é o custo de sua correção.

---

### **2. As 4 Métricas Principais**

1. **Densidade de Defeitos**:
    - **Fórmula**: \(\text{Densidade de Defeitos} = \frac{\text{Número de Defeitos}}{\text{Tamanho do Software}}\).
    - Indica a quantidade de falhas em relação ao porte do sistema (ex.: defeitos por KLOC — mil linhas de código). Densidades altas apontam para a necessidade de refatoração ou revisão do processo.
2. **MTTR (_Mean Time To Repair_)**:
    - **Fórmula**: \(\text{MTTR} = \frac{\text{Tempo Total Gasto nos Reparos}}{\text{Número de Reparos}}\).
    - Mede o tempo médio que a equipe leva para reparar um defeito após a sua identificação. Valores menores indicam maior rapidez na recuperação e menor tempo de indisponibilidade.
3. **Complexidade Ciclomática**:
    - **Fórmula**: \(M = E - N + 2P\) (onde \(E\) é o número de arestas, \(N\) o número de nós e \(P\) os componentes conectados).
    - Mede a quantidade de caminhos linearmente independentes no código-fonte. Quanto mais tomadas de decisão (`if/else`, laços) existirem, maior será a complexidade, dificultando os testes e a manutenção.
4. **Cobertura de Testes**:
    - **Fórmula**: \(\text{Cobertura} = \left(\frac{\text{Código Executado pelos Testes}}{\text{Código Total}}\right) \times 100\).
    - Indica a porcentagem de código percorrida pela suíte de testes. Contudo, ter **100% de cobertura não garante 100% de qualidade**, pois os testes podem passar pelo código sem validar as saídas de forma eficiente.

---

### **3. Ciclo de Vida e Integração das Métricas**

As métricas funcionam de maneira complementar em um ciclo contínuo de **Medir \(\rightarrow\) Analisar \(\rightarrow\) Melhorar \(\rightarrow\) Repetir**:

- **Detectar** (via _Densidade de Defeitos_) \(\rightarrow\) **Corrigir** (medido pelo _MTTR_) \(\rightarrow\) **Entender** (avaliando a _Complexidade Ciclomática_) \(\rightarrow\) **Prevenir** (ampliando a _Cobertura de Testes_).

---

### Perguntas

#### **Quest 1: Densidade de Defeitos**

- **Pergunta**: Um sistema possui 30 defeitos em 15 KLOC. Após uma melhoria, passou a ter 20 defeitos em 5 KLOC. A qualidade do sistema necessariamente melhorou? Justifique sua resposta.
- **Resposta**: **Não, a qualidade não melhorou**. No estado inicial, a densidade era de **2 defeitos/KLOC** (\(\frac{30}{15}\)). Após a mudança, a densidade subiu para **4 defeitos/KLOC** (\(\frac{20}{5}\)). Ou seja, proporcionalmente ao tamanho do código remanescente, a concentração de falhas **dobrou**.

---

#### **Quest 2: MTTR**

- **Pergunta**: Duas equipes encontraram 10 defeitos cada. A Equipe A possui MTTR de 2 horas, enquanto a Equipe B possui MTTR de 6 horas. Podemos afirmar que a Equipe A produz software de maior qualidade? Por quê?
- **Resposta**: **Não**. O MTTR mede apenas a **velocidade de correção** da equipe, não a qualidade inerente do código entregue. A Equipe A pode estar corrigindo rápido porque os erros são triviais ou porque faz correções superficiais, enquanto os defeitos da Equipe B podem ser mais complexos ou ter maior impacto na arquitetura.

---

#### **Quest 3: Cobertura de Testes**

- **Pergunta**: Um sistema possui 95% de cobertura de testes, mas continua apresentando vários erros em produção. Como isso é possível, se quase todo o código está sendo testado?
- **Resposta**: A cobertura indica apenas que a suíte de testes **passou pelas linhas de código**, mas não garante que as **asserções e validações do teste foram bem construídas**. Se os testes não verificarem cenários de exceção, dados reais do usuário ou regras de negócio complexas, os erros continuarão ocorrendo em produção.

---

#### **Quest 4: Complexidade Ciclomática**

- **Pergunta**: Um desenvolvedor reduziu uma função de 20 para 10 linhas, mas adicionou várias condições `if/else` dentro dela. Podemos afirmar que a complexidade do código diminuiu apenas porque ele ficou menor? Explique.
- **Resposta**: **Não**. A complexidade ciclomática é determinada pela quantidade de **caminhos de decisão independentes** no código, e não pelo número bruto de linhas. Ao adicionar mais ramificações `if/else`, a quantidade de caminhos possíveis aumentou, tornando o código mais complexo e mais difícil de testar e manter.

---

#### **Quest 5: A Pergunta "Chefão"**

- **Pergunta**: Uma equipe apresentou os seguintes resultados após seis meses (Cobertura: 95%, Complexidade ciclomática: baixa, Densidade de defeitos: baixa, MTTR: 1 hora). O gerente concluiu: _"Nosso software é definitivamente de alta qualidade."_ Essa conclusão está correta? Por quê?
- **Resposta**: **Não necessariamente**. Embora os indicadores técnicos internos sejam excelentes, a qualidade de um software também envolve a **satisfação do usuário final, usabilidade e se o produto atende às reais necessidades de negócio**. Um código impecável tecnicamente pode ser considerado sem qualidade se for inútil ou difícil de usar para o cliente final.

