import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from responses import (
    get_start_day_message,
    get_log_trade_message,
    get_rex_daily_message,
    get_rex_weekly_message
)
from responses_discipline import get_discipline_score
from responses_calendar import get_daily_calendar_message

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Threads cibles
COMMAND_CENTER_ID = 1360251758168903792
DISCIPLINE_THREAD_ID = 1360251872363151590
CALENDAR_THREAD_ID = 1360252054987083918

@bot.event
async def on_ready():
    print(f"✅ Bot connecté en tant que {bot.user}")

    # Command Center (boutons principaux)
    command_center = bot.get_channel(COMMAND_CENTER_ID)
    if command_center:
        view1 = discord.ui.View()
        view1.add_item(discord.ui.Button(label="📋 Start Day", style=discord.ButtonStyle.primary, custom_id="start_day_button"))
        view1.add_item(discord.ui.Button(label="🖊️ Log Trade", style=discord.ButtonStyle.secondary, custom_id="log_trade_button"))
        view1.add_item(discord.ui.Button(label="📘 End of Day", style=discord.ButtonStyle.success, custom_id="end_day_button", row=1))
        view1.add_item(discord.ui.Button(label="📊 End of Week", style=discord.ButtonStyle.danger, custom_id="end_week_button", row=1))
        await command_center.send("🧠 Assistant IA Ready - Actions disponibles :", view=view1)

    # Journal Discipline
    journal = bot.get_channel(DISCIPLINE_THREAD_ID)
    if journal:
        view2 = discord.ui.View()
        view2.add_item(discord.ui.Button(label="📊 Evaluer Discipline", style=discord.ButtonStyle.primary, custom_id="evaluate_discipline_button"))
        await journal.send("📋 Clique pour évaluer ta discipline du jour :", view=view2)

    # Calendrier
    calendar = bot.get_channel(CALENDAR_THREAD_ID)
    if calendar:
        view3 = discord.ui.View()
        view3.add_item(discord.ui.Button(label="📆 Disponible aujourd’hui", style=discord.ButtonStyle.success, custom_id="available_today_button"))
        await calendar.send("📋 Clique si tu es dispo pour trader aujourd’hui :", view=view3)

@bot.event
async def on_interaction(interaction: discord.Interaction):
    cid = interaction.data.get("custom_id")
    if cid == "start_day_button":
        await interaction.response.send_message(get_start_day_message(), ephemeral=False)
    elif cid == "log_trade_button":
        await interaction.response.send_message(get_log_trade_message(), ephemeral=False)
    elif cid == "end_day_button":
        await interaction.response.send_message(get_rex_daily_message(), ephemeral=False)
    elif cid == "end_week_button":
        await interaction.response.send_message(get_rex_weekly_message(), ephemeral=False)
    elif cid == "evaluate_discipline_button":
        message = get_discipline_score(
            plan_respected=True,
            risk_respected=False,
            tilt_detected=True
        )
        await interaction.response.send_message(message, ephemeral=False)
    elif cid == "available_today_button":
        msg = get_daily_calendar_message()
        await interaction.response.send_message(msg, ephemeral=False)

bot.run(TOKEN)