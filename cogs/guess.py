from discord.ext import commands 
import discord
import mysql.connector
import random
import asyncio
from aurora_lists import colors, riddles, ball, ball_arg, roasts, rp, vb, ww, xp, coin, dpe, hpe, vpe, dash, qge, ebe, ame, woe, ate, dfe, hae, mbe

db = mysql.connector.connect(
    host='localhost', user="root", passwd="your_pwd", database="database_name", auth_plugin="mysql_native_password")

cursor = db.cursor()

bot = commands.Bot(command_prefix = ".", case_insensitive=True, intents=discord.Intents.default())

class Guess(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command()
    async def guess(self, ctx):
        embed = discord.Embed(title="Guessing Game",
                            description="You will see a part of an image or something from a franchise and you will have to guess what it is. **PICK ONE** by typing it down",
                            color=0xff8fa9)
        embed.add_field(name="<:pink:832279712151765002> Anime (.anime)", value="A scene or a character can be shown", inline=False)
        embed.add_field(name="<:pink:832279712151765002> Geography (.geo)", value="A popular place (it can be fictional)", inline=False)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/807511480878497806/833765293088047198/aurora_guess.png")
        embed.set_footer(text="Have a great time | Bot by Molecule")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def anime(self, ctx):

        x = random.randint(1, 57)
        y = random.randint(1, 57)

        if x>y:
            xy = random.randint(y, x)
        elif x<y:
            xy = random.randint(x, y)
        elif x == y:
            xy = x

        cursor.execute("select link, name from ganime where sn = %s", [xy])
        res = cursor.fetchall()

        image = res[0][0]
        ans = res[0][1]

        embed2 = discord.Embed(title="What's your Guess", color=0xffe433)
        embed2.set_image(url=image)
        embed2.set_footer(text="just type it down below | anyone can answer 👍")
        await ctx.channel.send(embed=embed2)

        while True:

            def check(message):

                return ctx.channel == message.channel

            answer = await bot.wait_for('message', check=check)

            if answer.content.lower() == ans:
                await answer.reply("**GOOD JOB!** type ``.anime`` to play again")
                break
            elif answer.content.lower() == ".anime":
                pass
                return


    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def geo(self, ctx):
        y = random.randint(1, 15)
        cursor.execute("select link, name from ggeo where sn = %s", [y])
        res = cursor.fetchall()

        image = res[0][0]
        ans = res[0][1]

        embed2 = discord.Embed(title="What's your Guess", color=0xffe433)
        embed2.set_image(url=image)
        embed2.set_footer(text="just type it down below | anyone can answer 👍")
        await ctx.channel.send(embed=embed2)

        while True:

            def check(message):

                return ctx.channel == message.channel

            answer = await bot.wait_for('message', check=check)

            if answer.content.lower() == ans:
                await answer.reply("**GOOD JOB!** type ``.geo`` to play again")
                break
            elif answer.content.lower() == ".geo":
                pass
                return

async def setup(bot):
    await bot.add_cog(Guess(bot))
