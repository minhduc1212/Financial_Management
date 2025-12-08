import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from src.create import create
from src.change import change as change_function
from src.show import show_total_spend

#get token from .env file
load_dotenv()
TOKEN = os.getenv('TOKEN')

#set up the bot with necessary intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="?", intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(e)

@bot.tree.command(name="create", description="Create your present balance")
async def create_balance(interaction: discord.Interaction, balance_bank: float, balance_cash: float):
    create(interaction.user.name, balance_bank, balance_cash)
    await interaction.response.send_message(f'Financial data created with bank balance: {balance_bank} and cash balance: {balance_cash}')

@bot.tree.command(name="change", description="Change your financial data: spend or income with payment method, category, and amount")
async def change_financial_data(interaction: discord.Interaction, change: str):
    change_function(interaction.user.name, change)
    await interaction.response.send_message(f'Financial data updated with command: {change}')

@bot.tree.command(name="show_total_spend", description="Show total spend from bank and cash in lastest month")
async def show_spend(interaction: discord.Interaction):
    show_total_spend(interaction.user.name)
    await interaction.response.send_message(f'Total spend chart generated and saved as {interaction.user.name}_total_spend.png')
    with open(f"graph/{interaction.user.name}_total_spend.png", "rb") as file:
        picture = discord.File(file)
        await interaction.followup.send(file=picture)
    
bot.run(TOKEN)