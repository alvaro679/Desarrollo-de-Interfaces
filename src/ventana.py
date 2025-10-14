# Importamos las clases QApplication, QLabel y QWidget del módulo QtWidgets del paquete PySide6
from PySide6.QtWidgets import QApplication, QLabel, QWidget
class Ventana(QWidget):
    """
    Clase Ventana, hereda de QWidget, componente base.
    """
    # Constructor de la clase Ventana
    def __init__(self):
        # Llamada al constructor de la superclase
        super().__init__()
        # Asignamos el título de la ventana 
        self.setWindowTitle("Ventana")
        # Creamos una etiqueta con la ventana como elemento principal
        self.etiqueta1 = QLabel("¡Hola mundo!", self)