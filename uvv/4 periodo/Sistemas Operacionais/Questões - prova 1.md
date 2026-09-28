
### 1. Qual é a função de um sistema operacional?

O sistema operacional **controla o computador e gerencia seus recursos de hardware e software**, como processador, memória e periféricos. Ele também funciona como uma **interface entre o usuário e o computador**, tornando seu uso mais simples e seguro.

**Na prática:** quando você abre um programa, o SO organiza a memória, o processador e os dispositivos necessários para executá-lo.

---

### 2. O que significa o SO atuar como gerenciador de recursos?

Significa que o SO **controla e organiza o uso dos recursos do computador**, permitindo que diferentes programas utilizem processador, memória e dispositivos de E/S de maneira organizada e protegida.

**Exemplo:** dois programas querem usar a impressora. O SO controla o acesso para que um não atrapalhe o outro.

---

### 3. Qual a diferença entre sistema monoprogramável e multiprogramável?

- **Monoprogramável:** apenas um programa utiliza os recursos do sistema por vez.
    
- **Multiprogramável:** vários programas podem permanecer na memória e compartilhar os recursos do computador.
    

**Exemplo:** em um sistema multiprogramável, enquanto um programa espera uma leitura do disco, outro pode utilizar a CPU.

---

### 4. Qual a função da CPU, memória e dispositivos de E/S?

- **CPU:** executa instruções e controla as operações do sistema.
    
- **Memória:** armazena temporariamente instruções e dados utilizados pelos programas.
    
- **Dispositivos de E/S:** permitem a comunicação entre o computador e o ambiente externo, como teclado, disco, monitor e impressora.
    

**Para lembrar:**  
**CPU = executa | Memória = armazena | E/S = comunica.**

---

### 5. O que é concorrência?

É a capacidade de o sistema **gerenciar várias tarefas de forma concorrente**, alternando ou sobrepondo suas atividades de acordo com os recursos disponíveis. É um princípio fundamental dos sistemas multiprogramáveis.

**Exemplo:** ouvir música enquanto baixa um arquivo e usa o navegador.

---

### 6. Como pode existir concorrência em um sistema com um único processador?

O processador **alterna rapidamente entre os processos**. Enquanto um processo espera uma operação de E/S, outro pode utilizar a CPU. Assim, não existe execução simultânea de instruções, mas existe **execução concorrente por alternância**.

**Pegadinha:**  
Um único processador → **concorrência**, mas não necessariamente **paralelismo**.

---

### 7. Qual a diferença entre interrupção e exceção?

- **Interrupção:** é causada por um **evento externo** ao programa, como um dispositivo informando que terminou uma operação de E/S.
    
- **Exceção:** é causada pela **execução de uma instrução do próprio programa**, como uma divisão por zero.
    

**Para decorar:**

> Interrupção → evento externo → assíncrono.  
> Exceção → execução do programa → síncrono.

---

### 8. O que é uma System Call?

É uma **chamada que uma aplicação faz ao sistema operacional para solicitar um serviço do kernel**.

**Exemplo:** um programa precisa abrir um arquivo. Em vez de acessar diretamente o hardware, solicita esse serviço ao SO por meio de uma System Call.

O resumo apresenta as System Calls como uma das formas de comunicação entre aplicações e o kernel.

---

### 9. Qual a diferença entre modo usuário e modo kernel?

- **Modo usuário:** utilizado pelas aplicações, com acesso limitado aos recursos do sistema.
    
- **Modo kernel:** utilizado pelo núcleo do SO, com acesso privilegiado aos recursos e operações críticas.
    

Essa separação existe para proteger o sistema contra acessos indevidos.

**Exemplo:** um programa comum não deve poder alterar diretamente uma estrutura crítica da memória do SO.

---

### 10. Por que algumas operações são privilegiadas?

Porque algumas operações podem **comprometer a segurança e o funcionamento de todo o sistema** se forem executadas livremente por qualquer aplicação.

Por isso, ficam restritas ao **modo kernel**.

**Exemplo:** controlar determinados dispositivos ou alterar estruturas fundamentais da memória.

---

# Processos

### 11. O que é um processo?

É um **programa em execução**, juntamente com seu contexto e os recursos necessários para sua execução.

O resumo também diferencia processo de thread: o **processo é a unidade de alocação de recursos**, enquanto a thread é uma unidade de execução.

