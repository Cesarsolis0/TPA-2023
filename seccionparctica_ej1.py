import sys
from PyQt6.QtWidgets import QWidget , QApplication , QLabel , QHBoxLayout , QVBoxLayout , QPushButton ,QMessageBox
from PyQt6.QtGui import QFont

class ventana(QWidget):

    def __init__(self):
        super().__init__()
        self.inicializarui()

    def inicializarui(self):

        self.setMinimumWidth(600)
        self.setWindowTitle("Ejercicio 1 seccion parctica prueba individual")
        self.contenido()
        self.show()

    def contenido(self):

        nombre_label = QLabel("Nombre de Usuario")
        nombre_label.setFont(QFont("Arial",30))

        rutaimagen=QLabel("Imagen")
        

        descripcion_label = QLabel("texto descripcion usuario")

        atributo1_label = QLabel("atributo 1")
        atributo2_label = QLabel("atributo 2")
        atributo3_label = QLabel("atributo 3")
        atributo4_label = QLabel("atributo 4")
        atributo5_label = QLabel("atributo 5")
        atributo6_label = QLabel("atributo 6")

        valor1_label = QLabel("valor 1")
        valor2_label = QLabel("valor 2")
        valor3_label = QLabel("valor 3")
        valor4_label = QLabel("valor 4")
        valor5_label = QLabel("valor 5")
        valor6_label = QLabel("valor 6")

        ok_buton = QPushButton("OK")

        layout_principal=QVBoxLayout()
        layout_secundario=QHBoxLayout()

        layout_imagen=QVBoxLayout()
        layout_datos=QVBoxLayout()

        layout_datos1=QHBoxLayout()
        layout_datos2=QHBoxLayout()
        layout_datos3=QHBoxLayout()
        layout_datos4=QHBoxLayout()
        layout_datos5=QHBoxLayout()
        layout_datos6=QHBoxLayout()

        layout_datos1.addWidget(atributo1_label)
        layout_datos1.addWidget(valor1_label)

        layout_datos2.addWidget(atributo2_label)
        layout_datos2.addWidget(valor2_label)

        layout_datos3.addWidget(atributo3_label)
        layout_datos3.addWidget(valor3_label)

        layout_datos4.addWidget(atributo4_label)
        layout_datos4.addWidget(valor4_label)

        layout_datos5.addWidget(atributo5_label)
        layout_datos5.addWidget(valor5_label)

        layout_datos6.addWidget(atributo6_label)
        layout_datos6.addWidget(valor6_label)

        layout_imagen.addWidget(rutaimagen)
        layout_imagen.addWidget(descripcion_label)

        layout_datos.addLayout(layout_datos1)
        layout_datos.addLayout(layout_datos2)
        layout_datos.addLayout(layout_datos3)
        layout_datos.addLayout(layout_datos4)
        layout_datos.addLayout(layout_datos5)
        layout_datos.addLayout(layout_datos6)

        layout_secundario.addLayout(layout_imagen)
        layout_secundario.addLayout(layout_datos)

        layout_principal.addWidget(nombre_label)
        layout_principal.addLayout(layout_secundario)
        layout_principal.addWidget(ok_buton)

        self.setLayout(layout_principal)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ventana()
    sys.exit(app.exec())

        



