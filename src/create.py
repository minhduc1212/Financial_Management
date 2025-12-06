import json
import os
import datetime

def create(username,balance_bank, balance_cash):
    
    x = datetime.datetime.now()
    period = x.strftime("%Y-%m")

    #create a financial data structure
    financial_data = {
        "balance": [
            {
            "balance_bank": balance_bank
            },
            {
            "balance_cash": balance_cash
            }
        ],
        "financial records":[
            {
                "period": period,
                "expenses": 
                { 
                    "bank":
                    {
                        "entertainment": 0.0,
                        "food": 0.0,
                        "other": 0.0
                    },
                    "cash":
                    {
                        "entertainment": 0.0,
                        "food": 0.0,
                        "other": 0.0
                    }
                },
                "income": 
                {
                    "bank": 
                    {
                        "salary": 0,
                        "other": 0.0

                    },
                    "cash": 
                    {
                        "salary": 0,
                        "other": 0.0
                    }
                }
            }
        ]
    }

    #save the financial data to a JSON file
    with open(f'data/{username}_financial_data.json', 'w') as f:
        json.dump(financial_data, f, indent=4)