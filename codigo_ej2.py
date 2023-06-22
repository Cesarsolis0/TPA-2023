import sys
from PyQt6 import QtWidgets, uic 

from VentanaPrincipal import Ui_VentanaPrincipal

class Mascota:
    def __init__(self, nombre: str, especie: str, edad: int, peso:float):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso

    def __str__(self) -> str:
        return f"Mascota {self.nombre} de {self.edad} anios de la especie {self.especie} con {self.peso} Kg."


class Ventana(QtWidgets.QMainWindow, Ui_VentanaPrincipal):
    def __init__(self, *args, obj=None, **kwargs):
        super(Ventana, self).__init__(*args, **kwargs)
        #Implementación de Ui_VentanaPrincipal
        self.setupUi(self)
        self.mascotas=[]                                                    #agregado
        self.butonguardarmascota.clicked.connect(self.guardar_mascota)      #agregado
    
    def guardar_mascota(self):
        nombre = self.nombre.text()
        especie = self.especie.text()
        edad = int(self.edad.text())
        peso = float(self.peso.text())                                     #funcionagregada
        mascota_nueva = Mascota(nombre, especie, edad, peso)
        self.mascotas.append(mascota_nueva)
        QtWidgets.QMessageBox.information(self, "Guardado", "Mascota guardada con éxito",QtWidgets.QMessageBox.standardButton.Ok,QtWidgets.QMessageBox.standardButton.Ok)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    vista = Ventana()
    vista.show()
    app.exec()