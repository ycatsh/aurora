from discord.ext import commands 
import discord
import mysql.connector
import random
import asyncio
from aurora_lists import colors, riddles, ball, ball_arg, roasts, rp, vb, ww, xp, coin, dpe, hpe, vpe, dash, qge, ebe, ame, woe, ate, dfe, hae, mbe

db = mysql.connector.connect(
    host='localhost', user="root", passwd="your_pwd", database="database_name", auth_plugin="mysql_native_password")

cursor = db.cursor()

intents = discord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix = ".", case_insensitive=True, intents=intents)

class Shop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.group(name="shop", invoke_without_command=True)
    async def shop(self, ctx):
        shop = discord.Embed(title="Shop Items", description=f"**__LIMITED TIME OFFER__**\nget a {mbe} mystery box upon boosting [Aurora's community server](https://discord.gg/G9vTrsV4aG)\nIt can fetch you 8 - 15k coins and other in-game items\n\n", color=0x99ffd3)
        shop.add_field(name=f"{dpe} **Durability Potion** {dash} ``500``", value=f"*ID* → ``dp`` drink a like a fish to increase your defense by 5", inline = False)
        shop.add_field(name="_ _", value="_ _", inline = False)
        shop.add_field(name=f"{hpe} **Health Potion** {dash} ``200``", value="*ID* → ``hp`` keep chugging for good health, increase your health by 10", inline = False)
        shop.add_field(name="_ _", value="_ _", inline = False)
        shop.add_field(name=f"{vpe} **Vigour Potion** {dash} ``500``", value="*ID* → ``vp`` this booze makes you stronger, increase your attack level by 5", inline = False)
        shop.add_field(name="_ _", value="_ _", inline = False)
        shop.add_field(name=f"{qge} **Quantum Gun** {dash} ``2000``", value="*ID* → ``qg`` incinerate your opponents, does 20 damage", inline = False)
        shop.add_field(name="_ _", value="_ _", inline = False)
        shop.add_field(name=f"{ebe} **Energy Bazooka** {dash} ``5000``", value="*ID* → ``eb`` If you're against this weapon, you should be scared. does 75 damage", inline = False)
        shop.add_field(name="_ _", value="run ``.shop info <id>`` for more information on the items", inline=False)
        shop.set_footer(text="page 1/2")
        await ctx.send(embed=shop)

    @shop.command(name="2")
    async def shop_2(self, ctx):
        shop2 = discord.Embed(title="", color=0x99ffd3)
        shop2.add_field(name=f"{woe} **Witch's Orb** {dash} ``10,000``", value="*ID* → ``orb`` there is a 50% you'll lose all your coins or double them, use wisely", inline = False)
        shop2.add_field(name="_ _", value="_ _", inline = False)
        shop2.add_field(name=f"{ame} **Molecule** {dash} ``1,000,000``", value=f"*ID* → ``molecule`` an item only for the rich", inline=False)
        shop2.add_field(name="_ _", value="run ``.shop info <id>`` for more information on the items", inline=False)
        shop2.set_footer(text="page 2/2")
        await ctx.send(embed=shop2)

    @shop.command(name="info")
    async def shop_info(self, ctx, message):
        if message.lower() == "dp":
            se = discord.Embed(title="Durability Potion", description="drink a like a fish to increase your defense by 5, useful in duels to tank oppenents punches", color=0x8545b0)
            se.add_field(name="Buying Price: ``500``\nSelling Price: ``200``", value="_ _", inline=False)
            se.set_thumbnail(url="https://media.discordapp.net/attachments/807511480878497806/848819806497013780/dpot.png")
            await ctx.send(embed=se)
        elif message.lower() == "hp":
            se = discord.Embed(title="Health Potion", description="keep chugging for good health, increase your health by 10, useful in duels to stay alive ", color=0xb32937)
            se.add_field(name="Buying Price: ``200``\nSelling Price: ``75``", value="_ _", inline=False)
            se.set_thumbnail(url="https://media.discordapp.net/attachments/807511480878497806/848819986428198922/hpot.png")
            await ctx.send(embed=se)
        elif message.lower() == "vp":
            se = discord.Embed(title="Vigour Potion", description="this booze makes you stronger, increase your attack level by 5, useful in duels to deal more damage", color=0xffea00)
            se.add_field(name="Buying Price: ``500``\nSelling Price: ``250``", value="_ _", inline=False)
            se.set_thumbnail(url="https://media.discordapp.net/attachments/807511480878497806/848820149637087232/vpot.png")
            await ctx.send(embed=se)
        elif message.lower() == "qg":
            se = discord.Embed(title="Quantum Gun", description=" incinerate your opponents, does 20 damage. Use this in duels to defeat your opponents", color=0x00ff11)
            se.add_field(name="Buying Price: ``2000``\nSelling Price: ``1000``", value="_ _", inline=False)
            se.set_thumbnail(url="https://media.discordapp.net/attachments/807511480878497806/848820293237604402/qgun.png")
            await ctx.send(embed=se)
        elif message.lower() == "eb":
            se = discord.Embed(title="Energy Bazooka", description="If you're against this weapon, you should be scared. does 75 damage. Use this in duels to defeat your opponents", color=0x00bbff)
            se.add_field(name="Buying Price: ``5000``\nSelling Price: ``3000``", value="_ _", inline=False)
            se.set_thumbnail(url="https://media.discordapp.net/attachments/807511480878497806/848820441832751104/eb.png")
            await ctx.send(embed=se)  
        elif message.lower() == "orb":
            se = discord.Embed(title="Witch's Orb", description="there is a 50% you'll lose all your coins or double them, use wisely. If you have over 100k then only 100k will get doubled not your entire wallet", color=0xbb54ff)
            se.add_field(name="Buying Price: ``10,000``\nSelling Price: ``4000``", value="_ _", inline=False)
            se.set_thumbnail(url="https://media.discordapp.net/attachments/807511480878497806/848818984128479262/844221988419534869.png")
            await ctx.send(embed=se)
        elif message.lower() == "molecule":
            se = discord.Embed(title="Molecule", description="This item has no purpose, It can only be collected. Flex on people who can't aford it", color=0x54e5ff)
            se.add_field(name="Buying Price: ``1,000,000``\nSelling Price: ``Cannot be sold``", value="_ _", inline=False)
            se.set_thumbnail(url="https://media.discordapp.net/attachments/807511480878497806/848820623127216128/molecule.png")
            await ctx.send(embed=se)
        else:
            errormsg = discord.Embed(title=" ", Description=" ", color=0xffb12b)
            errormsg.add_field(name="Error", value="please enter a valid item's ID to get more information on it\nFormat: ``.shop info <id>``\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
            await ctx.reply(embed=errormsg, mention_author = False)

    @commands.group(name="sell", invoke_without_command=True)
    async def sell(self, ctx):
        await ctx.send("UNDER DEV")

    @commands.group(name= "buy", invoke_without_command=True)
    async def buy(self, ctx):
        errormsg = discord.Embed(title=" ", Description=" ", color=0xffb12b)
        errormsg.add_field(name="Error", value="please enter a valid amount and a valid ID to buy an item\nFormat: ``.buy <item id> <amount>``\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
        await ctx.reply(embed=errormsg, mention_author = False)       
        
    @buy.command(name="dp")
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def buy_dp(self, ctx, *, message):
        try:
            message = int(message)
            cursor.execute("select durapot from users where client_id = %s", [ctx.author.id])
            result = cursor.fetchall()
            cursor.execute("select user_coins from users where client_id = %s", [ctx.author.id])
            result2 = cursor.fetchall()

            if len(result2) == 0:
                await ctx.send(f"{ctx.author.name} hasn't started playing, to learn more about the game please run ``.rpg info`` or just start by ``.quest``")

            if message < 1: 
                await ctx.send("You cant buy like that 😂️")

            else:
                buy = result[0][0] + message
                money = result2[0][0] - message*500

                if money<0:
                    await ctx.reply(f"Check your balance first, you don't have enough money to buy {message} of this item", mention_author = False)
                    return
                else:
                    cursor.execute("UPDATE users set user_coins = %s, durapot = %s where client_id = %s", [money, buy, ctx.author.id])
                    await ctx.reply(f"{dpe} You've bought ``{message}`` Durability potion(s). Total in inventory = ``{buy}``")
                    db.commit() 
                
        except ValueError:
            errormsg = discord.Embed(title=" ", Description=" ", color=0xffb12b)
            errormsg.add_field(name="Error", value="please enter a valid amount of the item you're trying to buy \nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
            await ctx.reply(embed=errormsg, mention_author = False)

    @buy.command(name="hp")
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def buy_hp(self, ctx, *, message):
        try:
            message = int(message)
            cursor.execute("select healpot from users where client_id = %s", [ctx.author.id])
            result = cursor.fetchall()
            cursor.execute("select user_coins from users where client_id = %s", [ctx.author.id])
            result2 = cursor.fetchall()

            if len(result2) == 0:
                await ctx.send(f"{ctx.author.name} hasn't started playing, to learn more about the game please run ``.rpg info`` or just start by ``.quest``")

            if message < 1: 
                await ctx.send("You cant buy like that 😂️")
            else:

                buy = result[0][0] + message
                money = result2[0][0] - message*200

                if money<0:
                    await ctx.reply(f"Check your balance first, you don't have enough money to buy {message} of this item", mention_author = False)
                    return
                else:
                    cursor.execute("UPDATE users set user_coins = %s, healpot = %s where client_id = %s", [money, buy, ctx.author.id])
                    await ctx.reply(f"{hpe} You've bought ``{message}`` Health potion(s). Total in inventory = ``{buy}``")
                db.commit() 
                
        except ValueError:
            errormsg = discord.Embed(title=" ", Description=" ", color=0xffb12b)
            errormsg.add_field(name="Error", value="please enter a valid amount of the item you're trying to buy \nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
            await ctx.reply(embed=errormsg, mention_author = False)

    @buy.command(name="vp")
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def buy_vp(self, ctx, *, message):
        try:
            message = int(message)
            cursor.execute("select vigopot from users where client_id = %s", [ctx.author.id])
            result = cursor.fetchall()
            cursor.execute("select user_coins from users where client_id = %s", [ctx.author.id])
            result2 = cursor.fetchall()

            if len(result2) == 0:
                await ctx.send(f"{ctx.author.name} hasn't started playing, to learn more about the game please run ``.rpg info`` or just start by ``.quest``")

            if message < 1: 
                await ctx.send("You cant buy like that 😂️")
            else:

                buy = result[0][0] + message
                money = result2[0][0] - message*500

                if money<0:
                    await ctx.reply(f"Check your balance first, you don't have enough money to buy {message} of this item", mention_author = False)
                    return
                else:
                    cursor.execute("UPDATE users set user_coins = %s, vigopot = %s where client_id = %s", [money, buy, ctx.author.id])
                    await ctx.reply(f"{vpe} You've bought ``{message}`` Vigour potion(s). Total in inventory = ``{buy}``")
                    db.commit() 
                
        except ValueError:
            errormsg = discord.Embed(title=" ", Description=" ", color=0xffb12b)
            errormsg.add_field(name="Error", value="please enter a valid amount of the item you're trying to buy \nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
            await ctx.reply(embed=errormsg, mention_author = False)

    @buy.command(name="qg")
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def buy_qg(self, ctx, *, message):
        try:
            message = int(message)
            cursor.execute("select quagun from users where client_id = %s", [ctx.author.id])
            result = cursor.fetchall()
            cursor.execute("select user_coins from users where client_id = %s", [ctx.author.id])
            result2 = cursor.fetchall()

            if len(result2) == 0:
                await ctx.send(f"{ctx.author.name} hasn't started playing, to learn more about the game please run ``.rpg info`` or just start by ``.quest``")

            if message < 1: 
                await ctx.send("You cant buy like that 😂️")
            else:

                buy = result[0][0] + message
                money = result2[0][0] - message*2000

                if money<0:
                    await ctx.reply(f"Check your balance first, you don't have enough money to buy {message} of this item", mention_author = False)
                    return
                else:
                    cursor.execute("UPDATE users set user_coins = %s, quagun = %s where client_id = %s", [money, buy, ctx.author.id])
                    await ctx.reply(f"{qge} You've bought ``{message}`` Quantum Gun(s). Total in inventory = ``{buy}``")
                    db.commit() 

        except ValueError:
            errormsg = discord.Embed(title=" ", Description=" ", color=0xffb12b)
            errormsg.add_field(name="Error", value="please enter a valid amount of the item you're trying to buy \nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
            await ctx.reply(embed=errormsg, mention_author = False)

    @buy.command(name="eb")
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def buy_eb(self, ctx, *, message):
        try:
            message = int(message)
            cursor.execute("select enebazo from users where client_id = %s", [ctx.author.id])
            result = cursor.fetchall()
            cursor.execute("select user_coins from users where client_id = %s", [ctx.author.id])
            result2 = cursor.fetchall()

            if len(result2) == 0:
                await ctx.send(f"{ctx.author.name} hasn't started playing, to learn more about the game please run ``.rpg info`` or just start by ``.quest``")

            if message < 1: 
                await ctx.send("You cant buy like that 😂️")
            else:

                buy = result[0][0] + message
                money = result2[0][0] - message*5000

                if money<0:
                    await ctx.reply(f"Check your balance first, you don't have enough money to buy {message} of this item", mention_author = False)
                    return
                else:
                    cursor.execute("UPDATE users set user_coins = %s, enebazo = %s where client_id = %s", [money, buy, ctx.author.id])
                    await ctx.reply(f"{ebe} You've bought ``{message}`` Energy Bazooka(s). Total in inventory = ``{buy}``")
                    db.commit() 
                
        except ValueError:
            errormsg = discord.Embed(title=" ", Description=" ", color=0xffb12b)
            errormsg.add_field(name="Error", value="please enter a valid amount of the item you're trying to buy \nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
            await ctx.reply(embed=errormsg, mention_author = False)

    @buy.command(name="orb")
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def buy_orb(self, ctx, *, message):
        try:
            message = int(message)
            cursor.execute("select orb from users where client_id = %s", [ctx.author.id])
            result = cursor.fetchall()
            cursor.execute("select user_coins from users where client_id = %s", [ctx.author.id])
            result2 = cursor.fetchall()

            if len(result2) == 0:
                await ctx.send(f"{ctx.author.name} hasn't started playing, to learn more about the game please run ``.rpg info`` or just start by ``.quest``")

            if message < 1: 
                await ctx.send("You cant buy like that 😂️")
            else:

                buy = result[0][0] + message
                money = result2[0][0] - message*10000

                if money<0:
                    await ctx.reply(f"Check your balance first, you don't have enough money to buy {message} of this item", mention_author = False)
                    return
                else:
                    cursor.execute("UPDATE users set user_coins = %s, orb = %s where client_id = %s", [money, buy, ctx.author.id])
                    await ctx.reply(f"{woe} You've bought ``{message}`` Witch's Orb(s). Total in inventory = ``{buy}``")
                    db.commit() 
                
        except ValueError:
            errormsg = discord.Embed(title=" ", Description=" ", color=0xffb12b)
            errormsg.add_field(name="Error", value="please enter a valid amount of the item you're trying to buy \nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
            await ctx.reply(embed=errormsg, mention_author = False)

    @buy.command(name="molecule")
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def buy_molecule(self, ctx, *, message):
        try:
            message = int(message)
            cursor.execute("select molecule from users where client_id = %s", [ctx.author.id])
            result = cursor.fetchall()
            cursor.execute("select user_coins from users where client_id = %s", [ctx.author.id])
            result2 = cursor.fetchall()

            if len(result2) == 0:
                await ctx.send(f"{ctx.author.name} hasn't started playing, to learn more about the game please run ``.rpg info`` or just start by ``.quest``")

            if message < 1: 
                await ctx.send("You cant buy like that 😂️")
            else:
                buy = result[0][0] + message
                money = result2[0][0] - message*1000000

                if money<0:
                    await ctx.reply(f"Check your balance first, you don't have enough money to buy {message} of this item", mention_author = False)
                    return
                else:
                    cursor.execute("UPDATE users set user_coins = %s, molecule = %s where client_id = %s", [money, buy, ctx.author.id])
                    await ctx.reply(f"{ame} You've bought ``{message}`` Molecule(s). Total in inventory = ``{buy}``")
                    db.commit() 
                
        except ValueError:
            errormsg = discord.Embed(title=" ", Description=" ", color=0xffb12b)
            errormsg.add_field(name="Error", value="please enter a valid amount of the item you're trying to buy \nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
            await ctx.reply(embed=errormsg, mention_author = False)



    @commands.group(name="use", invoke_without_command=True)
    async def use(self, ctx):
        errormsg = discord.Embed(title=" ", Description=" ", color=0xffb12b)
        errormsg.add_field(name="Error", value="please enter a valid ID to use an item\nFormat: ``.use <item id> <quantity>``\n``quantity`` doesnt apply for these items: ``orb``, ``box``\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
        await ctx.reply(embed=errormsg, mention_author = False) 

    @use.command(name="dp")
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def use_dp(self, ctx, *, message):
        try:
            message = int(message)

            if message < 0:
                await ctx.reply("dont try to break me, you can use anything like that 😂️", mention_author = False)
            else:
                cursor.execute("select defense from users where client_id = %s", [ctx.author.id])
                result = cursor.fetchall()
                cursor.execute("select durapot from users where client_id = %s", [ctx.author.id])
                result2 = cursor.fetchall()
                DEF = result[0][0] + (5 * message)
                dpi = result2[0][0] - message
                final = (5 * message)

                if dpi < 0:
                    await ctx.send(f"{ctx.author.name} you dont have that many durability potions 😂️ dont't try to scam me")
                else:
                    cursor.execute("update users set durapot = %s, defense = %s where client_id = %s", [dpi, DEF, ctx.author.id])
                    await ctx.reply(f"You chugged down {message} {dpe} ``Durability Potion (s)`` to gain ``+{final}`` DEF", mention_author = False)
                    db.commit()
        except ValueError:
            errormsg = discord.Embed(title=" ", Description=" ", color=0xffb12b)
            errormsg.add_field(name="Error", value="please enter a valid amount of the item you're trying to use \nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
            await ctx.reply(embed=errormsg, mention_author = False)
            

    @use.command(name="hp")
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def use_hp(self, ctx, *, message):

        try:
            message = int(message)

            if message < 0:
                await ctx.reply("dont try to break me, you can use anything like that 😂️", mention_author = False)
            else:
                cursor.execute("select health from users where client_id = %s", [ctx.author.id])
                result = cursor.fetchall()
                cursor.execute("select healpot from users where client_id = %s", [ctx.author.id])
                result2 = cursor.fetchall()
                HEALTH = result[0][0] + (10 * message)
                hpi = result2[0][0] - message
                final = (10 * message)

                if hpi < 0:
                    await ctx.send(f"{ctx.author.name} you dont have that many health potions 😂️ dont't try to scam me")
                else:
                    cursor.execute("update users set healpot = %s, health = %s where client_id = %s", [hpi, HEALTH, ctx.author.id])
                    await ctx.reply(f"You chugged down {message} {hpe} ``Health Potion (s)`` to gain ``+{final}`` HEALTH", mention_author = False)
                    db.commit()

        except ValueError:
            errormsg = discord.Embed(title=" ", Description=" ", color=0xffb12b)
            errormsg.add_field(name="Error", value="please enter a valid amount of the item you're trying to buy \nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
            await ctx.reply(embed=errormsg, mention_author = False)
            

    @use.command(name="vp")
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def use_vp(self, ctx, *, message):
        try:
            message = int(message)
            if message < 0:
                await ctx.reply("dont try to break me, you can use anything like that 😂️", mention_author = False)
            else:
                cursor.execute("select attack from users where client_id = %s", [ctx.author.id])
                result = cursor.fetchall()
                cursor.execute("select vigopot from users where client_id = %s", [ctx.author.id])
                result2 = cursor.fetchall()
                vpi = result2[0][0] - message
                ATTCK = result[0][0] + (5 * message)
                final = (5 * message)

                if vpi < 0:
                    await ctx.send(f"{ctx.author.name} you dont that many vigour potions 😂️ dont't try to scam me")
                else:
                    cursor.execute("update users set vigopot = %s, attack = %s where client_id = %s", [vpi, ATTCK, ctx.author.id])
                    await ctx.reply(f"You chugged down {message} {vpe} ``Vigour Potion (s)`` to gain ``+{final}`` ATTCK", mention_author = False)
                    db.commit()
        except ValueError:
            errormsg = discord.Embed(title=" ", Description=" ", color=0xffb12b)
            errormsg.add_field(name="Error", value="please enter a valid amount of the item you're trying to buy \nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
            await ctx.reply(embed=errormsg, mention_author = False)

    @use.command(name="orb")
    @commands.cooldown(1, 10800, commands.BucketType.user)
    async def use_orb(self, ctx):
        cursor.execute("select user_coins from users where client_id = %s", [ctx.author.id])
        result = cursor.fetchall()
        cursor.execute("select orb from users where client_id = %s", [ctx.author.id])
        result2 = cursor.fetchall()

        walletmoney = result[0][0]
        orbs = result2[0][0]

        if orbs == 0:
            await ctx.send(f"{ctx.author.name} you dont have any orbs 😂️ dont't try to scam me")

        elif walletmoney == 0:
            await ctx.send(f"{ctx.author.name} you dont have any money 😂️ dont't try to scam me")

        else:
            chance = random.randint(1, 2)

            if chance == 1:
                if walletmoney > 100000:
                    wmfinal = walletmoney + 100000
                    cursor.execute("update users set user_coins = %s where client_id = %s", [wmfinal, ctx.author.id])
                    await ctx.reply(f"☑️ {woe} was in your favour! you doubled 100k from your balance", mention_author = False)
                    db.commit()

                else:
                    wmf = walletmoney * 2
                    cursor.execute("update users set user_coins = %s where client_id = %s", [wmf, ctx.author.id])
                    await ctx.reply(f"☑️ {woe} was in your favour! you doubled your wallet (max amount that can be doubled is 100k)", mention_author = False)
                    db.commit()

            elif chance == 2:
                cursor.execute("update users set user_coins = 0 where client_id = %s", [ctx.author.id])
                await ctx.reply(f"❌️ {woe} was not in your favour! you lost all your money - {walletmoney}", mention_author = False)
                db.commit()

    @use.command(name="box")
    @commands.cooldown(1, 120, commands.BucketType.user)
    async def use_box(self, ctx):
        cursor.execute("select box from users where client_id = %s", [ctx.author.id])
        res = cursor.fetchall()

        if len(res) == 0:
            await ctx.reply(f"{ctx.author.name} you dont any mystery boxes 😂️ dont't try to scam me", mention_author = False)

        else:

            rng = random.randint(1, 3)

            if rng == 1:
                cursor.execute("select user_coins, healpot, orb, box from users where client_id = %s", [ctx.author.id])
                res1 = cursor.fetchall()

                c = res1[0][0] + 10000
                h = res1[0][1] + 5
                o = res1[0][2] + 1
                b = res1[0][3] - 1

                cursor.execute("update users set user_coins = %s, healpot = %s, orb = %s, box = %s where client_id = %s", [c, h, o, b, ctx.author.id])

                r1 = await ctx.reply(f"{mbe} The Box contained the follwing:")
                await asyncio.sleep(0.5)
                await r1.edit(content=f"{mbe} The Box contained the follwing:\n\n{coin} 10,000 coins\n")
                await asyncio.sleep(0.5)
                await r1.edit(content=f"{mbe} The Box contained the follwing:\n\n{coin} 10,000 coins\n{hpe} 5 Health Potions\n")
                await asyncio.sleep(0.5)
                await r1.edit(content=f"{mbe} The Box contained the follwing:\n\n{coin} 10,000 coins\n{hpe} 5 Health Potions\n{woe} 1 orb")
                db.commit()
                
            elif rng == 2:

                cursor.execute("select user_coins, quagun, orb, box from users where client_id = %s", [ctx.author.id])
                res2 = cursor.fetchall()

                c2 = res2[0][0] + 8000
                q = res2[0][1] + 1
                o2 = res2[0][2] + 2
                b2 = res2[0][3] - 1

                cursor.execute("update users set user_coins = %s, quagun = %s, orb = %s, box = %s where client_id = %s", [c2, q, o2, b2, ctx.author.id])

                r2 = await ctx.reply(f"{mbe} The Box contained the follwing:")
                await asyncio.sleep(0.5)
                await r2.edit(content=f"{mbe} The Box contained the follwing:\n\n{coin} 8,000 coins\n")
                await asyncio.sleep(0.5)
                await r2.edit(content=f"{mbe} The Box contained the follwing:\n\n{coin} 8,000 coins\n{qge} 1 Quantum Gun\n")
                await asyncio.sleep(0.5)
                await r2.edit(content=f"{mbe} The Box contained the follwing:\n\n{coin} 8,000 coins\n{qge} 1 Quantum Gun\n{woe} 2 orbs")
                db.commit()

            elif rng == 3:
                
                cursor.execute("select user_coins, durapot, box from users where client_id = %s", [ctx.author.id])
                res3 = cursor.fetchall()

                c3 = res3[0][0] + 15000
                d = res3[0][1] + 3
                b3 = res3[0][2] - 1

                cursor.execute("update users set user_coins = %s, durapot = %s, box = %s where client_id = %s", [c3, d, b3, ctx.author.id])

                r3 = await ctx.reply(f"{mbe} The Box contained the follwing:")
                await asyncio.sleep(0.5)
                await r3.edit(content=f"{mbe} The Box contained the follwing:\n\n{coin} 15,000 coins\n")
                await asyncio.sleep(0.5)
                await r3.edit(content=f"{mbe} The Box contained the follwing:\n\n{coin} 15,000 coins\n{dpe} 3 Durability Potions")
                db.commit()


    @use.command(name="qg")
    async def use_qg(self, ctx):
        await ctx.send("This can only be used in a duel. To duel yor friends run ``.duel``")

    @use.command(name="eb")
    async def use_eb(self, ctx):
        await ctx.send("This can only be used in a duel. To duel yor friends run ``.duel``")

    @use.command(name="molecule")
    async def use_molecule(self, ctx):
        await ctx.send(f"{ame} ``molecule`` is a collectible and cannot be used")



async def setup(bot):
    await bot.add_cog(Shop(bot))