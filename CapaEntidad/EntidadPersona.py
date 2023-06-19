class Persona(object):  
    def __init__(self,vnombres,vpaterno,vmaterno,vcorreo,vedad,vsexo,vdireccion,vciudad):
        self.__correo=vcorreo 
        self.__paterno=vpaterno 
        self.__materno=vmaterno
        self.__nombres=vnombres
        self.__edad=vedad
        self.__sexo=vsexo
        self.__direccion=vdireccion
        self.__ciudad=vciudad
    @property 
    def datacorreo(self):
        return self.__correo

    @datacorreo.setter 
    def datacorreo(self,vcorreo):
        self.__correo=vcorreo
    

    @property 
    def datapaterno(self):
        return self.__paterno

    @datapaterno.setter 
    def datapaterno(self,vpaterno):
        self.__paterno=vpaterno


    @property 
    def datamaterno(self):
        return self.__materno

    @datamaterno.setter 
    def datamaterno(self,vmaterno):
        self.__materno=vmaterno

    
    @property 
    def datanombres(self):
        return self.__nombres

    @datanombres.setter 
    def datanombres(self,vnombres):
        self.__nombres=vnombres
    

    @property 
    def dataedad(self):
        return self.__edad

    @dataedad.setter 
    def dataedad(self,vedad):
        self.__edad=vedad

    
    @property 
    def datasexo(self):
        return self.__sexo

    @datasexo.setter 
    def datasexo(self,vsexo):
        self.__sexo=vsexo

    @property 
    def datadireccion(self):
        return self.__direccion

    @datadireccion.setter 
    def datadireccion(self,vdireccion):
        self.__direccion=vdireccion


    @property 
    def dataciudad(self):
        return self.__ciudad

    @dataciudad.setter 
    def dataciudad(self,vciudad):
        self.__ciudad=vciudad