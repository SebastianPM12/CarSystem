import sys
sys.path.append('./CapaEntidad')
from EntidadCarro import Carro as objcarro
listaCarros=[]
def grabarCarros(xplaca,xmarca,xcolor,xnumeroDeasientos,xvelocidadMaxima,xmotor,xmodelo):
    objcarro.dataplaca=xplaca
    objcarro.datamarca=xmarca
    objcarro.datacolor=xcolor
    objcarro.datanumeroDeAsientos=xnumeroDeasientos
    objcarro.datavelocidadMaxima=xvelocidadMaxima
    objcarro.datamotor=xmotor
    objcarro.datamodelo=xmodelo
    listaCarros.extend([objcarro.dataplaca,objcarro.datamarca,objcarro.datacolor,objcarro.datacolor,
                        objcarro.datanumeroDeAsientos,objcarro.datavelocidadMaxima,objcarro.datamotor,objcarro.datamodelo])
                        