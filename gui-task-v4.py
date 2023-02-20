import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QGroupBox, QLineEdit, QFormLayout, QSpinBox, QHBoxLayout, QVBoxLayout, QGridLayout, QRadioButton
from PyQt5.QtGui import QPixmap


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
    w.resize(1000, 500)
    w.setWindowTitle("Monitoring Tool")



    grid = QGridLayout(w)


    label1 = QLabel('Label 1')
    label2 = QLabel('Label 2')
    label3 = QLabel('Label 3')
    label4 = QLabel('Label 4')
    label5 = QLabel('Label 5')


    #box1
    group_box1 = QGroupBox("First Sensor Waist", w)
    group_box1.move(20, 20)
    group_box1.setFixedSize(400, 320)

    #list1
    form_layout1 = QFormLayout(group_box1)

    form_layout1.addRow(QLabel("Roll:"))
    form_layout1.addRow(QLineEdit())
    form_layout1.addRow(QLabel("Pitch:"))
    form_layout1.addRow(QLineEdit())
    form_layout1.addRow(QLabel("Acceleration:"))
    form_layout1.addRow(QLineEdit())


    #box2
    group_box2 = QGroupBox("Second Sensor Lett Things", w)
    group_box2.move(20, 20)
    group_box2.setFixedSize(400, 320)

    #list1
    form_layout2 = QFormLayout(group_box2)

    form_layout2.addRow(QLabel("Roll:"))
    form_layout2.addRow(QLineEdit())
    form_layout2.addRow(QLabel("Pitch:"))
    form_layout2.addRow(QLineEdit())
    form_layout2.addRow(QLabel("Acceleration:"))
    form_layout2.addRow(QLineEdit())




    #box3
    group_box3 = QGroupBox("Third Sensor Right Arm", w)
    group_box3.move(20, 20)
    group_box3.setFixedSize(400, 320)

    #list1
    form_layout3 = QFormLayout(group_box3)

    form_layout3.addRow(QLabel("Roll:"))
    form_layout3.addRow(QLineEdit())
    form_layout3.addRow(QLabel("Pitch:"))
    form_layout3.addRow(QLineEdit())
    form_layout3.addRow(QLabel("Acceleration:"))
    form_layout3.addRow(QLineEdit())


    #box4
    group_box4 = QGroupBox("Fourth Sensor Right Ankle", w)
    group_box4.move(20, 20)
    group_box4.setFixedSize(400, 320)

    #list1
    form_layout4 = QFormLayout(group_box4)

    form_layout4.addRow(QLabel("Roll:"))
    form_layout4.addRow(QLineEdit())
    form_layout4.addRow(QLabel("Pitch:"))
    form_layout4.addRow(QLineEdit())
    form_layout4.addRow(QLabel("Acceleration:"))
    form_layout4.addRow(QLineEdit())




#
#
#
    #box5
    group_box5 = QGroupBox("Sensor disposition", w)
    group_box5.move(20, 20)
    group_box5.setFixedSize(400, 320)

    form_layout5 = QFormLayout(group_box5)




    label9 = QLabel()
    pixmap = QPixmap("image.jpg")
    label9.setPixmap(pixmap)


    layout = QVBoxLayout()
    layout.addWidget(label9)
    group_box5.setLayout(layout)
#
#
#




#box6
    group_box6 = QGroupBox("Activity", w)
    group_box6.move(20, 20)
    group_box6.setFixedSize(400, 320)

    #list1
    form_layout6 = QFormLayout(group_box6)

    form_layout6.addRow(QLabel("Setect Activity:"))
    form_layout6.addRow(QRadioButton("Random"))
    form_layout6.addRow(QRadioButton("Sitting"))
    form_layout6.addRow(QRadioButton("Sittingdown"))
    form_layout6.addRow(QRadioButton("Standing"))
    form_layout6.addRow(QRadioButton("Standingup"))
    form_layout6.addRow(QRadioButton("Walking"))





#box7
    group_box7 = QGroupBox("First Sensor Waist", w)
    group_box7.move(20, 20)
    group_box7.setFixedSize(400, 320)

    #list1
    form_layout7 = QFormLayout(group_box7)

    form_layout7.addRow(QPushButton("Run"))
    form_layout7.addRow(QPushButton("Reset"))
    form_layout7.addRow(QLabel("Activity select:"))
    form_layout7.addRow(QLineEdit())
    form_layout7.addRow(QLabel("Activity predict:"))
    form_layout7.addRow(QLineEdit())








#box8
    group_box8 = QGroupBox("First Sensor Waist", w)
    group_box8.move(20, 20)
    group_box8.setFixedSize(400, 320)

    #list1
    form_layout8 = QFormLayout(group_box8)

    form_layout8.addRow(QLabel("Match:"))
    form_layout8.addRow(QLineEdit())
    form_layout8.addRow(QLabel("Match Percentage:"))
    form_layout8.addRow(QLineEdit())



    grid.addWidget(group_box1, 0, 0)
    grid.addWidget(group_box2, 0, 1)
    grid.addWidget(group_box3, 0, 2)
    grid.addWidget(group_box4, 0, 3)
    grid.addWidget(group_box5, 1, 0)
    grid.addWidget(group_box6, 1, 1)
    grid.addWidget(group_box7, 1, 2)
    grid.addWidget(group_box8, 1, 3)


    w.show()
    sys.exit(app.exec_())