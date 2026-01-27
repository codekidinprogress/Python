import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel,
    QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
)

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Page")
        self.setGeometry(400, 200, 400, 300)
        self.initUI()
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.username = QLineEdit()
        self.username.setPlaceholderText("Enter username")
        self.username.setObjectName("input")
        self.password = QLineEdit()
        self.password.setPlaceholderText("Enter password")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setObjectName("input")
        self.login_btn = QPushButton("Login")
        self.reset_btn = QPushButton("Reset")
        self.login_btn.setObjectName("login")
        self.reset_btn.setObjectName("reset")
        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        main_layout.addWidget(QLabel("Username:"))
        main_layout.addWidget(self.username)
        main_layout.addWidget(QLabel("Password:"))
        main_layout.addWidget(self.password)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.login_btn)
        button_layout.addWidget(self.reset_btn)
        main_layout.addLayout(button_layout)
        central_widget.setLayout(main_layout)
        self.reset_btn.clicked.connect(self.clearFields)
        self.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-family: Arial;
            }

            QLineEdit#input {
                font-size: 15px;
                padding: 10px;
                border: 2px solid gray;
                border-radius: 8px;
            }

            QPushButton {
                font-size: 16px;
                padding: 10px 30px;
                border-radius: 10px;
            }

            QPushButton#login {
                background-color: hsl(122, 100%, 64%);
            }

            QPushButton#login:hover {
                background-color: hsl(122, 100%, 84%);
            }

            QPushButton#reset {
                background-color: hsl(0, 100%, 64%);
            }

            QPushButton#reset:hover {
                background-color: hsl(0, 100%, 84%);
            }
        """)

    def clearFields(self):
        self.username.clear()
        self.password.clear()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
