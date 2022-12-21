# FSE_Trabalhos

## Aluno
|Matrícula | Aluno |
| -- | -- |
| 18/0100831  |  Gabriel Avelino Freire |

## Sobre 
O objetivo desse trabalho é criar um sistema distribuído para automação de salas controlando sensores e dispositivos e monitorando em tempo real. O sistema deve ser desenvolvido para funcionar em um conjunto de placas Raspberry Pi com um servidor central responsável pelo controle e interface com o usuário e servidores distribuídos para leitura e acionamento dos dispositivos. Dentre os dispositivos envolvidos estão o monitoramento de temperatura e umidade, sensores de presença, sensores de fumaça, sensores de contagem de pessoas, sensores de abertura e fechamento de portas e janelas, acionamento de lâmpadas, aparelhos de ar-condicionado, alarme e aspersores de água em caso de incêndio.

## Componentes do Sistema
Para simplificar a implementação e logística de testes do trabalho, a quantidade de salas do prédio e o número de sensores foi reduzido a um mínimo representativo. Estarão disponíveis para teste 4 placas Raspberry Pi para executar os Servidores Distribuídos e o Servidor Central. A configuração do sistema está detalhada abaixo:
O sistema do Servidor Central será composto por:

- 01 placa Raspberry Pi 4;

O sistema do Servidor Distribuído será composto por:

- 01 Placa Raspberry Pi 4;
- 01 Sensore de Temperatura (DHT22)
- 01 Circuito de potência com 5 relés para acionametno de Lâmpadas / Aparelhos de Ar-Condicionado, etc.;
- 02 Sensores de fechamento de portas/janelas;
- 01 Sensore de presença;
- 01 Sensore de fumaça;
- 02 Sensores de Contagem de Pessoas (Cada pessoa que passa aciona o sinal do sensor por aprox. 200 ms, são 2 sensores por sala);
- 01 Alarme (Buzzer).

**Linguagem**: 
- python (versão 3)<br>

**Bibliotecas**: 
- socket
- RPi.GPIO
- threading
- time
- AdaFruit <br>

## Arquiterura de arquivos
O trabalho se encontra na pasta Trabalho_1, onde possui os arquivos para rodar o programa com conexão TC/IP, segue os arquivos: 

### Servidor Central
**server.py**: Responsável pelo servidor central, onde recebe e envia dados para o servidor distribuído para controlar os elementos dessa sala.

### Servidor Distribuído
**Sala.py**: Serve como uma classe Sala, onde passa os parâmetros da sala como leds e sensores e suas respectivas funções para manipulação de estado.

**config.py**: Esse arquivo serve para fazer o parser do JSON da configuração da sala.

**server.py**: Responsável pelo servidor distribuído, é uma classe onde envia e recebe dados do servidor central, criando um cliente para comunicação com o servidor central.

**Main.py**: Arquivo principal, onde possui a lógica principal do projeto, onde o usuário controla todos os eletrônicos e sensores daquela sala.

## Como rodar o programa 
A seguir tem os passos para rodar o programa:

```sh
Clonar o repositório:  
git clone https://github.com/gabrielavelino/FSE_Trabalhos.git
```

```sh
Mudar para a pasta:
cd .\FSE_TRABALHOS\Trabalho_1\
```

```
Enviar para a Rasp:
scp -P 13508 -r Trabalho_1 <user_>@<000.00.00.00>:~
```

```
exemplo:
scp -P 13508 -r Trabalho_1 gabrielavelino@164.41.98.16:~
```

```
Dentro da Rasp:
cd Trabalho_1
```

```
Dentro da Rasp em 1 terminal:
python3 server.py 164.41.98.16(endereço da placa)
```

```
Dentro da Rasp em outro terminal:
python3 Main.py 164.41.98.16(endereço da placa)
```

## Vídeo Apresentação
Segue o link do vídeo de apresentação:
[![Apresentaçao Trabalho 1](https://res.cloudinary.com/marcomontalbano/image/upload/v1671596115/video_to_markdown/images/youtube--tr4_Ur7tzSY-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://www.youtube.com/watch?v=tr4_Ur7tzSY)

## Informações adicionais

Não foi implementado o arquivo log dos comandos do usuário, inicializar a sala com JSON e alguns problemas de lógica com o servidor e cliente.