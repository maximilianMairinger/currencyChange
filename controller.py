from PyQt5 import QtWidgets, uic
import sys
from view import *
from modell import *



def calculateValueInNewCurrency(value, fromCurrency, toCurrency, live):
  if isinstance(live, str):
    via = live
  elif isinstance(live, bool):
    if live:
      via = "api"
    else: 
      via = "offline"
  else:
    via = "api"

  if isinstance(toCurrency, str):
    toCurrency = toCurrency.split(",")
  else:
    if not isinstance(toCurrency, list):
      toCurrency = [str(toCurrency)]
    else:
      for i in range(len(toCurrency)):
        toCurrency[i] = str(toCurrency[i])


  for i in range(len(toCurrency)):
    toCurrency[i] = toCurrency[i].upper()


  fromCurrency = fromCurrency.upper()


  try:
    res = swapCurrency(value, fromCurrency, toCurrency, via)  

    return {
      "ok": True,
      "res": res
    }
  except Exception as e:
    print(e)
    return {
      "ok": False,
      "msg": e.args
    }
  
  





app = QtWidgets.QApplication(sys.argv)

window = Window()
window.show()
sys.exit(app.exec_())
