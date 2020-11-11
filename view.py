from PyQt5 import QtWidgets, uic


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

  def showResult(self, res):
    self.browser.setHtml(parseResultToHTML(res))
