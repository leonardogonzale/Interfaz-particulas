from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtGui import QPen, QColor, QTransform
from random import randint
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from particulas import Particula_libreria
from particula import Particula


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.particulas = Particula_libreria()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar_final)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)

        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)

        self.ui.mostar_tabla_pushButton_2.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_particula)

        self.ui.dibujar.clicked.connect(self.dibujar)
        self.ui.limpiar.clicked.connect(self.limpiar)
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)
    
    @Slot()
    def dibujar(self):
        pen = QPen()
        pen.setWidth(2)
        for particula in self.particulas:
            r = particula.rojo
            g = particula.verde
            b = particula.azul
            color = QColor(r, g, b)
            pen.setColor(color)

            self.scene.addEllipse(particula.origen_x, particula.origen_y, 4, 4, pen)
            self.scene.addEllipse(particula.destino_x, particula.destino_y, 4, 4, pen)
            self.scene.addLine(particula.origen_x, particula.origen_y, particula.destino_x, particula.destino_y, pen)
    
    @Slot()
    def limpiar(self):
        self.scene.clear()

    @Slot()
    def buscar_particula(self):
        ID = self.ui.buscar_lineEdit.text()

        encontrado = False
        for particula in self.particulas:
            if ID == particula.Id:
                self.ui.tabla.clear()
                self.ui.tabla.setRowCount(1)


                id_widget = QTableWidgetItem(str (particula.Id))
                origen_x_widget = QTableWidgetItem(str (particula.origen_x))
                origen_y_widget = QTableWidgetItem(str(particula.origen_y))
                destino_x_widget = QTableWidgetItem(str (particula.destino_x))
                destino_y_widget = QTableWidgetItem(str(particula.destino_y))
                velocidad_widget = QTableWidgetItem(str (particula.velocidad))
                rojo_widget = QTableWidgetItem(str (particula.rojo))
                verde_widget = QTableWidgetItem(str (particula.verde))
                azul_widget = QTableWidgetItem(str (particula.azul))
                distancia_widget = QTableWidgetItem(str (particula.distancia))

                self.ui.tabla.setItem(0, 0, id_widget)
                self.ui.tabla.setItem(0, 1, origen_x_widget)
                self.ui.tabla.setItem(0, 2, origen_y_widget)
                self.ui.tabla.setItem(0, 3, destino_x_widget)
                self.ui.tabla.setItem(0, 4, destino_y_widget)
                self.ui.tabla.setItem(0, 5, velocidad_widget)
                self.ui.tabla.setItem(0, 6, rojo_widget)
                self.ui.tabla.setItem(0, 7, verde_widget)
                self.ui.tabla.setItem(0, 8, azul_widget)
                self.ui.tabla.setItem(0, 9, distancia_widget)

                encontrado = True
                return
        if not encontrado:
            QMessageBox.warning(
                self,
                "Atención",
                f'La particula con Id "{ID}" no fue encontrada'
            )


    @Slot()
    def mostrar_tabla(self):
        self.ui.tabla.setColumnCount(10)
        headers = ["Id", "origen_x", "origen_y", "destino_x", "destino_y", "velocidad", "rojo", "verde", "azul", "Distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)

        self.ui.tabla.setRowCount(len(self.particulas))

        row = 0
        for particula in self.particulas:
            id_widget = QTableWidgetItem(str (particula.Id))
            origen_x_widget = QTableWidgetItem(str (particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(particula.origen_y))
            destino_x_widget = QTableWidgetItem(str (particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(particula.destino_y))
            velocidad_widget = QTableWidgetItem(str (particula.velocidad))
            rojo_widget = QTableWidgetItem(str (particula.rojo))
            verde_widget = QTableWidgetItem(str (particula.verde))
            azul_widget = QTableWidgetItem(str (particula.azul))
            distancia_widget = QTableWidgetItem(str (particula.distancia))

            self.ui.tabla.setItem(row, 0, id_widget)
            self.ui.tabla.setItem(row, 1, origen_x_widget)
            self.ui.tabla.setItem(row, 2, origen_y_widget)
            self.ui.tabla.setItem(row, 3, destino_x_widget)
            self.ui.tabla.setItem(row, 4, destino_y_widget)
            self.ui.tabla.setItem(row, 5, velocidad_widget)
            self.ui.tabla.setItem(row, 6, rojo_widget)
            self.ui.tabla.setItem(row, 7, verde_widget)
            self.ui.tabla.setItem(row, 8, azul_widget)
            self.ui.tabla.setItem(row, 9, distancia_widget)

            row += 1
            


    @Slot()
    def action_abrir_archivo(self):  
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir achivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.particulas.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se abrió el archivo" + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Error al abrir el archivo " + ubicacion
            )

    @Slot()
    def action_guardar_archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print(ubicacion)
        if self.particulas.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se pudo crear el archivo" + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo crear el archivo" + ubicacion
            )   

    @Slot()
    def click_mostrar(self):
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.particulas))

    @Slot()
    def click_agregar_inicio(self):
        id = self.ui.id_lineEdit.text()
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.particulas.agregar_inicio(particula)

    @Slot()
    def click_agregar_final(self):
        id = self.ui.id_lineEdit.text()
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.particulas.agregar_final(particula)
