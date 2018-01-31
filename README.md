# currency_converter_CLI
My solution to Kiwi.com task.Simple CLI currency_converter.

## Parameters
You will need to provide:
- Amount - amount which we want to convert - float
- Input - input currency - 3 letters name or currency symbol
- Output(optional) - requested/output currency - 3 letters name or currency symbol

## Example

```./currency_converter.py --amount 100.0 --input_currency EUR --output_currency CZK

{   
    "input": {
        "amount": 100.0,
        "currency": "EUR"
    },
    "output": {
        "CZK": 2707.36, 
    }
}
```
