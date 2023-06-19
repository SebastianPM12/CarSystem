from EntidadPersona import Persona
class Cliente(Persona):
    def __init__(self, vnombres, vpaterno, vmaterno, vcorreo, vedad, vsexo, vdireccion, vciudad,vdni):
        super().__init__(vnombres, vpaterno, vmaterno, vcorreo, vedad, vsexo, vdireccion, vciudad)
        self.__dni=vdni
    
    @property
    def datadni(self):
        return self.__dni
    
    @datadni.setter
    def datadni(self,mdni):
        self.__dni=mdni
    