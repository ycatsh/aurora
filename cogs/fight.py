from discord.ext import commands
from aurora_secrets import *
from aurora_lists import *
import asyncio
import discord
import random

class Fight(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cursor = bot.cursor

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def fight(self, ctx):
        self.cursor.execute(
            "SELECT user_xp, user_level, user_coins, health, attack FROM users WHERE client_id = %s", [ctx.author.id])
        result = self.cursor.fetchall()

        checkhealth = result[0][3]
        checkattack = result[0][4]

        if len(result) == 0:
            self.cursor.execute(
                "INSERT INTO users VALUES(%s, 0, 0, 0, 0, 0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0)", [ctx.author.id])
            await ctx.send(f"{ctx.author.name} hasn't started playing, to learn more about the game please run ``.rpg info`` or just start by ``.quest``")
            db.commit()
        elif checkhealth == 0:
            await ctx.reply(":x: You can't fight with ``0`` health, buy ``Health Potions`` from the shop")
        elif checkattack == 0:
            await ctx.reply(":x: You can't fight with ``0`` attack level, buy ``Vigour Potions`` from the shop")
        else:
            rf = 1
            if rf == 2:
                await ctx.reply(":x: You searched everywhere but couldn't find a monster, run the command to try again")
            elif rf == 1:
                FightGameOver = 0
                oni = "<:a_oni:849354328468881418>"
                ml = 10
                mh = 50
                self.cursor.execute(
                    "select user_level from users where client_id = %s", [ctx.author.id])
                fightres = self.cursor.fetchall()
                ff = discord.Embed(title="", color=random.choice(colors))
                ff.set_author(name=f"{ctx.author.name} vs Oni",
                            icon_url=ctx.author.avatar.url)
                ff.set_thumbnail(
                    url="https://media.discordapp.net/attachments/807511480878497806/849354270477910026/New_Piskel5.png")
                ff.add_field(name="You will be fighting ``Oni`` also known as Hell",
                            value=f"Monster Info:\nHealth = 50\nLevel = 10", inline=False)
                ff.add_field(name="List of usable commands:", value="1. ``weapon <item_id>`` you can use weapons to damage the monster\n2. ``punch`` just uses your attack level for damage dealt\n3. ``end`` end the fight abruptly, you will lose 200xp and 2000 coins", inline=False)
                await ctx.send(embed=ff)

                flvl = fightres[0][0]
                if flvl > ml:

                    while True:

                        await ctx.reply(f"{ctx.author.name} your level is higher than the monster, please continue with a valid command in under 30s", mention_author=False)

                        def check(message):

                            return ctx.author == message.author and ctx.channel == message.channel

                        try:

                            fChoice = await self.bot.wait_for('message', check=check, timeout=30)

                            if fChoice.author == ctx.message.author:
                                if fChoice.content.lower() == "weapon qg":
                                    self.cursor.execute(
                                        "select health, quagun from users where client_id = %s", [ctx.author.id])
                                    fightres2 = self.cursor.fetchall()

                                    fightq = fightres2[0][1]

                                    if fightq == 0:
                                        fighth = fightres2[0][0]
                                        finalFighth = fighth/2
                                        self.cursor.execute("update users set health = %s where client_id = %s", [
                                                    finalFighth, ctx.author.id])
                                        await fChoice.reply("You don't have that item, you ended up losing ``50%`` of your health", mention_author=False)
                                        db.commit()
                                    else:
                                        finalFightq = fightq - 1
                                        mh = mh - 20
                                        self.cursor.execute("update users set quagun = %s where client_id = %s", [
                                                    finalFightq, ctx.author.id])
                                        await fChoice.reply("You damaged the monster, it ended up with ``30`` Health", mention_author=False)
                                        db.commit()

                                elif fChoice.content.lower() == "weapon eb":
                                    self.cursor.execute(
                                        "select health, enebazo from users where client_id = %s", [ctx.author.id])
                                    fightres3 = self.cursor.fetchall()

                                    fighte = fightres3[0][1]

                                    if fighte == 0:
                                        fighth2 = fightres3[0][0]
                                        finalFighth2 = fighth2/2
                                        self.cursor.execute("update users set health = %s where client_id = %s", [
                                                    finalFighth2, ctx.author.id])
                                        await fChoice.reply("You don't have that item, you ended up losing ``50%`` of your health", mention_author=False)
                                        db.commit()
                                    else:
                                        finalFighte = fighte - 1
                                        mh = mh - 75
                                        self.cursor.execute("update users set enebazo = %s where client_id = %s", [
                                                    finalFighte, ctx.author.id])
                                        db.commit()

                                        if mh > 0:
                                            await fChoice.reply(f"You damaged the monster, it ended up with ``{mh}`` Health", mention_author=False)

                                elif fChoice.content.lower() == "punch":
                                    self.cursor.execute(
                                        "select attack from users where client_id = %s", [ctx.author.id])
                                    fightres4 = self.cursor.fetchall()
                                    fighta = fightres4[0][0]

                                    if fighta == 0:
                                        await fChoice.reply("lmao your attack level is ``0``, you dealt no damage", mention_author=False)
                                    else:
                                        mh = mh - fighta
                                        if mh > 0:
                                            await fChoice.reply(f"You damaged the monster, it ended up with ``{mh}`` Health", mention_author=False)

                                elif fChoice.content.lower() == "end":

                                    self.cursor.execute(
                                        "select user_xp, user_coins from users where client_id = %s", [ctx.author.id])
                                    finalres = self.cursor.fetchall()
                                    lxp = finalres[0][0] - 200
                                    lc = finalres[0][1] - 2000

                                    if lxp < 0:
                                        lxp = 0

                                    if lc < 0:
                                        lc = 0

                                    self.cursor.execute("update users set user_xp = %s, user_coins = %s where client_id = %s", [
                                                lxp, lc, ctx.author.id])
                                    await ctx.send(f"{ctx.author.mention} You lost the fight! Losing {xp}200  {coin} 2000")
                                    db.commit()
                                    FightGameOver += 1

                                if mh <= 0:
                                    rxp = random.randint(500, 1000)
                                    rc = random.randint(5000, 8000)
                                    self.cursor.execute(
                                        "select user_xp, user_coins from users where client_id = %s", [ctx.author.id])
                                    fightOver = self.cursor.fetchall()

                                    newUserXP = fightOver[0][0] + rxp
                                    newUserC = fightOver[0][1] + rc

                                    newUserLVL = newUserXP/1000

                                    self.cursor.execute("update users set user_xp = %s, user_coins = %s, user_level = %s where client_id = %s", [
                                                newUserXP, newUserC, newUserLVL, ctx.author.id])

                                    await ctx.send(f" {ctx.author.mention} Good Job! You have defeated {oni} Oni\nYou Gained: {xp}{rxp}   {coin} {rc}")
                                    db.commit()
                                    break

                                elif FightGameOver == 1:
                                    break

                        except asyncio.TimeoutError:
                            await ctx.send(f"next time respond in under ``30s`` after the command is issued :skull:")
                            break

                elif flvl < ml:
                    await ctx.reply("The Monster has a higher level, dealing ``100`` damage to you", mention_author=True)
                    self.cursor.execute(
                        "select health from users where client_id = %s", [ctx.author.id])
                    lhealth = self.cursor.fetchall()

                    fhealth = lhealth[0][0] - 100

                    if fhealth <= 0:
                        await ctx.send(f"{ctx.author.mention} You lost the fight! Losing {xp}200  {coin} 2000")
                        self.cursor.execute(
                            "select user_xp, user_coins from users where client_id = %s", [ctx.author.id])
                        finalres = self.cursor.fetchall()
                        lxp = finalres[0][0] - 200
                        lc = finalres[0][1] - 2000

                        if lxp < 0:
                            lxp = 0

                        if lc < 0:
                            lc = 0

                        self.cursor.execute("update users set user_xp = %s, user_coins = %s, health= %s where client_id = %s", [
                                    lxp, lc, fhealth, ctx.author.id])
                        db.commit()
                        FightGameOver += 1
                    else:

                        self.cursor.execute("update users set health = %s where client_id = %s", [
                                    fhealth, ctx.author.id])
                        while True:

                            await ctx.send(f"{ctx.author.name} please continue with a valid command")

                            def check(message):

                                return ctx.author == message.author and ctx.channel == message.channel

                            try:

                                fChoice = await self.bot.wait_for('message', check=check, timeout=30)

                                if fChoice.author == ctx.message.author:
                                    if fChoice.content.lower() == "weapon qg":
                                        self.cursor.execute(
                                            "select health, quagun from users where client_id = %s", [ctx.author.id])
                                        fightres2 = self.cursor.fetchall()

                                        fightq = fightres2[0][1]

                                        if fightq == 0:
                                            fighth = fightres2[0][0]
                                            finalFighth = fighth/2
                                            self.cursor.execute("update users set health = %s where client_id = %s", [
                                                        finalFighth, ctx.author.id])
                                            await fChoice.reply("You don't have that item, you ended up losing ``50%`` of your health", mention_author=False)
                                            db.commit()
                                        else:
                                            finalFightq = fightq - 1
                                            mh = mh - 20
                                            self.cursor.execute("update users set quagun = %s where client_id = %s", [
                                                        finalFightq, ctx.author.id])
                                            await fChoice.reply("You damaged the monster, it ended up with ``30`` Health", mention_author=False)
                                            db.commit()

                                    elif fChoice.content.lower() == "weapon eb":
                                        self.cursor.execute(
                                            "select health, enebazo from users where client_id = %s", [ctx.author.id])
                                        fightres3 = self.cursor.fetchall()

                                        fighte = fightres3[0][1]

                                        if fighte == 0:
                                            fighth2 = fightres3[0][0]
                                            finalFighth2 = fighth2/2
                                            self.cursor.execute("update users set health = %s where client_id = %s", [
                                                        finalFighth2, ctx.author.id])
                                            await fChoice.reply("You don't have that item, you ended up losing ``50%`` of your health", mention_author=False)
                                            db.commit()
                                        else:
                                            finalFighte = fighte - 1
                                            mh = mh - 75
                                            self.cursor.execute("update users set enebazo = %s where client_id = %s", [
                                                        finalFighte, ctx.author.id])
                                            db.commit()

                                            if mh > 0:
                                                await fChoice.reply(f"You damaged the monster, it ended up with ``{mh}`` Health", mention_author=False)

                                    elif fChoice.content.lower() == "punch":
                                        self.cursor.execute(
                                            "select attack from users where client_id = %s", [ctx.author.id])
                                        fightres4 = self.cursor.fetchall()
                                        fighta = fightres4[0][0]

                                        if fighta == 0:
                                            await fChoice.reply("lmao your attack level is ``0``, you dealt no damage", mention_author=False)
                                        else:
                                            mh = mh - fighta
                                            if mh > 0:
                                                await fChoice.reply(f"You damaged the monster, it ended up with ``{mh}`` Health", mention_author=False)

                                    elif fChoice.content.lower() == "end":
                                        self.cursor.execute(
                                            "select user_xp, user_coins from users where client_id = %s", [ctx.author.id])
                                        finalres = self.cursor.fetchall()
                                        lxp = finalres[0][0] - 200
                                        lc = finalres[0][1] - 2000

                                        if lxp < 0:
                                            lxp = 0

                                        if lc < 0:
                                            lc = 0

                                        self.cursor.execute("update users set user_xp = %s, user_coins = %s where client_id = %s", [
                                                    lxp, lc, ctx.author.id])
                                        await ctx.send(f"{ctx.author.mention} You lost the fight! Losing {xp}200  {coin} 2000")
                                        FightGameOver += 1
                                        db.commit()

                                    if mh <= 0:
                                        rxp = random.randint(500, 1000)
                                        rc = random.randint(5000, 8000)
                                        self.cursor.execute(
                                            "select user_xp, user_coins from users where client_id = %s", [ctx.author.id])
                                        fightOver = self.cursor.fetchall()

                                        newUserXP = fightOver[0][0] + rxp
                                        newUserC = fightOver[0][1] + rc

                                        newUserLVL = newUserXP/1000

                                        self.cursor.execute("update users set user_xp = %s, user_coins = %s, user_level = %s where client_id = %s", [
                                                    newUserXP, newUserC, newUserLVL, ctx.author.id])

                                        await ctx.send(f" {ctx.author.mention} Good Job! You have defeated {oni} Oni\nYou Gained: {xp}{rxp}   {coin} {rc}")
                                        db.commit()
                                        break

                                    elif FightGameOver == 1:
                                        break
                            except asyncio.TimeoutError:
                                await ctx.send(f"next time respond in under ``30s`` after the command is issued :skull:")
                                break


async def setup(bot):
    await bot.add_cog(Fight(bot))