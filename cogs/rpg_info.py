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

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
  
    @commands.command(aliases = ['pf'])
    async def profile(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author

        cursor.execute("select user_level from users where client_id = %s", [user.id])
        result = cursor.fetchall()

        cursor.execute("select user_coins from users where client_id = %s", [user.id])
        result2 = cursor.fetchall()

        cursor.execute("select defense from users where client_id = %s", [user.id])
        result3 = cursor.fetchall()

        cursor.execute("select health from users where client_id = %s", [user.id])
        result4 = cursor.fetchall()

        cursor.execute("select attack from users where client_id = %s", [user.id])
        result5 = cursor.fetchall()

        cursor.execute("select dplayed, dwins from users where client_id = %s", [user.id])
        result6 = cursor.fetchall()
        
        if len(result2) == 0:
            await ctx.send(f"{user.name} hasn't started playing, to learn more about the game please run ``.rpg info`` or just start by ``.quest``")
        else:

            moni = result2[0][0]
            lvl = result[0][0]
            deflvl = result3[0][0]
            heallvl = result4[0][0]
            attcklvl = result5[0][0]
            duelstatsplayed = result6[0][0]
            duelstatswon = result6[0][1]

            if duelstatsplayed == 0:

                pfp = discord.Embed(description="", color=random.choice(colors))
                pfp.set_author(name=f"{user.name}'s Profile", icon_url=user.avatar_url)
                pfp.add_field(name="MULTIPLAYER: _ _", value=f"**Duels**\nPlayed: 0\nWon: 0\nWin%: 0.0", inline=True)
                pfp.add_field(name="RPG PROGRESS:", value=f"{xp} Levels: {lvl}\n{coin} Coins: {moni} ", inline=True)
                pfp.add_field(name="STATS:", value=f"{ate} Attack: {attcklvl}\n{dfe} Defense: {deflvl}\n{hae} Health: {heallvl}", inline = False)
                pfp.set_thumbnail(url=user.avatar_url)
                await ctx.send(embed=pfp)
            else:
                
                winn = round((duelstatswon/duelstatsplayed) * 100)

                pfp = discord.Embed(description="", color=random.choice(colors))
                pfp.set_author(name=f"{user.name}'s Profile", icon_url=user.avatar_url)
                pfp.add_field(name="MULTIPLAYER: _ _", value=f"**Duels**\nPlayed: {duelstatsplayed}\nWon: {duelstatswon}\nWin Rate: {winn}%", inline=True)
                pfp.add_field(name="RPG PROGRESS:", value=f"{xp} Levels: {lvl}\n{coin} Coins: {moni} ", inline=True)
                pfp.add_field(name="STATS:", value=f"{ate} Attack: {attcklvl}\n{dfe} Defense: {deflvl}\n{hae} Health: {heallvl}", inline = False)
                pfp.set_thumbnail(url=user.avatar_url)
                await ctx.send(embed=pfp)
            

    @commands.group(name="inv", invoke_without_command=True)
    async def inv(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author

        cursor.execute("select durapot, healpot, vigopot, quagun, enebazo, molecule, orb, box from users where client_id = %s", [user.id])
        result = cursor.fetchall()

        if len(result) == 0:
            await ctx.send("Just Started? run ``.rpg info`` to learn more about the game 👌️")
        else:
            dpi = result[0][0]
            hpi = result[0][1]
            vpi = result[0][2]
            qgi = result[0][3]
            ebi = result[0][4]
            moi = result[0][5]
            ori = result[0][6]
            boi = result[0][7]

            pf = discord.Embed(title="", description="", color=random.choice(colors))
            pf.set_author(name=f"{user.name}'s inventory", icon_url=user.avatar_url)
            pf.add_field(name="Items:", value=f"{dpe} Durability Potions ─ {dpi}\nID → ``dp``\n_ _", inline=True)
            pf.add_field(name="    _ _ ", value=f"    _ _", inline=True)
            pf.add_field(name="Collectibles", value=f"{ame} Molecule ─ {moi}\nID → ``molecule``", inline=True)
            pf.add_field(name="_ _", value=f"{hpe} Health Potions ─ {hpi}\nID → ``hp``\n_ _", inline = True)
            pf.add_field(name="    _ _ ", value=f"    _ _", inline=True)
            pf.add_field(name="Market Items", value=f"UNDER DEV", inline=True)
            pf.add_field(name="_ _", value=f"{vpe} Vigour Potions ─ {vpi}\nID → ``vp``\n_ _", inline = False)
            pf.add_field(name="_ _", value=f"{woe} Witch's Orbs ─ {ori}\nID → ``orb``\n_ _", inline=False)
            pf.add_field(name="_ _", value=f"{qge} Quantum Guns ─ {qgi}\nID → ``qg``\n_ _", inline = False)
            pf.add_field(name="_ _", value=f"{ebe} Energy Bazookas ─ {ebi}\nID → ``eb``\n_ _", inline = False)
            pf.add_field(name="_ _", value=f"{mbe} Mystery Boxes ─ {boi}\nID → ``box``\n_ _", inline = False)
            
            await ctx.send(embed=pf)

    @commands.command()
    async def deletemydata(self, ctx):
        dmd = discord.Embed(color=random.choice(colors))
        dmd.add_field(name="Delete your info", value=f"{ctx.author.mention} ARE YOU SURE YOU WANT TO CONTINUE?\nDoing this will get rid of all your info in our database\nType ``yes`` under ``10s`` to continue with the deletion")
        await ctx.send(embed=dmd)

        def check(message):

            return ctx.author == message.author and ctx.channel == message.channel

        try:

            ans = await bot.wait_for('message', check=check, timeout=10)
            

            if ans.author == ctx.message.author:
                if ans.content.lower() == "yes":
                    cursor.execute("delete from users where client_id = %s", [ctx.author.id])
                    db.commit()
                    
                    await ctx.send(f"``🟢 SUCCESSFUL - {ctx.author.name} your data has been deleted``")
                else:
                    await ctx .send(f"``🔴 NOT SUCCESSFUL - {ctx.author.name} you failed to answer correctly``")
        except asyncio.TimeoutError:
            await ctx.send(f"``🔴 NOT SUCCESSFUL - {ctx.author.name} you failed to answer in time``")

async def setup(bot):
    await bot.add_cog(Info(bot))