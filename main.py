import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
PREFIX = os.getenv("PREFIX")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

async def load_commands():
    print('aura plus ego')
    base = os.path.join(os.path.dirname(__file__), "commands")

    for file in os.listdir(base):
        if file.endswith(".py") and file != "__init__.py":
            ext = file[:-3]

            try:
                await bot.load_extension(f"commands.{ext}")
                print(f"[GB DEBUG - LOADED] {ext}")
            except Exception as e:
                print(f"[GB DEBUG - ERROR] Nao deu pra carregar {ext}: {e}")

async def setup_hook():
    await load_commands()

bot.setup_hook = setup_hook

@bot.event
async def on_ready():
    print(f"Bot ta como {bot.user}")

bot.run(TOKEN)
