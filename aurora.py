from discord.ext import commands
from aurora_secrets import *
from aurora_lists import *
import discord
import asyncio
import os 

cursor = db.cursor()

intents = discord.Intents.all()
intents.messages = True

class Aurora(commands.Bot):
    def __init__(self, command_prefix, case_insensitive, intents, cursor):
        super().__init__(command_prefix=command_prefix, case_insensitive=case_insensitive, intents=intents)
        self.cursor = cursor

bot = Aurora(command_prefix=".", case_insensitive=True, intents=intents, cursor=cursor)
bot.remove_command("help")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('.help'))
    print(f"Servers: {len(bot.guilds)}")
    print(f'Connected to bot: {bot.user.name}')
    print('STATUS: Running')


async def load():
    for file_name in os.listdir('./cogs'):
        if file_name.endswith('.py'):
            await bot.load_extension(f'cogs.{file_name[:-3]}')

async def main():
    async with bot:
        await load()
        await bot.start(DISCORD_TOKEN)

asyncio.run(main())