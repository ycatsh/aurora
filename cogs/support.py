from discord.ext import commands 
import discord
import random
from aurora_lists import colors

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix = ".", case_insensitive=True, intents=intents)

class Support(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command(aliases=['credits', 'credit', 'creds'])
    async def cred(self, ctx):
        cred = discord.Embed(title="Credits and Information", description="Thank you for using this bot, I hope you had a great time!", color=0x40bd9b)
        cred.set_thumbnail(url="https://media.discordapp.net/attachments/807511480878497806/838063325568172062/info.png")
        cred.set_author(name="Molecule", url="https://www.youtube.com/channel/UCdNMAz_kPKrpp6ujliRLtLQ", icon_url="https://yt3.ggpht.com/ytc/AAUvwng1iHqfgIyaUVTmpRpYtxrpkHXY0WjqEvZ0KFeDMQ=s88-c-k-c0x00ffffff-no-rj")
        cred.add_field(name="My friends and other acquaintances ", value="Thank you for helping me with small problems and giving me ideas", inline=False)
        cred.add_field(name="Python discord server ", value="Website: https://pythondiscord.com/\nDiscord Server: https://discord.gg/python", inline=False)
        cred.add_field(name="Community & Support Server", value="Join Sever: [click here](https://discord.gg/G9vTrsV4aG)", inline=False)
        cred.add_field(name="To Vote", value="Use command: **``.vote``**", inline=False)

        cred.set_footer(text="Bot by Molecule | Owner")

        await ctx.send(embed=cred)

    @commands.command()
    async def vote(self, ctx):
        vote = discord.Embed(title="Vote for Aurora", desccription="", color= random.choice(colors))
        vote.add_field(name="top.gg", value="[Upvote](https://top.gg/bot/804228080952016897)", inline=False)
        vote.add_field(name="discordbotlist.com", value="[Upvote](https://discordbotlist.com/bots/aurora)", inline=False)
        vote.set_thumbnail(url="https://media.discordapp.net/attachments/807511480878497806/817463545368412221/Untitled_design3.png")
        vote.set_footer(text="Leave an honest review and upvote! ⬆ | Bot by Molecule")

        await ctx.send(embed=vote)

async def setup(bot):
    await bot.add_cog(Support(bot))
