import json


#save the financial data to a JSON file
with open('data/financial_data.json', 'r') as f:
    data = json.load(f)
    
outcome = "spend bank entertainment 100000"
action, payment_method, category, amount = outcome.split()
amount = int(amount)
if action == "spend":
    for item in data["spend"]:
        if payment_method in item:
            for cat in item[payment_method]:
                if category in cat:
                    cat[category] += amount
                    if payment_method == "bank":
                        data["balance"][0]["balance_bank"] -= amount
                    elif payment_method == "cash":
                        data["balance"][1]["balance_cash"] -= amount
                    break
            break
elif action == "income":
    for item in data["income"]:
        if payment_method in item:
            item[payment_method].append({category: amount})
            if payment_method == "bank":
                data["balance"][0]["balance_bank"] += amount
            elif payment_method == "cash": 
                data["balance"][1]["balance_cash"] += amount
            break
        
#save the updated financial data back to the JSON file
with open('data/financial_data.json', 'w') as f:
    json.dump(data, f, indent=4)