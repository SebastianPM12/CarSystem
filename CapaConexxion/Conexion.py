import pyodbc
nombreServidor='DESKTOP-GFEVOAC\SEBASSQL'
nombreDba='ConcesionarioDeCarros'
nombreusurao='sa'
contrausuraio='Mimamabonita1976'
try:
    conectar=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER='+nombreServidor+';DATABASE='
    +nombreDba+';UID='+nombreusurao+';PWD='+contrausuraio)
    print("CONEXION EXITOSA")
except Exception as mensaje:
    print("ERROR DE CONEXION: ", mensaje)
    