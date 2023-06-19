import sys
sys.path.append('./CapaEntidad')
from EntidadVendedor import Vendedor as objvendedor
listaVendedor=[]

def grabarVendedor(xcodigovendedor,xnombres,xpaterno,xmaterno,xcorreo,xedad,xsexo,xdireccion,xciudad,xfechacontrato):
    objvendedor.datacodigovendedor=xcodigovendedor
    objvendedor.datanombres=xnombres
    objvendedor.datapaterno=xpaterno
    objvendedor.datamaterno=xmaterno
    objvendedor.datacorreo=xcorreo
    objvendedor.dataedad=xedad
    objvendedor.datasexo=xsexo
    objvendedor.datadireccion=xdireccion
    objvendedor.dataciudad=xciudad
    objvendedor.datafechaDeContratacion=xfechacontrato
    listaVendedor.extend([objvendedor.datacodigovendedor,objvendedor.datanombres,objvendedor.datapaterno,objvendedor.datamaterno,
                          objvendedor.datacorreo,objvendedor.dataedad,objvendedor.datasexo,objvendedor.datadireccion
                          ,objvendedor.dataciudad,objvendedor.datafechaDeContratacion])
