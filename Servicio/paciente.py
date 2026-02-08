#---------------------
#GRUPO2 INTEGRANTES:
#DANIELA REYES OBANDO
#SYLVIA PINTADO CORREA
#JONATHAN ZAVALA ALCIVAR
#---------------------

from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtGui import QIntValidator
from Dominio.paciente import Paciente
from Datos.paciente_dao import PacienteDAO
from UI.vtnPrincipalSM import Ui_vtnPrincipalSM
import re
from datetime import datetime


class PacienteServicio(QMainWindow):
    """
    Clase que genera la lógica de los objetos Paciente
    """

    def __init__(self):
        super().__init__()
        self.ui = Ui_vtnPrincipalSM()
        self.ui.setupUi(self)

        self.ui.btnAgregar.clicked.connect(self.guardar)
        self.ui.btnActualizar.clicked.connect(self.actualizar)
        self.ui.btnEliminar.clicked.connect(self.eliminar)
        self.ui.btnLimpiar.clicked.connect(self.limpiar)
        self.ui.btnBuscar.clicked.connect(self.buscar)

        self.ui.txtCedula.setValidator(QIntValidator())
        self.ui.txtBuscarCedula.setValidator(QIntValidator())

    # funcion para guardar al paciente
    def guardar(self):
        nombre = self.ui.txtNombre.text().strip()
        apellido = self.ui.txtApellido.text().strip()
        cedula = self.ui.txtCedula.text().strip()
        edad = self.ui.txtEdad.text().strip()
        sexo = self.ui.cbSexo.currentText()
        especialidad = self.ui.txtEspecialidad.text().strip()
        tipourgencia = self.ui.cbTipoUrgencia.currentText()
        fecha_texto = self.ui.txtFecha.text().strip()
        hora = self.ui.txtHora.text().strip()
        totalpagar = self.ui.txtTotalPagar.text().strip()

        # Validaciones
        if nombre == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar el nombre")
            return
        elif apellido == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar el apellido")
            return
        elif len(cedula) != 10 or not cedula.isdigit():
            QMessageBox.warning(self, "Advertencia", "Debe ingresar una cédula válida de 10 dígitos")
            return
        elif not edad.isdigit() or int(edad) <= 0:
            QMessageBox.warning(self, "Advertencia", "Edad inválida")
            return
        elif sexo == "SELECCIONAR":
            QMessageBox.warning(self, "Advertencia", "Seleccione sexo")
            return
        elif especialidad == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar la especialidad")
            return
        elif tipourgencia == "SELECCIONAR":
            QMessageBox.warning(self, "Advertencia", "Seleccione tipo de urgencia")
            return

        try:
            fecha = datetime.strptime(fecha_texto, "%d-%m-%Y").date()
        except:
            QMessageBox.warning(self, "Advertencia", "Formato de fecha inválido. Use dd-MM-yyyy")
            return

        if not re.match(r"^([01]\d|2[0-3]):([0-5]\d)$", hora):
            QMessageBox.warning(self, "Advertencia", "Formato de hora inválido. Use HH:MM")
            return

        try:
            totalpagar = float(totalpagar)
        except:
            QMessageBox.warning(self, "Advertencia", "Total a pagar inválido")
            return

        paciente = Paciente(
            nombre=nombre,
            apellido=apellido,
            cedula=cedula,
            edad=int(edad),
            sexo=sexo,
            especialidad=especialidad,
            tipo_urgencia=tipourgencia,
            fecha=fecha,
            hora=hora,
            totalpagar=totalpagar
        )

        resultado = PacienteDAO.insertar_paciente(paciente)

        if resultado["ejecuto"]:
            print("PACIENTE GUARDADO")
            print(f"{cedula} | {nombre} {apellido} | {edad} | {sexo}")
            print(f"{especialidad} | {tipourgencia} | {fecha} {hora}")
            print(f"Total a pagar: {totalpagar}")
            print("-" * 40)

            self.ui.statusbar.showMessage("Paciente guardado correctamente", 3000)
            self.limpiar()
        else:
            QMessageBox.critical(self, "Error", resultado["mensaje"])

    #funcion para actualiza los datos del paciente
    def actualizar(self):
        cedula = self.ui.txtCedula.text().strip()

        if len(cedula) != 10:
            QMessageBox.warning(self, "Advertencia", "Ingrese una cédula válida para actualizar")
            return

        nombre = self.ui.txtNombre.text().strip()
        apellido = self.ui.txtApellido.text().strip()
        edad = self.ui.txtEdad.text().strip()
        sexo = self.ui.cbSexo.currentText()
        especialidad = self.ui.txtEspecialidad.text().strip()
        tipourgencia = self.ui.cbTipoUrgencia.currentText()
        fecha_texto = self.ui.txtFecha.text().strip()
        hora = self.ui.txtHora.text().strip()
        totalpagar = self.ui.txtTotalPagar.text().strip()

        if nombre == "" or apellido == "":
            QMessageBox.warning(self, "Advertencia", "Nombre y apellido obligatorios")
            return

        try:
            fecha = datetime.strptime(fecha_texto, "%d-%m-%Y").date()
            totalpagar = float(totalpagar)
        except:
            QMessageBox.warning(self, "Advertencia", "Datos inválidos")
            return

        paciente = Paciente(
            nombre=nombre,
            apellido=apellido,
            cedula=cedula,
            edad=int(edad),
            sexo=sexo,
            especialidad=especialidad,
            tipo_urgencia=tipourgencia,
            fecha=fecha,
            hora=hora,
            totalpagar=totalpagar
        )

        resultado = PacienteDAO.actualizar_paciente(paciente)

        if resultado["ejecuto"]:
            print("PACIENTE ACTUALIZADO:", cedula)
            self.ui.statusbar.showMessage("Paciente actualizado correctamente", 3000)
            self.limpiar()
        else:
            QMessageBox.critical(self, "Error", resultado["mensaje"])

    # funcion para elimina al paciente
    def eliminar(self):
        cedula = self.ui.txtCedula.text().strip()

        if len(cedula) != 10:
            QMessageBox.warning(self, "Advertencia", "Ingrese una cédula válida")
            return

        if QMessageBox.question(self, "Confirmar", "¿Desea eliminar este paciente?") == QMessageBox.Yes:
            resultado = PacienteDAO.eliminar_paciente(cedula)
            if resultado["ejecuto"]:
                print("PACIENTE ELIMINADO:", cedula)
                self.limpiar()

    # funcion para busca al paciente
    def buscar(self):
        cedula = self.ui.txtBuscarCedula.text().strip()

        if len(cedula) != 10:
            QMessageBox.warning(self, "Advertencia", "Ingrese una cédula válida")
            return

        paciente = PacienteDAO.seleccionar_paciente(cedula)

        if paciente:
            self.ui.txtNombre.setText(paciente.nombre)
            self.ui.txtApellido.setText(paciente.apellido)
            self.ui.txtCedula.setText(paciente.cedula)
            self.ui.txtEdad.setText(str(paciente.edad))
            self.ui.cbSexo.setCurrentText(paciente.sexo)
            self.ui.txtEspecialidad.setText(paciente.especialidad)
            self.ui.cbTipoUrgencia.setCurrentText(paciente.tipo_urgencia)
            self.ui.txtFecha.setText(paciente.fecha.strftime("%d-%m-%Y"))
            self.ui.txtHora.setText(paciente.hora)
            self.ui.txtTotalPagar.setText(str(paciente.totalpagar))
            self.ui.statusbar.showMessage("Paciente encontrado", 3000)
        else:
            QMessageBox.information(self, "Información", "Paciente no encontrado")

    # funcion para limpia los datos de la interfaz grafica
    def limpiar(self):
        self.ui.txtBuscarCedula.clear()
        self.ui.txtNombre.clear()
        self.ui.txtApellido.clear()
        self.ui.txtCedula.clear()
        self.ui.txtEdad.clear()
        self.ui.txtEspecialidad.clear()
        self.ui.cbSexo.setCurrentIndex(0)
        self.ui.cbTipoUrgencia.setCurrentIndex(0)
        self.ui.txtFecha.clear()
        self.ui.txtHora.clear()
        self.ui.txtTotalPagar.clear()
        self.ui.statusbar.showMessage("Formulario limpiado", 3000)
