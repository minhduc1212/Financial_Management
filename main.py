import json

balance_bank = 10000000
balance_cash = 10000000

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
with open('financial_data.json', 'w') as f:
    json.dump(financial_data, f, indent=4)
    
with open('financial_data.json', 'r') as f:
    data = json.load(f)
    
outcome = "spend bank entertainment 100000"
action, account, category, amount = outcome.split()
amount = int(amount)
if action == "spend":
    for item in data["spend"]:
        if account in item:
            for cat in item[account]:
                if category in cat:
                    cat[category] += amount
                    if account == "bank":
                        data["balance"][0]["balance_bank"] -= amount
                    elif account == "cash":
                        data["balance"][1]["balance_cash"] -= amount
                    break
            break
elif action == "income":
    for item in data["income"]:
        if account in item:
            item[account].append({category: amount})
            if account == "bank":
                data["balance"][0]["balance_bank"] += amount
            elif account == "cash":
                data["balance"][1]["balance_cash"] += amount
            break
#save the updated financial data back to the JSON file
with open('financial_data.json', 'w') as f:
    json.dump(data, f, indent=4)