import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QListWidget, QLineEdit, QMessageBox, QLabel
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class TodoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.file_path = os.path.join(os.path.dirname(__file__), "tasks.txt")
        self.setWindowTitle("To-Do List")
        self.setFixedSize(420, 480)
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
                color: white;
                font-family: Arial;
                font-size: 14px;
            }

            QLabel {
                color: white;
            }

            QLineEdit {
                background-color: #2c2c2c;
                border: 1px solid #444;
                border-radius: 8px;
                padding: 10px;
                color: white;
            }

            QListWidget {
                background-color: #2c2c2c;
                border-radius: 8px;
                padding: 8px;
            }

            QListWidget::item {
                padding: 8px;
                margin: 4px;
            }

            QListWidget::item:selected {
                background-color: #0078d7;
            }

            QPushButton {
                background-color: #0078d7;
                border: none;
                border-radius: 8px;
                padding: 10px;
                color: white;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #005fa3;
            }

            QPushButton:pressed {
                background-color: #003f6f;
            }
        """)
        layout = QVBoxLayout()
        layout.setSpacing(12)
        title = QLabel("📝 My To-Do List")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("What do you need to do?")
        self.task_list = QListWidget()
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)
        self.add_btn = QPushButton("Add")
        self.done_btn = QPushButton("Done")
        self.delete_btn = QPushButton("Delete")
        button_layout.addWidget(self.add_btn)
        button_layout.addWidget(self.done_btn)
        button_layout.addWidget(self.delete_btn)
        layout.addWidget(title)
        layout.addWidget(self.task_input)
        layout.addWidget(self.task_list)
        layout.addLayout(button_layout)
        self.setLayout(layout)
        self.add_btn.clicked.connect(self.add_task)
        self.done_btn.clicked.connect(self.mark_done)
        self.delete_btn.clicked.connect(self.delete_task)
        self.load_tasks()

    def add_task(self):
        task = self.task_input.text().strip()
        if not task:
            QMessageBox.warning(self, "Warning", "Task cannot be empty!")
            return
        self.task_list.addItem(task)
        self.task_input.clear()
        self.save_tasks()

    def mark_done(self):
        item = self.task_list.currentItem()
        if item and not item.text().startswith("✔"):
            item.setText("✔ " + item.text())
            self.save_tasks()

    def delete_task(self):
        row = self.task_list.currentRow()
        if row >= 0:
            self.task_list.takeItem(row)
            self.save_tasks()

    def save_tasks(self):
        with open(self.file_path, "w", encoding="utf-8") as f:
            for i in range(self.task_list.count()):
                f.write(self.task_list.item(i).text() + "\n")

    def load_tasks(self):
        if not os.path.exists(self.file_path):
            return

        with open(self.file_path, "r", encoding="utf-8") as f:
            for line in f:
                self.task_list.addItem(line.strip())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TodoApp()
    window.show()
    sys.exit(app.exec_())
