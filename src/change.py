import json
import datetime

def change(username, change):

    #save the financial data to a JSON 
    with open(f'data/{username}_financial_data.json', 'r') as f:
        data = json.load(f)

    #change = "- bank entertainment 50000"
    action, payment_method, category, amount = change.split()
    
    #if change in diff month, add new month to datas
    x = datetime.datetime.now()
    period = x.strftime("%Y-%m")
    if period != data["financial records"][0]["period"]:
        new_month ={
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
                        "salary": 0.0,
                        "other": 0.0

                    },
                    "cash": 
                    {
                        "salary": 0.0,
                        "other": 0.0
                    }
                }
            }
        data["financial records"].append(new_month)
    
    #convert amount to int
    amount = int(amount)
    
    #for the action change in expenses
    if action == "-":
        #check whether payment method in the expenses
        data["financial records"][-1]["expenses"][payment_method][category]+= amount
    elif action == "+":
        #check whether payment method in the income
        data["financial records"][-1]["income"][payment_method][category]+= amount

            
    #save the updated financial data back to the JSON file
    with open(f'data/{username}_financial_data.json', 'w') as f:
        json.dump(data, f, indent=4)