# coding=utf-8
import urllib
import json
import requests
def occurenceOfSymbol(symbol):
    listOfSymbols = {'лв':'BGN','R$':'RBL',
        '¥':'CNY','£':'GBP','₪':'ILS','₩':'KRW',
        '₱':'PHP','฿':'THB','$':'USD',}
    if symbol in listOfSymbols:
        return listOfSymbols[symbol]
    else:
        return False

def buildRequest(base, symbol):
    baseUrl = 'http://api.fixer.io/latest'
    url =( baseUrl + '?base=' + base)
    if symbol:
        url +=( '&symbols=' + symbol)
    return url

def getCurrencyExchangeRates(base, symbol):
    url = buildRequest(base, symbol)
    response = requests.get(url)
    response.status_code
    exchangeRatesJSON = response.text
    exchangeRates = json.loads(exchangeRatesJSON)
    return exchangeRates

def validateCurrency(input):
    listOfCurrencies = ['AUD','CAD','CHF',
        'CNY','CZK','DKK','GBP','HKD','HRK','HUF',
        'IDR','ILS','INR','JPY','KRW','MXN','MYR',
        'NOK','NZD','PHP','PLN','RON','RUB','SEK',
        'SGD','THB','TRY','USD']
    if input not in listOfCurrencies:
        return False
    else:
        return True

