import requests
import copy


def getAPIRate(fromCurrency, toCurrency):
  url = "https://api.exchangeratesapi.io/latest?base=" + fromCurrency + "&symbols=" + ",".join(toCurrency)
  res = requests.get(url).json()
  if "error" in res:
    raise Exception(res["error"])
  else:
    return res




offline = {"rates":{"CAD":1.4959,"HKD":11.2301,"LVL":0.7093,"PHP":66.106,"DKK":7.4405,"HUF":268.18,"CZK":26.258,"AUD":1.5668,"RON":4.1405,"SEK":10.2215,"IDR":13281.14,"INR":66.21,"BRL":2.5309,"RUB":42.6974,"LTL":3.4528,"JPY":132.41,"THB":47.839,"CHF":1.4743,"SGD":2.0133,"PLN":4.0838,"BGN":1.9558,"TRY":2.1084,"CNY":9.8863,"NOK":8.1825,"NZD":1.9573,"ZAR":10.8264,"USD":1.4481,"MXN":18.4995,"EEK":15.6466,"GBP":0.8972,"KRW":1627.4,"MYR":4.8424,"HRK":7.2753},"base":"EUR","date":"2010-01-12"}
if not offline["base"] in offline["rates"]:
  offline["rates"][offline["base"]] = 1.0
  
def getOfflineRate(fromCurrency, toCurrency):
  try:
    res = copy.deepcopy(offline)
  
    res["base"] = fromCurrency
    rates = res["rates"]
    fromValue = rates[fromCurrency]
    for key in toCurrency:
      rates[key] = rates[key] / fromValue

    return res
  except Exception as e:
    raise Exception("Unable to find currency")




rateCalculators = {
  "api": getAPIRate,
  "offline": getAPIRate
}




def swapCurrency(value, fromCurrency, toCurrency, via):
  try:
    calculator = rateCalculators[via]
  except Exception as e:
    raise Exception("Cannot find source for " + via)
  
  res = calculator(fromCurrency, toCurrency)

  try:
    rates = res["rates"]
    values = {}
    for key in toCurrency:
      values[key] = rates[key] * value

    return {
      "rates": res["rates"],
      "values": values,
      "date": res["date"],
      "baseCurrency": fromCurrency,
      "baseValue": value
    }
  except Exception as e:
    raise Exception("Unknown error")

  
