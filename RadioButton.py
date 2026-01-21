import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QCheckBox,
    QRadioButton, QPushButton, QVBoxLayout
)
class MyGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 GUI ")
        self.setGeometry(100, 100, 300, 250)
        self.label = QLabel("Select your preferences:", self)
        self.check1 = QCheckBox("Python")
        self.check2 = QCheckBox("Java")
        self.radio1 = QRadioButton("Beginner")
        self.radio2 = QRadioButton("Advanced")
        self.button = QPushButton("Submit")
        self.button.clicked.connect(self.show_selection)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.check1)
        layout.addWidget(self.check2)
        layout.addWidget(self.radio1)
        layout.addWidget(self.radio2)
        layout.addWidget(self.button)
        self.setLayout(layout)
    def show_selection(self):
        selected = "You selected:\n"
        if self.check1.isChecked():
            selected += "- Python\n"
        if self.check2.isChecked():
            selected += "- Java\n"
        if self.radio1.isChecked():
            selected += "- Level: Beginner\n"
        if self.radio2.isChecked():
            selected += "- Level: Advanced\n"
        self.label.setText(selected)
app = QApplication(sys.argv)
window = MyGUI()
window.show()
sys.exit(app.exec_())
