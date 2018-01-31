#!/usr/bin/python
# coding=utf-8
import argparse
from converter_helpers import getCurrencyExchangeRates,occurenceOfSymbol, validateCurrency
import json

parser = argparse.ArgumentParser(description='This is a converter for currencies')
parser.add_argument('--amount', help='Amount which you want to convert', required=True, type=float)
parser.add_argument('--input_currency', required=True)
parser.add_argument('--output_currency',  required=False)
args = parser.parse_args()

amount = args.amount
if amount == None:
    print("Invalid amount.This field cannot be empty. ")
    exit()

input_currency = args.input_currency
output_currency = args.output_currency

if occurenceOfSymbol(input_currency):
    input_currency = occurenceOfSymbol(input_currency)
if validateCurrency(input_currency) == False:
      print("Incorrect input.You must enter valid currency symbol1.")
      exit()

if occurenceOfSymbol(output_currency):
    output_currency = occurenceOfSymbol(output_currency)
if (output_currency != None):
    if validateCurrency(output_currency) == False:
        print("Incorrect output.You must enter valid currency symbol.")
        exit()

exchangeRates = getCurrencyExchangeRates(input_currency, output_currency)
if exchangeRates == False:
    exit()

response = {
    'input': {},
    'output': {},
}

response['input'] = {
    'amount': amount,
    'currency': input_currency,
}

for key, rate in exchangeRates['rates'].items():
    response['output'][key] = round(rate * amount, 2)

response = json.dumps(response, sort_keys=True, indent=4)

print(response)