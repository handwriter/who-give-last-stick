from design import Ui_Form as Design
from PyQt5.QtWidgets import QWidget, QApplication
import sys


class Widget(QWidget, Design):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.make_action)
        self.count = 37
        self.make_action_ii()

    def update(self, text=''):
        self.label.setText(str(self.count) + text)

    def make_action_ii(self):
        mad = self.count % 4
        if mad == 0:
            mad = 2
        self.count -= mad
        self.update(f' ИИ забрал: {mad}')
        if self.count == 0:
            self.pushButton.setEnabled(False)
            self.label.setText('ИИ выиграл!')

    def make_action(self):
        if self.spinBox.value() > self.count:
            self.label_2.setText('Неверное количество!')
        else:
            self.count -= self.spinBox.value()
            self.update()
            if self.count == 0:
                self.label.setText('Вы выиграли!')
                self.pushButton.setEnabled(False)
            else:
                self.make_action_ii()


app = QApplication(sys.argv)
ex = Widget()
ex.show()
sys.exit(app.exec_())