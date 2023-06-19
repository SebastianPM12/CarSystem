class Carro(object):
    def __init__(self,vplaca,vmarca,vcolor,vnumeroDeAsientos,vvelocidadMaxima,vmotor,vmodelo):
        self.__placa=vplaca
        self.__marca=vmarca
        self.__color=vcolor
        self.__numeroDeAsientos=vnumeroDeAsientos
        self.__velocidadMaxima=vvelocidadMaxima
        self.__motor=vmotor
        self.__modelo=vmodelo
    
    @property
    def dataplaca(self):
        return self.__placa
    
    @dataplaca.setter
    def dataplaca(self,mplaca):
        self.__placa=mplaca
    

    @property
    def datamarca(self):
        return self.__marca
    
    @datamarca.setter
    def datamarca(self,mmarca):
        self.__marca=mmarca
    

    @property
    def datacolor(self):
        return self.__color
    
    @datacolor.setter
    def datacolor(self,mcolor):
        self.__color=mcolor
    

    @property
    def datanumeroDeAsientos(self):
        return self.__numeroDeAsientos
    
    @datanumeroDeAsientos.setter
    def datanumeroDeAsientos(self,mnumeroDeAsientos):
        self.__numeroDeAsientos=mnumeroDeAsientos
    

    @property
    def datavelocidadMaxima(self):
        return self.__velocidadMaxima
    
    @datavelocidadMaxima.setter
    def datavelocidadMaxima(self,mvelocidadMaximas):
        self.__velocidadMaxima=mvelocidadMaximas
    


    @property
    def datamodelo(self):
        return self.__modelo
    
    @datamodelo.setter
    def datamodelo(self,mmodelo):
        self.__modelo=mmodelo
    

    @property
    def datamotor(self):
        return self.__motor
    
    @datamotor.setter
    def datamotor(self,mmotor):
        self.__motor=mmotor
    







    

