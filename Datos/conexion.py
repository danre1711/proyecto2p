#---------------------
#GRUPO 2 INTEGRANTES:
#DANIELA REYES OBANDO
#---------------------

import sys
import pyodbc as bd

class Conexion:
    """
    Clase que permite abrir conexion a la BBDD y abrir cursor.
    """
    _SERVIDOR = '127.0.0.1'
    _BBDD = 'SAP'
    _USUARIO = 'admin_sap'
    _PASSWORD = '1234'
    _conexion = None

    @classmethod
    def obtener_conexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(
                    'DRIVER={ODBC Driver 17 for SQL Server};'
                    f'SERVER={cls._SERVIDOR};DATABASE={cls._BBDD};UID={cls._USUARIO};PWD={cls._PASSWORD};'
                    'TrustServerCertificate=yes'
                )
                return cls._conexion
            except Exception as e:
                print(f"Error al conectar: {e}")
                sys.exit()
        return cls._conexion