import discord
from discord.ext import commands
import asyncio
import os

intents = discord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix = ".", case_insensitive=True, intents=intents)

bot.remove_command('help')
token = os.environ.get('TOKEN')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('.help'))
    print(f"Servers: {len(bot.guilds)}")
    print('STATUS: Running')

async def load_extensions():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def start():
    async with bot:
        await load_extensions()
        await bot.start(token)

asyncio.run(start())
