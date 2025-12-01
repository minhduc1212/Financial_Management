import matplotlib.pyplot as plt
import json

def show_total_spend(username):
    with open(f'data/{username}_financial_data.json', 'r') as file:
        json_data = json.load(file)
        spend = json_data['spend']
        
    sum_spend_bank = 0
    for item in spend[0]["bank"]:
        for category, amount in item.items():
            sum_spend_bank += amount

    sum_spend_cash = 0
    for item in spend[1]["cash"]:
        for category, amount in item.items():
            sum_spend_cash += amount

    fig, ax = plt.subplots()
    ax.bar(['Bank', 'Cash'], [sum_spend_bank, sum_spend_cash])
    ax.set_ylabel('Total Spend')
    ax.set_title('Total Spend from Bank vs Cash')
    plt.savefig(f"graph/{username}_total_spend.png")





    