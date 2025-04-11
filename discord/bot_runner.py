import discord
import os
from discord.ext import commands
from discord_config import WEBHOOK_URL
from responses import get_start_day_message

TOKEN = os.getenv("DISCORD_BOT_TOKEN")  # Set this in Railway

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot connecté en tant que {bot.user}")

    # Trouver le canal de command-center par ID
    channel_id = 1360251758168903792  # 🧵 command-center
    channel = bot.get_channel(channel_id)

    if channel:
        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="📋 Démarrer la Journée", style=discord.ButtonStyle.primary, custom_id="start_day_button"))

        await channel.send("**Assistant IA Ready** 🚀\nClique sur le bouton pour démarrer la journée :", view=view)

@bot.event
async def on_interaction(interaction: discord.Interaction):
    if interaction.data.get("custom_id") == "start_day_button":
        await interaction.response.send_message(get_start_day_message(), ephemeral=False)

bot.run(TOKEN)