import json

balance_bank = 10000000
balance_cash = 10000000

#create a financial data structure
financial_data = {
    "balance": [
        {"balance_bank": balance_bank},
        {"balance_cash": balance_cash}
    ],
    "spending": [
        {"bank": []},
        {"cash": []}
    ],
    "income": [
        {"bank": []},
        {"cash": []}
    ]
}

#save the financial data to a JSON file
with open('financial_data.json', 'w') as f:
    json.dump(financial_data, f, indent=4)