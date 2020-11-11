from PyQt5 import QtWidgets, uic
import sys
from view import *
from modell import *


res = swapCurrency(100, "USD", "EUR", True)




app = QtWidgets.QApplication(sys.argv)

window = Window()
window.showResult(res)
window.show()
sys.exit(app.exec_())
