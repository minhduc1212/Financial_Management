import json

def change(username, change):

    #save the financial data to a JSON 
    with open(f'data/{username}_financial_data.json', 'r') as f:
        data = json.load(f)

    #change = "spend bank entertainment 50000"
    action, payment_method, category, amount = change.split()
    amount = int(amount)

    #spend
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

    #income
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
    with open(f'data/{username}_financial_data.json', 'w') as f:
        json.dump(data, f, indent=4)