import discord
import os
from dotenv import load_dotenv
from discord import app_commands
from discord.ext import commands
from create import create
from change import change as change_function

#get token from .env file
load_dotenv()
TOKEN = os.getenv('TOKEN')

#set up the bot with necessary intents
intents = discord.Intents.default()
intents.message_content = True
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
    create(balance_bank, balance_cash)
    await interaction.response.send_message(f'Financial data created with bank balance: {balance_bank} and cash balance: {balance_cash}')

@bot.tree.command(name="change", description="Change your financial data: spend or income with payment method, category, and amount")
async def change_financial_data(interaction: discord.Interaction, change: str):
    change_function(change)
    await interaction.response.send_message(f'Financial data updated with command: {change}')

bot.run(TOKEN)