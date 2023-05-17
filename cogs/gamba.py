from discord.ext import commands
from aurora_secrets import *
from aurora_lists import *
import discord
import random


class Gamba(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cursor = bot.cursor

    @commands.command(aliases=['hl'])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def highlow(self, ctx):
        channel = ctx.channel
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        COIN = random.randint(100, 200)

        self.cursor.execute(
            "select user_coins from users where client_id = %s", [ctx.author.id])
        res = self.cursor.fetchall()

        if len(res) == 0:
            await ctx.send(f"{ctx.author.name} hasn't started playing, to learn more about the game please run ``.rpg info`` or just start by ``.quest``")
        else:
            f50 = discord.Embed(title="", description="")
            f50.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar.url)
            f50.add_field(
                name=f"Chosen Number is ``{x}``", value="Respond With:\n``high``, ``low``, ``jackpot``", inline=False)
            f50.set_footer(text="🧠 Think and use your sixth sense")
            await ctx.send(embed=f50)

            def check(message):

                return ctx.author == message.author and ctx.channel == message.channel

            guess = await self.bot.wait_for('message', check=check)

            if guess.author == ctx.message.author:
                if guess.content.lower() == ".highlow":
                    em = discord.Embed(title="", description="", colour=0xffb12b)
                    em.add_field(
                        name="ERROR", value="Please respond with the following options next time\n``high``, ``low``, ``jackpot``\n Support Server: [Join](https://discord.gg/G9vTrsV4aG)")
                    await ctx.send(embed=em)
                    return
                elif guess.content.lower() == ".hl":
                    em = discord.Embed(title="", description="", colour=0xffb12b)
                    em.add_field(
                        name="ERROR", value="Please respond with the following options next time\n``high``, ``low``, ``jackpot``\n Support Server: [Join](https://discord.gg/G9vTrsV4aG)")
                    await ctx.send(embed=em)
                    return
                elif guess.content.lower() == "high":
                    if y > x:

                        newCoins = res[0][0] + COIN
                        self.cursor.execute("update users set user_coins = %s where client_id = %s", [
                                    newCoins, ctx.author.id])

                        f51 = discord.Embed(title="🎉 You Won", description="_ _")
                        f51.set_author(name=f"{ctx.author}",
                                    icon_url=ctx.author.avatar.url)
                        f51.add_field(
                            name=f"Chosen Number was ``{x}``", value=f"``🟢`` Hidden Number was **``{y}``**\n_ _\nYou Won: {coin} {COIN}", inline=False)
                        f51.set_footer(text="some people have a big brain")
                        await channel.send(embed=f51)

                        db.commit()

                        return
                    elif x > y:

                        newCoins = res[0][0] - COIN

                        if newCoins < 0:
                            self.cursor.execute(
                                "update users set user_coins = 0 where client_id = %s", [ctx.author.id])
                            f51 = discord.Embed(
                                title="💀 You Lost", description=f"😂️👌️ **Lmao** you're too poor to lose {coin} {COIN} | Updated Balance: ``0``")
                            f51.set_author(
                                name=f"{ctx.author}", icon_url=ctx.author.avatar.url)
                            f51.add_field(
                                name=f"Chosen Number was ``{x}``", value=f"``🔴`` Hidden Number was **``{y}``**\n _ _\n You have {coin} 0", inline=False)
                            f51.set_footer(text="try again")
                            await channel.send(embed=f51)

                            db.commit()

                        else:
                            newCoins = res[0][0] - COIN
                            self.cursor.execute("update users set user_coins = %s where client_id = %s", [
                                        newCoins, ctx.author.id])

                            f51 = discord.Embed(
                                title="💀 You Lost", description="_ _")
                            f51.set_author(
                                name=f"{ctx.author}", icon_url=ctx.author.avatar.url)
                            f51.add_field(
                                name=f"Chosen Number was ``{x}``", value=f"``🔴`` Hidden Number was **``{y}``**\n _ _\n You Lost: {coin} {COIN}", inline=False)
                            f51.set_footer(text="try again")
                            await channel.send(embed=f51)

                            db.commit()

                    elif x == y:

                        newCoins = res[0][0] - 1000

                        if newCoins < 0:
                            self.cursor.execute(
                                "update users set user_coins = 0 where client_id = %s", [ctx.author.id])
                            f51 = discord.Embed(
                                title="💀 You Lost", description=f"😂️👌️ **Lmao** you're too poor to lose {coin} 1000 | Updated Balance: ``0``")
                            f51.set_author(
                                name=f"{ctx.author}", icon_url=ctx.author.avatar.url)
                            f51.add_field(
                                name=f"Chosen Number was ``{x}``", value=f"``🔴`` Hidden Number was **``{y}``**\n _ _\n You have {coin} 0", inline=False)
                            f51.set_footer(text="try again")
                            await channel.send(embed=f51)

                            db.commit()

                        else:
                            self.cursor.execute("update users set user_coins = %s where client_id = %s", [
                                        newCoins, ctx.author.id])

                            f51 = discord.Embed(
                                title=":headstone: You Lost Big Time", description="_ _")
                            f51.set_author(
                                name=f"{ctx.author}", icon_url=ctx.author.avatar.url)
                            f51.add_field(
                                name=f"Chosen Number was ``{x}``", value=f"``🔴`` Hidden Number was **``{y}``**\n_ _\nThe numbers were equal, You Missed The JACKPOT\n_ _\n You Lost: {coin} 1000", inline=False)
                            f51.set_footer(text="try again lol")
                            await channel.send(embed=f51)

                            db.commit()

                            return
                elif guess.content.lower() == "low":
                    if x > y:

                        newCoins = res[0][0] + COIN
                        self.cursor.execute("update users set user_coins = %s where client_id = %s", [
                                    newCoins, ctx.author.id])

                        f51 = discord.Embed(title="🎉 You Won", description="_ _")
                        f51.set_author(name=f"{ctx.author}",
                                    icon_url=ctx.author.avatar.url)
                        f51.add_field(
                            name=f"Chosen Number was ``{x}``", value=f"``🟢`` Hidden Number was **``{y}``**\n_ _\n You won {coin} {COIN}", inline=False)
                        f51.set_footer(text="some people have a big brain")
                        await channel.send(embed=f51)

                        db.commit()

                        return
                    elif y > x:
                        newCoins = res[0][0] - COIN

                        if newCoins < 0:
                            self.cursor.execute(
                                "update users set user_coins = 0 where client_id = %s", [ctx.author.id])
                            f51 = discord.Embed(
                                title="💀 You Lost", description=f"😂️👌️ **Lmao** you're too poor to lose {coin} {COIN} | Updated Balance: ``0``")
                            f51.set_author(
                                name=f"{ctx.author}", icon_url=ctx.author.avatar.url)
                            f51.add_field(
                                name=f"Chosen Number was ``{x}``", value=f"``🔴`` Hidden Number was **``{y}``**\n _ _\n You have {coin} 0", inline=False)
                            f51.set_footer(text="try again")
                            await channel.send(embed=f51)

                            db.commit()

                        else:

                            newCoins = res[0][0] - COIN
                            self.cursor.execute("update users set user_coins = %s where client_id = %s", [
                                        newCoins, ctx.author.id])

                            f51 = discord.Embed(
                                title="💀 You Lost", description="_ _")
                            f51.set_author(
                                name=f"{ctx.author}", icon_url=ctx.author.avatar.url)
                            f51.add_field(
                                name=f"Chosen Number was ``{x}``", value=f"``🔴`` Hidden Number was **``{y}``**\n_ _\nYou Lost: {coin} {COIN}", inline=False)

                            f51.set_footer(text="try again")
                            await channel.send(embed=f51)

                            db.commit()

                            return
                    elif x == y:
                        newCoins = res[0][0] - 1000

                        if newCoins < 0:
                            self.cursor.execute(
                                "update users set user_coins = 0 where client_id = %s", [ctx.author.id])
                            f51 = discord.Embed(
                                title="💀 You Lost", description=f"😂️👌️ **Lmao** you're too poor to lose {coin} 1000 | Updated Balance: ``0``")
                            f51.set_author(
                                name=f"{ctx.author}", icon_url=ctx.author.avatar.url)
                            f51.add_field(
                                name=f"Chosen Number was ``{x}``", value=f"``🔴`` Hidden Number was **``{y}``**\n _ _\n You have {coin} 0", inline=False)
                            f51.set_footer(text="try again")
                            await channel.send(embed=f51)

                            db.commit()

                        else:

                            self.cursor.execute("update users set user_coins = %s where client_id = %s", [
                                        newCoins, ctx.author.id])

                            f51 = discord.Embed(
                                title=":headstone: You Lost Big Time", description="_ _")
                            f51.set_author(
                                name=f"{ctx.author}", icon_url=ctx.author.avatar.url)
                            f51.add_field(
                                name=f"Chosen Number was ``{x}``", value=f"``🔴`` Hidden Number was **``{y}``**\n_ _\nThe numbers were equal, You Missed The JACKPOT\n_ _\nYou Lost: {coin} 1000", inline=False)
                            f51.set_footer(text="try again lol")
                            await channel.send(embed=f51)

                            db.commit()

                            return
                elif guess.content.lower() == "jackpot":
                    if x == y:

                        newCoins = res[0][0] + 2000
                        self.cursor.execute("update users set user_coins = %s where client_id = %s", [
                                    newCoins, ctx.author.id])

                        f52 = discord.Embed(
                            title="🏆 You Hit the JACKPOT", description="_ _")
                        f52.set_author(name=f"{ctx.author}",
                                    icon_url=ctx.author.avatar.url)
                        f52.add_field(
                            name=f"Chosen Number was ``{x}``", value=f"``👑`` Hidden Number was **``{y}``**\n_ _\nYou Won: {coin} 2000", inline=False)
                        f52.set_footer(text="some people have insane luck")
                        await channel.send(embed=f52)

                    else:

                        newCoins = res[0][0] - 1000

                        if newCoins < 0:
                            self.cursor.execute(
                                "update users set user_coins = 0 where client_id = %s", [ctx.author.id])
                            f51 = discord.Embed(
                                title="💀 You Lost", description=f"😂️👌️ **Lmao** you're too poor to lose {coin} 1000 | Updated Balance: ``0``")
                            f51.set_author(
                                name=f"{ctx.author}", icon_url=ctx.author.avatar.url)
                            f51.add_field(
                                name=f"Chosen Number was ``{x}``", value=f"``🔴`` Hidden Number was **``{y}``**\n _ _\n You have {coin} 0", inline=False)
                            f51.set_footer(text="try again")
                            await channel.send(embed=f51)

                            db.commit()

                        else:
                            self.cursor.execute("update users set user_coins = %s where client_id = %s", [
                                        newCoins, ctx.author.id])

                            f52 = discord.Embed(
                                title="👊 You Missed the JACKPOT", description="_ _")
                            f52.set_author(
                                name=f"{ctx.author}", icon_url=ctx.author.avatar.url)
                            f52.add_field(
                                name=f"Chosen Number was ``{x}``", value=f"``🔴`` Hidden Number was **``{y}``**\n_ _\nYou Lost: {coin} 1000", inline=False)
                            f52.set_footer(text="some people have mad bad luck")
                            await ctx.send(embed=f52)

                            db.commit()

                else:
                    em = discord.Embed(title="", description="", colour=0xffb12b)
                    em.add_field(
                        name="ERROR", value="Please respond with the following options next time\n``high``, ``low``, ``jackpot``\nrun the command again: ``.highlow``\n Support Server: [Join](https://discord.gg/G9vTrsV4aG)")
                    await ctx.send(embed=em)


    @commands.group(name="slots", invoke_without_command=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def slots(self, ctx, *, message):
        emoji_list = ["🛒️", "👍️", "💩️", "💸️", "🤝️", "💰️", "🌐️", "🧠️", 
                      "💩️", "😎️", "📀️","🍉️", "💍️", "🏐️", "💀️", "🤡️", 
                      "💰️", "💰️", "🤗️", "💩️", "🌌", "🌌", "😎️", "😎️", "💀️"]

        try:

            message = int(message)
            self.cursor.execute("select user_coins from users where client_id = %s", [ctx.author.id])
            result = self.cursor.fetchall()
            coinsss = result[0][0]

            if coinsss == 0:
                await ctx.reply("😂️❌️ You don't have coins to gamble with lol")

            elif coinsss < message:
                await ctx.reply("<:785066114580611082:836225528054022204>❌️ You don't have these many coins")

            elif message < 100:
                await ctx.reply("🤑️👎️ You can't bet less than 100")

            elif message > 100000:
                await ctx.reply("🤑️👎️ You can't bet more than 100,000")

            else:
                a = random.choice(emoji_list)
                b = random.choice(emoji_list)
                c = random.choice(emoji_list)
                y = f"{a}{b}{c}"

                if y == "💩️💩️💩️":
                    self.cursor.execute("select user_coins from users where client_id = %s", [ctx.author.id])

                    result2 = self.cursor.fetchall()
                    COIN = result2[0][0] + message*2

                    self.cursor.execute("update users set user_coins = %s where client_id = %s", [COIN, ctx.author.id])
                    final = message*2

                    slot = discord.Embed(title="")
                    slot.set_author(name=f"{ctx.author.name}'s Slots", icon_url=ctx.author.avatar.url)
                    slot.add_field(name=f"```[ {y} ]```",value="_ _", inline=False)
                    slot.add_field(name="_ _", value=f" You won! {coin} {final}")
                    
                    await ctx.reply(embed=slot, mention_author=False)
                    db.commit()

                elif y == "💰️💰️💰️":
                    self.cursor.execute("select user_coins from users where client_id = %s", [ctx.author.id])

                    result3 = self.cursor.fetchall()
                    COIN = result3[0][0] + message*4

                    self.cursor.execute("update users set user_coins = %s where client_id = %s", [COIN, ctx.author.id])
                    final = message*4
                    slot = discord.Embed(title="")
                    slot.set_author(name=f"{ctx.author.name}'s Slots", icon_url=ctx.author.avatar.url)
                    slot.add_field(name=f"```[ {y} ]```",value="_ _", inline=False)
                    slot.add_field(name="_ _", value=f" You won! {coin} {final}")
                    
                    await ctx.reply(embed=slot, mention_author=False)
                    db.commit()

                elif y == "🌌🌌🌌":

                    self.cursor.execute("select user_coins from users where client_id = %s", [ctx.author.id])

                    result4 = self.cursor.fetchall()
                    COIN = result4[0][0] + message*6

                    self.cursor.execute("update users set user_coins = %s where client_id = %s", [COIN, ctx.author.id])
                    final = message*6
                    slot = discord.Embed(title="")
                    slot.set_author(name=f"{ctx.author.name}'s Slots", icon_url=ctx.author.avatar.url)
                    slot.add_field(name=f"```[ {y} ]```",value="_ _", inline=False)
                    slot.add_field(name="_ _", value=f" You won! {coin} {final}")
                    
                    await ctx.reply(embed=slot, mention_author=False)
                    db.commit()

                elif y == "🤡️🤡️🤡️":

                    self.cursor.execute("select user_coins from users where client_id = %s", [ctx.author.id])

                    result5 = self.cursor.fetchall()
                    COIN = result5[0][0] + message*8

                    self.cursor.execute("update users set user_coins = %s where client_id = %s", [COIN, ctx.author.id])
                    final = message*8

                    slot = discord.Embed(title="")
                    slot.set_author(name=f"{ctx.author.name}'s Slots", icon_url=ctx.author.avatar.url)
                    slot.add_field(name=f"```[ {y} ]```",value="_ _", inline=False)
                    slot.add_field(name="_ _", value=f" You won! {coin} {final}")
                    
                    await ctx.reply(embed=slot, mention_author=False)
                    db.commit()

                elif y == "😎️😎️😎️":

                    self.cursor.execute("select user_coins from users where client_id = %s", [ctx.author.id])

                    result6 = self.cursor.fetchall()
                    COIN = result6[0][0] - message*2
                    final = message*2

                    if COIN < 0:
                        self.cursor.execute("update users set user_coins = 0 where client_id = %s", [ctx.author.id])
                        await ctx.reply(f"😂️👌️ **Lmao** you're too poor to lose {coin} {final} | Updated Balance: ``0``")
                        db.commit()

                    else:

                        self.cursor.execute("update users set user_coins = %s where client_id = %s", [COIN, ctx.author.id])

                        slot = discord.Embed(title="", description="")
                        slot.set_author(name=f"{ctx.author.name}'s Slots", icon_url=ctx.author.avatar.url)
                        slot.add_field(name=f"```[ {y} ]```", value="_ _", inline=False)
                        slot.add_field(name="_ _", value=f" You lost big time! {coin} {final}")
                        await ctx.reply(embed=slot, mention_author=False)
                        db.commit()

                elif y == "💀️💀️💀️":

                    self.cursor.execute("select user_coins from users where client_id = %s", [ctx.author.id])

                    result7 = self.cursor.fetchall()
                    COIN = result7[0][0] - message*4
                    final = message*4

                    if COIN < 0:
                        self.cursor.execute("update users set user_coins = 0 where client_id = %s", [ctx.author.id])
                        
                        await ctx.reply(f"😂️👌️ **Lmao** you're too poor to lose {coin} {final} | Updated Balance: ``0``")
                        db.commit()

                    else:

                        self.cursor.execute("update users set user_coins = %s where client_id = %s", [COIN, ctx.author.id])

                        slot = discord.Embed(title="")
                        slot.set_author(name=f"{ctx.author.name}'s Slots", icon_url=ctx.author.avatar.url)
                        slot.add_field(name=f"```[ {y} ]```", value="_ _", inline=False)
                        slot.add_field(name="_ _", value=f" You lost big time! {coin} {final}")
                        
                        await ctx.reply(embed=slot, mention_author=False)
                        db.commit()

                else:
                    self.cursor.execute("select user_coins from users where client_id = %s", [ctx.author.id])
                    result8 = self.cursor.fetchall()
                    COIN = result8[0][0] - message
                    self.cursor.execute("update users set user_coins = %s where client_id = %s", [COIN, ctx.author.id])

                    slot = discord.Embed(title="")
                    slot.set_author(name=f"{ctx.author.name}'s Slots", icon_url=ctx.author.avatar.url)
                    slot.add_field(name=f"```[ {y} ]```",value="_ _", inline=False)
                    slot.add_field(name="_ _", value=f" You lost! {coin} {message}")
                    
                    await ctx.reply(embed=slot, mention_author=False)
                    db.commit()

        except ValueError:

            error_msg = discord.Embed(title=" ", description=" ", color=0xffb12b)
            error_msg.add_field(name="Error", value="Please enter a valid amount\nrun ``.slots info`` for more information\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
            
            await ctx.send(embed=error_msg)


    @slots.command(name="info")
    async def slots_info(self, ctx):
        sinfo = discord.Embed(color=random.choice(colors))
        sinfo.add_field(name="WINNER INFO", value="```💩️💩️💩️ x2\n\n💰️💰️💰️ x4 \n\n🌌🌌🌌 x6\n\n🤡️🤡️🤡️ x8\n```")
        sinfo.add_field(name="LOSER INFO", value="```😎️😎️😎️ x2\n\n💀️💀️💀️ x4```")
        sinfo.set_footer(text="to play run: .slots <amount>")

        await ctx.send(embed=sinfo)

async def setup(bot):
    await bot.add_cog(Gamba(bot))