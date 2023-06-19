from EntidadPersona import Persona
class Vendedor(Persona):
    def __init__(self, vnombres, vpaterno, vmaterno, vcorreo, vedad, vsexo, vdireccion, vciudad,vCodigoVendedor,vFechaDeContratacion):
        super().__init__(vnombres, vpaterno, vmaterno, vcorreo, vedad, vsexo, vdireccion, vciudad)
        self.__codigoVendedor=vCodigoVendedor
        self.__fechaDeContratacion=vFechaDeContratacion
    

    @property
    def datacodigovendedor(self):
        return self.__codigoVendedor
    
    @datacodigovendedor.setter
    def datacodigovendedor(self,mcodigoVendedor):
        self.__codigoVendedor=mcodigoVendedor
    
    @property
    def datafechaDeContratacion(self):
        return self.__fechaDeContratacion
    
    @datafechaDeContratacion.setter
    def datafechaDeContratacion(self,mfechaDeContratacion):
        self.__fechaDeContratacion=mfechaDeContratacion