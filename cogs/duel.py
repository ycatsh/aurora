from discord.ext import commands
from aurora_secrets import *
from aurora_lists import *
import asyncio
import discord
import random

class Duel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cursor = bot.cursor

    @commands.command()
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def duel(self, ctx, p2: discord.Member):

        dx = 0
        dy = 0
        p1 = ctx.author
        user = [p1, p2]
        gameOver = 1
        winner = 1

        self.cursor.execute("select user_xp, user_coins, health from users where client_id = %s", [ctx.author.id])
        result = self.cursor.fetchall()

        self.cursor.execute("select user_xp, user_coins, health from users where client_id = %s", [p2.id])
        result2 = self.cursor.fetchall()

        if self.bot.user.mentioned_in(ctx.message):
            await ctx.send("Lmao you tried 😎️")
            return

        if len(result) == 0 and len(result2) == 0:
            await ctx.send(f"{ctx.author.mention} and {p2.mention} haven't started playing, to learn more about the game please run ``.rpg info`` or just start by ``.quest``")

        elif len(result2) == 0:
            await ctx.send(f"{p2.mention} hasn't started playing, to learn more about the game please run ``.rpg info`` or just start by ``.quest``")

        elif len(result) == 0:
            await ctx.send(f"{ctx.author.mention} hasn't started playing, to learn more about the game please run ``.rpg info`` or just start by ``.quest``")

        xpp2 = result2[0][0]
        coo2 = result2[0][1]
        hee2 = result2[0][2]
        xpp = result[0][0]
        coo = result[0][1]
        hee = result[0][2]

        if xpp < 3000 and xpp2 < 3000:
            await ctx.send(f"{ctx.author.mention} and {p2.mention} You must be **``level 3``** or higher to duel. check your level by running **``.profile``**")

        elif xpp < 3000:
            await ctx.send(f"{ctx.author.mention} You must be **``level 3``** or higher to duel. check your level by running **``.profile``**")

        elif xpp2 < 3000:
            await ctx.send(f"{p2.mention} You must be **``level 3``** or higher to duel. check your level by running **``.profile``**")

        elif p2 == ctx.author:
            await ctx.send("Don't try to get around me, you can't duel yourself")

        elif coo == 0 and coo2 == 0:
            await ctx.send(f"{ctx.author.mention} and {p2.mention} you can't duel with 0 coins 😂 ")

        elif coo == 0:
            await ctx.send(f"{ctx.author.mention} you can't duel with 0 coins 😂 ")

        elif coo2 == 0:
            await ctx.send(f"{p2.mention} you can't duel with 0 coins 😂 ")

        elif hee == 0 and hee2 == 0:
            await ctx.send(f"{ctx.author.mention} and {p2.mention} you can't duel with no health, run ``.shop`` to buy health potions")

        elif hee == 0:
            await ctx.send(f"{ctx.author.mention} you can't duel with no health, run ``.shop`` to buy health potions")

        elif hee2 == 0:
            await ctx.send(f"{p2.mention} you can't duel with no health, run ``.shop`` to buy health potions")

        else:

            p1 = ctx.author
            d = discord.Embed(title="Duels", description=f"{p1.mention} and {p2.mention} read the following before starting the match", color=random.choice(colors))
            d.add_field(name="STAKES", value="upon losing the duel you'll lose all your coins and only have ``1`` left", inline=False)
            d.add_field(name="WINNER", value="the winner recieves all the coins(-1) of the loser", inline=False)
            d.add_field(name="READY?", value=f"{p1.mention} and {p2.mention} type ``ok`` within ``30`` seconds to accept and continue with the duel", inline=False)
            d.add_field(name="``⚠️ WARNING ⚠️``", value=f"Attempting to duel someone else during a duel will result in you losing the current duel", inline=False)
            d.set_footer(text="you may even lose coins during the duel 👍")

            await ctx.send(embed=d)

            while True:

                def check(message):

                    return ctx.channel == message.channel

                try:

                    ans = await self.bot.wait_for("message", check=check, timeout=30)

                    if ans.content.lower() == "ok":
                        if ans.author == p1:
                            await ans.reply(f"{ans.author.name} has accepted the stakes and would like to continue")
                            dx += 4

                        if ans.author == p2:
                            await ans.reply(f"{ans.author.name} has accepted the stakes and would like to continue")
                            dy += 4

                        else:
                            pass

                        if dx == 4 and dy == 4:
                            break

                    else:
                        await ans.reply(f"😑️ bruh answer properly or just walk away from duels | this has ended run the command again")
                        break

                except asyncio.TimeoutError:
                    await ctx.send(f"Players didn't repond in time 💀️")
                    break

            if dx == 4 and dy == 4:
                self.cursor.execute("select user_coins, defense, health, attack, quagun, enebazo from users where client_id = %s", [p1.id])
                res = self.cursor.fetchall()

                c = res[0][0]
                d = res[0][1]
                h = res[0][2]
                a = res[0][3]
                q = res[0][4]
                e = res[0][5]

                self.cursor.execute("select user_coins, defense, health, attack, quagun, enebazo from users where client_id = %s", [p2.id])
                res2 = self.cursor.fetchall()

                c2 = res2[0][0]
                d2 = res2[0][1]
                h2 = res2[0][2]
                a2 = res2[0][3]
                q2 = res2[0][4]
                e2 = res2[0][5]

                turn = random.randint(0, 1)

                if turn == 0:
                    du = discord.Embed(title="", color=random.choice(colors))
                    du.add_field(name="List of usable commands:", value="1. ``weapon <item_id>`` - reduce the opponents health by using your weapons\n(there is a 20% chance that you'll miss)\n\n2. ``punch`` - reduce the opponents health by your attack level\n\n3. ``steal`` - 10% chance that you can steal 70% of the coins and run away otherwise you **lose** 50% of your coins\n(you won't get all the coins(-1) as stated before\n\n4. ``forfeit `` - surrender by giving away 30% of your coins")
                    du.add_field(name="Player's turn (random)", value=f"{p1.mention}'s turn, please use any of the above commands to continue", inline=False)
                    du.add_field(name="``⚠️ WARNING ⚠️``", value=f"Attempting to duel someone else during a duel will result in you losing the current duel", inline=False)
                    du.set_footer(text="To win, the opponent has to lose all their health")

                    await ctx.send(embed=du)

                elif turn == 1:
                    du = discord.Embed(title="", color=random.choice(colors))
                    du.add_field(name="List of usable commands:", value="1. ``weapon <item_id>`` - reduce the opponents health by using your weapons\n(there is a 20% chance that you'll miss)\n\n2. ``punch`` - reduce the opponents health by your attack level\n\n3. ``steal`` - 10% chance that you can steal 70% of the coins and run away otherwise you **lose** 50% of your coins\n(you won't get all the coins(-1) as stated before\n\n4. ``forfeit `` - surrender by giving away 30% of your coins")
                    du.add_field(name="Player's turn (random)", value=f"{p2.mention}'s turn, please use any of the above commands to continue", inline=False)
                    du.add_field(name="``⚠️ WARNING ⚠️``", value=f"Attempting to duel someone else during a duel will result in you losing the current duel", inline=False)
                    du.set_footer(text="To win, the opponent has to lose all their health")

                    await ctx.send(embed=du)

                while True:
                    def check(message):

                        return ctx.channel == message.channel

                    msg = await self.bot.wait_for("message", check=check)

                    if msg.author == user[turn]:

                        if msg.content.lower() == "forfeit":
                            if msg.author == p1:
                                await ctx.send(f"{p1.mention} has forfeited and will lose 30% of their coins to {p2.mention} | run ``.profile`` to use your updated balance")
                                newc = c * (3/10)
                                c2final = c2 + newc
                                cfinal = c - newc

                                self.cursor.execute("update users set user_coins = %s where client_id = %s", [cfinal, p1.id])
                                self.cursor.execute("update users set user_coins = %s where client_id =  %s", [c2final, p2.id])
                                db.commit()
                                winner += 2
                                gameOver += 1

                            elif msg.author == p2:
                                await ctx.send(f"{p2.mention} has forfeited and will lose 30% of their coins to {p1.mention} | run ``.profile`` to use your updated balance")
                                newc2 = c2 * (3/10)
                                c2final = c2 - newc2
                                cfinal = c + newc2

                                self.cursor.execute("update users set user_coins = %s where client_id = %s", [cfinal, p1.id])
                                self.cursor.execute("update users set user_coins = %s where client_id =  %s", [c2final, p2.id])
                                db.commit()
                                winner += 1
                                gameOver += 1

                        elif msg.content.lower() == "weapon qg":
                            y = random.randint(1, 5)
                            if msg.author == p1:
                                if q == 0:
                                    await ctx.send(f"Don't try to get around me, you don't have this item | {p2.mention}'s turn")

                                    if user[turn] == p1:
                                        user[turn] = p2
                                    elif user[turn] == p2:
                                        user[turn] = p1

                                elif y == 4:
                                    await ctx.send(f"{p1.mention} has missed! it's {p2.mention}'s turn ")

                                    if user[turn] == p1:
                                        user[turn] = p2
                                    elif user[turn] == p2:
                                        user[turn] = p1

                                else:
                                    h2final2 = h2 - 20
                                    qfinal = q - 1
                                    self.cursor.execute("UPDATE users set health = %s where client_id = %s", [h2final2, p2.id])
                                    self.cursor.execute("UPDATE users set quagun = %s where client_id = %s", [qfinal, p1.id])
                                    
                                    await ctx.send(f"{p1.mention} has hit {p2.mention}, removing 20 of their health | its {p2.mention}'s turn")
                                    db.commit()

                                    if user[turn] == p1:
                                        user[turn] = p2
                                    elif user[turn] == p2:
                                        user[turn] = p1

                                    if h2final2 <= 0:
                                        self.cursor.execute("UPDATE users set health = 0 where client_id = %s", [p2.id])
                                        loss2 = c2 - 1
                                        finalwin = c + loss2

                                        self.cursor.execute("UPDATE users set user_coins = 1 where client_id = %s", [p2.id])
                                        self.cursor.execute("UPDATE users set user_coins = %s where client_id = %s", [finalwin, p1.id])
                                        
                                        await ctx.send(f"{p1.mention} has won the duel, leaving {p2.mention} with zero health! they will recieve all the coins (-1) of the loser")
                                        db.commit()
                                        winner += 1
                                        gameOver += 1

                            elif msg.author == p2:
                                y2 = random.randint(1, 5)
                                if q2 == 0:
                                    await ctx.send(f"Don't try to get around me, you don't have this item | {p1.mention}'s turn")

                                    if user[turn] == p1:
                                        user[turn] = p2
                                    elif user[turn] == p2:
                                        user[turn] = p1

                                elif y2 == 4:
                                    await ctx.send(f"{p2.mention} has missed! it's {p1.mention}'s turn ")

                                    if user[turn] == p1:
                                        user[turn] = p2
                                    elif user[turn] == p2:
                                        user[turn] = p1

                                else:
                                    hfinal2 = h - 20
                                    q2final = q2 - 1
                                    self.cursor.execute("UPDATE users set health = %s where client_id = %s", [hfinal2, p1.id])
                                    self.cursor.execute("UPDATE users set quagun = %s where client_id = %s", [q2final, p2.id])
                                    
                                    await ctx.send(f"{p2.mention} has hit {p1.mention}, removing 20 of their health | its {p1.mention}'s turn")
                                    db.commit()

                                    if user[turn] == p1:
                                        user[turn] = p2
                                    elif user[turn] == p2:
                                        user[turn] = p1

                                    if hfinal <= 0:
                                        self.cursor.execute("UPDATE users set health = 0 where client_id = %s", [p1.id])
                                        loss = c - 1
                                        finalwin2 = c2 + loss

                                        self.cursor.execute("UPDATE users set user_coins = 1 where client_id = %s", [p1.id])
                                        self.cursor.execute("UPDATE users set user_coins = %s where client_id = %s", [finalwin2, p2.id])
                                        
                                        await ctx.send(f"{p2.mention} has won the duel, leaving {p1.mention} with zero health! they will recieve all the coins (-1) of the loser")
                                        db.commit()
                                        winner += 2
                                        gameOver += 1

                        elif msg.content.lower() == "weapon eb":
                            y3 = random.randint(1, 5)
                            if msg.author == p1:
                                if e == 0:
                                    await ctx.send(f"Don't try to get around me, you don't have this item | {p2.mention}'s turn")

                                    if user[turn] == p1:
                                        user[turn] = p2
                                    elif user[turn] == p2:
                                        user[turn] = p1

                                if y3 == 4:
                                    await ctx.send(f"{p1.mention} has missed! it's {p2.mention}'s turn ")

                                    if user[turn] == p1:
                                        user[turn] = p2
                                    elif user[turn] == p2:
                                        user[turn] = p1

                                else:
                                    h2final = h2 - 75
                                    efinal = e - 1
                                    self.cursor.execute("UPDATE users set health = %s where client_id = %s", [h2final, p2.id])
                                    self.cursor.execute("UPDATE users set enebazo = %s where client_id = %s", [efinal, p1.id])
                                    
                                    await ctx.send(f"{p1.mention} has hit {p2.mention}, removing 75 of their health | its {p2.mention}'s turn")
                                    db.commit()

                                    if user[turn] == p1:
                                        user[turn] = p2
                                    elif user[turn] == p2:
                                        user[turn] = p1

                                    if h2final <= 0:
                                        self.cursor.execute("UPDATE users set health = 0 where client_id = %s", [p2.id])
                                        
                                        loss2 = c2 - 1
                                        finalwin = c + loss2

                                        self.cursor.execute("UPDATE users set user_coins = 1 where client_id = %s", [p2.id])
                                        self.cursor.execute("UPDATE users set user_coins = %s where client_id = %s", [finalwin, p1.id])
                                        
                                        await ctx.send(f"{p1.mention} has won the duel, leaving {p2.mention} with zero health! they will recieve all the coins (-1) of the loser")
                                        db.commit()
                                        winner += 1
                                        gameOver += 1

                            elif msg.author == p2:
                                y4 = random.randint(1, 5)
                                if e2 == 0:
                                    await ctx.send(f"Don't try to get around me, you don't have this item | {p1.mention}'s turn")

                                    if user[turn] == p1:
                                        user[turn] = p2
                                    elif user[turn] == p2:
                                        user[turn] = p1

                                elif y4 == 4:

                                    await ctx.send(f"{p2.mention} has missed! it's {p1.mention}'s turn ")

                                    if user[turn] == p1:
                                        user[turn] = p2
                                    elif user[turn] == p2:
                                        user[turn] = p1

                                else:
                                    hfinal = h - 75
                                    e2final = e2 - 1

                                    self.cursor.execute("UPDATE users set health = %s where client_id = %s", [hfinal, p1.id])
                                    self.cursor.execute("UPDATE users set enebazo = %s where client_id = %s", [e2final, p2.id])
                                    
                                    await ctx.send(f"{p2.mention} has hit {p1.mention}, removing 75 of their health | its {p1.mention}'s turn")
                                    db.commit()

                                    if user[turn] == p1:
                                        user[turn] = p2
                                    elif user[turn] == p2:
                                        user[turn] = p1

                                    if hfinal <= 0:
                                        self.cursor.execute("UPDATE users set health = 0 where client_id = %s", [p1.id])
                                        
                                        loss = c - 1
                                        finalwin2 = c2 + loss
                                        self.cursor.execute("UPDATE users set user_coins = 1 where client_id = %s", [p1.id])
                                        self.cursor.execute("UPDATE users set user_coins = %s where client_id = %s", [finalwin2, p2.id])
                                        
                                        await ctx.send(f"{p2.mention} has won the duel, leaving {p1.mention} with zero health! they will recieve all the coins (-1) of the loser")
                                        db.commit()
                                        winner += 2
                                        gameOver += 1

                        elif msg.content.lower() == "punch":
                            if msg.author == p1:
                                if a > d2:
                                    await ctx.send(f"You hit {p2.name}, removing {a} of their health | its {p2.mention}'s turn")
                                    h2final3 = h2 - a
                                    self.cursor.execute("UPDATE users set health = %s where client_id = %s", [h2final3, p2.id])
                                    db.commit()

                                    if user[turn] == p1:
                                        user[turn] = p2
                                    elif user[turn] == p2:
                                        user[turn] = p1

                                    if h2final3 <= 0:
                                        self.cursor.execute("UPDATE users set health = 0 where client_id = %s", [p2.id])
                                        loss2 = c2 - 1
                                        finalwin = c + loss2

                                        self.cursor.execute("UPDATE users set user_coins = 1 where client_id = %s", [p2.id])
                                        self.cursor.execute("UPDATE users set user_coins = %s where client_id = %s", [finalwin, p1.id])
                                        
                                        await ctx.send(f"{p1.mention} has won the duel, leaving {p2.mention} with zero health! they will recieve all the coins (-1) of the loser")
                                        db.commit()
                                        winner += 1
                                        gameOver += 1

                                elif a <= d2:
                                    await ctx.send(f"{p2.mention} has tanked the hit losing no health as their defense is greater than or equal to {p1.mention} | its {p2.mention}'s turn")

                                    if user[turn] == p1:
                                        user[turn] = p2
                                    elif user[turn] == p2:
                                        user[turn] = p1

                            if msg.author == p2:
                                if a2 > d:
                                    await ctx.send(f"You hit {p1.name}, removing {a2} of their health | its {p1.mention}'s turn")
                                    hfinal3 = h - a2
                                    self.cursor.execute("UPDATE users set health = %s where client_id = %s", [hfinal3, p1.id])

                                    if user[turn] == p1:
                                        user[turn] = p2
                                    elif user[turn] == p2:
                                        user[turn] = p1

                                    if hfinal3 <= 0:
                                        self.cursor.execute("UPDATE users set health = 0 where client_id = %s", [p1.id])
                                        
                                        loss = c - 1
                                        finalwin2 = c2 + loss

                                        self.cursor.execute("UPDATE users set user_coins = 1 where client_id = %s", [p1.id])
                                        self.cursor.execute("UPDATE users set user_coins = %s where client_id = %s", [finalwin2, p2.id])
                                        
                                        await ctx.send(f"{p2.mention} has won the duel, leaving {p1.mention} with zero health! they will recieve all the coins (-1) of the loser")
                                        db.commit()
                                        winner += 2
                                        gameOver += 1

                                elif a2 <= d:
                                    await ctx.send(f"{p1.mention} has tanked the hit losing no health as their defense is greater than or equal to {p2.mention} | its {p1.mention}'s turn")

                                    if user[turn] == p1:
                                        user[turn] = p2
                                    elif user[turn] == p2:
                                        user[turn] = p1

                        elif msg.content.lower() == "steal":
                            s = random.randint(1, 10)
                            s2 = random.randint(1, 10)
                            if msg.author == p1:
                                if s == 5:
                                    lost = c2 * 4/5
                                    c2final2 = c2 - lost
                                    cfinal2 = c + lost

                                    self.cursor.execute("UPDATE users set user_coins = %s where client_id = %s", [c2final2, p2.id])
                                    self.cursor.execute("UPDATE users set user_coins = %s where client_id = %s", [cfinal2, p1.id])
                                   
                                    await ctx.send(f"⚡ **NO WAY** you were so fast that you stole {p2.mention}'s coins before they even blinked | GAME OVER")
                                    db.commit()
                                    winner += 1
                                    gameOver += 1

                                else:
                                    lost = c / 2
                                    c2final3 = c2 + lost
                                    cfinal3 = c - lost

                                    self.cursor.execute("UPDATE users set user_coins = %s where client_id = %s", [c2final3, p2.id])
                                    self.cursor.execute("UPDATE users set user_coins = %s where client_id = %s", [cfinal3, p1.id])
                                    
                                    await ctx.send(f"👊 **LMAO** you were too slow and ended up getting caught and losing 50% of your coins to {p2.mention} | its {p2.mention}'s turn")
                                    db.commit()

                                    if user[turn] == p1:
                                        user[turn] = p2
                                    elif user[turn] == p2:
                                        user[turn] = p1

                            elif msg.author == p2:
                                if s2 == 5:
                                    lost = c * 4/5
                                    cfinal2 = c - lost
                                    c2final2 = c2 + lost

                                    self.cursor.execute("UPDATE users set user_coins = %s where client_id = %s", [cfinal2, p1.id])
                                    self.cursor.execute("UPDATE users set user_coins = %s where client_id = %s", [c2final2, p2.id])
                                    
                                    await ctx.send(f"⚡ **NO WAY** you were so fast that you stole {p1.mention}'s coins before they even blinked | GAME OVER")
                                    db.commit()
                                    winner += 2
                                    gameOver += 1

                                else:
                                    lost = c2 / 2
                                    cfinal3 = c + lost
                                    c2final3 = c2 - lost
                                    
                                    self.cursor.execute("UPDATE users set user_coins = %s where client_id = %s", [cfinal3, p1.id])
                                    self.cursor.execute("UPDATE users set user_coins = %s where client_id = %s", [c2final3, p2.id])
                                    
                                    await ctx.send(f"👊 **LMAO** you were too slow and ended up getting caught and losing 50% of your coins to {p1.mention} | its {p1.mention}'s turn")
                                    db.commit()

                                    if user[turn] == p1:
                                        user[turn] = p2
                                    elif user[turn] == p2:
                                        user[turn] = p1

                        elif (msg.content.startswith(f".duel")):
                            if msg.author == p1:
                                await ctx.send(f"{msg.author.mention}, 😂️👎️ You can't start another duel because you are already in one | blame yourself for losing this duel\n{p2.mention} wins | run ``.profile`` to see your updated balance")
                                losss = c - 1
                                finalwin22 = c2 + losss

                                self.cursor.execute("UPDATE users set user_coins = 1 where client_id = %s", [p1.id])
                                self.cursor.execute("UPDATE users set user_coins = %s where client_id = %s", [finalwin22, p2.id])
                                
                                db.commit()
                                winner += 2
                                gameOver += 1

                            elif msg.author == p2:
                                await ctx.send(f"{msg.author.mention}, 😂️👎️ You can't start another duel because you are already in one | blame yourself for losing this duel\n{p1.mention} wins | run ``.profile`` to see your updated balance")
                                losss2 = c2 - 1
                                finalwinn = c + losss2
                                
                                self.cursor.execute("UPDATE users set user_coins = 1 where client_id = %s", [p2.id])
                                self.cursor.execute("UPDATE users set user_coins = %s where client_id = %s", [finalwinn, p1.id])
                                
                                db.commit()
                                winner += 1
                                gameOver += 1

                    elif msg.author.id == 804228080952016897:
                        pass

                    else:
                        await ctx.send("It's not your turn!")

                    if gameOver == 2:

                        if winner == 2:
                            drxp = random.randint(1000, 2000)

                            go = discord.Embed(title="GAME OVER", color=000000)
                            go.add_field(name=f"Winner: {p1.name}", value=f"{p1.mention} you will receive an additional {xp}{drxp}\nTo start a new game run ``.duel <@player2>`` (5 mins cooldown)")
                            
                            await ctx.send(embed=go)

                            self.cursor.execute("select user_xp from users where client_id = %s", [p1.id])
                            lazy = self.cursor.fetchall()

                            fdxp = lazy[0][0] + drxp
                            dfl = fdxp / 1000

                            self.cursor.execute("select dplayed, dwins from users where client_id = %s", [p1.id])
                            fres = self.cursor.fetchall()

                            self.cursor.execute("select dplayed from users where client_id = %s", [p2.id])
                            fress = self.cursor.fetchall()

                            dpfinal = fres[0][0] + 1
                            dpfinal2 = fress[0][0] + 1
                            dwfinal = fres[0][1] + 1

                            self.cursor.execute("update users set user_xp = %s, user_level = %s, dplayed = %s, dwins = %s where client_id = %s", [fdxp, dfl, dpfinal, dwfinal, p1.id])
                            self.cursor.execute("update users set dplayed = %s where client_id = %s", [dpfinal2, p2.id])

                            db.commit()

                        elif winner == 3:
                            drxp2 = random.randint(1000, 2000)
                            go = discord.Embed(title="GAME OVER", color=000000)
                            go.add_field(name=f"Winner: {p2.name}", value=f"{p2.mention} you will receive an additional {xp}{drxp2}\nTo start a new game run ``.duel <@player2>`` (5 mins cooldown)")
                            await ctx.send(embed=go)

                            self.cursor.execute("select user_xp from users where client_id = %s", [p2.id])
                            lazy2 = self.cursor.fetchall()

                            fdxp2 = lazy2[0][0] + drxp2
                            dfl2 = fdxp2 / 1000

                            self.cursor.execute("select dplayed, dwins from users where client_id = %s", [p2.id])
                            fres2 = self.cursor.fetchall()

                            self.cursor.execute("select dplayed from users where client_id = %s", [p1.id])
                            fress2 = self.cursor.fetchall()

                            dp2final = fres2[0][0] + 1
                            dpfinal22 = fress2[0][0] + 1
                            dw2final = fres2[0][1] + 1

                            self.cursor.execute("update users set user_xp = %s, user_level = %s, dplayed = %s, dwins = %s where client_id = %s", [fdxp2, dfl2, dp2final, dw2final, p2.id])
                            self.cursor.execute("update users set dplayed = %s where client_id = %s", [dpfinal22, p1.id])

                            db.commit()

                        db.commit()
                        break


async def setup(bot):
    await bot.add_cog(Duel(bot))