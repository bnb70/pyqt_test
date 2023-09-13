from Windows import Rename_Win
from PyQt6 import QtWidgets
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = Rename_Win()
    Form.show()
    sys.exit(app.exec())