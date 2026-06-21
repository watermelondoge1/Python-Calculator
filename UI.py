import sys
from calculator import Calculator
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLabel,
)

buttons = ["1", "2", "3", "+", "="]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.calc = Calculator()
        self.label = QLabel()
        self.button1 = QPushButton(buttons[0])
        self.button2 = QPushButton(buttons[1])
        self.button3 = QPushButton(buttons[2])
        self.buttonAdd = QPushButton(buttons[3])
        self.buttonEquals = QPushButton(buttons[4])

        self.button1.clicked.connect(self.number_clicked)
        self.button2.clicked.connect(self.number_clicked)
        self.button3.clicked.connect(self.number_clicked)
        self.buttonAdd.clicked.connect(self.operator_clicked)
        self.buttonEquals.clicked.connect(self.equals_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.buttonAdd)
        layout.addWidget(self.buttonEquals)
        numpad = QWidget()
        numpad.setLayout(layout)
        self.setCentralWidget(numpad)

    def number_clicked(self):
        button = self.sender()
        self.label.setText(self.label.text() + button.text())

    def operator_clicked(self):
        button = self.sender()
        firstNum = self.label.text()
        self.label.setText(firstNum + " " + button.text() + " ")

    def equals_clicked(self):
        expression = self.label.text()
        result = self.calc.evaluate(expression)
        self.label.setText(str(result))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
