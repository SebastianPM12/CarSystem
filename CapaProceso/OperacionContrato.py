import sys
sys.path.append('./CapaEntidad')
from EntidadContrato import contrato as objcontrato
listaContrato=[]
def grabarcontrato(xdni,xcodigovendedor,xcodigocontrato,xplaca,xfechadecontrato,xvalordelcarro):
    objcontrato.datadni=xdni    
    objcontrato.datacodigovendedor=xcodigovendedor
    objcontrato.datacodigocontrato=xcodigocontrato
    objcontrato.dataplaca=xplaca
    objcontrato.datafechaDeContrato=xfechadecontrato
    objcontrato.datavalordelCarro=xvalordelcarro
    listaContrato.extend([objcontrato.datadni,objcontrato.datacodigovendedor,objcontrato.datafechaDeContrato
                        ,objcontrato.dataplaca,objcontrato.datafechaDeContrato,objcontrato.datavalordelCarro])

