#---------------------
#GRUPO 2 INTEGRANTES:
#DANIELA REYES OBANDO
#---------------------

from Datos.conexion import Conexion
from Dominio.paciente import Paciente
import pyodbc as bd

class PacienteDAO:
    """
    DAO para gestión de Pacientes con CRUD completo
    """

    _INSERT = ("INSERT INTO Paciente (nombres, apellidos, cedula, edad, sexo, especialidad, "
               "tipourgencia, fecha, hora, totalpagar) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")

    _SELECT = ("SELECT nombres, apellidos, cedula, edad, sexo, especialidad, tipourgencia, fecha, hora, totalpagar "
               "FROM Paciente WHERE cedula = ?")

    _UPDATE = ("UPDATE Paciente SET nombres = ?, apellidos = ?, edad = ?, sexo = ?, especialidad = ?, "
               "tipourgencia = ?, fecha = ?, hora = ?, totalpagar = ? WHERE cedula = ?")

    _DELETE = "DELETE FROM Paciente WHERE cedula = ?"

    @classmethod
    def insertar_paciente(cls, paciente: Paciente):
        conn = Conexion.obtener_conexion()
        cursor = conn.cursor()
        try:
            datos = (
                paciente.nombre,
                paciente.apellido,
                paciente.cedula,
                paciente.edad,
                paciente.sexo,
                paciente.especialidad,
                paciente.tipo_urgencia,
                paciente.fecha,
                paciente.hora,
                paciente.totalpagar
            )
            cursor.execute(cls._INSERT, datos)
            conn.commit()
            return {'ejecuto': True, 'mensaje': 'Se guardó con éxito.'}
        except bd.IntegrityError as e_bd:
            return {'ejecuto': False, 'mensaje': f'Error de integridad: {e_bd}'}
        except Exception as e:
            return {'ejecuto': False, 'mensaje': f'Error: {e}'}
        finally:
            cursor.close()

    @classmethod
    def seleccionar_paciente(cls, cedula: str):
        conn = Conexion.obtener_conexion()
        cursor = conn.cursor()
        paciente = None
        try:
            cursor.execute(cls._SELECT, (cedula,))
            registro = cursor.fetchone()
            if registro:
                paciente = Paciente(
                    nombre=registro[0],
                    apellido=registro[1],
                    cedula=registro[2],
                    edad=registro[3],
                    sexo=registro[4],
                    especialidad=registro[5],
                    tipo_urgencia=registro[6],
                    fecha=registro[7],
                    hora=registro[8],
                    totalpagar=registro[9]
                )
            return paciente
        except Exception as e:
            print(f"Error al seleccionar paciente: {e}")
            return None
        finally:
            cursor.close()

    @classmethod
    def actualizar_paciente(cls, paciente: Paciente):
        conn = Conexion.obtener_conexion()
        cursor = conn.cursor()
        try:
            datos = (
                paciente.nombre,
                paciente.apellido,
                paciente.edad,
                paciente.sexo,
                paciente.especialidad,
                paciente.tipo_urgencia,
                paciente.fecha,
                paciente.hora,
                paciente.totalpagar,
                paciente.cedula
            )
            cursor.execute(cls._UPDATE, datos)
            conn.commit()
            if cursor.rowcount == 1:
                return {'ejecuto': True, 'mensaje': 'Se actualizó con éxito.'}
            else:
                return {'ejecuto': False, 'mensaje': 'No se encontró al paciente.'}
        except Exception as e:
            return {'ejecuto': False, 'mensaje': f'Error: {e}'}
        finally:
            cursor.close()

    @classmethod
    def eliminar_paciente(cls, cedula: str):
        conn = Conexion.obtener_conexion()
        cursor = conn.cursor()
        try:
            cursor.execute(cls._DELETE, (cedula,))
            conn.commit()
            if cursor.rowcount == 1:
                return {'ejecuto': True, 'mensaje': 'Se eliminó con éxito.'}
            else:
                return {'ejecuto': False, 'mensaje': 'No se encontró al paciente.'}
        except Exception as e:
            return {'ejecuto': False, 'mensaje': f'Error: {e}'}
        finally:
            cursor.close()