**Exemplo:** o arquivo `chrome.exe` é um programa; quando está sendo executado, temos um processo.

---

### 12. Qual a diferença entre programa e processo?

- **Programa:** conjunto de instruções armazenado, ainda sem estar necessariamente em execução.
    
- **Processo:** programa **em execução**, associado a recursos e informações de controle.
    

**Analogia:**  
Programa = receita escrita.  
Processo = alguém realmente preparando a receita.

---

### 13. O que é o BCP/PCB?

O **BCP (Bloco de Controle do Processo)** ou **PCB (Process Control Block)** é uma estrutura utilizada pelo sistema operacional para **armazenar informações de controle sobre um processo**.

Ele permite que o SO identifique e gerencie o processo, mantendo informações necessárias para sua execução e controle.

O resumo destaca que, na criação de um processo, o SO cria seu PCB e associa a ele um espaço de endereçamento.

---

### 14. Quais são os estados de um processo?

Os principais estados apresentados são:

- **Criação (New):** processo está sendo criado.
    
- **Pronto (Ready):** está preparado para executar, aguardando CPU.
    
- **Execução (Running):** está utilizando a CPU.
    
- **Espera/Bloqueado (Waiting):** aguarda algum evento, geralmente uma operação de E/S.
    
- **Terminado (Exit):** terminou sua execução.
    

**Decore o fluxo básico:**

**Criação → Pronto → Execução → Espera → Pronto → Execução → Terminado**

---

### 15. Por que um processo muda de estado?

Porque as condições necessárias para sua execução mudam.

**Exemplos:**

- Pronto → Execução: recebeu a CPU.
    
- Execução → Espera: solicitou uma operação de E/S.
    
- Espera → Pronto: a E/S terminou.
    
- Execução → Pronto: perdeu a CPU para outro processo.
    
- Execução → Terminado: terminou sua execução.
    

O objetivo é permitir que o SO gerencie a utilização da CPU e dos demais recursos de forma eficiente.

---

### 16. O que diferencia um processo CPU-bound de um I/O-bound?

**CPU-bound:** passa a maior parte do tempo utilizando a CPU, realizando muitos cálculos e poucas operações de E/S.

**I/O-bound:** passa grande parte do tempo esperando operações de entrada e saída.

**Exemplo:**

- Cálculos científicos → geralmente **CPU-bound**.
    
- Programa que realiza muitas leituras de arquivos → geralmente **I/O-bound**.
    

**Pegadinha:** I/O-bound não significa que o programa "não usa CPU"; significa que passa proporcionalmente mais tempo esperando E/S.

---

# Threads

### 17. O que é uma thread?

Uma **thread é uma unidade de execução dentro de um processo**.

Um processo pode possuir uma ou várias threads executando diferentes partes de uma aplicação de forma concorrente.

**Para decorar:**

> Processo = unidade de recursos.  
> Thread = unidade de execução.

---

### 18. Qual a diferença entre processo e thread?

O **processo** possui seu próprio espaço de endereçamento e recursos.

As **threads pertencentes ao mesmo processo compartilham o espaço de endereçamento e outros recursos**, tornando a comunicação entre elas mais simples e rápida.

|Processo|Thread|
|---|---|
|Unidade de alocação de recursos|Unidade de execução|
|Possui espaço de endereçamento próprio|Compartilha espaço do processo|
|Maior custo de criação|Menor custo de criação|
|Comunicação mais complexa|Comunicação mais simples|

---

### 19. O que significa um processo multithread?

Significa que **um único processo possui várias threads**, permitindo que diferentes partes da aplicação sejam executadas concorrentemente.

**Exemplo:** um editor de texto pode ter:

- uma thread para a interface;
    
- outra para salvar o arquivo;
    
- outra para verificar a ortografia.
    

Assim, uma tarefa pode continuar enquanto outra está ocupada.

---

### 20. Quais recursos podem ser compartilhados entre threads?

Threads do mesmo processo podem compartilhar:

- **espaço de endereçamento/memória;**
    
- **arquivos e descritores de arquivos;**
    
- **sinais;**
    
- **temporizadores;**
    
- **atributos de segurança;**
    
- outros recursos pertencentes ao processo.
    

Porém, cada thread possui seu **próprio contexto de execução**, por isso o compartilhamento de memória precisa ser controlado com mecanismos de sincronização.

---
