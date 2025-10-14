# Importamos las clases QApplication, QLabel y QWidget del módulo QtWidgets del paquete PySide6
from PySide6.QtWidgets import QApplication, QLabel, QWidget
from src.ventana import Ventana


# Cada aplicación será una sola instancia de QApplication
app = QApplication([])
# Creamos un objeto ventana
ventana1 = Ventana()
# Mostramos la ventana (por defecto los componentes están ocultos)
ventana1.show()
# Iniciamos el bucle de eventos
app.exec()