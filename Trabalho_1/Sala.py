import RPi.GPIO as GPIO



class Sala():
    def __init__(self,sensor_presenca, 
    sensor_fumaca, 
    sensor_janela,
    sensor_porta, 
    sensor_contagem_pessoas_entrada, 
    sensor_contagem_pessoas_saida, 
    sensor_temp,
    estado_lampada_1 = 0,
    estado_lampada_2 = 0,
    estado_ar_condicionado = 0,
    estado_projetor = 0,
    estado_alarme = 0,
    estado_sensor_presenca = 0,
    estado_sensor_fumaca = 0,
    estado_sensor_janela = 0,
    estado_sensor_porta = 0,
    estado_sensor_contagem_pessoas_entrada = 0,
    estado_sensor_contagem_pessoas_saida = 0,
    estado_sensor_temp = 0):

        self.sensor_presenca = sensor_presenca
        self.sensor_fumaca = sensor_fumaca
        self.sensor_janela = sensor_janela
        self.sensor_porta = sensor_porta
        self.sensor_contagem_pessoas_entrada = sensor_contagem_pessoas_entrada
        self.sensor_contagem_pessoas_saida = sensor_contagem_pessoas_saida
        self.sensor_temp = sensor_temp
        self.estado_lampada_1 = estado_lampada_1
        self.estado_lampada_2 = estado_lampada_2
        self.estado_ar_condicionado = estado_ar_condicionado
        self.estado_projetor = estado_projetor
        self.estado_alarme = estado_alarme
        self.estado_sensor_presenca = estado_sensor_presenca
        self.estado_sensor_fumaca = estado_sensor_fumaca
        self.estado_sensor_janela = estado_sensor_janela
        self.estado_sensor_porta = estado_sensor_porta
        self.estado_sensor_contagem_pessoas_entrada = estado_sensor_contagem_pessoas_entrada
        self.estado_sensor_contagem_pessoas_saida = estado_sensor_contagem_pessoas_saida
        self.estado_sensor_temp = estado_sensor_temp
    

    
    def setEstadoSensorFumaca(self, estado):
        self.estado_sensor_fumaca = estado
    
    def getEstadoSensorFumaca(self):
        return self.estado_sensor_fumaca
    
    def getTemperatura():
        pass
    
    def pegaEstado(self,estado):
        if (estado == 1):
            print('esta ligado')
        else:
            print('esta desligado')
    
    def manipulaLed(self,num,pos):
        # sala_1 = ConfigJson('configuracao_sala1.json')

        # print(sala_1.json['outputs'])

        # 18 - lampada-1, 23 - lampada-2, 24 - ar_condicionado, 25_Alarme
        led = [18,23,24,25]


        if(num==1): 
            GPIO.output(led[pos], GPIO.HIGH)
        else:
            GPIO.output(led[pos], GPIO.LOW)

    def sensorAlarme(self):
        alarme = [8]
        if (self.estado_sensor_fumaca == 1):
            GPIO.output(alarme, GPIO.HIGH)
            print('ALARME DISPARADO')
        else:
            GPIO.output(alarme, GPIO.LOW)
        
    def sensorFumaca(self,GPIO_IN):
        
        print('\n' + str(self.getEstadoSensorFumaca()))
        if self.getEstadoSensorFumaca() == 0:
            self.setEstadoSensorFumaca(1)
            print('\n' + str(self.getEstadoSensorFumaca()))
            print('\nsensor de fumaça ativado')
            self.sensorAlarme()
        else:
            self.setEstadoSensorFumaca(0)
            self.sensorAlarme()
            print('\nsensor de fumaça foi desativado')

    def manipulaSensores(self):
        GPIO.add_event_detect(self.sensor_fumaca, GPIO.BOTH, callback=self.sensorFumaca,bouncetime = 300)