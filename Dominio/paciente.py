#---------------------
#GRUPO 2 INTEGRANTES:
#DANIELA REYES OBANDO
#---------------------

class Paciente:
    """
    Clase que crea objetos para los datos de un paciente
    """
    def __init__(self, cedula=str, nombre=str, apellido=str, edad=int, sexo=str,
                 especialidad=str, tipo_urgencia=str, fecha=None, hora=None, totalpagar=0.0):
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
        self._edad = edad
        self._sexo = sexo
        self._especialidad = especialidad
        self._tipo_urgencia = tipo_urgencia
        self._fecha = fecha
        self._hora = hora
        self._totalpagar = totalpagar

    #propiedades para nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    #propiedades para apellido
    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, nuevo_apellido):
        self._apellido = nuevo_apellido

    #propiedades para cedula
    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, nuevo_cedula):
        self._cedula = nuevo_cedula

    #propiedades para edad
    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nuevo_edad):
        self._edad = nuevo_edad

    #propiedades para sexo
    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, nuevo_sexo):
        self._sexo = nuevo_sexo

    #propiedades para especialidad
    @property
    def especialidad(self):
        return self._especialidad

    @especialidad.setter
    def especialidad(self, nuevo_especialidad):
        self._especialidad = nuevo_especialidad

    #propiedades para tipo_urgencia
    @property
    def tipo_urgencia(self):
        return self._tipo_urgencia

    @tipo_urgencia.setter
    def tipo_urgencia(self, nuevo_tipo_urgencia):
        self._tipo_urgencia = nuevo_tipo_urgencia

    #propiedades para fecha
    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, nuevo_fecha):
        self._fecha = nuevo_fecha

    #propiedades para hora
    @property
    def hora(self):
        return self._hora

    @hora.setter
    def hora(self, nuevo_hora):
        self._hora = nuevo_hora

    #propiedades para totalpagar
    @property
    def totalpagar(self):
        return self._totalpagar

    @totalpagar.setter
    def totalpagar(self, nuevo_total):
        self._totalpagar = nuevo_total

    def __str__(self):
        return (f'Paciente: [Nombre:{self._nombre}, Apellido:{self._apellido}, Cedula:{self._cedula}, '
                f'Edad:{self._edad}, Sexo:{self._sexo}, Especialidad:{self._especialidad}, '
                f'Tipo_urgencia:{self._tipo_urgencia}, Fecha:{self._fecha}, Hora:{self._hora}, '
                f'TotalPagar:{self._totalpagar}]')