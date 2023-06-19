class contrato(object):
    def __init__(self, vdni, vcodigoVendedor, vcodigoDeContrato, vplaca, vfechaDeContrato, vvalordelCarro):
        self.__dni=vdni
        self.__codigoVendedor=vcodigoVendedor
        self.__codigoDeContrato=vcodigoDeContrato
        self.__placa=vplaca
        self.__fechaDeContrato=vfechaDeContrato
        self.__valorDelCarro=vvalordelCarro
    
    @property
    def datadni(self):
        return self.__dni
    
    @datadni.setter
    def datadni(self,vdni):
        self.__dni=vdni
    

    @property
    def datacodigovendedor(self):
        return self.__codigoVendedor
    
    @datacodigovendedor.setter
    def datacodigovendedor(self,vcodigoVendedor):
        self.__codigoVendedor=vcodigoVendedor
    

    @property
    def datacodigocontrato(self):
        return self.__codigoDeContrato
    
    @datacodigocontrato.setter
    def datacodigocontrato(self,mcodigoContrato):
        self.__codigoDeContrato=mcodigoContrato
    

    @property
    def dataplaca(self):
        return self.__placa
    
    @dataplaca.setter
    def dataplaca(self,vplaca):
        self.__placa=vplaca
    

    @property
    def datafechaDeContrato(self):
        return self.__fechaDeContrato
    
    @datafechaDeContrato.setter
    def datafechaDeContrato(self,vfechaDeContrato):
        self.__fechaDeContrato=vfechaDeContrato
    

    @property
    def datavalordelCarro(self):
        return self.__valorDelCarro
    
    @datavalordelCarro.setter
    def datavalordelCarro(self,vvalordelCarro):
        self.__valorDelCarro=vvalordelCarro


      