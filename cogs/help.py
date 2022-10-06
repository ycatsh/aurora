from discord.ext import commands 
import discord

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(invoke_without_command=True)
    async def help(self, ctx):
        help = discord.Embed(title='Welcome to the Official Aurora BOT', url="https://www.youtube.com/channel/UCdNMAz_kPKrpp6ujliRLtLQ", description=" ", color=0x66c9ff)
        help.add_field(name="Here is the list of things you can do:", value=chr(173), inline=False)
        help.add_field(name="⚔️ ``.rpg``", value="Adventure\nGame", inline=True)
        help.add_field(name="🖼 ``.guess``", value=" Guessing\nGame", inline=True)
        help.add_field(name="🎮️ ``.games``", value="Mini\nGames", inline=True)
        help.add_field(name=chr(173), value="_ _", inline=False)
        help.add_field(name="🍦️ ``.fun``", value="Fun & Casual\nCommands", inline=True)
        help.add_field(name="🎗 ``.wait``", value="Coming\nSoon", inline=True)
        help.add_field(name="😂️ ``.meme``", value="Memes\nOnly", inline=True)
        help.add_field(name=chr(173), value="_ _", inline=False)
        help.add_field(name="📄️ ``.cred``", value="Credits\n& Info", inline=True)
        help.add_field(name="⚙️ ``.util``", value="Useful\nCommands", inline=True)
        help.add_field(name="👍️ ``.wait``", value="Coming\nSoon", inline=True)
        help.add_field(name=chr(173), value="[Join our support server](https://discord.gg/G9vTrsV4aG)", inline = False)
        help.set_thumbnail(url="https://media.discordapp.net/attachments/807511480878497806/832260603380498452/aurora_help.png")

        help.set_footer(text="Use the commands for more info 👍️ ")
        await ctx.send(embed=help)


async def setup(bot):
    await bot.add_cog(Help(bot))