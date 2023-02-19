import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QGroupBox, QLineEdit, QFormLayout, QSpinBox, QHBoxLayout, QVBoxLayout

def dialog ():
    mbox = QMessageBox() #
    mbox.setText("lorem ipsum")
    mbox.setDetailedText("you")
    mbox.setStandardButtons(QMessageBox.OK, QMessageBox.NO)
    mbox.exec_()

#main window
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(500, 500)
    w.setWindowTitle("Basic GUI")



    h_layout = QHBoxLayout()


    #box1
    group_box1 = QGroupBox("First Sensor Waist", w)
    group_box1.move(20, 20)
    group_box1.setFixedSize(400, 320)


    #list1
    form_layout = QFormLayout(group_box1)





    form_layout.addRow(QLabel("Roll:"))
    form_layout.addRow(QLineEdit())
    form_layout.addRow(QLabel("Pitch:"))
    form_layout.addRow(QLineEdit())
    form_layout.addRow(QLabel("Acceleration:"))
    form_layout.addRow(QLineEdit())










    w.show()
    sys.exit(app.exec_())