import RPi.GPIO as GPIO
from time import sleep

class Sala():
    def __init__(self,sensor_presenca, 
    sensor_fumaca, 
    sensor_janela,
    sensor_porta, 
    sensorContagemPessoasEntrada, 
    sensorContagemPessoasSaida, 
    sensor_temp,
    estadoLampada_1 = 0,
    estadoLampada_2 = 0,
    estadoArCondicionado = 0,
    estadoProjetor = 0,
    estado_alarme = 0,
    estado_sensor_presenca = 0,
    estado_sensor_fumaca = 0,
    estado_sensor_janela = 0,
    estado_sensor_porta = 0,
    estado_sensorContagemPessoasEntrada = 0,
    estado_sensorContagemPessoasSaida = 0,
    estado_sensor_temp = 0,
    estadoAlarmeSala = 0):

        self.sensor_presenca = sensor_presenca
        self.sensor_fumaca = sensor_fumaca
        self.sensor_janela = sensor_janela
        self.sensor_porta = sensor_porta
        self.sensorContagemPessoasEntrada = sensorContagemPessoasEntrada
        self.sensorContagemPessoasSaida = sensorContagemPessoasSaida
        self.sensor_temp = sensor_temp
        self.estadoLampada_1 = estadoLampada_1
        self.estadoLampada_2 = estadoLampada_2
        self.estadoArCondicionado = estadoArCondicionado
        self.estadoProjetor = estadoProjetor
        self.estado_alarme = estado_alarme
        self.estado_sensor_presenca = estado_sensor_presenca
        self.estado_sensor_fumaca = estado_sensor_fumaca
        self.estado_sensor_janela = estado_sensor_janela
        self.estado_sensor_porta = estado_sensor_porta
        self.estado_sensorContagemPessoasEntrada = estado_sensorContagemPessoasEntrada
        self.estado_sensorContagemPessoasSaida = estado_sensorContagemPessoasSaida
        self.estado_sensor_temp = estado_sensor_temp
        self.estadoAlarmeSala = estadoAlarmeSala
    

    # GETTERS AND SETTERS
    def setEstadoLampada1(self, estado):
        self.estadoLampada_1 = estado
    
    def getEstadoLampada1(self):
        return self.estadoLampada_1
    
    def setEstadoLampada2(self, estado):
        self.estadoLampada_2 = estado
    
    def getEstadoLampada2(self):
        return self.estadoLampada_2
    
    def setEstadoArCondicionado(self, estado):
        self.estadoArCondicionado = estado
    
    def getEstadoArCondicionado(self):
        return self.estadoArCondicionado
    
    def setEstadoProjetor(self, estado):
        self.estadoProjetor = estado
    
    def getEstadoProjetor(self):
        return self.estadoProjetor

    def setEstadoSensorFumaca(self, estado):
        self.estado_sensor_fumaca = estado
    
    def getEstadoSensorFumaca(self):
        return self.estado_sensor_fumaca

    def setEstadoSensorJanela(self, estado):
        self.estado_sensor_janela = estado
    
    def getEstadoSensorJanela(self):
        return self.estado_sensor_janela
    
    def setEstadoSensorPorta(self, estado):
        self.estado_sensor_porta = estado
    
    def getEstadoSensorPorta(self):
        return self.estado_sensor_porta

    def setEstadoSensorPresenca(self, estado):
        self.estado_sensor_presenca = estado
    
    def getEstadoSensorPresenca(self):
        return self.estado_sensor_presenca
    
    def setEstadoAlarmeSala(self, estado):
        self.estadoAlarmeSala = estado
    
    def getEstadoAlarmeSala(self):
        return self.estadoAlarmeSala
        
    def setEstadoSensorPessoasEntrada(self,estado):
        if estado >=0:
            self.estado_sensorContagemPessoasEntrada = estado
        

    
    def getEstadoSensorPessoasEntrada(self):
        return self.estado_sensorContagemPessoasEntrada
    
    def setEstadoSensorPessoasSaida(self,estado):
        self.estado_sensorContagemPessoasSaida = estado
    
    def getEstadoSensorPessoasSaida(self):
        return self.estado_sensorContagemPessoasSaida
    
    
    
    def estadosAparelhosON(self,pos):
        if(pos == 0):
            self.setEstadoLampada1(1)
        if(pos == 1):
            self.setEstadoLampada2(1)
        if(pos == 2):
            self.setEstadoArCondicionado(1)
        if(pos == 3):
            self.setEstadoProjetor(1)
        if(pos == 4):
            self.setEstadoLampada2(1)

    def estadosAparelhosOFF(self,pos):
        if(pos == 0):
            self.setEstadoLampada1(0)
        if(pos == 1):
            self.setEstadoLampada2(0)
        if(pos == 2):
            self.setEstadoArCondicionado(0)
        if(pos == 3):
            self.setEstadoProjetor(0)
        if(pos == 4):
            self.setEstadoLampada2(0)

    def manipulaLed(self,num,pos):
        # sala_1 = ConfigJson('configuracao_sala1.json')

        # print(sala_1.json['outputs'])

        # 18 - lampada-1, 23 - lampada-2, 24 - ar_condicionado, 25_Alarme
        led = [18,23,24,25,8]
        if(num==1): 
            GPIO.output(led[pos], GPIO.HIGH)
            self.estadosAparelhosON(pos)
        else:
            GPIO.output(led[pos], GPIO.LOW)
            self.estadosAparelhosOFF(pos)
    
    def manipulaLedSala2(self,num,pos):
        # sala_1 = ConfigJson('configuracao_sala1.json')

        # print(sala_1.json['outputs'])

        # 18 - lampada-1, 23 - lampada-2, 24 - ar_condicionado, 25_Alarme
        led = [26,19,13,6,5]
        if(num==1): 
            GPIO.output(led[pos], GPIO.HIGH)
            self.estadosAparelhosON(pos)
        else:
            GPIO.output(led[pos], GPIO.LOW)
            self.estadosAparelhosOFF(pos)
    
    def temperatura(self,dhtDevice):
                try:
                    temperature = dhtDevice.temperature
                    humidade = dhtDevice.humidade
                    print("---------- Climatiza????o da Sala ---------- \n")
                    print(f"Temp: {temperature} C    humidade: {humidade}% \n")
                    # time.sleep(2)

                except RuntimeError as error:
                    print(error.args[0])

    def alarmeSala(self):
        if (self.getEstadoAlarmeSala() == 0 and self.getEstadoSensorPresenca() == 1):
            print('\n----- Sensor Alarme da sala desligado ----\n')
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(23, GPIO.HIGH)
            print('Ligou as lampadas!')
            sleep(15)
            GPIO.output(18, GPIO.LOW)
            GPIO.output(23, GPIO.LOW)

        elif(self.getEstadoAlarmeSala() == 1):
            print('Sensor Alarme da sala ligado')
            if(self.getEstadoSensorPresenca() == 1 or self.getEstadoSensorJanela() == 1 or self.getEstadoSensorPorta() == 1):
                print('Detectado invas??o na sala')
                self.sensorAlarme()
    
    # SENSORES
    def sensorAlarme(self):
        alarme = [8]
        if (self.estado_sensor_fumaca == 1 or self.estado_sensor_porta == 1 or self.estado_sensor_janela == 1 or self.estado_sensor_presenca == 1):
            GPIO.output(alarme, GPIO.HIGH)
            print('ALARME DISPARADO')
        else:
            GPIO.output(alarme, GPIO.LOW)
    
    def sensorFumaca(self,GPIO_IN):
        
        if self.getEstadoSensorFumaca() == 0:
            self.setEstadoSensorFumaca(1)
            
            print('\nsensor de fuma??a ativado')
            self.sensorAlarme()
        else:
            self.setEstadoSensorFumaca(0)
            self.sensorAlarme()
            print('\nsensor de fuma??a foi desativado')
    
    def sensorJanela(self,GPIO_IN):
        
        if self.getEstadoSensorJanela() == 0:
            self.setEstadoSensorJanela(1)

            print('\nsensor da Janela ativado')
            
        else:
            self.setEstadoSensorJanela(0)
            print('\nsensor de Janela foi desativado')
    
    def sensorPorta(self,GPIO_IN):
        
        if self.getEstadoSensorPorta() == 0:
            self.setEstadoSensorPorta(1)
            print('\nsensor da Porta ativado')
        else:
            self.setEstadoSensorPorta(0)
            print('\nsensor de Porta foi desativado')
    
    def sensorPresenca(self,GPIO_IN):
        
        if self.getEstadoSensorPresenca() == 0:
            self.setEstadoSensorPresenca(1)
            print('\nsensor da Presenca ativado')
        else:
            self.setEstadoSensorPresenca(0)
            print('\nsensor de Presenca foi desativado')

    def sensorEntradaPessoas(self,GPIO_IN):

        self.setEstadoSensorPessoasEntrada(self.estado_sensorContagemPessoasEntrada + 1)
        print('Pessoa Entrando!')
        print('N??mero de pessoa na sala: ', self.getEstadoSensorPessoasEntrada())
        # if self.getEstadoSensorPessoasEntrada() == 0:
        #     self.setEstadoSensorPessoasEntrada(1)
        #     print('\nsensor da entrada ativado')
        # else:
        #     self.setEstadoSensorPessoasEntrada(0)
        #     print(self.getEstadoSensorPessoasEntrada())
        #     print('\nsensor de entrada foi desativado')
    
    def sensorSaidaPessoas(self,GPIO_IN):
        self.setEstadoSensorPessoasEntrada(self.estado_sensorContagemPessoasEntrada - 1)
        print('Pessoa Saindo!')
        print('N??mero de pessoa na sala: ', self.getEstadoSensorPessoasEntrada())
        # if self.getEstadoSensorPessoasSaida() == 0:
        #     self.setEstadoSensorPessoasSaida(1)
        #     print('\nsensor da saida ativado')
        # else:
        #     self.setEstadoSensorPessoasSaida(0)
        #     print('\nsensor de saida foi desativado')

    