from PyQt6 import QtWidgets
import sys,os

class Rename_Win(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.filePath = ''
        self.setWindowTitle('win_shutdown')
        self.resize(300, 200)
        self.ui()

    def ui(self):

        input1_x = 20 ; input1_y = 40
        btn1_x = input1_x + 110 ; btn1_y = input1_y
        btn2_x = input1_x + 110 ; btn2_y = input1_y + 25
        input1_label_x = input1_x + 2 ; input1_label_y = input1_y - 20

        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.move(btn1_x, btn1_y)
        self.btn1.setText('確認')
        self.btn1.clicked.connect(self.shutdiwwn)

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.move(btn2_x, btn2_y)
        self.btn2.setText('取消')
        self.btn2.clicked.connect(self.clear_)

        self.input1 = QtWidgets.QLineEdit(self)
        self.input1.setGeometry(input1_x, input1_y, 100, 20)

        self.input1_label = QtWidgets.QLabel(self)
        self.input1_label.move(input1_label_x, input1_label_y)
        self.input1_label.setText('輸入關機秒數')

    def OpenFiles(self):
        self.filePath, filterType = QtWidgets.QFileDialog.getOpenFileNames()  # 選取多個檔案

    def shutdiwwn(self):
        time = self.input1.text()
        os.system(f"shutdown -s -t {time}")

    def clear_(self):
        os.system("shutdown -a")




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = Rename_Win()
    Form.show()
    sys.exit(app.exec())