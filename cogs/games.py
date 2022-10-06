from discord.ext import commands 
import discord
import random
import asyncio
from aurora_lists import colors, riddles, ball, ball_arg, roasts, rp, vb, ww, xp, coin, dpe, hpe, vpe, dash, qge, ebe, ame, woe, ate, dfe, hae, mbe

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix = ".", case_insensitive=True, intents=intents)

class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command(aliases=['mini_games'])
    async def games(self, ctx):
        bbo = discord.Embed(title="Mini Games", description="Choose which one you want to play!", color=0xa3ff61)
        bbo.add_field(name="🏀 ``.bbgame``", value="basketball, simple shooting game", inline=False)
        bbo.add_field(name=":soccer: ``.fbgame``", value="football, simple kicking game", inline=False)
        bbo.add_field(name="<:greenball:830467077058854922> ``.blgame``", value="bowling, simple bowling game", inline=False)
        bbo.set_thumbnail(url="https://media.discordapp.net/attachments/807511480878497806/832282579050823711/aurora_games.png")
        await ctx.send(embed=bbo)

    @commands.command()
    async def bbgame(self, ctx):
        bbem= discord.Embed(title="Game Info", description="**React** to the appropriate power level to make a shot based on your intuition", color=random.choice(colors))
        bbem.add_field(name="Start Game: ``.shoot``", value="_ _", inline=False)
        bbem.add_field(name="Power levels (correspond to the reactions):", value="_ _", inline=False)
        bbem.set_image(url='https://media.discordapp.net/attachments/807511480878497806/819109874897911848/brown_square_red_square_orange_square_yellow_square_green_square_blue_square_white_large_square_.png')

        await ctx.send(embed=bbem)

    @commands.command(aliases=["basketball"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def shoot(self, ctx):
        x = random.randint(1, 8)
        coloremojis = {"🟫": 7, "🟥": 6, "🟧": 5, "🟨": 4, "🟩": 3, "🟦": 2, "⬜": 1}
        b = await ctx.reply("<:bbball:830475864172789800>" + ("<:transparent:830476759463231498>" * x) + ':wastebasket:', mention_author=False)
        for color in coloremojis.keys():
            await b.add_reaction(color)

        def check(reaction, user):
            int(x)
            return user == ctx.author and str(reaction.emoji) in coloremojis.keys()

        reaction, user = await bot.wait_for("reaction_add", check=check)

        a = (x - coloremojis[str(reaction.emoji)])

        await b.edit(content="<:bbball:830475864172789800>" + "<:transparent:830476759463231498>"* a + ':wastebasket:', mention_author=False)
        int(a)

        if a == 0:
            await b.edit(content="<:yay:830336856415666187>", mention_author=False)
            await ctx.send(f"{ctx.author.mention}, Nice Shot! <a:jedipepe:796237771990761532> type ``.shoot`` to play again")

        elif a > 0:
            await b.edit(content="<:bbball:830475864172789800>" + "<:transparent:830476759463231498>" * a + ":wastebasket:", mention_author=False)
            await ctx.send(f"{ctx.author.mention}, oh no! you're too short <a:wutpepe:796237684170424351> type ``.shoot`` to play again")

        elif a < 0:
            await b.edit(content=':wastebasket:'+ "<:transparent:830476759463231498>" + "<:bbball:830475864172789800>", mention_author=False)
            await ctx.send(f"{ctx.author.mention}, oh no! you went past the basket <a:wutpepe:796237684170424351> type ``.shoot`` to play again")

    @commands.command()
    async def fbgame(self, ctx):
        fb = discord.Embed(title="Game Info", description="the goal keeper can  move anywhere! use your luck...\nlist of choices to decide where the ball goes (use after command):\n ``left`` ``middle`` ``right``", color=random.choice(colors))
        fb.add_field(name="Start Game: ``.kickball``", value = "_ _")
        await ctx.send(embed=fb)

    @commands.command(aliases=["kb"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def kickball(self, ctx):
        x = random.randint(0, 2)
        goalie = ":man_standing:\n"
        goal = ":goal::goal::goal:\n"
        goal2 = ":goal::goal:"
        goalmid = ":goal::soccer::goal:\n"
        ball = ":soccer:"
        plane = goal+"<:transparent:830476759463231498>"*x+goalie+ball
        f = await ctx.reply(plane, mention_author=False)

        def check(message):

            return ctx.author == message.author and ctx.channel == message.channel

        ans = await bot.wait_for('message', check=check)

        if ans.author == ctx.message.author:

            if ans.content.lower() == "right":
                y = random.randint(1, 3)
                r = random.randint(1, 2)
                if y == 3:
                    newplane = goal + "<:transparent:830476759463231498>" * 2 + goalie + "<:transparent:830476759463231498>"*2+ ball
                    await f.edit(content=newplane)
                    await ctx.send(f"{ctx.author.mention} "+ww+ " lol the goalie blocked your kick")
                    return

                elif y == 1:
                    newplane = goal2+ball+ "\n" + "<:transparent:830476759463231498>" + goalie
                    await f.edit(content=newplane)
                    await ctx.send(f"{ctx.author.mention} "+vb + " you made it into the goal")
                    return

                elif y == 2:
                    newplane = goal2 + ball + "\n" + "<:transparent:830476759463231498>" * 1 + goalie
                    await f.edit(content=newplane)
                    await ctx.send(f"{ctx.author.mention} " + vb + " you made it into the goal")
                    return

                if r == 1:
                    newplane = goal + "<:transparent:830476759463231498>" * 2 + goalie + "<:transparent:830476759463231498>" * 2 + ball
                    await f.edit(content=newplane)
                    await ctx.send(f"{ctx.author.mention} " + ww + " lol the goalie blocked your kick")
                    return

                if x == 2:
                    newplane = goal + "<:transparent:830476759463231498>" * 2 + goalie + "<:transparent:830476759463231498>"*2+ ball
                    await f.edit(content=newplane)
                    await ctx.send(f"{ctx.author.mention} "+ww+ " lol the goalie blocked your kick")
                    return

                return

            if ans.content.lower() == "left":
                y = random.randint(1, 3)
                r = random.randint(1, 2)
                if y == 1:
                    newplane = goal + goalie + ball
                    await f.edit(content=newplane)
                    await ctx.send(f"{ctx.author.mention} "+ww+ " lol the goalie blocked your kick")
                    return

                elif y == 3:
                    newplane = ball+goal2+ "\n" + "<:transparent:830476759463231498>" * 2 + goalie
                    await f.edit(content=newplane)
                    await ctx.send(f"{ctx.author.mention} "+vb + " you made it into the goal")
                    return

                elif y == 2:
                    newplane = ball+goal2 + "\n" + "<:transparent:830476759463231498>" * 1 + goalie
                    await f.edit(content=newplane)
                    await ctx.send(f"{ctx.author.mention} "+vb + " you made it into the goal")
                    return

                if r == 1:
                    newplane = goal + goalie + ball
                    await f.edit(content=newplane)
                    await ctx.send(f"{ctx.author.mention} "+ww+ " lol the goalie blocked your kick")
                    return

                if x == 0:
                    newplane = goal + goalie + ball
                    await f.edit(content=newplane)
                    await ctx.send(f"{ctx.author.mention} "+ww+ " lol the goalie blocked your kick")
                    return

                return

            if ans.content.lower() == "middle":
                y = random.randint(1, 3)
                r = random.randint(1, 2)
                if y == 1:
                    newplane = goalmid + goalie
                    await f.edit(content=newplane)
                    await ctx.send(f"{ctx.author.mention} " + vb + " you made it into the goal")
                    return

                elif y == 3:
                    newplane = goalmid + "<:transparent:830476759463231498>"*2 + goalie
                    await f.edit(content=newplane)
                    await ctx.send(f"{ctx.author.mention} " + vb + " you made it into the goal")
                    return

                elif y == 2:
                    newplane = goal + "<:transparent:830476759463231498>"*1 + goalie +"<:transparent:830476759463231498>"*1+ ball
                    await f.edit(content=newplane)
                    await ctx.send(f"{ctx.author.mention} "+ww+ " lol the goalie blocked your kick")
                    return

                if r == 1:
                    newplane = goal + goalie + ball
                    await f.edit(content=newplane)
                    await ctx.send(f"{ctx.author.mention} " + ww + " lol the goalie blocked your kick")
                    return

                if x == 1:
                    newplane = goal + "<:transparent:830476759463231498>"+goalie + "<:transparent:830476759463231498>"+ ball
                    await f.edit(content=newplane)
                    await ctx.send(f"{ctx.author.mention} "+ww+ " lol the goalie blocked your kick")
                return

            if ans.content.lower() == ".kickball":
                em = discord.Embed(title="", description="", colour=0xffb12b)
                em.add_field(name="ERROR", value="Please respond with the following options next time\n``left``, ``middle``, ``right``\n Support Server: [Join](https://discord.gg/G9vTrsV4aG)")
                await ctx.send(embed=em)
                return
            else:
                em = discord.Embed(title="", description="", colour=0xffb12b)
                em.add_field(name="ERROR",
                            value="Please respond with the following options next time\n``left``, ``middle``, ``right`` & ``.kickball`` to run the command again\n Support Server: [Join](https://discord.gg/G9vTrsV4aG)")
                await ctx.send(embed=em)
                return

    @commands.command()   
    async def blgame(self, ctx):
        bl = discord.Embed(title="Game Info", description="Choose an appropriate power level to knock down all the pins\n(type the number listed below)", color=random.choice(colors))
        bl.add_field(name="Start Game: ``.bowl``", value = "_ _", inline=False)
        bl.add_field(name="power levels list:", value="1, 2, 3, 4, 5, 6", inline=False)
        await ctx.send(embed=bl)

    @commands.command()
    async def bowl(self, ctx):
        powerlevel = "<:12:831762862124171275><:34:831762862304526356><:56:831762862388936755>"
        win = f"{ctx.author.mention} <a:4919pepelaugh:830345716437352448> You knocked all the pins! "
        lose = f"{ctx.author.mention} <a:2813pepeexit:830345717478326273> lol your too short!"
        bounds = f"{ctx.author.mention} " + ww + " yo slow down the ball went out of bounds"
        emoji = ["<:purpleball:830467076291821638>", "<:redball:830467075575119962>", "<:greenball:830467077058854922>", "<:blueball:830467076455137321>"]
        em = random.choice(emoji)
        plane = "<:pin:830469397465792512><:pin:830469397465792512><:pin:830469397465792512>\n      <:pin:830469397465792512><:pin:830469397465792512>\n             <:pin:830469397465792512>"
        broken = f"<:pin:830469397465792512><:pin:830469397465792512><:pin:830469397465792512>\n      <:pin:830469397465792512><:pin:830469397465792512>\n             <:fallenpin3:830469397671182346>{em}"
        broken2 = f"<:pin:830469397465792512><:pin:830469397465792512><:pin:830469397465792512>\n      <:fallenpin2:830469397000486963><:fallenpin1:830469397092892742>{em}\n             <:fallenpin3:830469397671182346>"
        broken3 = "<:fallenpin2:830469397000486963><:fallenpin3:830469397671182346><:fallenpin1:830469397092892742>\n      <:fallenpin2:830469397000486963><:fallenpin1:830469397092892742>\n             <:fallenpin3:830469397671182346>"
        x = random.randint(1, 6)
        newplane = plane + "\n<:transparent:830476759463231498>"*x + "\n" + "             "+em+"\n"*2+powerlevel
        b = await ctx.reply(newplane, mention_author=False)

        def check(message):

            return ctx.author == message.author and ctx.channel == message.channel

        ans = await bot.wait_for('message', check=check)

        if ans.author == ctx.message.author:
            if ans.content.lower() == "1":
                if 1 == x:
                    await b.edit(content=plane + "\n"*2+ "             " + em)
                    await asyncio.sleep(0.5)
                    await b.edit(content=broken)
                    await asyncio.sleep(0.5)
                    await b.edit(content=broken2)
                    await asyncio.sleep(0.5)
                    await b.edit(content="<:transparent:830476759463231498>" + em + "\n" + broken3)
                    await ctx.send(win)
                elif 1<x:
                    await b.edit(content=plane + "\n"*4 + "             " + em)
                    await ctx.send(lose)

            elif ans.content.lower() == "2":
                if 2 == x:
                    await b.edit(content=plane + "\n"*3+ "             " + em)
                    await asyncio.sleep(0.5)
                    await b.edit(content=broken)
                    await asyncio.sleep(0.5)
                    await b.edit(content=broken2)
                    await asyncio.sleep(0.5)
                    await b.edit(content="<:transparent:830476759463231498>" + em + "\n" + broken3)
                    await ctx.send(win)
                elif 2<x:
                    await b.edit(content=plane + "\n"*2 + "             " + em)
                    await ctx.send(lose)
            elif ans.content.lower() == "3":
                if 3 == x:
                    await b.edit(content=plane + "\n"*3+ "             " + em)
                    await asyncio.sleep(0.5)
                    await b.edit(content=broken)
                    await asyncio.sleep(0.5)
                    await b.edit(content=broken2)
                    await asyncio.sleep(0.5)
                    await b.edit(content="<:transparent:830476759463231498>" + em + "\n" + broken3)
                    await ctx.send(win)
                elif 3<x:
                    await b.edit(content=plane + "\n"*3 + "             " + em)
                    await ctx.send(lose)
                elif 3>x:
                    await b.edit(content="<:transparent:830476759463231498>"+em+"\n"*2+plane)
                    await ctx.send(bounds)
            elif ans.content.lower() == "4":
                if 4 == x:
                    await b.edit(content=plane + "\n"*3+ "             " + em)
                    await asyncio.sleep(0.5)
                    await b.edit(content=broken)
                    await asyncio.sleep(0.5)
                    await b.edit(content=broken2)
                    await asyncio.sleep(0.5)
                    await b.edit(content="<:transparent:830476759463231498>" + em + "\n" + broken3)
                    await ctx.send(win)
                elif 4<x:
                    await b.edit(content=plane + "\n"*3 + "             " + em)
                    await ctx.send(lose)
                elif 4>x:
                    await b.edit(content="<:transparent:830476759463231498>"+em+"\n"*3+plane)
                    await ctx.send(bounds)
            elif ans.content.lower() == "5":
                if 5 == x:
                    await b.edit(content=plane + "\n"*3+ "             " + em)
                    await asyncio.sleep(0.5)
                    await b.edit(content=broken)
                    await asyncio.sleep(0.5)
                    await b.edit(content=broken2)
                    await asyncio.sleep(0.5)
                    await b.edit(content="<:transparent:830476759463231498>" + em + "\n" + broken3)
                    await ctx.send(win)
                elif 5<x:
                    await b.edit(content=plane + "\n"*3 + "             " + em)
                    await ctx.send(lose)
                elif 5>x:
                    await b.edit(content="<:transparent:830476759463231498>"+em+"\n"*4+plane)
                    await ctx.send(bounds)

            elif ans.content.lower() == "6":
                if 6 == x:
                    await b.edit(content=plane + "\n"*3+ "             " + em)
                    await asyncio.sleep(0.5)
                    await b.edit(content=broken)
                    await asyncio.sleep(0.5)
                    await b.edit(content=broken2)
                    await asyncio.sleep(0.5)
                    await b.edit(content="<:transparent:830476759463231498>" + em + "\n" + broken3)
                    await ctx.send(win)
                elif 6>x:
                    await b.edit(content="<:transparent:830476759463231498>"+em+"\n"*6+plane)
                    await ctx.send(bounds)
            else:
                if ans.content.lower() == ".bowl":
                    em = discord.Embed(title="", description="", colour=0xffb12b)
                    em.add_field(name="ERROR",
                                value="Please respond with the following options next time\n``1``, ``2``, ``3``, ``4``, ``5``, ``6``\nrun ``.blgame`` for more info\nSupport Server: [Join](https://discord.gg/G9vTrsV4aG)")
                    await ctx.send(embed=em)
                    return
                else:
                    em = discord.Embed(title="", description="", colour=0xffb12b)
                    em.add_field(name="ERROR",
                                value="Please respond with the following options next time\n``1``, ``2``, ``3``, ``4``, ``5``, ``6`` & ``.bowl`` to run the command again\nrun ``.blgame`` for more info\n Support Server: [Join](https://discord.gg/G9vTrsV4aG)")
                    await ctx.send(embed=em)
                    return

async def setup(bot):
    await bot.add_cog(Game(bot))