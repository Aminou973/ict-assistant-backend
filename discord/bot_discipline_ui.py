import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from responses_discipline import get_discipline_score

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# ID du thread 🧵 journal-discipline
DISCIPLINE_THREAD_ID = 1360251872363151590

@bot.event
async def on_ready():
    print(f"✅ Bot connecté en tant que {bot.user}")
    channel = bot.get_channel(DISCIPLINE_THREAD_ID)
    if channel:
        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="📊 Evaluer Discipline", style=discord.ButtonStyle.primary, custom_id="evaluate_discipline_button"))
        await channel.send("🧠 Clique ci-dessous pour évaluer ta discipline du jour :", view=view)

@bot.event
async def on_interaction(interaction: discord.Interaction):
    if interaction.data.get("custom_id") == "evaluate_discipline_button":
        # Simule une évaluation exemple (à remplacer plus tard par interface interactive)
        message = get_discipline_score(
            plan_respected=True,
            risk_respected=False,
            tilt_detected=True
        )
        await interaction.response.send_message(message, ephemeral=False)

bot.run(TOKEN)