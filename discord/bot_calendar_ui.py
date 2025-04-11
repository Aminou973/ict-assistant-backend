import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from responses_calendar import get_daily_calendar_message

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# ID du thread calendrier
CALENDAR_THREAD_ID = 1360252054987083918

@bot.event
async def on_ready():
    print(f"✅ Bot connecté en tant que {bot.user}")
    channel = bot.get_channel(CALENDAR_THREAD_ID)
    if channel:
        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="📆 Disponible aujourd’hui", style=discord.ButtonStyle.success, custom_id="available_today_button"))
        await channel.send("📋 Clique si tu es dispo pour trader aujourd’hui :", view=view)

@bot.event
async def on_interaction(interaction: discord.Interaction):
    if interaction.data.get("custom_id") == "available_today_button":
        msg = get_daily_calendar_message()
        await interaction.response.send_message(msg, ephemeral=False)

bot.run(TOKEN)