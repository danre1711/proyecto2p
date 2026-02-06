#---------------------
#GRUPO 2 INTEGRANTES:
#DANIELA REYES OBANDO
#---------------------

import sys
from PySide6.QtWidgets import QApplication
from Servicio.paciente import PacienteServicio
app = QApplication()
vtn_principal = PacienteServicio()
vtn_principal.show()
sys.exit(app.exec())
