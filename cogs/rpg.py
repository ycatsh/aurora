from discord.ext import commands
from aurora_secrets import *
from aurora_lists import *
import discord
import random


class RPG_START(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cursor = bot.cursor

    @commands.group(name="rpg", invoke_without_command=True)
    async def rpg(self, ctx):
        rpg = discord.Embed(title="RPG GAME (UNDER DEV)", description="The following are the commands which you can use\n **run ``.rpg info`` to learn more about the game**\n_ _", color=0x99ffd3)
        rpg.set_thumbnail(url="https://media.discordapp.net/attachments/807511480878497806/834121432849973288/rpg.png")
        rpg.add_field(name="_ _", value="_ _", inline=False)
        rpg.add_field(name="📈️ __MARKETPLACE__ (UNDER DEV)", value="``.market info`` ``.market`` ``.stocks``", inline=False)
        rpg.add_field(name="🎖️ __LEVELING__", value="``.quest`` ``.train`` ``.fight``", inline=True)
        rpg.add_field(name="_ _", value="_ _", inline=True)
        rpg.add_field(name="🗡️ __MULTIPLAYER__", value="``.duel``", inline=True)
        rpg.add_field(name="📂️ __PROGRESS__", value="``.profile`` ``.inv``", inline=True)
        rpg.add_field(name="_ _", value="_ _", inline=True)
        rpg.add_field(name="🛒️ __SHOPPING__", value="``.shop`` ``.buy`` ``.use``", inline=True)
        rpg.add_field(name="💸️ __GAMBLING__", value="``.highlow`` ``.slots``", inline=True)
        rpg.add_field(name="_ _", value="_ _", inline=True)
        rpg.add_field(name="📮️ __SETTINGS__", value="``.deletemydata``", inline=True)
        rpg.set_footer(text="First step to start playing, run .quest")

        await ctx.send(embed=rpg)


    @rpg.command(name="info")
    async def rpg_info(self, ctx):
        info = discord.Embed(title="RPG GAME INFO (UNDER DEV)", description="The main objective is to gain xp and levels to unlock various items and to move forward in the game\n**first ting you must do is go on your first adventure! run ``.quest``**", color=0x787878)
        info.add_field(name="__GAME FEATURES__", value="→ Earn COINS and XP with ``.quest`` ``.train``. Fight monsters with ``.fight``\n→ Check your data and progess with ``.profile``", inline=False)
        info.add_field(name="__MARKETPLACE__ (UNDER DEV)", value="→ Trade stocks of different hypothetical companies to earn money.\nrun ``.market info`` to learn more", inline=False)
        info.add_field(name="__SHOP INFO__", value="→ To buy items like weapons or potions use ``.shop``\n→The items can only be bought by COINS", inline=False)
        info.add_field(name="__GAMBLING__", value="→ To earn more money (coins) use ``.highlow`` ``.slots``\n→ You can only earn COINS not XP")
        info.add_field(name="__OTHER FEATURES__", value="→ Multiplayer\n To play with your friends: ``.duel``", inline=False)
        info.set_footer(text="Enjoy your time 👍")
        await ctx.send(embed=info)


    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def quest(self, ctx):
        COINS = random.randint(5, 20)
        XP = random.randint(20, 80)
        x = random.randint(1, 500)
        y = random.choice(creatures)
        a = random.choice(phrases)

        if x == 50:
            y = "<:rpgdragon:834847137242021889> dragon"
            XP = 2000
            COINS = 1000

        await ctx.send(f"{ctx.author.mention}, {a}\n{y}\n**{xp}XP:** {XP}  **{coin} COINS:** {COINS}")
        
        self.cursor.execute("SELECT user_xp, user_level, user_coins FROM users WHERE client_id = %s", [ctx.author.id])
        result = self.cursor.fetchall()

        if len(result) == 0:
            self.cursor.execute("INSERT INTO users VALUES(%s, %s, 0, %s, 0, 0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0)", [ctx.author.id, XP, COINS])
            db.commit()

        else:

            newXP = result[0][0] + XP
            currentLevel = result[0][1]
            newCoins = result[0][2] + COINS

            if newXP > 0:
                currentLevel = newXP/1000

            self.cursor.execute("UPDATE users SET user_xp = %s, user_level = %s, user_coins = %s WHERE client_id = %s", [newXP, currentLevel, newCoins, ctx.author.id])
            db.commit()

    @commands.command(aliases=['pf'])
    async def profile(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author

        self.cursor.execute("select user_level from users where client_id = %s", [user.id])
        result = self.cursor.fetchall()

        self.cursor.execute("select user_coins from users where client_id = %s", [user.id])
        result2 = self.cursor.fetchall()

        self.cursor.execute("select defense from users where client_id = %s", [user.id])
        result3 = self.cursor.fetchall()

        self.cursor.execute("select health from users where client_id = %s", [user.id])
        result4 = self.cursor.fetchall()

        self.cursor.execute("select attack from users where client_id = %s", [user.id])
        result5 = self.cursor.fetchall()

        self.cursor.execute("select dplayed, dwins from users where client_id = %s", [user.id])
        result6 = self.cursor.fetchall()

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
                pfp.set_author(name=f"{user.name}'s Profile",icon_url=user.avatar.url)
                pfp.add_field(name="MULTIPLAYER: _ _",value=f"**Duels**\nPlayed: 0\nWon: 0\nWin%: 0.0", inline=True)
                pfp.add_field(name="RPG PROGRESS:", value=f"{xp} Levels: {lvl}\n{coin} Coins: {moni} ", inline=True)
                pfp.add_field(name="STATS:", value=f"{ate} Attack: {attcklvl}\n{dfe} Defense: {deflvl}\n{hae} Health: {heallvl}", inline=False)
                pfp.set_thumbnail(url=user.avatar.url)
                
                await ctx.send(embed=pfp)

            else:

                winn = round((duelstatswon/duelstatsplayed) * 100)

                pfp = discord.Embed(description="", color=random.choice(colors))
                pfp.set_author(name=f"{user.name}'s Profile",icon_url=user.avatar.url)
                pfp.add_field(name="MULTIPLAYER: _ _",value=f"**Duels**\nPlayed: {duelstatsplayed}\nWon: {duelstatswon}\nWin Rate: {winn}%", inline=True)
                pfp.add_field(name="RPG PROGRESS:", value=f"{xp} Levels: {lvl}\n{coin} Coins: {moni} ", inline=True)
                pfp.add_field(name="STATS:", value=f"{ate} Attack: {attcklvl}\n{dfe} Defense: {deflvl}\n{hae} Health: {heallvl}", inline=False)
                pfp.set_thumbnail(url=user.avatar.url)
                
                await ctx.send(embed=pfp)


    @commands.group(name="inv", invoke_without_command=True)
    async def inv(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author

        self.cursor.execute("select durapot, healpot, vigopot, quagun, enebazo, molecule, orb, box from users where client_id = %s", [user.id])
        result = self.cursor.fetchall()

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
            pf.set_author(name=f"{user.name}'s inventory", icon_url=user.avatar.url)
            pf.add_field(name="Items:", value=f"{dpe} Durability Potions ─ {dpi}\nID → ``dp``\n_ _", inline=True)
            pf.add_field(name="    _ _ ", value=f"    _ _", inline=True)
            pf.add_field(name="Collectibles", value=f"{ame} Molecule ─ {moi}\nID → ``molecule``", inline=True)
            pf.add_field(name="_ _", value=f"{hpe} Health Potions ─ {hpi}\nID → ``hp``\n_ _", inline=True)
            pf.add_field(name="    _ _ ", value=f"    _ _", inline=True)
            pf.add_field(name="Market Items", value=f"UNDER DEV", inline=True)
            pf.add_field(name="_ _", value=f"{vpe} Vigour Potions ─ {vpi}\nID → ``vp``\n_ _", inline=False)
            pf.add_field(name="_ _", value=f"{woe} Witch's Orbs ─ {ori}\nID → ``orb``\n_ _", inline=False)
            pf.add_field(name="_ _", value=f"{qge} Quantum Guns ─ {qgi}\nID → ``qg``\n_ _", inline=False)
            pf.add_field(name="_ _", value=f"{ebe} Energy Bazookas ─ {ebi}\nID → ``eb``\n_ _", inline=False)
            pf.add_field(name="_ _", value=f"{mbe} Mystery Boxes ─ {boi}\nID → ``box``\n_ _", inline=False)

            await ctx.send(embed=pf)


    @commands.command()
    @commands.cooldown(1, 45, commands.BucketType.user)
    async def train(self, ctx):
        q1 = ["https://cdn.discordapp.com/attachments/1057267168846299196/1057267285473103912/pink.png", "https://cdn.discordapp.com/attachments/1057267168846299196/1057267285850607636/yellow.png", "https://cdn.discordapp.com/attachments/1057267168846299196/1057267286290993153/blue.png", "https://cdn.discordapp.com/attachments/1057267168846299196/1057267286668496966/green.png"]
        a = random.choice(q1)
        XP = random.randint(150, 250)
        COIN = random.randint(75, 125)

        col = discord.Embed(title="", description="")
        col.add_field(name="_ _", value="**identify this color →**")
        col.set_thumbnail(url=a)

        await ctx.reply(embed=col, mention_author=False)

        self.cursor.execute("SELECT user_xp, user_level, user_coins FROM users WHERE client_id = %s", [ctx.author.id])
        result = self.cursor.fetchall()

        if len(result) == 0:
            self.cursor.execute("INSERT INTO users VALUES(%s, 0, 0, 0, 0, 0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0)", [ctx.author.id])
            db.commit()

        def check(message):

            return ctx.author == message.author and ctx.channel == message.channel

        anscol = await self.bot.wait_for('message', check=check)

        if anscol.author == ctx.message.author:

            if a == "https://media.discordapp.net/attachments/807511480878497806/835889048731385887/blue.png":
                if anscol.content.lower() == "blue":
                    await ctx.reply(f"**Good Job!** you practiced hard and gained:\n{xp}: {XP}\n{coin}: {COIN}", mention_author=False)
                    self.cursor.execute("select user_xp, user_level, user_coins from users where client_id = %s", [ctx.author.id])
                    result = self.cursor.fetchall()

                    newXP = result[0][0]+XP
                    newCoins = result[0][2]+COIN

                    if newXP > 0:
                        currentLevel = newXP/1000

                    self.cursor.execute("update users set user_xp = %s, user_level = %s, user_coins = %s where client_id = %s", [newXP, currentLevel, newCoins, ctx.author.id])

                    db.commit()

                else:
                    self.cursor.execute(
                        "select user_xp, user_coins from users where client_id = %s", [ctx.author.id])
                    result = self.cursor.fetchall()

                    newXP = result[0][0]-50
                    newCoins = result[0][1]-100

                    if newXP > 0:
                        currentLevel = newXP/1000

                    if newCoins < 0:
                        await ctx.send("😂️👌️ **Lmao** You're so poor that you can even lose ``100`` coins | Updated Balance: ``0``")
                        self.cursor.execute("update users set user_xp = %s, user_level = %s, user_coins = 0 where client_id = %s", [newXP, currentLevel, ctx.author.id])

                        db.commit()

                    else:
                        self.cursor.execute("update users set user_xp = %s, user_level = %s, user_coins = %s where client_id = %s", [newXP, currentLevel, newCoins, ctx.author.id])
                        await ctx.reply(f"**lol** you lost {xp} 50 XP and {coin} 100 coins", mention_author=False)

                        db.commit()

            elif a == "https://media.discordapp.net/attachments/807511480878497806/835889073901928449/green.png":
                if anscol.content.lower() == "green":
                    await ctx.reply(f"**Good Job!** you trained and trained to gain:\n{xp}: {XP}\n{coin}: {COIN}", mention_author=False)
                    self.cursor.execute("select user_xp, user_level, user_coins from users where client_id = %s", [ctx.author.id])
                    result = self.cursor.fetchall()

                    newXP = result[0][0]+XP
                    newCoins = result[0][2]+COIN

                    if newXP > 0:
                        currentLevel = newXP/1000

                    self.cursor.execute("update users set user_xp = %s, user_level = %s, user_coins = %s where client_id = %s", [newXP, currentLevel, newCoins, ctx.author.id])

                    db.commit()

                else:
                    self.cursor.execute("select user_xp, user_coins from users where client_id = %s", [ctx.author.id])
                    result = self.cursor.fetchall()

                    newXP = result[0][0]-50
                    newCoins = result[0][1]-100

                    if newXP > 0:
                        currentLevel = newXP/1000

                    if newCoins < 0:
                        await ctx.send("😂️👌️ **Lmao** You're so poor that you can even lose ``100`` coins | Updated Balance: ``0``")
                        self.cursor.execute("update users set user_xp = %s, user_level = %s, user_coins = 0 where client_id = %s", [newXP, currentLevel, ctx.author.id])

                        db.commit()

                    else:
                        self.cursor.execute("update users set user_xp = %s, user_level = %s, user_coins = %s where client_id = %s", [newXP, currentLevel, newCoins, ctx.author.id])
                        await ctx.reply(f"**lol** you lost {xp} 50 XP and {coin} 100 coins", mention_author=False)
                        db.commit()

            elif a == "https://media.discordapp.net/attachments/807511480878497806/835889002908614666/yellow.png":
                if anscol.content.lower() == "yellow":
                    await ctx.reply(f"**Good Job!** after a long session you gained:\n{xp}: {XP}\n{coin}: {COIN}", mention_author=False)
                    self.cursor.execute("select user_xp, user_level, user_coins from users where client_id = %s", [ctx.author.id])
                    result = self.cursor.fetchall()

                    newXP = result[0][0]+XP
                    newCoins = result[0][2]+COIN

                    if newXP > 0:
                        currentLevel = newXP/1000

                    self.cursor.execute("update users set user_xp = %s, user_level = %s, user_coins = %s where client_id = %s", [newXP, currentLevel, newCoins, ctx.author.id])

                    db.commit()

                else:
                    self.cursor.execute("select user_xp, user_coins from users where client_id = %s", [ctx.author.id])
                    result = self.cursor.fetchall()

                    newXP = result[0][0]-50
                    newCoins = result[0][1]-100

                    if newXP > 0:
                        currentLevel = newXP/1000

                    if newCoins < 0:
                        await ctx.send("😂️👌️ **Lmao** You're so poor that you can even lose ``100`` coins | Updated Balance: ``0``")
                        self.cursor.execute("update users set user_xp = %s, user_level = %s, user_coins = 0 where client_id = %s", [newXP, currentLevel, ctx.author.id])

                        db.commit()

                    else:
                        self.cursor.execute("update users set user_xp = %s, user_level = %s, user_coins = %s where client_id = %s", [newXP, currentLevel, newCoins, ctx.author.id])
                        await ctx.reply(f"**lol** you lost {xp} 50 XP and {coin} 100 coins", mention_author=False)

                        db.commit()

            elif a == "https://media.discordapp.net/attachments/807511480878497806/835889001839460362/pink.png":
                if anscol.content.lower() == "pink":
                    await ctx.reply(f"**Good Job!** after filling up a bucket with sweat you gained:\n{xp}: {XP}\n{coin}: {COIN}", mention_author=False)
                    self.cursor.execute("select user_xp, user_level, user_coins from users where client_id = %s", [ctx.author.id])
                    result = self.cursor.fetchall()

                    newXP = result[0][0]+XP
                    newCoins = result[0][2]+COIN

                    if newXP > 0:
                        currentLevel = newXP/1000

                    self.cursor.execute("update users set user_xp = %s, user_level = %s, user_coins = %s where client_id = %s", [newXP, currentLevel, newCoins, ctx.author.id])

                    db.commit()

                else:
                    self.cursor.execute("select user_xp, user_coins from users where client_id = %s", [ctx.author.id])
                    result = self.cursor.fetchall()

                    newXP = result[0][0]-50
                    newCoins = result[0][1]-100

                    if newXP > 0:
                        currentLevel = newXP/1000

                    if newCoins < 0:
                        await ctx.send("😂️👌️ **Lmao** You're so poor that you can even lose ``100`` coins | Updated Balance: ``0``")
                        self.cursor.execute("update users set user_xp = %s, user_level = %s, user_coins = 0 where client_id = %s", [newXP, currentLevel, ctx.author.id])

                        db.commit()

                    else:
                        self.cursor.execute("update users set user_xp = %s, user_level = %s, user_coins = %s where client_id = %s", [newXP, currentLevel, newCoins, ctx.author.id])
                        await ctx.reply(f"**lol** you lost {xp} 50 XP and {coin} 100 coins", mention_author=False)


async def setup(bot):
    await bot.add_cog(RPG_START(bot))