import json
def create(balance_bank, balance_cash):

    #create a financial data structure
    financial_data = {
        "balance": [
            {"balance_bank": balance_bank},
            {"balance_cash": balance_cash}
        ],
        "spend": [
            {"bank": [
            {"entertainment": 0},
            {"food": 0},
            {"other": 0}    
            ]},
            {"cash": [{"entertainment": 0},
            {"food": 0},
            {"other": 0}]}
        ],
        "income": [
            {"bank": []},
            {"cash": []}
        ]
    }

    #save the financial data to a JSON file
    with open('data/financial_data.json', 'w') as f:
        json.dump(financial_data, f, indent=4)