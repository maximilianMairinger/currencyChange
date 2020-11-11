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

    html += "<li><b>" + str(round(value, 2)) + " " + currency +  "</b> (Kurs: " + str(round(rate, 2)) + ")</li>"

  html += "</ul>"
  html += "Stand: " + res["date"]
  

  return html


class Window(QtWidgets.QWidget):

  def __init__(self):
    super().__init__()
    uic.loadUi("view.ui", self)


    self.fromInput.setValidator(QRegExpValidator(QRegExp("^[A-Z,a-z]{1,3}$")))
    self.toInput.setValidator(QRegExpValidator(QRegExp("^([A-Z,a-z]{1,3})(,([A-Z,a-z]{1,3})){0,1000}$")))



    def reset():
      self.clearHTML()
      self.clearInputs()

    self.resetButton.clicked.connect(reset)

    def go():
      value = float(self.betragInput.text())
      fromCurrency = self.fromInput.text()
      toCurrency = self.toInput.text()
      live = self.liveCheckbox.isChecked()
      print("live", live)
      self.statusLabel.setText("Abfragen...")

      self.clearHTML()
      
      ret = controller.calculateValueInNewCurrency(value, fromCurrency, toCurrency, live)
      if ret["ok"]:
        self.showResult(ret["res"])
        self.statusLabel.setText("Erflogreich")
      else: 
        try:
          if len(ret["msg"]) == 1:
            s = str(ret["msg"][0])
          else:
            s = str(ret["msg"])
        except Exception as e:
          str(ret["msg"])
          
        self.statusLabel.setText(s)
      

    self.goButton.clicked.connect(go)

  def clearHTML(self):
    self.browser.setHtml("")


  def clearInputs(self):
    self.betragInput.setValue(0)
    self.fromInput.setText("")
    self.toInput.setText("")
    self.liveCheckbox.setChecked(False)

  def showResult(self, res):
    self.browser.setHtml(parseResultToHTML(res))

