import matplotlib.pyplot as plt
import json

def show_total_spend(username):
    with open(f'data/{username}_financial_data.json', 'r') as file:
        json_data = json.load(file)
        expenses = json_data['financial records'][-1]
        
    sum_spend_bank = expenses["bank"]["food"] + expenses["bank"]["other"] + expenses["bank"]["entertainment"]

    sum_spend_cash = expenses["cash"]["food"] + expenses["cash"]["other"] + expenses["cash"]["entertainment"]
    

    fig, ax = plt.subplots()
    ax.bar(['Bank', 'Cash'], [sum_spend_bank, sum_spend_cash])
    ax.set_ylabel('Total Spend')
    ax.set_title('Total Spend from Bank vs Cash')
    plt.savefig(f"graph/{username}_total_spend.png")





    