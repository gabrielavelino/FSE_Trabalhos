# FSE_Trabalhos

## Critérios de Avaliação

A avaliação será realizada seguindo os seguintes critérios:

|   ITEM    |   DETALHE  |   VALOR   |
|-----------|------------|:---------:|
|**Servidor Central**    |       |       |
|**Interface (Monitoramento)**  |   Interface gráfica (via terminal, web, etc) apresentando o estado de cada dispositivo (entradas e saídas), a temperatura, umidade e o número de pessoas ocupando o prédio sendo atualizada periodicamente.  |   1,0   |
|**Interface (Acionamento de Dispositivos)** |   Mecanismo para acionamento de lâmpadas, aparelhos de ar-condicionado e projetores individualmente ou em grupos. |   1,0   |
|**Acionamento do Alarme**   |   Mecanismo de ligar/desligar alarme e acionamento do alarme de acordo com o estado dos sensores com alerta no acionamento. |   0,5   |
|**Alarme de Incêndio**   |   Implementação da rotina de acionamento do alarme de incêncio. |   0,5   |
|**Log (CSV)**   |   Geração de Log em arquivo CSV.  |   0,5 |
|**Servidores Distribuídos**    |       |       |
|**Inicialização (Arquivo de Configuração)**    |   Correta inicialização do serviço à partir do arquivo de configuração JSON.  |   5   |
|**Leitura de Temperatura / Umidade**    |   Leitura, armazenamento e envio dos valores de temperatura / umidade por sala.  |   1   |
|**Acionamento de Dispositivos** |   Correto acionamento de lâmpadas, aparelhos de ar-condicionado e aspersor pelo comando do Servidor Central.    |   2   |
|**Estado dos Sensores** |   Correta leitura e envio (*mensagem push*) para o Servidor Central um alerta pelo acionamento dos sensores de presença / abertura de portas/janelas e sensor de fumaça.   |   3  |
|**Contagem de pessoas** |   Correta leitura dos sensores de contagem de pessoas (Por andar e Total).   |   4  |
|**Geral**    |       |       |
|**Comunicação TCP/IP**  |   Correta implementação de comunicação entre os servidores usando o protocolo TCP/IP, incluindo as mensagens do tipo *push*. |   1,5   |
|**Qualidade do Código / Execução** |   Utilização de boas práticas como o uso de bons nomes, modularização e organização em geral, bom desempenho da aplicação sem muito uso da CPU. |  1,5 |
|**Pontuação Extra** |   Qualidade e usabilidade acima da média. |   0,5   |