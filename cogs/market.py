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

class Market(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
    
    @commands.group(name="market", invoke_without_command=True)
    async def market(self, ctx):
        await ctx.send("UNDER DEV")

        cursor.execute("SELECT * FROM user_market WHERE client_id = %s", [ctx.author.id])
        result = cursor.fetchall()

        if len(result) == 0:
            cursor.execute("INSERT INTO user_market VALUES(%s, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)", [ctx.author.id])
            db.commit()

        mp = discord.Embed(title="MARKETPLACE", description="run ``.market info`` to learn more\nThe Following are the items you can buy from respective companies", color=random.choice(colors))
        mp.add_field(name="Essencery", value=f"Potato ─ 10 | *ID* → ``potato``\nCorn ─ 20 | *ID* → ``corn``\nCookies ─ 50 | *ID* → ``cookies``", inline = False)
        mp.add_field(name="Books & Co.", value=f"Pens ─ 5 | *ID* → ``pens``\nSheets ─ 10 | *ID* → ``sheets``\nManga ─ 1000 | *ID* → ``manga``", inline = False)
        mp.add_field(name="Utlity Mart", value=f"Screws ─ 20 | *ID* → ``screws``\nHammer ─ 400 | *ID* → ``hammer``\nPower Drill ─ 2000 | *ID* → ``pwrdrill``", inline = False)
        mp.add_field(name="Solitare", value=f"Gold ─ 10000 | *ID* → ``gold``\nPlatinum ─ 15000 | *ID* → ``plat``\nDiamond ─ 20000 | *ID* → ``diamond``", inline = False)
        mp.set_footer(text="run < .market buy id quantity > to buy these items")
        await ctx.send(embed=mp)

    @market.command(name="info")
    async def market_info(self, ctx): 
        await ctx.send("UNDER DEV")

        cursor.execute("SELECT * FROM user_market WHERE client_id = %s", [ctx.author.id])
        result = cursor.fetchall()

        if len(result) == 0:
            cursor.execute("INSERT INTO user_market VALUES(%s, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)", [ctx.author.id])
            db.commit()

        mi = discord.Embed(title="MARKETPLACE - INFO", description="⚠️ Please read the following carefully: every aspect of this is completely fictional and any refrences to real life is purely  coincidental", color=random.choice(colors))
        mi.add_field(name="Basic Idea", value="To be the richest, your main focus would be to become rich", inline = False)
        mi.add_field(name="How is it done?", value="by running ``.market`` you can buy items, This works in favor of the company selling the particular item. You can also invest in companies by ``.stocks``, keep in mind you can make/lose coins depending upon the company's stock prices", inline = False)
        mi.add_field(name="Basic things you need to know", value="If a certain item is bought alot its value is bound to decrease, which may be beneficial to the particular company selling this 'item' hence affecting its stock prices and Net Worth", inline = False)
        mi.add_field(name="A few Rules", value="``1.`` All transactions of coins are your responsibility\n``2.`` If you lose coins after investing, its again your responsibility and refunds will not be entertained", inline = False)
        await ctx.send(embed=mi)

    @market.command(name="buy")
    async def market_buy(self, ctx):
        await ctx.send("UNDER DEV")


    @commands.group(name="stocks", aliases = ["stock"], invoke_without_command=True)
    async def stocks(self, ctx):
        await ctx.send("UNDER DEV")


async def setup(bot):
    await bot.add_cog(Market(bot))
