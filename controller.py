from PyQt5 import QtWidgets, uic
import sys
from view import *
from modell import *



def calculateValueInNewCurrency(value, fromCurrency, toCurrency, live):
  if isinstance(str, live):
    via = live
  elif isinstance(bool, live):
    if live:
      via = "api"
    else: 
      via = "offline"
  else:
    via = "api"


  if isinstance(toCurrency, str):
    toCurrency = ",".split(toCurrency)
  else:
    if not isinstance(toCurrency, list):
      toCurrency = [str(toCurrency)]
    else:
      for i in range(len(toCurrency)):
        toCurrency[i] = str(toCurrency[i])

  
  for i in range(len(toCurrency)):
    toCurrency[i] = upper(toCurrency[i])

  try:
    res = swapCurrency(value, fromCurrency, toCurrency, via)  
    return {
      "ok": True,
      "res": res
    }
  except Exception as e:
    return {
      "ok": False,
      "msg": e.args
    }
  
  





app = QtWidgets.QApplication(sys.argv)

window = Window()
window.show()
sys.exit(app.exec_())
