from discord.ext import commands
from aurora_secrets import *
from aurora_lists import *
import discord
import random

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        help = discord.Embed(title='Welcome to the official Aurora discord bot', url="https://yashg.dev", description=" ", color=0x66c9ff)
        help.add_field(name="Here is the list of things you can do:", value=chr(173), inline=False)
        help.add_field(name="⚔️ ``.rpg``", value="Adventure\nGame", inline=True)
        help.add_field(name="🖼 ``.guess``", value=" Guessing\nGame", inline=True)
        help.add_field(name="🎮️ ``.games``", value="Mini\nGames", inline=True)
        help.add_field(name=chr(173), value="_ _", inline=False)
        help.add_field(name="🍦️ ``.fun``", value="Fun & Casual\nCommands", inline=True)
        help.add_field(name="🎗 ``.memories``", value="Summary\nof every year", inline=True)
        help.add_field(name="😂️ ``.meme``", value="Memes\nOnly", inline=True)
        help.add_field(name=chr(173), value="_ _", inline=False)
        help.add_field(name="📄️ ``.cred``", value="Credits\n& Info", inline=True)
        help.add_field(name="⚙️ ``.util``", value="Useful\nCommands", inline=True)
        help.add_field(name="👍️ ``.wait``", value="Coming\nSoon", inline=True)
        help.add_field(name=chr(173), value="[Join our support server](https://discord.gg/G9vTrsV4aG)", inline=False)
        help.set_thumbnail(url="https://media.discordapp.net/attachments/807511480878497806/832260603380498452/aurora_help.png")

        help.set_footer(text="Use the commands for more info 👍️ ")
        await ctx.send(embed=help)


    @commands.command()
    async def wait(self, ctx):
        await ctx.send("Patience is a virtue")


    @commands.command(aliases=['credits', 'credit', 'creds'])
    async def cred(self, ctx):
        cred = discord.Embed(title="Credits and Information", description="Thank you for using this bot, I hope you had a great time!", color=0x40bd9b)
        cred.set_thumbnail(url="https://media.discordapp.net/attachments/807511480878497806/838063325568172062/info.png")
        cred.set_author(name="Ycatsh", url="https://yashg.dev", icon_url="https://avatars.githubusercontent.com/u/91330011?v=4")
        cred.add_field(name="My friends and other acquaintances ",value="Thank you for helping me with small problems and giving me ideas", inline=False)
        cred.add_field(name="Python discord server ", value="Website: https://pythondiscord.com/\nDiscord Server: https://discord.gg/python", inline=False)
        cred.add_field(name="Community & Support Server", value="Join Sever: [click here](https://discord.gg/G9vTrsV4aG)", inline=False)
        cred.add_field(name="To Vote", value="Use command: **``.vote``**", inline=False)
        cred.set_footer(text="Bot by Ycatsh | Owner")

        await ctx.send(embed=cred)


    @commands.command()
    async def vote(self, ctx):
        vote = discord.Embed(title="Vote for Aurora", description="", color=random.choice(colors))
        vote.add_field(name="top.gg", value="[Upvote](https://top.gg/bot/804228080952016897)", inline=False)
        vote.add_field(name="discordbotlist.com", value="[Upvote](https://discordbotlist.com/bots/aurora)", inline=False)
        vote.set_thumbnail(url="https://media.discordapp.net/attachments/807511480878497806/817463545368412221/Untitled_design3.png")
        vote.set_footer(text="Leave an honest review and upvote! ⬆ | Bot by Molecule")

        await ctx.send(embed=vote)


async def setup(bot):
    await bot.add_cog(Info(bot))