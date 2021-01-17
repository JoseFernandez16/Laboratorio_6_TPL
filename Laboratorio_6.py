import random
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock

class Sumas_rapidasWindow(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.contador=5
        self.en_racha=0
        self.flag_contador=False

    def iniciar(self):
        self.ids.racha.text="Racha: 0"
        self.ids.respuesta.text=''
        self.evento1=Clock.schedule_once(self.numeros_aleatorios)
        if self.flag_contador==False:
            self.evento2=Clock.schedule_interval(self.iniciar_contador,1)
            self.flag_contador=True
        else:
            self.evento2.cancel()
            self.contador=5
            self.evento2=Clock.schedule_interval(self.iniciar_contador,1)


    def numeros_aleatorios(self,dt):
        primer_numero=str(random.randint(1,99))
        segundo_numero=str(random.randint(1,99))
        self.ids.num1.text=primer_numero
        self.ids.num2.text=segundo_numero

    def iniciar_contador(self,dt):
        if self.contador>0:
            self.ids.tiempo_restante.text=str(self.contador)
            self.contador-=1
        else:
            self.ids.racha.text="Fallaste :c"
            self.ids.tiempo_restante.text='--'
            self.en_racha=0
            self.contador=5
            self.evento2.cancel()
            self.ids.num1.text=''
            self.ids.num2.text=''
            pass

    def verificar_suma(self):
        suma=int(self.ids.num1.text)+int(self.ids.num2.text)
        if suma==int(self.ids.respuesta.text):
            self.en_racha+=1
            nueva_racha="Racha: "+str(self.en_racha)
            self.ids.racha.text=nueva_racha
            self.evento2.cancel()
            self.contador=5
            self.evento2=Clock.schedule_interval(self.iniciar_contador,1)
            self.evento1=Clock.schedule_once(self.numeros_aleatorios)
            self.ids.respuesta.text=''
        else:
            self.ids.racha.text="Fallaste :c"
            self.en_racha=0
            self.evento2.cancel()
            self.ids.tiempo_restante.text='--'
            self.ids.num1.text=''
            self.ids.num2.text=''
            self.ids.respuesta.text=''
            pass


class Sumas_rapidasApp(App):
    def build(self):

        return Sumas_rapidasWindow()


if __name__=='__main__':
    Sumas_rapidasApp().run()