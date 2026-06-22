import sys
from calculator import Calculator
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QGridLayout,
    QWidget,
    QLabel,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.calc = Calculator()
        self.label = QLabel()
        buttonsList = [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "0",
            "+",
            "-",
            "*",
            "/",
            "=",
            "C",
        ]
        self.buttons = {}

        for text in buttonsList:
            button = QPushButton(text)
            self.buttons[text] = button

            if text.isdigit():
                button.clicked.connect(self.number_clicked)
            elif text == "=":
                button.clicked.connect(self.equals_clicked)
            elif text == "C":
                button.clicked.connect(self.clear)
            else:
                button.clicked.connect(self.operator_clicked)

        layout = QGridLayout()
        layout.addWidget(self.label, 0, 0)

        layout.addWidget(self.buttons["7"], 1, 0)
        layout.addWidget(self.buttons["8"], 1, 1)
        layout.addWidget(self.buttons["9"], 1, 2)
        layout.addWidget(self.buttons["/"], 1, 3)

        layout.addWidget(self.buttons["4"], 2, 0)
        layout.addWidget(self.buttons["5"], 2, 1)
        layout.addWidget(self.buttons["6"], 2, 2)
        layout.addWidget(self.buttons["*"], 2, 3)

        layout.addWidget(self.buttons["1"], 3, 0)
        layout.addWidget(self.buttons["2"], 3, 1)
        layout.addWidget(self.buttons["3"], 3, 2)
        layout.addWidget(self.buttons["-"], 3, 3)

        layout.addWidget(self.buttons["C"], 4, 0)
        layout.addWidget(self.buttons["0"], 4, 1)
        layout.addWidget(self.buttons["+"], 4, 2)
        layout.addWidget(self.buttons["="], 4, 3)
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

    def clear(self):
        self.label.setText("")

    def equals_clicked(self):
        expression = self.label.text()
        print(expression)
        result = self.calc.evaluate(expression)
        self.label.setText(str(result))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
