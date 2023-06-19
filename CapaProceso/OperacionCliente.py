import sys
sys.path.append('./CapaEntidad')
from EntidadCliente import Cliente as objcliente

listacliente=[]
def grabardocente(xdni,xnombres,xapellidopaterno,xapellidomaterno,xcorreo,xedad,xsexo,xdireccion):
    objcliente.datadni=xdni
    objcliente.datanombres=xnombres
    objcliente.datapaterno=xapellidopaterno
    objcliente.datamaterno=xapellidomaterno
    objcliente.datacorreo=xcorreo
    objcliente.dataedad=xedad
    objcliente.datasexo=xsexo
    objcliente.datadireccion=xdireccion
    listacliente.extend([objcliente.datadni,objcliente.datanombres,objcliente.datapaterno,objcliente.datamaterno,
                        objcliente.datacorreo,objcliente.dataedad,objcliente.datasexo,objcliente.datadireccion])