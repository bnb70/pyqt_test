from PyQt6 import QtWidgets
import sys,os

class Rename_Win(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.filePath = ''
        self.setWindowTitle('Rename_File')
        self.resize(300, 200)
        self.ui()

    def ui(self):

        input1_x = 20 ; input1_y = 100
        btn1_x = 20 ; btn1_y = 20
        btn2_x = input1_x + 110 ; btn2_y = input1_y
        btn3_x = 20 ; btn3_y = 160
        input1_label_x = input1_x + 2 ; input1_label_y = input1_y - 20

        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.move(btn1_x, btn1_y)
        self.btn1.setText('選擇檔案')
        self.btn1.clicked.connect(self.OpenFiles)

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.move(btn2_x, btn2_y)
        self.btn2.setText('確認')
        self.btn2.clicked.connect(self.RenameFiles)

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.move(btn3_x, btn3_y)
        self.btn2.setText('離開')
        self.btn2.clicked.connect(QtWidgets.QApplication.instance().quit)

        self.input1 = QtWidgets.QLineEdit(self)
        self.input1.setGeometry(input1_x, input1_y, 100, 20)

        self.input1_label = QtWidgets.QLabel(self)
        self.input1_label.move(input1_label_x, input1_label_y)
        self.input1_label.setText('輸入分割符號')

    def OpenFiles(self):
        self.filePath, filterType = QtWidgets.QFileDialog.getOpenFileNames()  # 選取多個檔案

    def RenameFiles(self):
        cut_ = self.input1.text()



        for i in self.filePath:
            old_name = i.split('/')[-1]
            path = i.split(old_name[0])[0]
            cut_name = old_name.split(cut_)[0] + cut_
            new_name = old_name.split(cut_name)[1:]
            replace = path + new_name[0]
            os.rename(i, replace)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = Rename_Win()
    Form.show()
    sys.exit(app.exec())