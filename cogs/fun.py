from discord.ext import commands
from aurora_secrets import *
from aurora_lists import *
import discord
import asyncio
import random


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fun(self, ctx):
        fun = discord.Embed(title="FUN", description="Busy day? why not have some fun", color=0xffdd00)
        fun.add_field(name="🔪️ ``.destroyme``", value="wanna get roasted?", inline=False)
        fun.add_field(name=":gun: ``.destroy <@user>``", value="wanna destroy someone?", inline=False)
        fun.add_field(name="✂️ ``.start``", value="rock paper scissors", inline=False)
        fun.add_field(name=":8ball: ``.8ball``", value="a classic 8ball answer", inline=False)
        fun.add_field(name="🤔️ ``.riddle``", value="train your brain", inline=False)
        fun.add_field(name="<:ruler:832256221431988265> ``.numbers``", value="fun commands which use basic math", inline=False)
        fun.add_field(name="🐱‍💻 ``.hack``", value="wanna get hacked? or wanna hack?", inline=False)
        fun.set_thumbnail( url="https://media.discordapp.net/attachments/807511480878497806/832262569917808670/aurora_fun.png")

        await ctx.send(embed=fun)


    @commands.command()
    async def destroyme(self, ctx):
        await ctx.send(f"{ctx.author.mention} {random.choice(roasts)}")


    @commands.command()
    async def destroy(self, ctx, member: discord.Member):
        if self.bot.user.mentioned_in(ctx.message):
            await ctx.send("Imagine being dumb enough to try to destroy me")
        elif member == member:
            await ctx.send('{0.name}, '.format(member)+(random.choice(roasts)))


    @commands.command(name="8ball")
    async def eight_ball(self, ctx, *, message):
        msg = message
        if any(word in msg for word in ball_arg):
            await ctx.reply("Listen kid, the owner and I are **chad** so back off 😄", mention_author=False)
        else:
            await ctx.reply("🎱️ " + random.choice(ball), mention_author=False)


    @commands.command()
    async def riddle(self, ctx):
        ridem = discord.Embed(title=" ", description="",color=random.choice(colors))
        ridem.add_field(name="The answer is marked as spoiler",value=(random.choice(riddles)), inline=False)

        await ctx.send(embed=ridem)


    @commands.command()
    async def start(self, ctx):
        rps = discord.Embed(title="Rock Paper Scissor Game", description="Use the following words as your action", color=0x6b6b6b)
        rps.add_field(name="Run: ``.rps <choice>``\n_ _\nChoices:", value="``👊 Rock``_ _ _ _``✌ Scissors``_ _ _ _``✋ Paper``")
        rps.set_footer(text="You don't have to use the emoji")

        await ctx.send(embed=rps)


    @commands.command()
    async def rps(self, ctx, *, message):
        msg = message
        user_choice = msg
        comp_choice = random.choice(rp)
        if any(word.lower() in msg.lower() for word in rp):
            await ctx.send(comp_choice)

        if user_choice.lower() == 'rock':
            if comp_choice == 'rock':
                await ctx.send(f'{ctx.author.mention}, ``🟡`` Draw')
            elif comp_choice == 'paper':
                await ctx.send(f'{ctx.author.mention}, ``🔴`` You Lose')
            elif comp_choice == 'scissors':
                await ctx.send(f"{ctx.author.mention}, ``🟢`` You Win")

        elif user_choice.lower() == 'paper':
            if comp_choice == 'rock':
                await ctx.send(f"{ctx.author.mention}, ``🟢`` You Win")
            elif comp_choice == 'paper':
                await ctx.send(f"{ctx.author.mention}, ``🟡`` Draw")
            elif comp_choice == 'scissors':
                await ctx.send(f'{ctx.author.mention}, ``🔴`` You Lose')

        elif user_choice.lower() == 'scissors':
            if comp_choice == 'rock':
                await ctx.send(f'{ctx.author.mention}, ``🔴`` You Lose')
            elif comp_choice == 'paper':
                await ctx.send(f"{ctx.author.mention}, ``🟢`` You Win")
            elif comp_choice == 'scissors':
                await ctx.send(f"{ctx.author.mention}, ``🟡`` Draw")
        else:
            await ctx.send("You can only use ``rock``, ``paper``, ``scissors`` (case insensitive)")


    @commands.command(aliases=["number"])
    async def numbers(self, ctx):
        no = discord.Embed(title="NUMBERS", description="Command List:", colour=0x46850)
        no.add_field(name="❌ ``.oddeven <choice>``", value="guess whether the number will be odd or even between 5 and 25", inline=False)
        no.add_field(name="✅ ``.findnum <number>``", value="guess a number between 1 to 10", inline=False)
        
        await ctx.send(embed=no)


    @commands.command()
    async def oddeven(ctx, *, message):
        x = random.randint(5, 25)

        if message == "odd":
            if x % 2 == 0:
                await ctx.send(f"``🔴`` You lose, the number was: ``{x}``")

            elif x % 2 == 1:
                await ctx.send(f"``🟢`` You win, the number was: ``{x}``")

            return

        if message == "even":
            if x % 2 == 0:
                await ctx.send(f"``🟢`` You win, the number was: ``{x}``")

            elif x % 2 == 1:
                await ctx.send(f"``🔴`` You lose, the number was: ``{x}``")

            return

        if message != "odd" or "even":
            error_msg = discord.Embed(title=" ", description=" ", color=0xffb12b)
            error_msg.add_field(name="Error", value="please enter a valid choice: ``odd`` or ``even``\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
            await ctx.send(embed=error_msg)


    @commands.command()
    async def findnum(ctx, *, message):
        x = random.randint(1, 10)

        try:
            message = int(message)
            if message > 10:
                await ctx.send("Error! Enter a number between ``1`` to ``10``")

                return
            
            elif message < 1:
                await ctx.send("Error! Enter a number between ``1`` to ``10``")
                
                return
            
            elif message == x:
                await ctx.send(f"🎉 **No Way!** you guessed it right. The number was ``{x}``")
                
                return
            
            elif message != x:
                await ctx.send(f"💀 **Fail!** you guessed it wrong. The number was ``{x}``")
                
                return
            
        except ValueError:
            error_msg = discord.Embed(title=" ", description=" ", color=0xffb12b)
            error_msg.add_field(name="Error", value="please enter a valid number between ``1`` to ``10``\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
            
            await ctx.send(embed=error_msg)


    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def hack(ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
            await ctx.send("ayo forgot to mention someone? I guess I'll have to hack you...")

        await asyncio.sleep(1)

        hax = discord.Embed(title="```Virus Activated```",description=f"{user.mention}", colour=0x63ff52)
        hax.add_field(name="Now we wait...", value="```lol, your info and device is mine :)```")
        hax.set_image(url="https://media.discordapp.net/attachments/807511480878497806/829318751177539594/Untitled_design2.gif")
        hax.set_footer(text="🤡🤝")
        j = await ctx.send(embed=hax)

        await asyncio.sleep(1)
        h = await ctx.send("fetching client's gmail account and password... ")
        await asyncio.sleep(1)
        await h.edit(content=f"Gmail: ``{user}@aurorafan.com``\npassword: ``" + random.choice(fake_pwds)+"``")
        await asyncio.sleep(1)
        await h.edit(content="retrieving friends list.")
        await h.edit(content="retrieving friends list..")
        await h.edit(content="retrieving friends list...")
        await asyncio.sleep(0.5)
        await h.edit(content="``*no friends were found 😆*``")
        await asyncio.sleep(1)
        await h.edit(content="installing forknite mobile hacks on device.")
        await h.edit(content="installing forknite mobile hacks on device..")
        await h.edit(content="installing forknite mobile hacks on device...")
        await asyncio.sleep(0.5)
        await h.edit(content="injecting virus.")
        await h.edit(content="injecting virus...")
        await asyncio.sleep(0.5)
        await h.edit(content="``🟢 SUCCESSFUL!``")
        await asyncio.sleep(1)
        await h.edit(content="*high level* *totally dangerous* hack was completed ;)")

        newhax = discord.Embed(title="```Virus Activated```",description=f"{user.mention}", colour=0x63ff52)
        newhax.add_field(name="Hack Completed",value="```lol, your info and device is mine :)```")
        newhax.set_image(url="https://media.discordapp.net/attachments/807511480878497806/829318751177539594/Untitled_design2.gif")
        newhax.set_footer(text="🤡🤝")

        await j.edit(embed=newhax)
                
                
async def setup(bot):
    await bot.add_cog(Fun(bot))