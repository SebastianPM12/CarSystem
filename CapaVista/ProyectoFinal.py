from select import select
from sqlite3 import Cursor
import sys
sys.path.append('./CapaProceso')
sys.path.append('./CapaConexxion')
from Conexion import conectar
import OperacionVendedor as objvendedor
import OperacionCliente as objcliente
import OperacionContrato as objcontrato
import OperacionCarro as objcarro
import datetime 
from turtle import st
from PyQt6 import uic,QtWidgets
from PyQt6.QtWidgets import QMainWindow,QApplication,QMessageBox
from InterfazCarroFinal import Ui_MainWindow

class Final(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUi()
    
    def initUi(self):
        self.ui.mdiArea.addSubWindow(self.ui.subVentanaClientes)
        self.ui.mdiArea.addSubWindow(self.ui.subVentanaVendedores)
        self.ui.mdiArea.addSubWindow(self.ui.subVentanaCarros)
        self.ui.mdiArea.addSubWindow(self.ui.subVentanaContratos)
        ahora= datetime.datetime.now()
        self.ui.vFechaDeContratacion.setText(str(ahora.strftime('%d/%m/%Y')))
        self.ui.coFechaDeContrato.setText(str(ahora.strftime('%d/%m/%Y')))
        self.show()
        self.ui.cRegistrar.clicked.connect(self.grabarcliente)
        self.ui.cBuscar.clicked.connect(self.buscarcliente)
        self.ui.cEliminar.clicked.connect(self.eliminarcliente)
        self.ui.cActualizar.click.connect(self.actualizarcliente)
        self.ui.vRegistrar.clicked.connect(self.grabarvendedor)
        self.ui.vBuscar.clicked.connect(self.buscarvendedor)
        self.ui.vEliminar.clicked.connect(self.eliminarvendedor)
        self.ui.vActualizar.click.connect(self.actualizarvendedor)
        self.ui.bAgrabar_7.clicked.connect(self.grabarcontrato)
        self.ui.caRegistrar.clicked.connect(self.registrarCarro)
        self.ui.bAnuevo_6.clicked.connect(self.nuevocontrato)
        self.ui.caNuevo.clicked.connect(self.nuevocarro)
        self.ui.cNuevo.clicked.connect(self.nuevocliente)
        self.ui.vNuevo.clicked.connect(self.nuevovendedor)
        self.ui.caListo.clicked.connect(self.listo)


    def listo(self):
        if(self.ui.cacboMarca.currentIndex()==0):
            QMessageBox.information(self,"ERROR","INGRESE SU MARCA")
            self.ui.cacboMarca.setFocus()
        elif(self.ui.cacboMarca_2.currentIndex()==0):
            QMessageBox.information(self,"ERROR","INGRESE SU MODELO")
            self.ui.cacboMarca_2.setFocus()
        else:
            marca=self.ui.cacboMarca.itemText(self.ui.cacboMarca.currentIndex())
            año=int(self.ui.cacboMarca_2.itemText(self.ui.cacboMarca_2.currentIndex()))
            if(marca=="AUDI" and año==2021):
                self.ui.caNumeroDeAsientos.setText(str(4))
                self.ui.caVelocidad.setText("123KM/H")
                self.ui.caMotor.setText("SJ200")
                self.ui.covalorCarro.setText(str(5000))
            elif(marca=="AUDI" and año==2022):
                self.ui.caNumeroDeAsientos.setText(str(2))
                self.ui.caVelocidad.setText("150KM/H")
                self.ui.caMotor.setText("SJ500")
                self.ui.covalorCarro.setText(str(7000))
            elif(marca=="TESLA" and año==2021):
                self.ui.caNumeroDeAsientos.setText(str(2))
                self.ui.caVelocidad.setText("120KM/H")
                self.ui.caMotor.setText("GG100")
                self.ui.covalorCarro.setText(str(5000))
            elif(marca=="TESLA" and año==2022):
                self.ui.caNumeroDeAsientos.setText(str(2))
                self.ui.caVelocidad.setText("140KM/H")
                self.ui.caMotor.setText("GG500")
                self.ui.covalorCarro.setText(str(8000))
            elif(marca=="FERRARI" and año==2021):
                self.ui.caNumeroDeAsientos.setText(str(2))
                self.ui.caVelocidad.setText("180KM/H")
                self.ui.caMotor.setText("NB2222")
                self.ui.covalorCarro.setText(str(100000))
            elif(marca=="FERRARI" and año==2022):
                self.ui.caNumeroDeAsientos.setText(str(2))
                self.ui.caVelocidad.setText("200KM/H")
                self.ui.caMotor.setText("NB3333")
                self.ui.covalorCarro.setText(str(140000))
            elif(marca=="NISSAN" and año==2021):
                self.ui.caNumeroDeAsientos.setText(str(4))
                self.ui.caVelocidad.setText("100KM/H")
                self.ui.caMotor.setText("OP33")
                self.ui.covalorCarro.setText(str(3000))
            elif(marca=="NISSAN" and año==2022):
                self.ui.caNumeroDeAsientos.setText(str(4))
                self.ui.caVelocidad.setText("122KM/H")
                self.ui.caMotor.setText("OP37")
                self.ui.covalorCarro.setText(str(5300))

    
    def nuevocontrato(self):
        self.ui.cDni3.setText("")
        self.ui.vCodigo3.setText("")
        self.ui.coCodigo.setText("")
        self.ui.caPlaca2.setText("")
        self.ui.covalorCarro.setText("")
        self.ui.coFechaDeContrato.setText("")


    def nuevocarro(self):
        self.ui.caPlaca.setText("")
        self.ui.cacboMarca.setCurrentIndex(0)
        self.ui.cacboMarca_2.setCurrentIndex(0)
        self.ui.cacboMarca_3.setCurrentIndex(0)
        self.ui.caNumeroDeAsientos.setText("")
        self.ui.caVelocidad.setText("")
        self.ui.caMotor.setText("")
        self.ui.caPlaca.setFocus()
    
    def nuevovendedor(self):
        self.ui.vCodigo.setText("")
        self.ui.vPaterno.setText("")
        self.ui.vMaterno.setText("")
        self.ui.vNombres.setText("")
        self.ui.vFechaDeContratacion.setText("")
        self.ui.vspinBoxEdad.setValue(0)
        self.ui.vcboSex.setCurrentIndex(0)
        self.ui.vDireccion.setText("")
        self.ui.vCiudad.setText("")
        self.ui.vCorreo.setText("")
        self.listadoVendedor()
        self.ui.vCodigo.setFocus()
    
    def nuevocliente(self):
        self.ui.cNombres.setText("")
        self.ui.cPaterno.setText("")
        self.ui.cMaterno.setText("")
        self.ui.ccomboBoxSex.setCurrentIndex(0)
        self.ui.cDni.setText("")
        self.ui.cCiudad.setText("")
        self.ui.cCorreo.setText("")
        self.ui.caspinBoxEdad.setValue(0)
        self.ui.cDireccion.setText("")
        self.listadoVendedor()
        self.ui.cNombres.setFocus()
    

    def registrarCarro(self):
        try:
            mplaca=self.ui.caPlaca.text()
            mmarca=self.ui.cacboMarca.itemText(self.ui.cacboMarca.currentIndex())
            mmodelo=self.ui.cacboMarca_2.itemText(self.ui.cacboMarca_2.currentIndex())
            mcolor=self.ui.cacboMarca_3.itemText(self.ui.cacboMarca_3.currentIndex())
            masientos=int(self.ui.caNumeroDeAsientos.text())
            velocidad=self.ui.caVelocidad.text()
            mvelocidad=velocidad+"Km"
            mmotor=self.ui.caMotor.text()
            objcarro.grabarCarros(mplaca,mmarca,mmodelo,mcolor,masientos,mvelocidad,mmotor)
            with conectar.cursor() as cursor:
                cursor.execute('{call InsertCarro(?,?,?,?,?,?,?)}',(objcarro.listaCarros[0],objcarro.listaCarros[1],objcarro.listaCarros[2],objcarro.listaCarros[3],
                                objcarro.listaCarros[4],objcarro.listaCarros[5],objcarro.listaCarros[6]))
                objcarro.listaCarros.clear()
                QMessageBox.information(self,"Registro","DATOS DEL CARRO REGISTRADO")
        except Exception as error:
            QMessageBox.information(self,"ERROR EN REGISTRO", error)

    def grabarcontrato(self):
        try:
            vdni=int(self.ui.cDni3.text())
            vcodigo=self.ui.vCodigo3.text()
            vcodigocontrato=self.ui.coCodigo.text()
            vplaca=self.ui.caPlaca2.text()
            vvalorcarro=float(self.ui.covalorCarro.text())
            vfechacontrato=self.ui.coFechaDeContrato.text()
            objcontrato.grabarcontrato(vdni,vcodigo,vcodigocontrato,vplaca,vfechacontrato,vvalorcarro)
            with conectar.cursor() as cursor:
                cursor.execute('{call InsertContrato(?,?,?,?,?,?)}',(objcontrato.listaContrato[0],objcontrato.listaContrato[1],objcontrato.listaContrato[2],objcontrato.listaContrato[3]
                ,objcontrato.listaContrato[4],objcontrato.listaContrato[5]))
                objcliente.listacliente.clear()
                QMessageBox.information(self,"Registro","DATOS DEL CONTRATO REGISTRADO")
        except Exception as error:
            QMessageBox.information(self,"ERROR EN REGISTRO", error)


    def grabarcliente(self):
        try:
            valordni=int(self.ui.cDni.text())
            valornombre=self.ui.cNombres.text().upper()
            valorpaterno=self.ui.cPaterno.text().upper()
            valormaterno=self.ui.cMaterno.text().upper()
            valorcorreo=self.ui.cCorreo.text()
            valoredad=int(self.ui.caspinBoxEdad.value())
            valorsexo=self.ui.ccomboBoxSex.itemText(self.ui.ccomboBoxSex.currentIndex())
            valordireccion=self.ui.cDireccion.text()
            valorciudad=self.ui.cCiudad.text().upper()
            objcliente.grabardocente(valordni,valornombre,valorpaterno,valormaterno,valorcorreo,valoredad
                                    ,valorsexo,valordireccion,valorciudad)
            with conectar.cursor() as cursor:
                cursor.execute('{call InsertCliente(?,?,?,?,?,?,?,?,?)}',(objcliente.listacliente[0],objcliente.listacliente[1],objcliente.listacliente[2],objcliente.listacliente[3]
                ,objcliente.listacliente[4],objcliente.listacliente[5],objcliente.listacliente[6],objcliente.listacliente[7],objcliente.listacliente[8]))
                objcliente.listacliente.clear()
                self.ui.tableWidget.clearContents()
                self.listadoCliente()
                QMessageBox.information(self,"Registro","DATOS DEL CLIENTE REGISTRADO")
                self.nuevocliente
        except Exception as error:
            QMessageBox.information(self,"ERROR EN INGRESO", error)
    
    def grabarvendedor(self):
        try:
            mnombres=self.ui.vNombres.text()
            mcodigo=self.ui.vCodigo.text()
            mpaterno=self.ui.vPaterno.text()
            mmaterno=self.ui.vMaterno.text()
            medad=int(self.ui.vspinBoxEdad.value())
            msexo=self.ui.vcboSex.itemText(self.ui.vcboSex.currentIndex())
            mdireccion=self.ui.vDireccion.text()
            mciudad=self.ui.vCiudad.text()
            mcorreo=self.ui.vCorreo.text()
            mfecha=self.ui.vFechaDeContratacion.text()
            objvendedor.grabarVendedor(mnombres,mcodigo,mpaterno,mmaterno,medad,msexo,mdireccion,mdireccion,mciudad,mcorreo,mfecha)
            with conectar.cursor() as cursor:
                cursor.execute('{call InsertVendedor(?,?,?,?,?,?,?,?,?,?)}',(objvendedor.listaVendedor[0],objvendedor.listaVendedor[1],objvendedor.listaVendedor[2],objvendedor.listaVendedor[3]
                ,objvendedor.listaVendedor[4],objvendedor.listaVendedor[5],objvendedor.listaVendedor[6],objvendedor.listaVendedor[7],objvendedor.listaVendedor[8],objvendedor.listaVendedor[9]))
            objvendedor.listaVendedor.clear()
            self.ui.tableWidget_2.clearContents()
            self.listadoVendedor()
            QMessageBox.information(self,"Registro","DATOS DEL VENDEDOR REGISTRADO")
            self.nuevovendedor
        except Exception as error:
            QMessageBox.information(self,"ERROR EN INGRESO", error)
    

    def listadoCliente(self):
        try: 
            with conectar.cursor() as cursor:
                cursor.execute("EXEC ListadoCliente")
                lista_cliente=cursor.fetchall()
                indicefila=0
                for data in lista_cliente:
                    self.ui.tableWidget.insertRow(indicefila)
                    self.ui.tableWidget.setItem(indicefila,0,QtWidgets.QTableWidget(str(data[0])))
                    self.ui.tableWidget.setItem(indicefila,0,QtWidgets.QTableWidget(data[1]))
                    self.ui.tableWidget.setItem(indicefila,0,QtWidgets.QTableWidget(data[2]))
                    self.ui.tableWidget.setItem(indicefila,0,QtWidgets.QTableWidget(data[3]))
                    self.ui.tableWidget.setItem(indicefila,0,QtWidgets.QTableWidget(data[4]))
                    self.ui.tableWidget.setItem(indicefila,0,QtWidgets.QTableWidget(str(data[5])))
                    self.ui.tableWidget.setItem(indicefila,0,QtWidgets.QTableWidget(data[6]))
                    self.ui.tableWidget.setItem(indicefila,0,QtWidgets.QTableWidget(data[7]))
                    self.ui.tableWidget.setItem(indicefila,0,QtWidgets.QTableWidget(data[8]))
                    indicefila+=1
        except Exception as error:
            QMessageBox.information(self,"ERROR DE LISTADO", error)
    
    def listadoVendedor(self):
        try:
            with conectar.cursor() as cursor:
                cursor.execute("EXEC ListadoVendedor")
                lista_vendedor=cursor.fetchall()
                inidicefile=0
                for data in lista_vendedor:
                    self.ui.tableWidget_2.insertRow(inidicefile)
                    self.ui.tableWidget_2.setItem(inidicefile,0,QtWidgets.QTableWidget(data[0]))
                    self.ui.tableWidget_2.setItem(inidicefile,0,QtWidgets.QTableWidget(data[1]))
                    self.ui.tableWidget_2.setItem(inidicefile,0,QtWidgets.QTableWidget(data[2]))
                    self.ui.tableWidget_2.setItem(inidicefile,0,QtWidgets.QTableWidget(data[3]))
                    self.ui.tableWidget_2.setItem(inidicefile,0,QtWidgets.QTableWidget(str(data[4])))
                    self.ui.tableWidget_2.setItem(inidicefile,0,QtWidgets.QTableWidget(data[5]))
                    self.ui.tableWidget_2.setItem(inidicefile,0,QtWidgets.QTableWidget(data[6]))
                    self.ui.tableWidget_2.setItem(inidicefile,0,QtWidgets.QTableWidget(data[7]))
                    self.ui.tableWidget_2.setItem(inidicefile,0,QtWidgets.QTableWidget(data[8]))
                    self.ui.tableWidget_2.setItem(inidicefile,0,QtWidgets.QTableWidget(data[9]))
                    inidicefile+=1
        except Exception as error:
            QMessageBox.information(self,"ERROR DE LISTADO", error)

    def buscarcliente(self):
        try: 
            with conectar.cursor() as cursor:
                cursor.execute('{CALL SelectCliente(?)}',(int(self.ui.cDni2.text)))
                buscar_cliente=cursor.fetchall()
                indicefila=0
                self.ui.tableWidget.clearContents()
                for data in buscar_cliente:
                    self.ui.tableWidget.insertRow(indicefila)
                    self.ui.tableWidget.setItem(indicefila,0,QtWidgets.QTableWidget(str(data[0])))
                    self.ui.tableWidget.setItem(indicefila,0,QtWidgets.QTableWidget(data[1]))
                    self.ui.tableWidget.setItem(indicefila,0,QtWidgets.QTableWidget(data[2]))
                    self.ui.tableWidget.setItem(indicefila,0,QtWidgets.QTableWidget(data[3]))
                    self.ui.tableWidget.setItem(indicefila,0,QtWidgets.QTableWidget(data[4]))
                    self.ui.tableWidget.setItem(indicefila,0,QtWidgets.QTableWidget(str(data[5])))
                    self.ui.tableWidget.setItem(indicefila,0,QtWidgets.QTableWidget(data[6]))
                    self.ui.tableWidget.setItem(indicefila,0,QtWidgets.QTableWidget(data[7]))
                    self.ui.tableWidget.setItem(indicefila,0,QtWidgets.QTableWidget(data[8]))
                    indicefila+=1
                    self.ui.cDni.setText(data[0])
                    self.ui.cNombres.setText(data[1])
                    self.ui.cPaterno.setText(data[2])
                    self.ui.cMaterno.setText(data[3])
                    self.ui.cCorreo.setText(data[4])
                    self.ui.caspinBoxEdad.setValue(data[5])
                    self.ui.ccomboBoxSex.setCurrentIndex(data[6])
                    self.ui.cDireccion.setText(data[7])
                    self.ui.cCiudad.setText(data[8])
        except Exception as error:
            QMessageBox.information(self,"ERROR DE BUSQUEDA", error)
    

    def buscarvendedor(self):
        try: 
            with conectar.cursor() as cursor:
                cursor.execute('{CALL SelectCliente(?)}',(int(self.ui.vCodigo2.text)))
                buscar_vendedor=cursor.fetchall()
                indicefila=0
                self.ui.tableWidget_2.clearContents()
                for data in buscar_vendedor:
                    self.ui.tableWidget_2.insertRow(indicefila)
                    self.ui.tableWidget_2.setItem(indicefila,0,QtWidgets.QTableWidget(data[0]))
                    self.ui.tableWidget_2.setItem(indicefila,0,QtWidgets.QTableWidget(data[1]))
                    self.ui.tableWidget_2.setItem(indicefila,0,QtWidgets.QTableWidget(data[2]))
                    self.ui.tableWidget_2.setItem(indicefila,0,QtWidgets.QTableWidget(data[3]))
                    self.ui.tableWidget_2.setItem(indicefila,0,QtWidgets.QTableWidget(str(data[4])))
                    self.ui.tableWidget_2.setItem(indicefila,0,QtWidgets.QTableWidget(data[5]))
                    self.ui.tableWidget_2.setItem(indicefila,0,QtWidgets.QTableWidget(data[6]))
                    self.ui.tableWidget_2.setItem(indicefila,0,QtWidgets.QTableWidget(data[7]))
                    self.ui.tableWidget_2.setItem(indicefila,0,QtWidgets.QTableWidget(data[8]))
                    self.ui.tableWidget_2.setItem(indicefila,0,QtWidgets.QTableWidget(data[9]))
                    indicefila+=1
                    self.ui.vNombres.setText(data[0])
                    self.ui.vCodigo.setText(data[1])
                    self.ui.vPaterno.setText(data[2])
                    self.ui.vMaterno.setText(data[3])
                    self.ui.vspinBoxEdad.setValue(data[4])
                    self.ui.vcboSex.setCurrentIndex(data[5])
                    self.ui.vDireccion.setText(data[6])
                    self.ui.vCiudad.setText(data[7])
                    self.ui.vCorreo.setText(data[8])
                    self.ui.vFechaDeContratacion.setText(data[9])
        except Exception as error:
            QMessageBox.information(self,"ERROR DE BUSQUEDA", error)        
    
    def actualizarcliente(self):
        opcionactualizar=QMessageBox.question(self,"ACTUALIZAR","ACTUALIZAR DATOS DEL DOCENTE?",
                        QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No,QMessageBox.StandardButton.Yes)
        if opcionactualizar==QMessageBox.StandardButton.Yes:
            try:
                valordni=int(self.ui.cDni.text())
                valornombre=self.ui.cNombres.text().upper()
                valorpaterno=self.ui.cPaterno.text().upper()
                valormaterno=self.ui.cMaterno.text().upper()
                valorcorreo=self.ui.cCorreo.text()
                valoredad=int(self.ui.caspinBoxEdad.value())
                valorsexo=self.ui.ccomboBoxSex.itemText(self.ui.ccomboBoxSex.currentIndex())
                valordireccion=self.ui.cDireccion.text()
                valorciudad=self.ui.cCiudad.text().upper()
                with conectar.cursor() as cursor:
                    cursor.execute('{call UpdateCliente(?,?,?,?,?,?,?,?,?)}',(valordni,valornombre,valorpaterno,valormaterno,valorcorreo,
                    valoredad,valorsexo,valordireccion,valorciudad))
                    conectar.commit
                    self.nuevocliente()
                    QMessageBox.information(self,"Registro","DATOS DEL CLIENTE ACTUALIZADO")
            except Exception as error:
                QMessageBox.information(self,"ERROR EN ACTUALIZAR", error)
    
    
    def actualizarvendedor(self):
        opcionactualizar=QMessageBox.question(self,"ACTUALIZAR","ACTUALIZAR DATOS DEL DOCENTE?",
                        QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No,QMessageBox.StandardButton.Yes)
        if opcionactualizar==QMessageBox.StandardButton.Yes:
            try:
                mnombres=self.ui.vNombres.text()
                mcodigo=self.ui.vCodigo.text()
                mpaterno=self.ui.vPaterno.text()
                mmaterno=self.ui.vMaterno.text()
                medad=int(self.ui.vspinBoxEdad.value())
                msexo=self.ui.vcboSex.itemText(self.ui.vcboSex.currentIndex())
                mdireccion=self.ui.vDireccion.text()
                mciudad=self.ui.vCiudad.text()
                mcorreo=self.ui.vCorreo.text()
                mfecha=self.ui.vFechaDeContratacion.text()
                with conectar.cursor() as cursor:
                    cursor.execute('{call UpdateVendedor(?,?,?,?,?,?,?,?,?,?)}',(mnombres,mcodigo,mpaterno,mmaterno,medad,
                    msexo,mdireccion,mciudad,mcorreo,mfecha))
                    conectar.commit
                    self.nuevovendedor()
                    QMessageBox.information(self,"Registro","DATOS DEL VENDEDOR ACTUALIZADO")
            except Exception as error:
                QMessageBox.information(self,"ERROR EN ACTUALIZAR", error)
                


    def eliminarcliente(self):
        opcionactualizar=QMessageBox.question(self,"ELIMINAR ","ELIMINAR DATOS DEL DOCENTE?",
                        QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No,QMessageBox.StandardButton.Yes)
        if opcionactualizar==QMessageBox.StandardButton.Yes:
            try:
                valordni=int(self.ui.cDni2.text())
                with conectar.cursor() as cursor:
                    cursor.execute('{call DeleteCliente(?)}',(valordni))
                    self.ui.tableWidget.clearContents()
                    self.listadoCliente()
                    QMessageBox.information(self,"DELETE","DATOS DEL CLIENTE ELIMINADO")
            except Exception as error:
                QMessageBox.information(self,"ERROR EN ELIMINAR", error)     
    
    def eliminarvendedor(self):
        opcionactualizar=QMessageBox.question(self,"ELIMINAR ","ELIMINAR DATOS DEL DOCENTE?",
                        QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No,QMessageBox.StandardButton.Yes)
        if opcionactualizar==QMessageBox.StandardButton.Yes:
            try:
                valorcodigo=int(self.ui.vCodigo2.text())
                with conectar.cursor() as cursor:
                    cursor.execute('{call DeleteVendedor(?)}',(valorcodigo))
                    self.ui.tableWidget_2.clearContents()
                    self.listadoVendedor()
                    QMessageBox.information(self,"DELETE","DATOS DEL VENDEDOR ELIMINADO")
            except Exception as error:
                QMessageBox.information(self,"ERROR EN ELIMINAR", error)     



if __name__=='__main__':
    app=QApplication(sys.argv)
    ventana01=Final()
    ventana01.show()
    sys.exit(app.exec())