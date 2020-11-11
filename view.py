from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QRegExpValidator
import controller




def parseResultToHTML(res):
  html = ""
  html += "<b>" + str(res["baseValue"]) + " " + res["baseCurrency"] + "</b> entsprechen"
  html += "<ul>"

  values = res["values"]
  rates = res["rates"]
  for currency in values:
    value = values[currency]
    rate = rates[currency]

    html += "<li><b>" + str(value) + " " + str(currency) +  "</b> (Kurs: " + str(rate) + ")</li>"

  html += "</ul>"
  html += "Stand: " + res["date"]
  

  return html


class Window(QtWidgets.QWidget):

  def __init__(self):
    super().__init__()
    uic.loadUi("view.ui", self)


    


    def go():
      value = float(self.betragInput.text())
      fromCurrency = self.fromInput.text()
      toCurrency = self.toInput.text()
      live = self.liveCheckbox.isChecked()
      
      controller.calculateValueInNewCurrency(value, fromCurrency, toCurrency, live)
      

    self.goButton.clicked.connect(go)

  def showResult(self, res):
    self.browser.setHtml(parseResultToHTML(res))

