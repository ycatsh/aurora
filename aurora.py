import discord
import random
import itertools
import asyncio
import datetime
import datetime
import time
from discord.ext import commands
from aurora_lists import *
from aurora_secrets import DISCORD_TOKEN, db, reddit

s_time = time.time()

cursor = db.cursor()

intents = discord.Intents.all()
intents.messages = True

bot = commands.Bot(command_prefix=".", case_insensitive=True, intents=intents)

bot.remove_command("help")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('.help'))
    print(f"Servers: {len(bot.guilds)}")
    print('Connected to bot: {}'.format(bot.user.name))
    print('STATUS: Running')


@bot.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            join = discord.Embed(
                title="", description="Hello! Thanks for adding Aurora to your server 🤝️", color=0x2ea8ff)
            join.add_field(
                name="_ _", value="◇─────────────────────────────────◇")
            join.set_author(name="Aurora",
                            icon_url="https://media.discordapp.net/attachments/807511480878497806/832503256118591498/Aurora.png")
            join.add_field(name="_ _",
                           value="→ Do ``.help`` to check out all my commands and features\n_ _\n**Developer's Recommendation:**\n→ Run ``.rpg`` go on a quest, gamble and duel with friends\n→ Run ``.games`` mini games which are super fun to play\n→ Run ``.guess`` to test your knowledge on Anime/Geo/Star Wars\n_ _\n◇─────────────────────────────────◇",
                           inline=False)
            join.add_field(
                name="_ _", value="[Join Aurora Support Server](https://discord.gg/G9vTrsV4aG)", inline=False)
            join.set_footer(text="Enjoy using the bot 👍 | Molecule")
            join.set_thumbnail(
                url="https://media.discordapp.net/attachments/807511480878497806/832503256118591498/Aurora.png")

            await channel.send(embed=join)
            break


@bot.group(invoke_without_command=True)
async def help(ctx):
    help = discord.Embed(title='Welcome to the Official Aurora BOT',
                         url="https://www.youtube.com/channel/UCdNMAz_kPKrpp6ujliRLtLQ", description=" ", color=0x66c9ff)
    help.add_field(name="Here is the list of things you can do:",
                   value=chr(173), inline=False)
    help.add_field(name="⚔️ ``.rpg``", value="Adventure\nGame", inline=True)
    help.add_field(name="🖼 ``.guess``", value=" Guessing\nGame", inline=True)
    help.add_field(name="🎮️ ``.games``", value="Mini\nGames", inline=True)
    help.add_field(name=chr(173), value="_ _", inline=False)
    help.add_field(name="🍦️ ``.fun``",
                   value="Fun & Casual\nCommands", inline=True)
    help.add_field(name="🎗 ``.memories``",
                   value="Summary\nof every year", inline=True)
    help.add_field(name="😂️ ``.meme``", value="Memes\nOnly", inline=True)
    help.add_field(name=chr(173), value="_ _", inline=False)
    help.add_field(name="📄️ ``.cred``", value="Credits\n& Info", inline=True)
    help.add_field(name="⚙️ ``.util``", value="Useful\nCommands", inline=True)
    help.add_field(name="👍️ ``.wait``", value="Coming\nSoon", inline=True)
    help.add_field(name=chr(
        173), value="[Join our support server](https://discord.gg/G9vTrsV4aG)", inline=False)
    help.set_thumbnail(
        url="https://media.discordapp.net/attachments/807511480878497806/832260603380498452/aurora_help.png")

    help.set_footer(text="Use the commands for more info 👍️ ")
    await ctx.send(embed=help)


@bot.group(name="rpg", invoke_without_command=True)
async def rpg(ctx):
    rpg = discord.Embed(title="RPG GAME (UNDER DEV)",
                        description="The following are the commands which you can use\n **run ``.rpg info`` to learn more about the game**\n_ _", color=0x99ffd3)
    rpg.set_thumbnail(
        url="https://media.discordapp.net/attachments/807511480878497806/834121432849973288/rpg.png")
    rpg.add_field(name="_ _", value="_ _", inline=False)
    rpg.add_field(name="📈️ __MARKETPLACE__ (UNDER DEV)",
                  value="``.market info`` ``.market`` ``.stocks``", inline=False)
    rpg.add_field(name="🎖️ __LEVELING__",
                  value="``.quest`` ``.train`` ``.fight``", inline=True)
    rpg.add_field(name="_ _", value="_ _", inline=True)
    rpg.add_field(name="🗡️ __MULTIPLAYER__", value="``.duel``", inline=True)
    rpg.add_field(name="📂️ __PROGRESS__",
                  value="``.profile`` ``.inv``", inline=True)
    rpg.add_field(name="_ _", value="_ _", inline=True)
    rpg.add_field(name="🛒️ __SHOPPING__",
                  value="``.shop`` ``.buy`` ``.use``", inline=True)
    rpg.add_field(name="💸️ __GAMBLING__",
                  value="``.highlow`` ``.slots``", inline=True)
    rpg.add_field(name="_ _", value="_ _", inline=True)
    rpg.add_field(name="📮️ __SETTINGS__",
                  value="``.deletemydata``", inline=True)
    rpg.set_footer(text="First step to start playing, run .quest")
    await ctx.send(embed=rpg)


@rpg.command(name="info")
async def rpg_info(ctx):
    info = discord.Embed(title="RPG GAME INFO (UNDER DEV)",
                         description="The main objective is to gain xp and levels to unlock various items and to move forward in the game\n**first ting you must do is go on your first adventure! run ``.quest``**", color=0x787878)
    info.add_field(name="__GAME FEATURES__",
                   value="→ Earn COINS and XP with ``.quest`` ``.train``. Fight monsters with ``.fight``\n→ Check your data and progess with ``.profile``", inline=False)
    info.add_field(name="__MARKETPLACE__ (UNDER DEV)",
                   value="→ Trade stocks of different hypothetical companies to earn money.\nrun ``.market info`` to learn more", inline=False)
    info.add_field(name="__SHOP INFO__",
                   value="→ To buy items like weapons or potions use ``.shop``\n→The items can only be bought by COINS", inline=False)
    info.add_field(name="__GAMBLING__",
                   value="→ To earn more money (coins) use ``.highlow`` ``.slots``\n→ You can only earn COINS not XP")
    info.add_field(name="__OTHER FEATURES__",
                   value="→ Multiplayer\n To play with your friends: ``.duel``", inline=False)
    info.set_footer(text="Enjoy your time 👍")
    await ctx.send(embed=info)


@bot.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def quest(ctx):
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
    cursor.execute(
        "SELECT user_xp, user_level, user_coins FROM users WHERE client_id = %s", [ctx.author.id])
    result = cursor.fetchall()

    if len(result) == 0:
        cursor.execute("INSERT INTO users VALUES(%s, %s, 0, %s, 0, 0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0)", [
                       ctx.author.id, XP, COINS])
        db.commit()

    else:

        newXP = result[0][0] + XP
        currentLevel = result[0][1]
        newCoins = result[0][2] + COINS

        if newXP > 0:
            currentLevel = newXP/1000

        cursor.execute("UPDATE users SET user_xp = %s, user_level = %s, user_coins = %s WHERE client_id = %s", [
                       newXP, currentLevel, newCoins, ctx.author.id])
        db.commit()


@bot.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def fight(ctx):
    cursor.execute(
        "SELECT user_xp, user_level, user_coins, health, attack FROM users WHERE client_id = %s", [ctx.author.id])
    result = cursor.fetchall()

    checkhealth = result[0][3]
    checkattack = result[0][4]

    if len(result) == 0:
        cursor.execute(
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
            cursor.execute(
                "select user_level from users where client_id = %s", [ctx.author.id])
            fightres = cursor.fetchall()
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

                        fChoice = await bot.wait_for('message', check=check, timeout=30)

                        if fChoice.author == ctx.message.author:
                            if fChoice.content.lower() == "weapon qg":
                                cursor.execute(
                                    "select health, quagun from users where client_id = %s", [ctx.author.id])
                                fightres2 = cursor.fetchall()

                                fightq = fightres2[0][1]

                                if fightq == 0:
                                    fighth = fightres2[0][0]
                                    finalFighth = fighth/2
                                    cursor.execute("update users set health = %s where client_id = %s", [
                                                   finalFighth, ctx.author.id])
                                    await fChoice.reply("You don't have that item, you ended up losing ``50%`` of your health", mention_author=False)
                                    db.commit()
                                else:
                                    finalFightq = fightq - 1
                                    mh = mh - 20
                                    cursor.execute("update users set quagun = %s where client_id = %s", [
                                                   finalFightq, ctx.author.id])
                                    await fChoice.reply("You damaged the monster, it ended up with ``30`` Health", mention_author=False)
                                    db.commit()

                            elif fChoice.content.lower() == "weapon eb":
                                cursor.execute(
                                    "select health, enebazo from users where client_id = %s", [ctx.author.id])
                                fightres3 = cursor.fetchall()

                                fighte = fightres3[0][1]

                                if fighte == 0:
                                    fighth2 = fightres3[0][0]
                                    finalFighth2 = fighth2/2
                                    cursor.execute("update users set health = %s where client_id = %s", [
                                                   finalFighth2, ctx.author.id])
                                    await fChoice.reply("You don't have that item, you ended up losing ``50%`` of your health", mention_author=False)
                                    db.commit()
                                else:
                                    finalFighte = fighte - 1
                                    mh = mh - 75
                                    cursor.execute("update users set enebazo = %s where client_id = %s", [
                                                   finalFighte, ctx.author.id])
                                    db.commit()

                                    if mh > 0:
                                        await fChoice.reply(f"You damaged the monster, it ended up with ``{mh}`` Health", mention_author=False)

                            elif fChoice.content.lower() == "punch":
                                cursor.execute(
                                    "select attack from users where client_id = %s", [ctx.author.id])
                                fightres4 = cursor.fetchall()
                                fighta = fightres4[0][0]

                                if fighta == 0:
                                    await fChoice.reply("lmao your attack level is ``0``, you dealt no damage", mention_author=False)
                                else:
                                    mh = mh - fighta
                                    if mh > 0:
                                        await fChoice.reply(f"You damaged the monster, it ended up with ``{mh}`` Health", mention_author=False)

                            elif fChoice.content.lower() == "end":

                                cursor.execute(
                                    "select user_xp, user_coins from users where client_id = %s", [ctx.author.id])
                                finalres = cursor.fetchall()
                                lxp = finalres[0][0] - 200
                                lc = finalres[0][1] - 2000

                                if lxp < 0:
                                    lxp = 0

                                if lc < 0:
                                    lc = 0

                                cursor.execute("update users set user_xp = %s, user_coins = %s where client_id = %s", [
                                               lxp, lc, ctx.author.id])
                                await ctx.send(f"{ctx.author.mention} You lost the fight! Losing {xp}200  {coin} 2000")
                                db.commit()
                                FightGameOver += 1

                            if mh <= 0:
                                rxp = random.randint(500, 1000)
                                rc = random.randint(5000, 8000)
                                cursor.execute(
                                    "select user_xp, user_coins from users where client_id = %s", [ctx.author.id])
                                fightOver = cursor.fetchall()

                                newUserXP = fightOver[0][0] + rxp
                                newUserC = fightOver[0][1] + rc

                                newUserLVL = newUserXP/1000

                                cursor.execute("update users set user_xp = %s, user_coins = %s, user_level = %s where client_id = %s", [
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
                cursor.execute(
                    "select health from users where client_id = %s", [ctx.author.id])
                lhealth = cursor.fetchall()

                fhealth = lhealth[0][0] - 100

                if fhealth <= 0:
                    await ctx.send(f"{ctx.author.mention} You lost the fight! Losing {xp}200  {coin} 2000")
                    cursor.execute(
                        "select user_xp, user_coins from users where client_id = %s", [ctx.author.id])
                    finalres = cursor.fetchall()
                    lxp = finalres[0][0] - 200
                    lc = finalres[0][1] - 2000

                    if lxp < 0:
                        lxp = 0

                    if lc < 0:
                        lc = 0

                    cursor.execute("update users set user_xp = %s, user_coins = %s, health= %s where client_id = %s", [
                                   lxp, lc, fhealth, ctx.author.id])
                    db.commit()
                    FightGameOver += 1
                else:

                    cursor.execute("update users set health = %s where client_id = %s", [
                                   fhealth, ctx.author.id])
                    while True:

                        await ctx.send(f"{ctx.author.name} please continue with a valid command")

                        def check(message):

                            return ctx.author == message.author and ctx.channel == message.channel

                        try:

                            fChoice = await bot.wait_for('message', check=check, timeout=30)

                            if fChoice.author == ctx.message.author:
                                if fChoice.content.lower() == "weapon qg":
                                    cursor.execute(
                                        "select health, quagun from users where client_id = %s", [ctx.author.id])
                                    fightres2 = cursor.fetchall()

                                    fightq = fightres2[0][1]

                                    if fightq == 0:
                                        fighth = fightres2[0][0]
                                        finalFighth = fighth/2
                                        cursor.execute("update users set health = %s where client_id = %s", [
                                                       finalFighth, ctx.author.id])
                                        await fChoice.reply("You don't have that item, you ended up losing ``50%`` of your health", mention_author=False)
                                        db.commit()
                                    else:
                                        finalFightq = fightq - 1
                                        mh = mh - 20
                                        cursor.execute("update users set quagun = %s where client_id = %s", [
                                                       finalFightq, ctx.author.id])
                                        await fChoice.reply("You damaged the monster, it ended up with ``30`` Health", mention_author=False)
                                        db.commit()

                                elif fChoice.content.lower() == "weapon eb":
                                    cursor.execute(
                                        "select health, enebazo from users where client_id = %s", [ctx.author.id])
                                    fightres3 = cursor.fetchall()

                                    fighte = fightres3[0][1]

                                    if fighte == 0:
                                        fighth2 = fightres3[0][0]
                                        finalFighth2 = fighth2/2
                                        cursor.execute("update users set health = %s where client_id = %s", [
                                                       finalFighth2, ctx.author.id])
                                        await fChoice.reply("You don't have that item, you ended up losing ``50%`` of your health", mention_author=False)
                                        db.commit()
                                    else:
                                        finalFighte = fighte - 1
                                        mh = mh - 75
                                        cursor.execute("update users set enebazo = %s where client_id = %s", [
                                                       finalFighte, ctx.author.id])
                                        db.commit()

                                        if mh > 0:
                                            await fChoice.reply(f"You damaged the monster, it ended up with ``{mh}`` Health", mention_author=False)

                                elif fChoice.content.lower() == "punch":
                                    cursor.execute(
                                        "select attack from users where client_id = %s", [ctx.author.id])
                                    fightres4 = cursor.fetchall()
                                    fighta = fightres4[0][0]

                                    if fighta == 0:
                                        await fChoice.reply("lmao your attack level is ``0``, you dealt no damage", mention_author=False)
                                    else:
                                        mh = mh - fighta
                                        if mh > 0:
                                            await fChoice.reply(f"You damaged the monster, it ended up with ``{mh}`` Health", mention_author=False)

                                elif fChoice.content.lower() == "end":
                                    cursor.execute(
                                        "select user_xp, user_coins from users where client_id = %s", [ctx.author.id])
                                    finalres = cursor.fetchall()
                                    lxp = finalres[0][0] - 200
                                    lc = finalres[0][1] - 2000

                                    if lxp < 0:
                                        lxp = 0

                                    if lc < 0:
                                        lc = 0

                                    cursor.execute("update users set user_xp = %s, user_coins = %s where client_id = %s", [
                                                   lxp, lc, ctx.author.id])
                                    await ctx.send(f"{ctx.author.mention} You lost the fight! Losing {xp}200  {coin} 2000")
                                    FightGameOver += 1
                                    db.commit()

                                if mh <= 0:
                                    rxp = random.randint(500, 1000)
                                    rc = random.randint(5000, 8000)
                                    cursor.execute(
                                        "select user_xp, user_coins from users where client_id = %s", [ctx.author.id])
                                    fightOver = cursor.fetchall()

                                    newUserXP = fightOver[0][0] + rxp
                                    newUserC = fightOver[0][1] + rc

                                    newUserLVL = newUserXP/1000

                                    cursor.execute("update users set user_xp = %s, user_coins = %s, user_level = %s where client_id = %s", [
                                                   newUserXP, newUserC, newUserLVL, ctx.author.id])

                                    await ctx.send(f" {ctx.author.mention} Good Job! You have defeated {oni} Oni\nYou Gained: {xp}{rxp}   {coin} {rc}")
                                    db.commit()
                                    break

                                elif FightGameOver == 1:
                                    break
                        except asyncio.TimeoutError:
                            await ctx.send(f"next time respond in under ``30s`` after the command is issued :skull:")
                            break


@bot.group(name="shop", invoke_without_command=True)
async def shop(ctx):
    shop = discord.Embed(
        title="Shop Items", description=f"**__LIMITED TIME OFFER__**\nget a {mbe} mystery box upon boosting [Aurora's community server](https://discord.gg/G9vTrsV4aG)\nIt can fetch you 8 - 15k coins and other in-game items\n\n", color=0x99ffd3)
    shop.add_field(name=f"{dpe} **Durability Potion** {dash} ``500``",
                   value=f"*ID* → ``dp`` drink a like a fish to increase your defense by 5", inline=False)
    shop.add_field(name="_ _", value="_ _", inline=False)
    shop.add_field(name=f"{hpe} **Health Potion** {dash} ``200``",
                   value="*ID* → ``hp`` keep chugging for good health, increase your health by 10", inline=False)
    shop.add_field(name="_ _", value="_ _", inline=False)
    shop.add_field(name=f"{vpe} **Vigour Potion** {dash} ``500``",
                   value="*ID* → ``vp`` this booze makes you stronger, increase your attack level by 5", inline=False)
    shop.add_field(name="_ _", value="_ _", inline=False)
    shop.add_field(name=f"{qge} **Quantum Gun** {dash} ``2000``",
                   value="*ID* → ``qg`` incinerate your opponents, does 20 damage", inline=False)
    shop.add_field(name="_ _", value="_ _", inline=False)
    shop.add_field(name=f"{ebe} **Energy Bazooka** {dash} ``5000``",
                   value="*ID* → ``eb`` If you're against this weapon, you should be scared. does 75 damage", inline=False)
    shop.add_field(
        name="_ _", value="run ``.shop info <id>`` for more information on the items", inline=False)
    shop.set_footer(text="page 1/2")
    await ctx.send(embed=shop)


@shop.command(name="2")
async def shop_2(ctx):
    shop2 = discord.Embed(title="", color=0x99ffd3)
    shop2.add_field(name=f"{woe} **Witch's Orb** {dash} ``10,000``",
                    value="*ID* → ``orb`` there is a 50% you'll lose all your coins or double them, use wisely", inline=False)
    shop2.add_field(name="_ _", value="_ _", inline=False)
    shop2.add_field(name=f"{ame} **Molecule** {dash} ``1,000,000``",
                    value=f"*ID* → ``molecule`` an item only for the rich", inline=False)
    shop2.add_field(
        name="_ _", value="run ``.shop info <id>`` for more information on the items", inline=False)
    shop2.set_footer(text="page 2/2")
    await ctx.send(embed=shop2)


@shop.command(name="info")
async def shop_info(ctx, message):
    if message.lower() == "dp":
        se = discord.Embed(title="Durability Potion",
                           description="drink a like a fish to increase your defense by 5, useful in duels to tank oppenents punches", color=0x8545b0)
        se.add_field(
            name="Buying Price: ``500``\nSelling Price: ``200``", value="_ _", inline=False)
        se.set_thumbnail(
            url="https://media.discordapp.net/attachments/807511480878497806/848819806497013780/dpot.png")
        await ctx.send(embed=se)
    elif message.lower() == "hp":
        se = discord.Embed(
            title="Health Potion", description="keep chugging for good health, increase your health by 10, useful in duels to stay alive ", color=0xb32937)
        se.add_field(
            name="Buying Price: ``200``\nSelling Price: ``75``", value="_ _", inline=False)
        se.set_thumbnail(
            url="https://media.discordapp.net/attachments/807511480878497806/848819986428198922/hpot.png")
        await ctx.send(embed=se)
    elif message.lower() == "vp":
        se = discord.Embed(
            title="Vigour Potion", description="this booze makes you stronger, increase your attack level by 5, useful in duels to deal more damage", color=0xffea00)
        se.add_field(
            name="Buying Price: ``500``\nSelling Price: ``250``", value="_ _", inline=False)
        se.set_thumbnail(
            url="https://media.discordapp.net/attachments/807511480878497806/848820149637087232/vpot.png")
        await ctx.send(embed=se)
    elif message.lower() == "qg":
        se = discord.Embed(
            title="Quantum Gun", description=" incinerate your opponents, does 20 damage. Use this in duels to defeat your opponents", color=0x00ff11)
        se.add_field(
            name="Buying Price: ``2000``\nSelling Price: ``1000``", value="_ _", inline=False)
        se.set_thumbnail(
            url="https://media.discordapp.net/attachments/807511480878497806/848820293237604402/qgun.png")
        await ctx.send(embed=se)
    elif message.lower() == "eb":
        se = discord.Embed(
            title="Energy Bazooka", description="If you're against this weapon, you should be scared. does 75 damage. Use this in duels to defeat your opponents", color=0x00bbff)
        se.add_field(
            name="Buying Price: ``5000``\nSelling Price: ``3000``", value="_ _", inline=False)
        se.set_thumbnail(
            url="https://media.discordapp.net/attachments/807511480878497806/848820441832751104/eb.png")
        await ctx.send(embed=se)
    elif message.lower() == "orb":
        se = discord.Embed(
            title="Witch's Orb", description="there is a 50% you'll lose all your coins or double them, use wisely. If you have over 100k then only 100k will get doubled not your entire wallet", color=0xbb54ff)
        se.add_field(
            name="Buying Price: ``10,000``\nSelling Price: ``4000``", value="_ _", inline=False)
        se.set_thumbnail(
            url="https://media.discordapp.net/attachments/807511480878497806/848818984128479262/844221988419534869.png")
        await ctx.send(embed=se)
    elif message.lower() == "molecule":
        se = discord.Embed(
            title="Molecule", description="This item has no purpose, It can only be collected. Flex on people who can't aford it", color=0x54e5ff)
        se.add_field(
            name="Buying Price: ``1,000,000``\nSelling Price: ``Cannot be sold``", value="_ _", inline=False)
        se.set_thumbnail(
            url="https://media.discordapp.net/attachments/807511480878497806/848820623127216128/molecule.png")
        await ctx.send(embed=se)
    else:
        error_msg = discord.Embed(title=" ", description=" ", color=0xffb12b)
        error_msg.add_field(
            name="Error", value="please enter a valid item's ID to get more information on it\nFormat: ``.shop info <id>``\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
        await ctx.reply(embed=error_msg, mention_author=False)


@bot.group(name="sell", invoke_without_command=True)
async def sell(ctx):
    await ctx.send("UNDER DEV")


@bot.group(name="buy", invoke_without_command=True)
async def buy(ctx):
    error_msg = discord.Embed(title=" ", description=" ", color=0xffb12b)
    error_msg.add_field(
        name="Error", value="please enter a valid amount and a valid ID to buy an item\nFormat: ``.buy <item id> <amount>``\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
    await ctx.reply(embed=error_msg, mention_author=False)


@buy.command(name="dp")
@commands.cooldown(1, 20, commands.BucketType.user)
async def buy_dp(ctx, *, message):
    try:
        message = int(message)
        cursor.execute(
            "select durapot from users where client_id = %s", [ctx.author.id])
        result = cursor.fetchall()
        cursor.execute(
            "select user_coins from users where client_id = %s", [ctx.author.id])
        result2 = cursor.fetchall()

        if len(result2) == 0:
            await ctx.send(f"{ctx.author.name} hasn't started playing, to learn more about the game please run ``.rpg info`` or just start by ``.quest``")

        if message < 1:
            await ctx.send("You cant buy like that 😂️")

        else:
            buy = result[0][0] + message
            money = result2[0][0] - message*500

            if money < 0:
                await ctx.reply(f"Check your balance first, you don't have enough money to buy {message} of this item", mention_author=False)
                return
            else:
                cursor.execute("UPDATE users set user_coins = %s, durapot = %s where client_id = %s", [
                               money, buy, ctx.author.id])
                await ctx.reply(f"{dpe} You've bought ``{message}`` Durability potion(s). Total in inventory = ``{buy}``")
                db.commit()

    except ValueError:
        error_msg = discord.Embed(title=" ", description=" ", color=0xffb12b)
        error_msg.add_field(
            name="Error", value="please enter a valid amount of the item you're trying to buy \nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
        await ctx.reply(embed=error_msg, mention_author=False)


@buy.command(name="hp")
@commands.cooldown(1, 20, commands.BucketType.user)
async def buy_hp(ctx, *, message):
    try:
        message = int(message)
        cursor.execute(
            "select healpot from users where client_id = %s", [ctx.author.id])
        result = cursor.fetchall()
        cursor.execute(
            "select user_coins from users where client_id = %s", [ctx.author.id])
        result2 = cursor.fetchall()

        if len(result2) == 0:
            await ctx.send(f"{ctx.author.name} hasn't started playing, to learn more about the game please run ``.rpg info`` or just start by ``.quest``")

        if message < 1:
            await ctx.send("You cant buy like that 😂️")
        else:

            buy = result[0][0] + message
            money = result2[0][0] - message*200

            if money < 0:
                await ctx.reply(f"Check your balance first, you don't have enough money to buy {message} of this item", mention_author=False)
                return
            else:
                cursor.execute("UPDATE users set user_coins = %s, healpot = %s where client_id = %s", [
                               money, buy, ctx.author.id])
                await ctx.reply(f"{hpe} You've bought ``{message}`` Health potion(s). Total in inventory = ``{buy}``")
            db.commit()

    except ValueError:
        error_msg = discord.Embed(title=" ", description=" ", color=0xffb12b)
        error_msg.add_field(
            name="Error", value="please enter a valid amount of the item you're trying to buy \nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
        await ctx.reply(embed=error_msg, mention_author=False)


@buy.command(name="vp")
@commands.cooldown(1, 20, commands.BucketType.user)
async def buy_vp(ctx, *, message):
    try:
        message = int(message)
        cursor.execute(
            "select vigopot from users where client_id = %s", [ctx.author.id])
        result = cursor.fetchall()
        cursor.execute(
            "select user_coins from users where client_id = %s", [ctx.author.id])
        result2 = cursor.fetchall()

        if len(result2) == 0:
            await ctx.send(f"{ctx.author.name} hasn't started playing, to learn more about the game please run ``.rpg info`` or just start by ``.quest``")

        if message < 1:
            await ctx.send("You cant buy like that 😂️")
        else:

            buy = result[0][0] + message
            money = result2[0][0] - message*500

            if money < 0:
                await ctx.reply(f"Check your balance first, you don't have enough money to buy {message} of this item", mention_author=False)
                return
            else:
                cursor.execute("UPDATE users set user_coins = %s, vigopot = %s where client_id = %s", [
                               money, buy, ctx.author.id])
                await ctx.reply(f"{vpe} You've bought ``{message}`` Vigour potion(s). Total in inventory = ``{buy}``")
                db.commit()

    except ValueError:
        error_msg = discord.Embed(title=" ", description=" ", color=0xffb12b)
        error_msg.add_field(
            name="Error", value="please enter a valid amount of the item you're trying to buy \nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
        await ctx.reply(embed=error_msg, mention_author=False)


@buy.command(name="qg")
@commands.cooldown(1, 20, commands.BucketType.user)
async def buy_qg(ctx, *, message):
    try:
        message = int(message)
        cursor.execute(
            "select quagun from users where client_id = %s", [ctx.author.id])
        result = cursor.fetchall()
        cursor.execute(
            "select user_coins from users where client_id = %s", [ctx.author.id])
        result2 = cursor.fetchall()

        if len(result2) == 0:
            await ctx.send(f"{ctx.author.name} hasn't started playing, to learn more about the game please run ``.rpg info`` or just start by ``.quest``")

        if message < 1:
            await ctx.send("You cant buy like that 😂️")
        else:

            buy = result[0][0] + message
            money = result2[0][0] - message*2000

            if money < 0:
                await ctx.reply(f"Check your balance first, you don't have enough money to buy {message} of this item", mention_author=False)
                return
            else:
                cursor.execute("UPDATE users set user_coins = %s, quagun = %s where client_id = %s", [
                               money, buy, ctx.author.id])
                await ctx.reply(f"{qge} You've bought ``{message}`` Quantum Gun(s). Total in inventory = ``{buy}``")
                db.commit()

    except ValueError:
        error_msg = discord.Embed(title=" ", description=" ", color=0xffb12b)
        error_msg.add_field(
            name="Error", value="please enter a valid amount of the item you're trying to buy \nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
        await ctx.reply(embed=error_msg, mention_author=False)


@buy.command(name="eb")
@commands.cooldown(1, 20, commands.BucketType.user)
async def buy_eb(ctx, *, message):
    try:
        message = int(message)
        cursor.execute(
            "select enebazo from users where client_id = %s", [ctx.author.id])
        result = cursor.fetchall()
        cursor.execute(
            "select user_coins from users where client_id = %s", [ctx.author.id])
        result2 = cursor.fetchall()

        if len(result2) == 0:
            await ctx.send(f"{ctx.author.name} hasn't started playing, to learn more about the game please run ``.rpg info`` or just start by ``.quest``")

        if message < 1:
            await ctx.send("You cant buy like that 😂️")
        else:

            buy = result[0][0] + message
            money = result2[0][0] - message*5000

            if money < 0:
                await ctx.reply(f"Check your balance first, you don't have enough money to buy {message} of this item", mention_author=False)
                return
            else:
                cursor.execute("UPDATE users set user_coins = %s, enebazo = %s where client_id = %s", [
                               money, buy, ctx.author.id])
                await ctx.reply(f"{ebe} You've bought ``{message}`` Energy Bazooka(s). Total in inventory = ``{buy}``")
                db.commit()

    except ValueError:
        error_msg = discord.Embed(title=" ", description=" ", color=0xffb12b)
        error_msg.add_field(
            name="Error", value="please enter a valid amount of the item you're trying to buy \nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
        await ctx.reply(embed=error_msg, mention_author=False)


@buy.command(name="orb")
@commands.cooldown(1, 20, commands.BucketType.user)
async def buy_orb(ctx, *, message):
    try:
        message = int(message)
        cursor.execute(
            "select orb from users where client_id = %s", [ctx.author.id])
        result = cursor.fetchall()
        cursor.execute(
            "select user_coins from users where client_id = %s", [ctx.author.id])
        result2 = cursor.fetchall()

        if len(result2) == 0:
            await ctx.send(f"{ctx.author.name} hasn't started playing, to learn more about the game please run ``.rpg info`` or just start by ``.quest``")

        if message < 1:
            await ctx.send("You cant buy like that 😂️")
        else:

            buy = result[0][0] + message
            money = result2[0][0] - message*10000

            if money < 0:
                await ctx.reply(f"Check your balance first, you don't have enough money to buy {message} of this item", mention_author=False)
                return
            else:
                cursor.execute("UPDATE users set user_coins = %s, orb = %s where client_id = %s", [
                               money, buy, ctx.author.id])
                await ctx.reply(f"{woe} You've bought ``{message}`` Witch's Orb(s). Total in inventory = ``{buy}``")
                db.commit()

    except ValueError:
        error_msg = discord.Embed(title=" ", description=" ", color=0xffb12b)
        error_msg.add_field(
            name="Error", value="please enter a valid amount of the item you're trying to buy \nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
        await ctx.reply(embed=error_msg, mention_author=False)


@buy.command(name="molecule")
@commands.cooldown(1, 20, commands.BucketType.user)
async def buy_molecule(ctx, *, message):
    try:
        message = int(message)
        cursor.execute(
            "select molecule from users where client_id = %s", [ctx.author.id])
        result = cursor.fetchall()
        cursor.execute(
            "select user_coins from users where client_id = %s", [ctx.author.id])
        result2 = cursor.fetchall()

        if len(result2) == 0:
            await ctx.send(f"{ctx.author.name} hasn't started playing, to learn more about the game please run ``.rpg info`` or just start by ``.quest``")

        if message < 1:
            await ctx.send("You cant buy like that 😂️")
        else:
            buy = result[0][0] + message
            money = result2[0][0] - message*1000000

            if money < 0:
                await ctx.reply(f"Check your balance first, you don't have enough money to buy {message} of this item", mention_author=False)
                return
            else:
                cursor.execute("UPDATE users set user_coins = %s, molecule = %s where client_id = %s", [
                               money, buy, ctx.author.id])
                await ctx.reply(f"{ame} You've bought ``{message}`` Molecule(s). Total in inventory = ``{buy}``")
                db.commit()

    except ValueError:
        error_msg = discord.Embed(title=" ", description=" ", color=0xffb12b)
        error_msg.add_field(
            name="Error", value="please enter a valid amount of the item you're trying to buy \nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
        await ctx.reply(embed=error_msg, mention_author=False)


@bot.group(name="use", invoke_without_command=True)
async def use(ctx):
    error_msg = discord.Embed(title=" ", description=" ", color=0xffb12b)
    error_msg.add_field(
        name="Error", value="please enter a valid ID to use an item\nFormat: ``.use <item id> <quantity>``\n``quantity`` doesnt apply for these items: ``orb``, ``box``\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
    await ctx.reply(embed=error_msg, mention_author=False)


@use.command(name="dp")
@commands.cooldown(1, 20, commands.BucketType.user)
async def use_dp(ctx, *, message):
    try:
        message = int(message)

        if message < 0:
            await ctx.reply("dont try to break me, you can use anything like that 😂️", mention_author=False)
        else:
            cursor.execute(
                "select defense from users where client_id = %s", [ctx.author.id])
            result = cursor.fetchall()
            cursor.execute(
                "select durapot from users where client_id = %s", [ctx.author.id])
            result2 = cursor.fetchall()
            DEF = result[0][0] + (5 * message)
            dpi = result2[0][0] - message
            final = (5 * message)

            if dpi < 0:
                await ctx.send(f"{ctx.author.name} you dont have that many durability potions 😂️ dont't try to scam me")
            else:
                cursor.execute("update users set durapot = %s, defense = %s where client_id = %s", [
                               dpi, DEF, ctx.author.id])
                await ctx.reply(f"You chugged down {message} {dpe} ``Durability Potion (s)`` to gain ``+{final}`` DEF", mention_author=False)
                db.commit()
    except ValueError:
        error_msg = discord.Embed(title=" ", description=" ", color=0xffb12b)
        error_msg.add_field(
            name="Error", value="please enter a valid amount of the item you're trying to use \nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
        await ctx.reply(embed=error_msg, mention_author=False)


@use.command(name="hp")
@commands.cooldown(1, 20, commands.BucketType.user)
async def use_hp(ctx, *, message):

    try:
        message = int(message)

        if message < 0:
            await ctx.reply("dont try to break me, you can use anything like that 😂️", mention_author=False)
        else:
            cursor.execute(
                "select health from users where client_id = %s", [ctx.author.id])
            result = cursor.fetchall()
            cursor.execute(
                "select healpot from users where client_id = %s", [ctx.author.id])
            result2 = cursor.fetchall()
            HEALTH = result[0][0] + (10 * message)
            hpi = result2[0][0] - message
            final = (10 * message)

            if hpi < 0:
                await ctx.send(f"{ctx.author.name} you dont have that many health potions 😂️ dont't try to scam me")
            else:
                cursor.execute("update users set healpot = %s, health = %s where client_id = %s", [
                               hpi, HEALTH, ctx.author.id])
                await ctx.reply(f"You chugged down {message} {hpe} ``Health Potion (s)`` to gain ``+{final}`` HEALTH", mention_author=False)
                db.commit()

    except ValueError:
        error_msg = discord.Embed(title=" ", description=" ", color=0xffb12b)
        error_msg.add_field(
            name="Error", value="please enter a valid amount of the item you're trying to buy \nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
        await ctx.reply(embed=error_msg, mention_author=False)


@use.command(name="vp")
@commands.cooldown(1, 20, commands.BucketType.user)
async def use_vp(ctx, *, message):
    try:
        message = int(message)
        if message < 0:
            await ctx.reply("dont try to break me, you can use anything like that 😂️", mention_author=False)
        else:
            cursor.execute(
                "select attack from users where client_id = %s", [ctx.author.id])
            result = cursor.fetchall()
            cursor.execute(
                "select vigopot from users where client_id = %s", [ctx.author.id])
            result2 = cursor.fetchall()
            vpi = result2[0][0] - message
            ATTCK = result[0][0] + (5 * message)
            final = (5 * message)

            if vpi < 0:
                await ctx.send(f"{ctx.author.name} you dont that many vigour potions 😂️ dont't try to scam me")
            else:
                cursor.execute("update users set vigopot = %s, attack = %s where client_id = %s", [
                               vpi, ATTCK, ctx.author.id])
                await ctx.reply(f"You chugged down {message} {vpe} ``Vigour Potion (s)`` to gain ``+{final}`` ATTCK", mention_author=False)
                db.commit()
    except ValueError:
        error_msg = discord.Embed(title=" ", description=" ", color=0xffb12b)
        error_msg.add_field(
            name="Error", value="please enter a valid amount of the item you're trying to buy \nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
        await ctx.reply(embed=error_msg, mention_author=False)


@use.command(name="orb")
@commands.cooldown(1, 10800, commands.BucketType.user)
async def use_orb(ctx):
    cursor.execute(
        "select user_coins from users where client_id = %s", [ctx.author.id])
    result = cursor.fetchall()
    cursor.execute("select orb from users where client_id = %s",
                   [ctx.author.id])
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
                cursor.execute("update users set user_coins = %s where client_id = %s", [
                               wmfinal, ctx.author.id])
                await ctx.reply(f"☑️ {woe} was in your favour! you doubled 100k from your balance", mention_author=False)
                db.commit()

            else:
                wmf = walletmoney * 2
                cursor.execute("update users set user_coins = %s where client_id = %s", [
                               wmf, ctx.author.id])
                await ctx.reply(f"☑️ {woe} was in your favour! you doubled your wallet (max amount that can be doubled is 100k)", mention_author=False)
                db.commit()

        elif chance == 2:
            cursor.execute(
                "update users set user_coins = 0 where client_id = %s", [ctx.author.id])
            await ctx.reply(f"❌️ {woe} was not in your favour! you lost all your money - {walletmoney}", mention_author=False)
            db.commit()


@use.command(name="box")
@commands.cooldown(1, 120, commands.BucketType.user)
async def use_box(ctx):
    cursor.execute("select box from users where client_id = %s",
                   [ctx.author.id])
    res = cursor.fetchall()

    if len(res) == 0:
        await ctx.reply(f"{ctx.author.name} you dont any mystery boxes 😂️ dont't try to scam me", mention_author=False)

    else:

        rng = random.randint(1, 3)

        if rng == 1:
            cursor.execute(
                "select user_coins, healpot, orb, box from users where client_id = %s", [ctx.author.id])
            res1 = cursor.fetchall()

            c = res1[0][0] + 10000
            h = res1[0][1] + 5
            o = res1[0][2] + 1
            b = res1[0][3] - 1

            cursor.execute("update users set user_coins = %s, healpot = %s, orb = %s, box = %s where client_id = %s", [
                           c, h, o, b, ctx.author.id])

            r1 = await ctx.reply(f"{mbe} The Box contained the follwing:")
            await asyncio.sleep(0.5)
            await r1.edit(content=f"{mbe} The Box contained the follwing:\n\n{coin} 10,000 coins\n")
            await asyncio.sleep(0.5)
            await r1.edit(content=f"{mbe} The Box contained the follwing:\n\n{coin} 10,000 coins\n{hpe} 5 Health Potions\n")
            await asyncio.sleep(0.5)
            await r1.edit(content=f"{mbe} The Box contained the follwing:\n\n{coin} 10,000 coins\n{hpe} 5 Health Potions\n{woe} 1 orb")
            db.commit()

        elif rng == 2:

            cursor.execute(
                "select user_coins, quagun, orb, box from users where client_id = %s", [ctx.author.id])
            res2 = cursor.fetchall()

            c2 = res2[0][0] + 8000
            q = res2[0][1] + 1
            o2 = res2[0][2] + 2
            b2 = res2[0][3] - 1

            cursor.execute("update users set user_coins = %s, quagun = %s, orb = %s, box = %s where client_id = %s", [
                           c2, q, o2, b2, ctx.author.id])

            r2 = await ctx.reply(f"{mbe} The Box contained the follwing:")
            await asyncio.sleep(0.5)
            await r2.edit(content=f"{mbe} The Box contained the follwing:\n\n{coin} 8,000 coins\n")
            await asyncio.sleep(0.5)
            await r2.edit(content=f"{mbe} The Box contained the follwing:\n\n{coin} 8,000 coins\n{qge} 1 Quantum Gun\n")
            await asyncio.sleep(0.5)
            await r2.edit(content=f"{mbe} The Box contained the follwing:\n\n{coin} 8,000 coins\n{qge} 1 Quantum Gun\n{woe} 2 orbs")
            db.commit()

        elif rng == 3:

            cursor.execute(
                "select user_coins, durapot, box from users where client_id = %s", [ctx.author.id])
            res3 = cursor.fetchall()

            c3 = res3[0][0] + 15000
            d = res3[0][1] + 3
            b3 = res3[0][2] - 1

            cursor.execute("update users set user_coins = %s, durapot = %s, box = %s where client_id = %s", [
                           c3, d, b3, ctx.author.id])

            r3 = await ctx.reply(f"{mbe} The Box contained the follwing:")
            await asyncio.sleep(0.5)
            await r3.edit(content=f"{mbe} The Box contained the follwing:\n\n{coin} 15,000 coins\n")
            await asyncio.sleep(0.5)
            await r3.edit(content=f"{mbe} The Box contained the follwing:\n\n{coin} 15,000 coins\n{dpe} 3 Durability Potions")
            db.commit()


@use.command(name="qg")
async def use_qg(ctx):
    await ctx.send("This can only be used in a duel. To duel yor friends run ``.duel``")


@use.command(name="eb")
async def use_eb(ctx):
    await ctx.send("This can only be used in a duel. To duel yor friends run ``.duel``")


@use.command(name="molecule")
async def use_molecule(ctx):
    await ctx.send(f"{ame} ``molecule`` is a collectible and cannot be used")


@bot.command(aliases=['pf'])
async def profile(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    cursor.execute(
        "select user_level from users where client_id = %s", [user.id])
    result = cursor.fetchall()

    cursor.execute(
        "select user_coins from users where client_id = %s", [user.id])
    result2 = cursor.fetchall()

    cursor.execute("select defense from users where client_id = %s", [user.id])
    result3 = cursor.fetchall()

    cursor.execute("select health from users where client_id = %s", [user.id])
    result4 = cursor.fetchall()

    cursor.execute("select attack from users where client_id = %s", [user.id])
    result5 = cursor.fetchall()

    cursor.execute(
        "select dplayed, dwins from users where client_id = %s", [user.id])
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
            pfp.set_author(name=f"{user.name}'s Profile",
                           icon_url=user.avatar.url)
            pfp.add_field(name="MULTIPLAYER: _ _",
                          value=f"**Duels**\nPlayed: 0\nWon: 0\nWin%: 0.0", inline=True)
            pfp.add_field(
                name="RPG PROGRESS:", value=f"{xp} Levels: {lvl}\n{coin} Coins: {moni} ", inline=True)
            pfp.add_field(
                name="STATS:", value=f"{ate} Attack: {attcklvl}\n{dfe} Defense: {deflvl}\n{hae} Health: {heallvl}", inline=False)
            pfp.set_thumbnail(url=user.avatar.url)
            await ctx.send(embed=pfp)
        else:

            winn = round((duelstatswon/duelstatsplayed) * 100)

            pfp = discord.Embed(description="", color=random.choice(colors))
            pfp.set_author(name=f"{user.name}'s Profile",
                           icon_url=user.avatar.url)
            pfp.add_field(name="MULTIPLAYER: _ _",
                          value=f"**Duels**\nPlayed: {duelstatsplayed}\nWon: {duelstatswon}\nWin Rate: {winn}%", inline=True)
            pfp.add_field(
                name="RPG PROGRESS:", value=f"{xp} Levels: {lvl}\n{coin} Coins: {moni} ", inline=True)
            pfp.add_field(
                name="STATS:", value=f"{ate} Attack: {attcklvl}\n{dfe} Defense: {deflvl}\n{hae} Health: {heallvl}", inline=False)
            pfp.set_thumbnail(url=user.avatar.url)
            await ctx.send(embed=pfp)


@bot.group(name="inv", invoke_without_command=True)
async def inv(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    cursor.execute(
        "select durapot, healpot, vigopot, quagun, enebazo, molecule, orb, box from users where client_id = %s", [user.id])
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

        pf = discord.Embed(title="", description="",
                           color=random.choice(colors))
        pf.set_author(name=f"{user.name}'s inventory",
                      icon_url=user.avatar.url)
        pf.add_field(
            name="Items:", value=f"{dpe} Durability Potions ─ {dpi}\nID → ``dp``\n_ _", inline=True)
        pf.add_field(name="    _ _ ", value=f"    _ _", inline=True)
        pf.add_field(name="Collectibles",
                     value=f"{ame} Molecule ─ {moi}\nID → ``molecule``", inline=True)
        pf.add_field(
            name="_ _", value=f"{hpe} Health Potions ─ {hpi}\nID → ``hp``\n_ _", inline=True)
        pf.add_field(name="    _ _ ", value=f"    _ _", inline=True)
        pf.add_field(name="Market Items", value=f"UNDER DEV", inline=True)
        pf.add_field(
            name="_ _", value=f"{vpe} Vigour Potions ─ {vpi}\nID → ``vp``\n_ _", inline=False)
        pf.add_field(
            name="_ _", value=f"{woe} Witch's Orbs ─ {ori}\nID → ``orb``\n_ _", inline=False)
        pf.add_field(
            name="_ _", value=f"{qge} Quantum Guns ─ {qgi}\nID → ``qg``\n_ _", inline=False)
        pf.add_field(
            name="_ _", value=f"{ebe} Energy Bazookas ─ {ebi}\nID → ``eb``\n_ _", inline=False)
        pf.add_field(
            name="_ _", value=f"{mbe} Mystery Boxes ─ {boi}\nID → ``box``\n_ _", inline=False)

        await ctx.send(embed=pf)


@bot.command()
@commands.cooldown(1, 45, commands.BucketType.user)
async def train(ctx):
    q1 = ["https://cdn.discordapp.com/attachments/1057267168846299196/1057267285473103912/pink.png", "https://cdn.discordapp.com/attachments/1057267168846299196/1057267285850607636/yellow.png",
          "https://cdn.discordapp.com/attachments/1057267168846299196/1057267286290993153/blue.png", "https://cdn.discordapp.com/attachments/1057267168846299196/1057267286668496966/green.png"]
    a = random.choice(q1)
    XP = random.randint(150, 250)
    COIN = random.randint(75, 125)

    col = discord.Embed(title="", description="")
    col.add_field(name="_ _", value="**identify this color →**")
    col.set_thumbnail(url=a)
    await ctx.reply(embed=col, mention_author=False)

    cursor.execute(
        "SELECT user_xp, user_level, user_coins FROM users WHERE client_id = %s", [ctx.author.id])
    result = cursor.fetchall()

    if len(result) == 0:
        cursor.execute(
            "INSERT INTO users VALUES(%s, 0, 0, 0, 0, 0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0)", [ctx.author.id])
        db.commit()

    def check(message):

        return ctx.author == message.author and ctx.channel == message.channel

    anscol = await bot.wait_for('message', check=check)

    if anscol.author == ctx.message.author:

        if a == "https://media.discordapp.net/attachments/807511480878497806/835889048731385887/blue.png":
            if anscol.content.lower() == "blue":
                await ctx.reply(f"**Good Job!** you practiced hard and gained:\n{xp}: {XP}\n{coin}: {COIN}", mention_author=False)
                cursor.execute(
                    "select user_xp, user_level, user_coins from users where client_id = %s", [ctx.author.id])
                result = cursor.fetchall()

                newXP = result[0][0]+XP
                newCoins = result[0][2]+COIN

                if newXP > 0:
                    currentLevel = newXP/1000

                cursor.execute("update users set user_xp = %s, user_level = %s, user_coins = %s where client_id = %s", [
                               newXP, currentLevel, newCoins, ctx.author.id])

                db.commit()

            else:
                cursor.execute(
                    "select user_xp, user_coins from users where client_id = %s", [ctx.author.id])
                result = cursor.fetchall()

                newXP = result[0][0]-50
                newCoins = result[0][1]-100

                if newXP > 0:
                    currentLevel = newXP/1000

                if newCoins < 0:
                    await ctx.send("😂️👌️ **Lmao** You're so poor that you can even lose ``100`` coins | Updated Balance: ``0``")
                    cursor.execute("update users set user_xp = %s, user_level = %s, user_coins = 0 where client_id = %s", [
                                   newXP, currentLevel, ctx.author.id])

                    db.commit()

                else:
                    cursor.execute("update users set user_xp = %s, user_level = %s, user_coins = %s where client_id = %s", [
                                   newXP, currentLevel, newCoins, ctx.author.id])
                    await ctx.reply(f"**lol** you lost {xp} 50 XP and {coin} 100 coins", mention_author=False)

                    db.commit()

        elif a == "https://media.discordapp.net/attachments/807511480878497806/835889073901928449/green.png":
            if anscol.content.lower() == "green":
                await ctx.reply(f"**Good Job!** you trained and trained to gain:\n{xp}: {XP}\n{coin}: {COIN}", mention_author=False)
                cursor.execute(
                    "select user_xp, user_level, user_coins from users where client_id = %s", [ctx.author.id])
                result = cursor.fetchall()

                newXP = result[0][0]+XP
                newCoins = result[0][2]+COIN

                if newXP > 0:
                    currentLevel = newXP/1000

                cursor.execute("update users set user_xp = %s, user_level = %s, user_coins = %s where client_id = %s", [
                               newXP, currentLevel, newCoins, ctx.author.id])

                db.commit()

            else:
                cursor.execute(
                    "select user_xp, user_coins from users where client_id = %s", [ctx.author.id])
                result = cursor.fetchall()

                newXP = result[0][0]-50
                newCoins = result[0][1]-100

                if newXP > 0:
                    currentLevel = newXP/1000

                if newCoins < 0:
                    await ctx.send("😂️👌️ **Lmao** You're so poor that you can even lose ``100`` coins | Updated Balance: ``0``")
                    cursor.execute("update users set user_xp = %s, user_level = %s, user_coins = 0 where client_id = %s", [
                                   newXP, currentLevel, ctx.author.id])

                    db.commit()

                else:
                    cursor.execute("update users set user_xp = %s, user_level = %s, user_coins = %s where client_id = %s", [
                                   newXP, currentLevel, newCoins, ctx.author.id])
                    await ctx.reply(f"**lol** you lost {xp} 50 XP and {coin} 100 coins", mention_author=False)
                    db.commit()

        elif a == "https://media.discordapp.net/attachments/807511480878497806/835889002908614666/yellow.png":
            if anscol.content.lower() == "yellow":
                await ctx.reply(f"**Good Job!** after a long session you gained:\n{xp}: {XP}\n{coin}: {COIN}", mention_author=False)
                cursor.execute(
                    "select user_xp, user_level, user_coins from users where client_id = %s", [ctx.author.id])
                result = cursor.fetchall()

                newXP = result[0][0]+XP
                newCoins = result[0][2]+COIN

                if newXP > 0:
                    currentLevel = newXP/1000

                cursor.execute("update users set user_xp = %s, user_level = %s, user_coins = %s where client_id = %s", [
                               newXP, currentLevel, newCoins, ctx.author.id])

                db.commit()

            else:
                cursor.execute(
                    "select user_xp, user_coins from users where client_id = %s", [ctx.author.id])
                result = cursor.fetchall()

                newXP = result[0][0]-50
                newCoins = result[0][1]-100

                if newXP > 0:
                    currentLevel = newXP/1000

                if newCoins < 0:
                    await ctx.send("😂️👌️ **Lmao** You're so poor that you can even lose ``100`` coins | Updated Balance: ``0``")
                    cursor.execute("update users set user_xp = %s, user_level = %s, user_coins = 0 where client_id = %s", [
                                   newXP, currentLevel, ctx.author.id])

                    db.commit()

                else:
                    cursor.execute("update users set user_xp = %s, user_level = %s, user_coins = %s where client_id = %s", [
                                   newXP, currentLevel, newCoins, ctx.author.id])
                    await ctx.reply(f"**lol** you lost {xp} 50 XP and {coin} 100 coins", mention_author=False)

                    db.commit()

        elif a == "https://media.discordapp.net/attachments/807511480878497806/835889001839460362/pink.png":
            if anscol.content.lower() == "pink":
                await ctx.reply(f"**Good Job!** after filling up a bucket with sweat you gained:\n{xp}: {XP}\n{coin}: {COIN}", mention_author=False)
                cursor.execute(
                    "select user_xp, user_level, user_coins from users where client_id = %s", [ctx.author.id])
                result = cursor.fetchall()

                newXP = result[0][0]+XP
                newCoins = result[0][2]+COIN

                if newXP > 0:
                    currentLevel = newXP/1000

                cursor.execute("update users set user_xp = %s, user_level = %s, user_coins = %s where client_id = %s", [
                               newXP, currentLevel, newCoins, ctx.author.id])

                db.commit()

            else:
                cursor.execute(
                    "select user_xp, user_coins from users where client_id = %s", [ctx.author.id])
                result = cursor.fetchall()

                newXP = result[0][0]-50
                newCoins = result[0][1]-100

                if newXP > 0:
                    currentLevel = newXP/1000

                if newCoins < 0:
                    await ctx.send("😂️👌️ **Lmao** You're so poor that you can even lose ``100`` coins | Updated Balance: ``0``")
                    cursor.execute("update users set user_xp = %s, user_level = %s, user_coins = 0 where client_id = %s", [
                                   newXP, currentLevel, ctx.author.id])

                    db.commit()

                else:
                    cursor.execute("update users set user_xp = %s, user_level = %s, user_coins = %s where client_id = %s", [
                                   newXP, currentLevel, newCoins, ctx.author.id])
                    await ctx.reply(f"**lol** you lost {xp} 50 XP and {coin} 100 coins", mention_author=False)


@bot.command(aliases=['hl'])
@commands.cooldown(1, 10, commands.BucketType.user)
async def highlow(ctx):
    channel = ctx.channel
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    COIN = random.randint(100, 200)

    cursor.execute(
        "select user_coins from users where client_id = %s", [ctx.author.id])
    res = cursor.fetchall()

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

        guess = await bot.wait_for('message', check=check)

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
                    cursor.execute("update users set user_coins = %s where client_id = %s", [
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
                        cursor.execute(
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
                        cursor.execute("update users set user_coins = %s where client_id = %s", [
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
                        cursor.execute(
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
                        cursor.execute("update users set user_coins = %s where client_id = %s", [
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
                    cursor.execute("update users set user_coins = %s where client_id = %s", [
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
                        cursor.execute(
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
                        cursor.execute("update users set user_coins = %s where client_id = %s", [
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
                        cursor.execute(
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

                        cursor.execute("update users set user_coins = %s where client_id = %s", [
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
                    cursor.execute("update users set user_coins = %s where client_id = %s", [
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
                        cursor.execute(
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
                        cursor.execute("update users set user_coins = %s where client_id = %s", [
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


@bot.group(name="slots", invoke_without_command=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def slots(ctx, *, message):
    emoji_list = ["🛒️", "👍️", "💩️", "💸️", "🤝️", "💰️", "🌐️", "🧠️", "💩️", "😎️", "📀️",
                  "🍉️", "💍️", "🏐️", "💀️", "🤡️", "💰️", "💰️", "🤗️", "💩️", "🌌", "🌌", "😎️", "😎️", "💀️"]

    try:

        message = int(message)
        cursor.execute(
            "select user_coins from users where client_id = %s", [ctx.author.id])
        result = cursor.fetchall()
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
                cursor.execute(
                    "select user_coins from users where client_id = %s", [ctx.author.id])

                result2 = cursor.fetchall()
                COIN = result2[0][0] + message*2

                cursor.execute("update users set user_coins = %s where client_id = %s", [
                               COIN, ctx.author.id])
                final = message*2
                slot = discord.Embed(title="")
                slot.set_author(
                    name=f"{ctx.author.name}'s Slots", icon_url=ctx.author.avatar.url)
                slot.add_field(name=f"```[ {y} ]```",
                               value="_ _", inline=False)
                slot.add_field(name="_ _", value=f" You won! {coin} {final}")
                await ctx.reply(embed=slot, mention_author=False)
                db.commit()

            elif y == "💰️💰️💰️":
                cursor.execute(
                    "select user_coins from users where client_id = %s", [ctx.author.id])

                result3 = cursor.fetchall()
                COIN = result3[0][0] + message*4

                cursor.execute("update users set user_coins = %s where client_id = %s", [
                               COIN, ctx.author.id])
                final = message*4
                slot = discord.Embed(title="")
                slot.set_author(
                    name=f"{ctx.author.name}'s Slots", icon_url=ctx.author.avatar.url)
                slot.add_field(name=f"```[ {y} ]```",
                               value="_ _", inline=False)
                slot.add_field(name="_ _", value=f" You won! {coin} {final}")
                await ctx.reply(embed=slot, mention_author=False)
                db.commit()

            elif y == "🌌🌌🌌":

                cursor.execute(
                    "select user_coins from users where client_id = %s", [ctx.author.id])

                result4 = cursor.fetchall()
                COIN = result4[0][0] + message*6

                cursor.execute("update users set user_coins = %s where client_id = %s", [
                               COIN, ctx.author.id])
                final = message*6
                slot = discord.Embed(title="")
                slot.set_author(
                    name=f"{ctx.author.name}'s Slots", icon_url=ctx.author.avatar.url)
                slot.add_field(name=f"```[ {y} ]```",
                               value="_ _", inline=False)
                slot.add_field(name="_ _", value=f" You won! {coin} {final}")
                await ctx.reply(embed=slot, mention_author=False)
                db.commit()

            elif y == "🤡️🤡️🤡️":

                cursor.execute(
                    "select user_coins from users where client_id = %s", [ctx.author.id])

                result5 = cursor.fetchall()
                COIN = result5[0][0] + message*8

                cursor.execute("update users set user_coins = %s where client_id = %s", [
                               COIN, ctx.author.id])
                final = message*8
                slot = discord.Embed(title="")
                slot.set_author(
                    name=f"{ctx.author.name}'s Slots", icon_url=ctx.author.avatar.url)
                slot.add_field(name=f"```[ {y} ]```",
                               value="_ _", inline=False)
                slot.add_field(name="_ _", value=f" You won! {coin} {final}")
                await ctx.reply(embed=slot, mention_author=False)
                db.commit()

            elif y == "😎️😎️😎️":

                cursor.execute(
                    "select user_coins from users where client_id = %s", [ctx.author.id])

                result6 = cursor.fetchall()
                COIN = result6[0][0] - message*2
                final = message*2

                if COIN < 0:
                    cursor.execute(
                        "update users set user_coins = 0 where client_id = %s", [ctx.author.id])
                    await ctx.reply(f"😂️👌️ **Lmao** you're too poor to lose {coin} {final} | Updated Balance: ``0``")
                    db.commit()

                else:

                    cursor.execute("update users set user_coins = %s where client_id = %s", [
                                   COIN, ctx.author.id])

                    slot = discord.Embed(title="", description="")
                    slot.set_author(
                        name=f"{ctx.author.name}'s Slots", icon_url=ctx.author.avatar.url)
                    slot.add_field(
                        name=f"```[ {y} ]```", value="_ _", inline=False)
                    slot.add_field(
                        name="_ _", value=f" You lost big time! {coin} {final}")
                    await ctx.reply(embed=slot, mention_author=False)
                    db.commit()

            elif y == "💀️💀️💀️":

                cursor.execute(
                    "select user_coins from users where client_id = %s", [ctx.author.id])

                result7 = cursor.fetchall()
                COIN = result7[0][0] - message*4
                final = message*4

                if COIN < 0:
                    cursor.execute(
                        "update users set user_coins = 0 where client_id = %s", [ctx.author.id])
                    await ctx.reply(f"😂️👌️ **Lmao** you're too poor to lose {coin} {final} | Updated Balance: ``0``")
                    db.commit()

                else:

                    cursor.execute("update users set user_coins = %s where client_id = %s", [
                                   COIN, ctx.author.id])
                    db.commit()

                    slot = discord.Embed(title="")
                    slot.set_author(
                        name=f"{ctx.author.name}'s Slots", icon_url=ctx.author.avatar.url)
                    slot.add_field(
                        name=f"```[ {y} ]```", value="_ _", inline=False)
                    slot.add_field(
                        name="_ _", value=f" You lost big time! {coin} {final}")
                    await ctx.reply(embed=slot, mention_author=False)
                    db.commit()

            else:
                cursor.execute(
                    "select user_coins from users where client_id = %s", [ctx.author.id])
                result8 = cursor.fetchall()
                COIN = result8[0][0] - message
                cursor.execute("update users set user_coins = %s where client_id = %s", [
                               COIN, ctx.author.id])

                slot = discord.Embed(title="")
                slot.set_author(
                    name=f"{ctx.author.name}'s Slots", icon_url=ctx.author.avatar.url)
                slot.add_field(name=f"```[ {y} ]```",
                               value="_ _", inline=False)
                slot.add_field(
                    name="_ _", value=f" You lost! {coin} {message}")
                await ctx.reply(embed=slot, mention_author=False)
                db.commit()

    except ValueError:

        error_msg = discord.Embed(title=" ", description=" ", color=0xffb12b)
        error_msg.add_field(
            name="Error", value="Please enter a valid amount\nrun ``.slots info`` for more information\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
        await ctx.send(embed=error_msg)


@slots.command(name="info")
async def slots_info(ctx):
    sinfo = discord.Embed(color=random.choice(colors))
    sinfo.add_field(name="WINNER INFO",
                    value="```💩️💩️💩️ x2\n\n💰️💰️💰️ x4 \n\n🌌🌌🌌 x6\n\n🤡️🤡️🤡️ x8\n```")
    sinfo.add_field(name="LOSER INFO", value="```😎️😎️😎️ x2\n\n💀️💀️💀️ x4```")
    sinfo.set_footer(text="to play run: .slots <amount>")
    await ctx.send(embed=sinfo)


@bot.command()
@commands.cooldown(1, 300, commands.BucketType.user)
async def duel(ctx, p2: discord.Member):

    dx = 0
    dy = 0
    p1 = ctx.author
    user = [p1, p2]
    gameOver = 1
    winner = 1

    cursor.execute(
        "select user_xp, user_coins, health from users where client_id = %s", [ctx.author.id])
    result = cursor.fetchall()

    cursor.execute(
        "select user_xp, user_coins, health from users where client_id = %s", [p2.id])
    result2 = cursor.fetchall()

    if bot.user.mentioned_in(ctx.message):
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
        d = discord.Embed(title="Duels",
                          description=f"{p1.mention} and {p2.mention} read the following before starting the match",
                          color=random.choice(colors))
        d.add_field(name="STAKES", value="upon losing the duel you'll lose all your coins and only have ``1`` left",
                    inline=False)
        d.add_field(
            name="WINNER", value="the winner recieves all the coins(-1) of the loser", inline=False)
        d.add_field(name="READY?", value=f"{p1.mention} and {p2.mention} type ``ok`` within ``30`` seconds to accept and continue with the duel",
                    inline=False)
        d.add_field(name="``⚠️ WARNING ⚠️``",
                    value=f"Attempting to duel someone else during a duel will result in you losing the current duel", inline=False)
        d.set_footer(text="you may even lose coins during the duel 👍")
        await ctx.send(embed=d)

        while True:

            def check(message):

                return ctx.channel == message.channel

            try:

                ans = await bot.wait_for("message", check=check, timeout=30)

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
            cursor.execute(
                "select user_coins, defense, health, attack, quagun, enebazo from users where client_id = %s", [p1.id])
            res = cursor.fetchall()

            c = res[0][0]
            d = res[0][1]
            h = res[0][2]
            a = res[0][3]
            q = res[0][4]
            e = res[0][5]

            cursor.execute(
                "select user_coins, defense, health, attack, quagun, enebazo from users where client_id = %s", [p2.id])
            res2 = cursor.fetchall()

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
                du.add_field(name="Player's turn (random)",
                             value=f"{p1.mention}'s turn, please use any of the above commands to continue", inline=False)
                du.add_field(name="``⚠️ WARNING ⚠️``",
                             value=f"Attempting to duel someone else during a duel will result in you losing the current duel", inline=False)
                du.set_footer(
                    text="To win, the opponent has to lose all their health")
                await ctx.send(embed=du)

            elif turn == 1:
                du = discord.Embed(title="", color=random.choice(colors))
                du.add_field(name="List of usable commands:", value="1. ``weapon <item_id>`` - reduce the opponents health by using your weapons\n(there is a 20% chance that you'll miss)\n\n2. ``punch`` - reduce the opponents health by your attack level\n\n3. ``steal`` - 10% chance that you can steal 70% of the coins and run away otherwise you **lose** 50% of your coins\n(you won't get all the coins(-1) as stated before\n\n4. ``forfeit `` - surrender by giving away 30% of your coins")
                du.add_field(name="Player's turn (random)",
                             value=f"{p2.mention}'s turn, please use any of the above commands to continue", inline=False)
                du.add_field(name="``⚠️ WARNING ⚠️``",
                             value=f"Attempting to duel someone else during a duel will result in you losing the current duel", inline=False)
                du.set_footer(
                    text="To win, the opponent has to lose all their health")
                await ctx.send(embed=du)

            while True:
                def check(message):

                    return ctx.channel == message.channel

                msg = await bot.wait_for("message", check=check)

                if msg.author == user[turn]:

                    if msg.content.lower() == "forfeit":
                        if msg.author == p1:
                            await ctx.send(
                                f"{p1.mention} has forfeited and will lose 30% of their coins to {p2.mention} | run ``.profile`` to use your updated balance")
                            newc = c * (3/10)
                            c2final = c2 + newc
                            cfinal = c - newc

                            cursor.execute(
                                "update users set user_coins = %s where client_id = %s", [cfinal, p1.id])
                            cursor.execute("update users set user_coins = %s where client_id =  %s", [
                                           c2final, p2.id])
                            db.commit()
                            winner += 2
                            gameOver += 1

                        elif msg.author == p2:
                            await ctx.send(
                                f"{p2.mention} has forfeited and will lose 30% of their coins to {p1.mention} | run ``.profile`` to use your updated balance")
                            newc2 = c2 * (3/10)
                            c2final = c2 - newc2
                            cfinal = c + newc2

                            cursor.execute(
                                "update users set user_coins = %s where client_id = %s", [cfinal, p1.id])
                            cursor.execute("update users set user_coins = %s where client_id =  %s", [
                                           c2final, p2.id])
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
                                cursor.execute("UPDATE users set health = %s where client_id = %s", [
                                               h2final2, p2.id])
                                cursor.execute(
                                    "UPDATE users set quagun = %s where client_id = %s", [qfinal, p1.id])
                                await ctx.send(f"{p1.mention} has hit {p2.mention}, removing 20 of their health | its {p2.mention}'s turn")
                                db.commit()

                                if user[turn] == p1:
                                    user[turn] = p2
                                elif user[turn] == p2:
                                    user[turn] = p1

                                if h2final2 <= 0:
                                    cursor.execute(
                                        "UPDATE users set health = 0 where client_id = %s", [p2.id])
                                    loss2 = c2 - 1
                                    finalwin = c + loss2
                                    cursor.execute(
                                        "UPDATE users set user_coins = 1 where client_id = %s", [p2.id])
                                    cursor.execute("UPDATE users set user_coins = %s where client_id = %s", [
                                                   finalwin, p1.id])
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
                                cursor.execute("UPDATE users set health = %s where client_id = %s", [
                                               hfinal2, p1.id])
                                cursor.execute("UPDATE users set quagun = %s where client_id = %s", [
                                               q2final, p2.id])
                                await ctx.send(f"{p2.mention} has hit {p1.mention}, removing 20 of their health | its {p1.mention}'s turn")
                                db.commit()

                                if user[turn] == p1:
                                    user[turn] = p2
                                elif user[turn] == p2:
                                    user[turn] = p1

                                if hfinal <= 0:
                                    cursor.execute(
                                        "UPDATE users set health = 0 where client_id = %s", [p1.id])
                                    loss = c - 1
                                    finalwin2 = c2 + loss
                                    cursor.execute(
                                        "UPDATE users set user_coins = 1 where client_id = %s", [p1.id])
                                    cursor.execute("UPDATE users set user_coins = %s where client_id = %s", [
                                                   finalwin2, p2.id])
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
                                cursor.execute("UPDATE users set health = %s where client_id = %s", [
                                               h2final, p2.id])
                                cursor.execute(
                                    "UPDATE users set enebazo = %s where client_id = %s", [efinal, p1.id])
                                await ctx.send(f"{p1.mention} has hit {p2.mention}, removing 75 of their health | its {p2.mention}'s turn")
                                db.commit()

                                if user[turn] == p1:
                                    user[turn] = p2
                                elif user[turn] == p2:
                                    user[turn] = p1

                                if h2final <= 0:
                                    cursor.execute(
                                        "UPDATE users set health = 0 where client_id = %s", [p2.id])
                                    loss2 = c2 - 1
                                    finalwin = c + loss2
                                    cursor.execute(
                                        "UPDATE users set user_coins = 1 where client_id = %s", [p2.id])
                                    cursor.execute("UPDATE users set user_coins = %s where client_id = %s", [
                                                   finalwin, p1.id])
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
                                cursor.execute(
                                    "UPDATE users set health = %s where client_id = %s", [hfinal, p1.id])
                                cursor.execute("UPDATE users set enebazo = %s where client_id = %s", [
                                               e2final, p2.id])
                                await ctx.send(f"{p2.mention} has hit {p1.mention}, removing 75 of their health | its {p1.mention}'s turn")
                                db.commit()

                                if user[turn] == p1:
                                    user[turn] = p2
                                elif user[turn] == p2:
                                    user[turn] = p1

                                if hfinal <= 0:
                                    cursor.execute(
                                        "UPDATE users set health = 0 where client_id = %s", [p1.id])
                                    loss = c - 1
                                    finalwin2 = c2 + loss
                                    cursor.execute(
                                        "UPDATE users set user_coins = 1 where client_id = %s", [p1.id])
                                    cursor.execute("UPDATE users set user_coins = %s where client_id = %s", [
                                                   finalwin2, p2.id])
                                    await ctx.send(f"{p2.mention} has won the duel, leaving {p1.mention} with zero health! they will recieve all the coins (-1) of the loser")
                                    db.commit()
                                    winner += 2
                                    gameOver += 1

                    elif msg.content.lower() == "punch":
                        if msg.author == p1:
                            if a > d2:
                                await ctx.send(f"You hit {p2.name}, removing {a} of their health | its {p2.mention}'s turn")
                                h2final3 = h2 - a
                                cursor.execute("UPDATE users set health = %s where client_id = %s", [
                                               h2final3, p2.id])
                                db.commit()

                                if user[turn] == p1:
                                    user[turn] = p2
                                elif user[turn] == p2:
                                    user[turn] = p1

                                if h2final3 <= 0:
                                    cursor.execute(
                                        "UPDATE users set health = 0 where client_id = %s", [p2.id])
                                    loss2 = c2 - 1
                                    finalwin = c + loss2
                                    cursor.execute(
                                        "UPDATE users set user_coins = 1 where client_id = %s", [p2.id])
                                    cursor.execute("UPDATE users set user_coins = %s where client_id = %s", [
                                                   finalwin, p1.id])
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
                                cursor.execute("UPDATE users set health = %s where client_id = %s", [
                                               hfinal3, p1.id])

                                if user[turn] == p1:
                                    user[turn] = p2
                                elif user[turn] == p2:
                                    user[turn] = p1

                                if hfinal3 <= 0:
                                    cursor.execute(
                                        "UPDATE users set health = 0 where client_id = %s", [p1.id])
                                    loss = c - 1
                                    finalwin2 = c2 + loss
                                    cursor.execute(
                                        "UPDATE users set user_coins = 1 where client_id = %s", [p1.id])
                                    cursor.execute("UPDATE users set user_coins = %s where client_id = %s", [
                                                   finalwin2, p2.id])
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
                                cursor.execute("UPDATE users set user_coins = %s where client_id = %s", [
                                               c2final2, p2.id])
                                cursor.execute("UPDATE users set user_coins = %s where client_id = %s", [
                                               cfinal2, p1.id])
                                await ctx.send(f"⚡ **NO WAY** you were so fast that you stole {p2.mention}'s coins before they even blinked | GAME OVER")
                                db.commit()
                                winner += 1
                                gameOver += 1

                            else:
                                lost = c / 2
                                c2final3 = c2 + lost
                                cfinal3 = c - lost
                                cursor.execute("UPDATE users set user_coins = %s where client_id = %s", [
                                               c2final3, p2.id])
                                cursor.execute("UPDATE users set user_coins = %s where client_id = %s", [
                                               cfinal3, p1.id])
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
                                cursor.execute("UPDATE users set user_coins = %s where client_id = %s", [
                                               cfinal2, p1.id])
                                cursor.execute("UPDATE users set user_coins = %s where client_id = %s", [
                                               c2final2, p2.id])
                                await ctx.send(f"⚡ **NO WAY** you were so fast that you stole {p1.mention}'s coins before they even blinked | GAME OVER")
                                db.commit()
                                winner += 2
                                gameOver += 1

                            else:
                                lost = c2 / 2
                                cfinal3 = c + lost
                                c2final3 = c2 - lost
                                cursor.execute("UPDATE users set user_coins = %s where client_id = %s", [
                                               cfinal3, p1.id])
                                cursor.execute("UPDATE users set user_coins = %s where client_id = %s", [
                                               c2final3, p2.id])
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
                            cursor.execute(
                                "UPDATE users set user_coins = 1 where client_id = %s", [p1.id])
                            cursor.execute("UPDATE users set user_coins = %s where client_id = %s", [
                                           finalwin22, p2.id])
                            db.commit()
                            winner += 2
                            gameOver += 1

                        elif msg.author == p2:
                            await ctx.send(f"{msg.author.mention}, 😂️👎️ You can't start another duel because you are already in one | blame yourself for losing this duel\n{p1.mention} wins | run ``.profile`` to see your updated balance")
                            losss2 = c2 - 1
                            finalwinn = c + losss2
                            cursor.execute(
                                "UPDATE users set user_coins = 1 where client_id = %s", [p2.id])
                            cursor.execute("UPDATE users set user_coins = %s where client_id = %s", [
                                           finalwinn, p1.id])
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
                        go.add_field(
                            name=f"Winner: {p1.name}", value=f"{p1.mention} you will receive an additional {xp}{drxp}\nTo start a new game run ``.duel <@player2>`` (5 mins cooldown)")
                        await ctx.send(embed=go)

                        cursor.execute(
                            "select user_xp from users where client_id = %s", [p1.id])
                        lazy = cursor.fetchall()

                        fdxp = lazy[0][0] + drxp

                        dfl = fdxp / 1000

                        cursor.execute(
                            "select dplayed, dwins from users where client_id = %s", [p1.id])
                        fres = cursor.fetchall()

                        cursor.execute(
                            "select dplayed from users where client_id = %s", [p2.id])
                        fress = cursor.fetchall()

                        dpfinal = fres[0][0] + 1
                        dpfinal2 = fress[0][0] + 1
                        dwfinal = fres[0][1] + 1

                        cursor.execute("update users set user_xp = %s, user_level = %s, dplayed = %s, dwins = %s where client_id = %s", [
                                       fdxp, dfl, dpfinal, dwfinal, p1.id])
                        cursor.execute("update users set dplayed = %s where client_id = %s", [
                                       dpfinal2, p2.id])

                        db.commit()

                    elif winner == 3:
                        drxp2 = random.randint(1000, 2000)
                        go = discord.Embed(title="GAME OVER", color=000000)
                        go.add_field(
                            name=f"Winner: {p2.name}", value=f"{p2.mention} you will receive an additional {xp}{drxp2}\nTo start a new game run ``.duel <@player2>`` (5 mins cooldown)")
                        await ctx.send(embed=go)

                        cursor.execute(
                            "select user_xp from users where client_id = %s", [p2.id])
                        lazy2 = cursor.fetchall()

                        fdxp2 = lazy2[0][0] + drxp2

                        dfl2 = fdxp2 / 1000

                        cursor.execute(
                            "select dplayed, dwins from users where client_id = %s", [p2.id])
                        fres2 = cursor.fetchall()

                        cursor.execute(
                            "select dplayed from users where client_id = %s", [p1.id])
                        fress2 = cursor.fetchall()

                        dp2final = fres2[0][0] + 1
                        dpfinal22 = fress2[0][0] + 1
                        dw2final = fres2[0][1] + 1

                        cursor.execute("update users set user_xp = %s, user_level = %s, dplayed = %s, dwins = %s where client_id = %s", [
                                       fdxp2, dfl2, dp2final, dw2final, p2.id])
                        cursor.execute("update users set dplayed = %s where client_id = %s", [
                                       dpfinal22, p1.id])

                        db.commit()

                    db.commit()
                    break


@bot.command()
async def deletemydata(ctx):
    dmd = discord.Embed(color=random.choice(colors))
    dmd.add_field(name="Delete your info",
                  value=f"{ctx.author.mention} ARE YOU SURE YOU WANT TO CONTINUE?\nDoing this will get rid of all your info in our database\nType ``yes`` under ``10s`` to continue with the deletion")
    await ctx.send(embed=dmd)

    def check(message):

        return ctx.author == message.author and ctx.channel == message.channel

    try:

        ans = await bot.wait_for('message', check=check, timeout=10)

        if ans.author == ctx.message.author:
            if ans.content.lower() == "yes":
                cursor.execute(
                    "delete from users where client_id = %s", [ctx.author.id])
                db.commit()

                await ctx.send(f"``🟢 SUCCESSFUL - {ctx.author.name} your data has been deleted``")
            else:
                await ctx .send(f"``🔴 NOT SUCCESSFUL - {ctx.author.name} you failed to answer correctly``")
    except asyncio.TimeoutError:
        await ctx.send(f"``🔴 NOT SUCCESSFUL - {ctx.author.name} you failed to answer in time``")


@bot.command(aliases=["mem"])
async def memories(ctx):
    mem = discord.Embed(
        title="MEMORIES", description="Be grateful about everything, accept the sadness\nand move on, remember everything!", color=0xf7f7f7)
    mem.add_field(name="``.2020``", value="year 2020,  a crisis", inline=False)
    mem.add_field(name="``.2021``", value="year 2021,  a hope", inline=False)
    mem.set_image(
        url="https://media.discordapp.net/attachments/807511480878497806/829624717023248404/Untitled_design4.png")
    mem.set_footer(
        text="*Summary here refers to: all world happenings in a nutshell*")
    await ctx.send(embed=mem)


@bot.command(name="2020")
async def twenty_twenty(ctx):
    mem = discord.Embed(
        title="2020", description="It was by far one of the most difficult years for everyone\nCOVID - 19 had caused many hardships.", color=random.choice(colors))
    mem.add_field(
        name="_ _", value="--------------------------------------------------------------------", inline=False)
    mem.add_field(name="January - Kobe",
                  value="It was the worst possible news we could have ever gotten.\nHe will not be forgotten", inline=False)
    mem.add_field(name="February - Disasters ",
                  value="feb saw several environmental disasters", inline=False)
    mem.add_field(name="March - COVID - 19 ",
                  value="worsens across the world especially Italy", inline=False)
    mem.add_field(name="April - Asteroid ",
                  value="Asteroid which flew past close to Earth", inline=False)
    mem.add_field(name="May - COVID - 19", value="worsens again", inline=False)
    mem.add_field(name="August - Disasters ",
                  value="Aug saw several environmental disasters", inline=False)
    mem.add_field(name="October - COVID - 19 ",
                  value="COVID worsens again!", inline=False)
    mem.add_field(name="November - COVID - 19 ",
                  value="Widely Controlled! but not completely", inline=False)
    mem.add_field(name="December - NA ",
                  value="nothing major but we finally go through 2020 and survived!", inline=False)
    mem.add_field(
        name="_ _", value="--------------------------------------------------------------------", inline=False)
    mem.set_footer(
        text="(Only months which had major events) We must be grateful to survive through this 🤝")
    mem.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=mem)


@bot.command(name="2021")
async def twenty_twenty_one(ctx):
    mem = discord.Embed(
        title="2021", description="It came as a ray of hope to fight COVID - 19", color=random.choice(colors))
    mem.add_field(
        name="_ _", value="--------------------------------------------------------------------", inline=False)
    mem.add_field(name="January - Vaccine",
                  value="The Vaccine was announced for the Public (45 yrs above)", inline=False)
    mem.add_field(name="February - Response ",
                  value="worldwide response towards COVID", inline=False)
    mem.add_field(name="March - COVID - 19",
                  value="It worsens Again!", inline=False)
    mem.add_field(name="April - Ongoing", value="-NA-", inline=False)
    mem.add_field(
        name="_ _", value="--------------------------------------------------------------------", inline=False)
    mem.set_footer(text="(Only months which had major events)")
    mem.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=mem)


@bot.command()
async def wait(ctx):
    await ctx.send("Patience is a virtue")


@bot.command(aliases=['mini_games'])
async def games(ctx):
    bbo = discord.Embed(
        title="Mini Games", description="Choose which one you want to play!", color=0xa3ff61)
    bbo.add_field(name="🏀 ``.bbgame``",
                  value="basketball, simple shooting game", inline=False)
    bbo.add_field(name=":soccer: ``.fbgame``",
                  value="football, simple kicking game", inline=False)
    bbo.add_field(name="<:greenball:830467077058854922> ``.blgame``",
                  value="bowling, simple bowling game", inline=False)
    bbo.set_thumbnail(
        url="https://media.discordapp.net/attachments/807511480878497806/832282579050823711/aurora_games.png")
    await ctx.send(embed=bbo)


@bot.command()
async def bbgame(ctx):
    bbem = discord.Embed(
        title="Game Info", description="**React** to the appropriate power level to make a shot based on your intuition", color=random.choice(colors))
    bbem.add_field(name="Start Game: ``.shoot``", value="_ _", inline=False)
    bbem.add_field(
        name="Power levels (correspond to the reactions):", value="_ _", inline=False)
    bbem.set_image(url='https://media.discordapp.net/attachments/807511480878497806/819109874897911848/brown_square_red_square_orange_square_yellow_square_green_square_blue_square_white_large_square_.png')

    await ctx.send(embed=bbem)


@bot.command(aliases=["basketball"])
@commands.cooldown(1, 3, commands.BucketType.user)
async def shoot(ctx):
    x = random.randint(1, 8)
    coloremojis = {"🟫": 7, "🟥": 6, "🟧": 5, "🟨": 4, "🟩": 3, "🟦": 2, "⬜": 1}
    b = await ctx.reply("<:bbball:830475864172789800>" + ("<:transparent:830476759463231498>" * x) + ':wastebasket:', mention_author=False)
    for color in coloremojis.keys():
        await b.add_reaction(color)

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in coloremojis.keys()

    reaction, user = await bot.wait_for("reaction_add", check=check)

    a = int(x - coloremojis[str(reaction.emoji)])

    await b.edit(content="<:bbball:830475864172789800>" + "<:transparent:830476759463231498>" * a + ':wastebasket:')

    if a == 0:
        await b.edit(content="<:yay:830336856415666187>")
        await ctx.send(f"{ctx.author.mention}, Nice Shot! <a:jedipepe:796237771990761532> type ``.shoot`` to play again")

    elif a > 0:
        await b.edit(content="<:bbball:830475864172789800>" + "<:transparent:830476759463231498>" * a + ":wastebasket:")
        await ctx.send(f"{ctx.author.mention}, oh no! you're too short <a:wutpepe:796237684170424351> type ``.shoot`` to play again")

    elif a < 0:
        await b.edit(content=':wastebasket:' + "<:transparent:830476759463231498>" + "<:bbball:830475864172789800>")
        await ctx.send(f"{ctx.author.mention}, oh no! you went past the basket <a:wutpepe:796237684170424351> type ``.shoot`` to play again")


@bot.command()
async def fbgame(ctx):
    fb = discord.Embed(title="Game Info", description="the goal keeper can  move anywhere! use your luck...\nlist of choices to decide where the ball goes (use after command):\n ``left`` ``middle`` ``right``", color=random.choice(colors))
    fb.add_field(name="Start Game: ``.kickball``", value="_ _")
    await ctx.send(embed=fb)


@bot.command(aliases=["kb"])
@commands.cooldown(1, 3, commands.BucketType.user)
async def kickball(ctx):
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
                newplane = goal + "<:transparent:830476759463231498>" * 2 + \
                    goalie + "<:transparent:830476759463231498>"*2 + ball
                await f.edit(content=newplane)
                await ctx.send(f"{ctx.author.mention} "+ww + " lol the goalie blocked your kick")
                return

            elif y == 1:
                newplane = goal2+ball + "\n" + "<:transparent:830476759463231498>" + goalie
                await f.edit(content=newplane)
                await ctx.send(f"{ctx.author.mention} "+vb + " you made it into the goal")
                return

            elif y == 2:
                newplane = goal2 + ball + "\n" + "<:transparent:830476759463231498>" * 1 + goalie
                await f.edit(content=newplane)
                await ctx.send(f"{ctx.author.mention} " + vb + " you made it into the goal")
                return

            if r == 1:
                newplane = goal + "<:transparent:830476759463231498>" * 2 + \
                    goalie + "<:transparent:830476759463231498>" * 2 + ball
                await f.edit(content=newplane)
                await ctx.send(f"{ctx.author.mention} " + ww + " lol the goalie blocked your kick")
                return

            if x == 2:
                newplane = goal + "<:transparent:830476759463231498>" * 2 + \
                    goalie + "<:transparent:830476759463231498>"*2 + ball
                await f.edit(content=newplane)
                await ctx.send(f"{ctx.author.mention} "+ww + " lol the goalie blocked your kick")
                return

            return

        if ans.content.lower() == "left":
            y = random.randint(1, 3)
            r = random.randint(1, 2)
            if y == 1:
                newplane = goal + goalie + ball
                await f.edit(content=newplane)
                await ctx.send(f"{ctx.author.mention} "+ww + " lol the goalie blocked your kick")
                return

            elif y == 3:
                newplane = ball+goal2 + "\n" + "<:transparent:830476759463231498>" * 2 + goalie
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
                await ctx.send(f"{ctx.author.mention} "+ww + " lol the goalie blocked your kick")
                return

            if x == 0:
                newplane = goal + goalie + ball
                await f.edit(content=newplane)
                await ctx.send(f"{ctx.author.mention} "+ww + " lol the goalie blocked your kick")
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
                newplane = goal + "<:transparent:830476759463231498>"*1 + \
                    goalie + "<:transparent:830476759463231498>"*1 + ball
                await f.edit(content=newplane)
                await ctx.send(f"{ctx.author.mention} "+ww + " lol the goalie blocked your kick")
                return

            if r == 1:
                newplane = goal + goalie + ball
                await f.edit(content=newplane)
                await ctx.send(f"{ctx.author.mention} " + ww + " lol the goalie blocked your kick")
                return

            if x == 1:
                newplane = goal + "<:transparent:830476759463231498>" + \
                    goalie + "<:transparent:830476759463231498>" + ball
                await f.edit(content=newplane)
                await ctx.send(f"{ctx.author.mention} "+ww + " lol the goalie blocked your kick")
            return

        if ans.content.lower() == ".kickball":
            em = discord.Embed(title="", description="", colour=0xffb12b)
            em.add_field(
                name="ERROR", value="Please respond with the following options next time\n``left``, ``middle``, ``right``\n Support Server: [Join](https://discord.gg/G9vTrsV4aG)")
            await ctx.send(embed=em)
            return
        else:
            em = discord.Embed(title="", description="", colour=0xffb12b)
            em.add_field(name="ERROR",
                         value="Please respond with the following options next time\n``left``, ``middle``, ``right`` & ``.kickball`` to run the command again\n Support Server: [Join](https://discord.gg/G9vTrsV4aG)")
            await ctx.send(embed=em)
            return


@bot.command()
async def blgame(ctx):
    bl = discord.Embed(
        title="Game Info", description="Choose an appropriate power level to knock down all the pins\n(type the number listed below)", color=random.choice(colors))
    bl.add_field(name="Start Game: ``.bowl``", value="_ _", inline=False)
    bl.add_field(name="power levels list:",
                 value="1, 2, 3, 4, 5, 6", inline=False)
    await ctx.send(embed=bl)


@bot.command()
async def bowl(ctx):
    powerlevel = "<:12:831762862124171275><:34:831762862304526356><:56:831762862388936755>"
    win = f"{ctx.author.mention} <a:4919pepelaugh:830345716437352448> You knocked all the pins! "
    lose = f"{ctx.author.mention} <a:2813pepeexit:830345717478326273> lol your too short!"
    bounds = f"{ctx.author.mention} " + ww + \
        " yo slow down the ball went out of bounds"
    emoji = ["<:purpleball:830467076291821638>", "<:redball:830467075575119962>",
             "<:greenball:830467077058854922>", "<:blueball:830467076455137321>"]
    em = random.choice(emoji)
    plane = "<:pin:830469397465792512><:pin:830469397465792512><:pin:830469397465792512>\n      <:pin:830469397465792512><:pin:830469397465792512>\n             <:pin:830469397465792512>"
    broken = f"<:pin:830469397465792512><:pin:830469397465792512><:pin:830469397465792512>\n      <:pin:830469397465792512><:pin:830469397465792512>\n             <:fallenpin3:830469397671182346>{em}"
    broken2 = f"<:pin:830469397465792512><:pin:830469397465792512><:pin:830469397465792512>\n      <:fallenpin2:830469397000486963><:fallenpin1:830469397092892742>{em}\n             <:fallenpin3:830469397671182346>"
    broken3 = "<:fallenpin2:830469397000486963><:fallenpin3:830469397671182346><:fallenpin1:830469397092892742>\n      <:fallenpin2:830469397000486963><:fallenpin1:830469397092892742>\n             <:fallenpin3:830469397671182346>"
    x = random.randint(1, 6)
    newplane = plane + "\n<:transparent:830476759463231498>" * \
        x + "\n" + "             "+em+"\n"*2+powerlevel
    b = await ctx.reply(newplane, mention_author=False)

    def check(message):

        return ctx.author == message.author and ctx.channel == message.channel

    ans = await bot.wait_for('message', check=check)

    if ans.author == ctx.message.author:
        if ans.content.lower() == "1":
            if 1 == x:
                await b.edit(content=plane + "\n"*2 + "             " + em)
                await asyncio.sleep(0.5)
                await b.edit(content=broken)
                await asyncio.sleep(0.5)
                await b.edit(content=broken2)
                await asyncio.sleep(0.5)
                await b.edit(content="<:transparent:830476759463231498>" + em + "\n" + broken3)
                await ctx.send(win)
            elif 1 < x:
                await b.edit(content=plane + "\n"*4 + "             " + em)
                await ctx.send(lose)

        elif ans.content.lower() == "2":
            if 2 == x:
                await b.edit(content=plane + "\n"*3 + "             " + em)
                await asyncio.sleep(0.5)
                await b.edit(content=broken)
                await asyncio.sleep(0.5)
                await b.edit(content=broken2)
                await asyncio.sleep(0.5)
                await b.edit(content="<:transparent:830476759463231498>" + em + "\n" + broken3)
                await ctx.send(win)
            elif 2 < x:
                await b.edit(content=plane + "\n"*2 + "             " + em)
                await ctx.send(lose)
        elif ans.content.lower() == "3":
            if 3 == x:
                await b.edit(content=plane + "\n"*3 + "             " + em)
                await asyncio.sleep(0.5)
                await b.edit(content=broken)
                await asyncio.sleep(0.5)
                await b.edit(content=broken2)
                await asyncio.sleep(0.5)
                await b.edit(content="<:transparent:830476759463231498>" + em + "\n" + broken3)
                await ctx.send(win)
            elif 3 < x:
                await b.edit(content=plane + "\n"*3 + "             " + em)
                await ctx.send(lose)
            elif 3 > x:
                await b.edit(content="<:transparent:830476759463231498>"+em+"\n"*2+plane)
                await ctx.send(bounds)
        elif ans.content.lower() == "4":
            if 4 == x:
                await b.edit(content=plane + "\n"*3 + "             " + em)
                await asyncio.sleep(0.5)
                await b.edit(content=broken)
                await asyncio.sleep(0.5)
                await b.edit(content=broken2)
                await asyncio.sleep(0.5)
                await b.edit(content="<:transparent:830476759463231498>" + em + "\n" + broken3)
                await ctx.send(win)
            elif 4 < x:
                await b.edit(content=plane + "\n"*3 + "             " + em)
                await ctx.send(lose)
            elif 4 > x:
                await b.edit(content="<:transparent:830476759463231498>"+em+"\n"*3+plane)
                await ctx.send(bounds)
        elif ans.content.lower() == "5":
            if 5 == x:
                await b.edit(content=plane + "\n"*3 + "             " + em)
                await asyncio.sleep(0.5)
                await b.edit(content=broken)
                await asyncio.sleep(0.5)
                await b.edit(content=broken2)
                await asyncio.sleep(0.5)
                await b.edit(content="<:transparent:830476759463231498>" + em + "\n" + broken3)
                await ctx.send(win)
            elif 5 < x:
                await b.edit(content=plane + "\n"*3 + "             " + em)
                await ctx.send(lose)
            elif 5 > x:
                await b.edit(content="<:transparent:830476759463231498>"+em+"\n"*4+plane)
                await ctx.send(bounds)

        elif ans.content.lower() == "6":
            if 6 == x:
                await b.edit(content=plane + "\n"*3 + "             " + em)
                await asyncio.sleep(0.5)
                await b.edit(content=broken)
                await asyncio.sleep(0.5)
                await b.edit(content=broken2)
                await asyncio.sleep(0.5)
                await b.edit(content="<:transparent:830476759463231498>" + em + "\n" + broken3)
                await ctx.send(win)
            elif 6 > x:
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


@bot.command(aliases=['credits', 'credit', 'creds'])
async def cred(ctx):
    cred = discord.Embed(title="Credits and Information",
                         description="Thank you for using this bot, I hope you had a great time!", color=0x40bd9b)
    cred.set_thumbnail(
        url="https://media.discordapp.net/attachments/807511480878497806/838063325568172062/info.png")
    cred.set_author(name="Molecule", url="https://www.youtube.com/channel/UCdNMAz_kPKrpp6ujliRLtLQ",
                    icon_url="https://yt3.ggpht.com/ytc/AAUvwng1iHqfgIyaUVTmpRpYtxrpkHXY0WjqEvZ0KFeDMQ=s88-c-k-c0x00ffffff-no-rj")
    cred.add_field(name="My friends and other acquaintances ",
                   value="Thank you for helping me with small problems and giving me ideas", inline=False)
    cred.add_field(name="Python discord server ",
                   value="Website: https://pythondiscord.com/\nDiscord Server: https://discord.gg/python", inline=False)
    cred.add_field(name="Community & Support Server",
                   value="Join Sever: [click here](https://discord.gg/G9vTrsV4aG)", inline=False)
    cred.add_field(
        name="To Vote", value="Use command: **``.vote``**", inline=False)

    cred.set_footer(text="Bot by Molecule | Owner")

    await ctx.send(embed=cred)


@bot.command()
async def vote(ctx):
    vote = discord.Embed(title="Vote for Aurora",
                         description="", color=random.choice(colors))
    vote.add_field(
        name="top.gg", value="[Upvote](https://top.gg/bot/804228080952016897)", inline=False)
    vote.add_field(name="discordbotlist.com",
                   value="[Upvote](https://discordbotlist.com/bots/aurora)", inline=False)
    vote.set_thumbnail(
        url="https://media.discordapp.net/attachments/807511480878497806/817463545368412221/Untitled_design3.png")
    vote.set_footer(
        text="Leave an honest review and upvote! ⬆ | Bot by Molecule")

    await ctx.send(embed=vote)


@bot.command(aliases=['utility'])
async def util(ctx):
    ut = discord.Embed(
        title="UTILITY", description="utility commands", color=0x878787)
    ut.add_field(name="🏓 ``.ping``", value=" Latency (ms)", inline=False)
    ut.add_field(name="📈️ ``.stats``",
                 value="Displays ping, uptime, sever count")
    ut.add_field(name="📝 ``.perm <numbers>``",
                 value="space your numbers", inline=False)
    ut.add_field(name="❌ ``.purge <number>``",
                 value="clear messages", inline=False)
    ut.add_field(name="✏ ``.prefix (disabled cmd)``",
                 value=".prefix <new prefix>", inline=False)
    ut.set_thumbnail(
        url="https://media.discordapp.net/attachments/807511480878497806/832286879713722374/aurora_util.png")
    ut.set_footer(text="Bot by Molecule")

    await ctx.send(embed=ut)


@bot.command()
async def ping(ctx):
    if bot.latency > 0.15:
        highping = discord.Embed(title=' ', description=" ")
        highping.add_field(name=f"🔴 {(round(bot.latency * 1000))} ms",
                           value=" That's high ping right there ", inline=False)
        await ctx.send(embed=highping)
    elif bot.latency < 0.15:
        lowping = discord.Embed(title=' ', description=" ")
        lowping.add_field(name=f"🟢 {(round(bot.latency * 1000))} ms",
                          value=" That's low ping right there ", inline=False)
        await ctx.send(embed=lowping)


@bot.command()
async def stats(ctx):
    c_time = time.time()
    diff = int(round(c_time - s_time))
    uptime = str(datetime.timedelta(seconds=diff))
    highping = discord.Embed(title=' ', description=" ")
    highping.add_field(
        name=f"Ping", value=f"{(round(bot.latency * 1000))} ms", inline=True)
    highping.add_field(name=f"Servers Count",
                       value=f"{str(len(bot. guilds))} servers", inline=True)
    highping.add_field(name=f"Uptime", value=f"{uptime} ", inline=False)
    await ctx.send(embed=highping)


@bot.command(pass_context=True)
@commands.has_permissions(manage_guild=True)
@commands.bot_has_guild_permissions()
async def purge(ctx, limit: int):
    if limit < 1:
        await ctx.send("bruh its impossible to delete that many messages")
    elif limit > 500:
        await ctx.send("you can only delete 500 or less at a time")
    else:
        await ctx.channel.purge(limit=limit + 1)
        await ctx.send(f'<a:8584_verified_blue:829373373640998922> **-** ``{limit}`` **messages have been deleted**', delete_after=4)


@bot.command()
async def perm(ctx, nums: int):
    tmpList = []
    ans = ""

    for i in range(len(str(nums))):
        tmpList.append(str(nums)[i])

    permList = list(itertools.permutations(tmpList))

    for j in permList:
        ans += f"{j}\n"

    await ctx.send(f'>>> ```{ans}```')


@bot.command()
async def prefix(ctx):
    noy = discord.Embed(title="", description="", color=0xffb12b)
    noy.add_field(name="ERROR - DISABLED COMMAND",
                  value="this command is disabled", inline=False)
    await ctx.send(embed=noy)


@bot.command()
async def fun(ctx):
    fun = discord.Embed(
        title="FUN", description="Busy day? why not have some fun", color=0xffdd00)
    fun.add_field(name="🔪️ ``.destroyme``",
                  value="wanna get roasted?", inline=False)
    fun.add_field(name=":gun: ``.destroy <@user>``",
                  value="wanna destroy someone?", inline=False)
    fun.add_field(name="✂️ ``.start``",
                  value="rock paper scissors", inline=False)
    fun.add_field(name=":8ball: ``.8ball``",
                  value="a classic 8ball answer", inline=False)
    fun.add_field(name="🤔️ ``.riddle``",
                  value="train your brain", inline=False)
    fun.add_field(name="<:ruler:832256221431988265> ``.numbers``",
                  value="fun commands which use basic math", inline=False)
    fun.add_field(name="🐱‍💻 ``.hack``",
                  value="wanna get hacked? or wanna hack?", inline=False)
    fun.set_thumbnail(
        url="https://media.discordapp.net/attachments/807511480878497806/832262569917808670/aurora_fun.png")

    await ctx.send(embed=fun)


@bot.command()
async def destroyme(ctx):
    await ctx.send(f"{ctx.author.mention} {random.choice(roasts)}")


@bot.command()
async def destroy(ctx, member: discord.Member):
    if bot.user.mentioned_in(ctx.message):
        await ctx.send("Imagine being dumb enough to try to destroy me")
    elif member == member:
        await ctx.send('{0.name}, '.format(member)+(random.choice(roasts)))


@bot.command(name="8ball")
async def eight_ball(ctx, *, message):
    msg = message
    if any(word in msg for word in ball_arg):
        await ctx.reply("Listen kid, the owner and I are **chad** so back off 😄", mention_author=False)
    else:
        await ctx.reply("🎱️ " + random.choice(ball), mention_author=False)


@bot.command()
async def riddle(ctx):
    ridem = discord.Embed(title=" ", description="",
                          color=random.choice(colors))
    ridem.add_field(name="The answer is marked as spoiler",
                    value=(random.choice(riddles)), inline=False)
    await ctx.send(embed=ridem)


@bot.command()
async def start(ctx):
    rps = discord.Embed(title="Rock Paper Scissor Game",
                        description="Use the following words as your action", color=0x6b6b6b)
    rps.add_field(name="Run: ``.rps <choice>``\n_ _\nChoices:",
                  value="``👊 Rock``_ _ _ _``✌ Scissors``_ _ _ _``✋ Paper``")
    rps.set_footer(text="You don't have to use the emoji")
    await ctx.send(embed=rps)


@bot.command()
async def rps(ctx, *, message):
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


@bot.command(aliases=["number"])
async def numbers(ctx):
    no = discord.Embed(
        title="NUMBERS", description="Command List:", colour=0x46850)
    no.add_field(name="❌ ``.oddeven <choice>``",
                 value="guess whether the number will be odd or even between 5 and 25", inline=False)
    no.add_field(name="✅ ``.findnum <number>``",
                 value="guess a number between 1 to 10", inline=False)
    await ctx.send(embed=no)


@bot.command()
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
        error_msg.add_field(
            name="Error", value="please enter a valid choice: ``odd`` or ``even``\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
        await ctx.send(embed=error_msg)


@bot.command()
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
        error_msg.add_field(
            name="Error", value="please enter a valid number between ``1`` to ``10``\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
        await ctx.send(embed=error_msg)


@bot.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def hack(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
        await ctx.send("ayo forgot to mention someone? I guess I'll have to hack you...")

    await asyncio.sleep(1)
    hax = discord.Embed(title="```Virus Activated```",
                        description=f"{user.mention}", colour=0x63ff52)
    hax.add_field(name="Now we wait...",
                  value="```lol, your info and device is mine :)```")
    hax.set_image(
        url="https://media.discordapp.net/attachments/807511480878497806/829318751177539594/Untitled_design2.gif")
    hax.set_footer(text="🤡🤝")
    j = await ctx.send(embed=hax)
    await asyncio.sleep(1)
    h = await ctx.send("fetching client's gmail account and password... ")
    await asyncio.sleep(1)
    await h.edit(content=f"Gmail: ``{user}@aurorafan.com``\npassword: ``"+random.choice(fake_pwds)+"``")
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
    newhax = discord.Embed(title="```Virus Activated```",
                           description=f"{user.mention}", colour=0x63ff52)
    newhax.add_field(name="Hack Completed",
                     value="```lol, your info and device is mine :)```")
    newhax.set_image(
        url="https://media.discordapp.net/attachments/807511480878497806/829318751177539594/Untitled_design2.gif")
    newhax.set_footer(text="🤡🤝")
    await j.edit(embed=newhax)


@bot.command(pass_context=True)
@commands.cooldown(1, 2, commands.BucketType.user)
async def meme(ctx):
    if not hasattr(bot, 'nextMeme'):
        bot.nextMeme = getmeme()

    name, url = bot.nextMeme
    embed0 = discord.Embed(title=name, color=random.choice(colors))
    embed0.set_image(url=url)

    await ctx.send(embed=embed0)

    bot.nextMeme = getmeme()


def getmeme():
    subreddit = reddit.subreddit("memes")
    subreddit2 = reddit.subreddit("dankmemes")
    all_subs = []

    hot = subreddit.new(limit=100)
    hot2 = subreddit2.new(limit=100)

    for submission in hot:
        all_subs.append(submission)
    for submission1 in hot2:
        all_subs.append(submission1)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        return name, url


@bot.command()
async def guess(ctx):
    embed = discord.Embed(title="Guessing Game",
                          description="You will see a part of an image or something from a franchise and you will have to guess what it is. **PICK ONE** by typing it down",
                          color=0xff8fa9)
    embed.add_field(name="<:pink:832279712151765002> Anime (.anime)",
                    value="A scene or a character can be shown", inline=False)
    embed.add_field(name="<:pink:832279712151765002> Geography (.geo)",
                    value="A popular place (it can be fictional)", inline=False)
    embed.set_thumbnail(
        url="https://media.discordapp.net/attachments/807511480878497806/833765293088047198/aurora_guess.png")
    embed.set_footer(text="Have a great time | Bot by Molecule")
    await ctx.send(embed=embed)


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def anime(ctx):

    x = random.randint(1, 57)
    y = random.randint(1, 57)

    if x > y:
        xy = random.randint(y, x)
    elif x < y:
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
            return


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def geo(ctx):
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
            return


@bot.group(name="market", invoke_without_command=True)
async def market(ctx):
    await ctx.send("UNDER DEV")

    cursor.execute(
        "SELECT * FROM user_market WHERE client_id = %s", [ctx.author.id])
    result = cursor.fetchall()

    if len(result) == 0:
        cursor.execute(
            "INSERT INTO user_market VALUES(%s, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)", [ctx.author.id])
        db.commit()

    mp = discord.Embed(
        title="MARKETPLACE", description="run ``.market info`` to learn more\nThe Following are the items you can buy from respective companies", color=random.choice(colors))
    mp.add_field(name="Essencery",
                 value=f"Potato ─ 10 | *ID* → ``potato``\nCorn ─ 20 | *ID* → ``corn``\nCookies ─ 50 | *ID* → ``cookies``", inline=False)
    mp.add_field(name="Books & Co.",
                 value=f"Pens ─ 5 | *ID* → ``pens``\nSheets ─ 10 | *ID* → ``sheets``\nManga ─ 1000 | *ID* → ``manga``", inline=False)
    mp.add_field(name="Utlity Mart", value=f"Screws ─ 20 | *ID* → ``screws``\nHammer ─ 400 | *ID* → ``hammer``\nPower Drill ─ 2000 | *ID* → ``pwrdrill``", inline=False)
    mp.add_field(name="Solitare", value=f"Gold ─ 10000 | *ID* → ``gold``\nPlatinum ─ 15000 | *ID* → ``plat``\nDiamond ─ 20000 | *ID* → ``diamond``", inline=False)
    mp.set_footer(text="run < .market buy id quantity > to buy these items")
    await ctx.send(embed=mp)


@market.command(name="info")
async def market_info(ctx):
    await ctx.send("UNDER DEV")

    cursor.execute(
        "SELECT * FROM user_market WHERE client_id = %s", [ctx.author.id])
    result = cursor.fetchall()

    if len(result) == 0:
        cursor.execute(
            "INSERT INTO user_market VALUES(%s, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)", [ctx.author.id])
        db.commit()

    mi = discord.Embed(title="MARKETPLACE - INFO",
                       description="⚠️ Please read the following carefully: every aspect of this is completely fictional and any refrences to real life is purely  coincidental", color=random.choice(colors))
    mi.add_field(name="Basic Idea",
                 value="To be the richest, your main focus would be to become rich", inline=False)
    mi.add_field(name="How is it done?", value="by running ``.market`` you can buy items, This works in favor of the company selling the particular item. You can also invest in companies by ``.stocks``, keep in mind you can make/lose coins depending upon the company's stock prices", inline=False)
    mi.add_field(name="Basic things you need to know",
                 value="If a certain item is bought alot its value is bound to decrease, which may be beneficial to the particular company selling this 'item' hence affecting its stock prices and Net Worth", inline=False)
    mi.add_field(name="A few Rules", value="``1.`` All transactions of coins are your responsibility\n``2.`` If you lose coins after investing, its again your responsibility and refunds will not be entertained", inline=False)
    await ctx.send(embed=mi)


@market.command(name="buy")
async def market_buy(ctx):
    await ctx.send("UNDER DEV")


@bot.group(name="stocks", aliases=["stock"], invoke_without_command=True)
async def stocks(ctx):
    await ctx.send("UNDER DEV")


@bot.event
async def on_command_error(ctx, error):
    error = getattr(error, 'original', error)
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You can't do that :( ")
    elif isinstance(error, commands.MemberNotFound):
        error_msg = discord.Embed(title=" ", description=" ", color=0xffb12b)
        error_msg.add_field(
            name="Error", value="Please mention a user\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
        await ctx.send(embed=error_msg)
    elif isinstance(error, commands.MissingRequiredArgument):
        if ctx.command.name == "findnum":
            error_msg = discord.Embed(
                title=" ", description=" ", color=0xffb12b)
            error_msg.add_field(
                name="Error", value="please enter a valid number between 1 to 10 (not decimal)\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
            await ctx.send(embed=error_msg)
        elif ctx.command.name == "8ball":
            error_msg = discord.Embed(
                title=" ", description=" ", color=0xffb12b)
            error_msg.add_field(
                name="Error", value="please type down a message after the ``.8ball``\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
            await ctx.reply(embed=error_msg, mention_author=False)
        elif ctx.command.name == "dp":
            error_msg = discord.Embed(
                title=" ", description=" ", color=0xffb12b)
            error_msg.add_field(
                name="Error", value="please enter the number of items you want\nformat: ``.shop <item> <number>``\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
            await ctx.reply(embed=error_msg, mention_author=False)
        elif ctx.command.name == "hp":
            error_msg = discord.Embed(
                title=" ", description=" ", color=0xffb12b)
            error_msg.add_field(
                name="Error", value="please enter the number of items you want\nformat: ``.shop <item> <number>``\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
            await ctx.reply(embed=error_msg, mention_author=False)
        elif ctx.command.name == "vp":
            error_msg = discord.Embed(
                title=" ", description=" ", color=0xffb12b)
            error_msg.add_field(
                name="Error", value="please enter the number of items you want\nformat: ``.shop <item> <number>``\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
            await ctx.reply(embed=error_msg, mention_author=False)
        elif ctx.command.name == "slots":
            error_msg = discord.Embed(
                title=" ", description=" ", color=0xffb12b)
            error_msg.add_field(
                name="Error", value="please enter a valid amount to gamble with\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
            await ctx.reply(embed=error_msg, mention_author=False)
        else:
            error_msg = discord.Embed(
                title=" ", description=" ", color=0xffb12b)
            error_msg.add_field(
                name="Error", value="please enter the necessary arguments\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
            await ctx.send(embed=error_msg)
    elif isinstance(error, commands.CommandOnCooldown):
        if ctx.command.name == "meme":
            cool = discord.Embed(title="Slow it down",
                                 description=" ", color=0xa58fff)
            cool.add_field(
                name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.meme`` is ``1s``\nTry again in ``{error.retry_after:.2f}s``")
            await ctx.send(embed=cool)
        elif ctx.command.name == "highlow":
            cool = discord.Embed(title="Slow it down",
                                 description=" ", color=0xa58fff)
            cool.add_field(
                name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.highlow`` is ``10s``\nTry again in ``{error.retry_after:.2f}s``")
            await ctx.send(embed=cool)
        elif ctx.command.name == "anime":
            cool = discord.Embed(title="Slow it down",
                                 description=" ", color=0xa58fff)
            cool.add_field(
                name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.anime`` is ``5s``\nTry again in ``{error.retry_after:.2f}s``")
            await ctx.send(embed=cool)
        elif ctx.command.name == "geo":
            cool = discord.Embed(title="Slow it down",
                                 description=" ", color=0xa58fff)
            cool.add_field(
                name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.geo`` is ``5s``\nTry again in ``{error.retry_after:.2f}s``")
            await ctx.send(embed=cool)
        elif ctx.command.name == "sw":
            cool = discord.Embed(title="Slow it down",
                                 description=" ", color=0xa58fff)
            cool.add_field(
                name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.sw`` is ``5s``\nTry again in ``{error.retry_after:.2f}s``")
            await ctx.send(embed=cool)
        elif ctx.command.name == "shoot":
            cool = discord.Embed(title="Slow it down",
                                 description=" ", color=0xa58fff)
            cool.add_field(
                name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.shoot`` is ``3s``\nTry again in ``{error.retry_after:.2f}s``")
            await ctx.send(embed=cool)
        elif ctx.command.name == "kickball":
            cool = discord.Embed(title="Slow it down",
                                 description=" ", color=0xa58fff)
            cool.add_field(
                name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.kickball`` is ``3s``\nTry again in ``{error.retry_after:.2f}s``")
            await ctx.send(embed=cool)
        elif ctx.command.name == "bowl":
            cool = discord.Embed(title="Slow it down",
                                 description=" ", color=0xa58fff)
            cool.add_field(
                name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.bowl`` is ``3s``\nTry again in ``{error.retry_after:.2f}s``")
            await ctx.send(embed=cool)
        elif ctx.command.name == "hack":
            cool = discord.Embed(title="Slow it down",
                                 description=" ", color=0xa58fff)
            cool.add_field(
                name="⏪ ⏪ ⏪", value=f"don't hack people too much, Default cooldown for ``.hack`` is ``30s``\nTry again in ``{error.retry_after:.2f}s``")
            await ctx.send(embed=cool)
        elif ctx.command.name == "quest":
            cool = discord.Embed(title="Slow it down",
                                 description=" ", color=0xa58fff)
            cool.add_field(
                name="⏪ ⏪ ⏪", value=f"you have already hunted enough, Default cooldown for ``.quest`` is ``30s``\nTry again in ``{error.retry_after:.2f}s``")
            await ctx.send(embed=cool)
        elif ctx.command.name == "train":
            cool = discord.Embed(title="Slow it down",
                                 description=" ", color=0xa58fff)
            cool.add_field(
                name="⏪ ⏪ ⏪", value=f"you have already trained, Default cooldown for ``.train`` is ``45s``\nTry again in ``{error.retry_after:.2f}s``")
            await ctx.send(embed=cool)
        elif ctx.command.name == "dp":
            cool = discord.Embed(title="Slow it down",
                                 description=" ", color=0xa58fff)
            cool.add_field(
                name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.buy`` and ``.use`` is ``20s``\nTry again in ``{error.retry_after:.2f}s``")
            await ctx.send(embed=cool)
        elif ctx.command.name == "hp":
            cool = discord.Embed(title="Slow it down",
                                 description=" ", color=0xa58fff)
            cool.add_field(
                name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.buy`` and ``.use`` is ``20s``\nTry again in ``{error.retry_after:.2f}s``")
            await ctx.send(embed=cool)
        elif ctx.command.name == "vp":
            cool = discord.Embed(title="Slow it down",
                                 description=" ", color=0xa58fff)
            cool.add_field(
                name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.buy`` and ``.use`` is ``20s``\nTry again in ``{error.retry_after:.2f}s``")
            await ctx.send(embed=cool)
        elif ctx.command.name == "qg":
            cool = discord.Embed(title="Slow it down",
                                 description=" ", color=0xa58fff)
            cool.add_field(
                name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.buy`` and ``.use`` is ``20s``\nTry again in ``{error.retry_after:.2f}s``")
            await ctx.send(embed=cool)
        elif ctx.command.name == "eb":
            cool = discord.Embed(title="Slow it down",
                                 description=" ", color=0xa58fff)
            cool.add_field(
                name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.buy`` and ``.use`` is ``20s``\nTry again in ``{error.retry_after:.2f}s``")
            await ctx.send(embed=cool)
        elif ctx.command.name == "orb":
            cool = discord.Embed(title="Slow it down",
                                 description=" ", color=0xa58fff)
            cool.add_field(
                name="⏪ ⏪ ⏪", value=f"Default cooldown for this item\n``.buy`` - ``20s``\n``.use`` - ``3hr``\nTry again in ``{error.retry_after:.2f}s``")
            await ctx.send(embed=cool)
        elif ctx.command.name == "molecule":
            cool = discord.Embed(title="Slow it down",
                                 description=" ", color=0xa58fff)
            cool.add_field(
                name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.buy`` and ``.use`` is ``20s``\nTry again in ``{error.retry_after:.2f}s``")
            await ctx.send(embed=cool)
        elif ctx.command.name == "box":
            cool = discord.Embed(title="Slow it down",
                                 description=" ", color=0xa58fff)
            cool.add_field(
                name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.box`` is ``2m``\nTry again in ``{error.retry_after:.2f}s``")
            await ctx.send(embed=cool)
        elif ctx.command.name == "slots":
            cool = discord.Embed(title="Slow it down",
                                 description=" ", color=0xa58fff)
            cool.add_field(
                name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.slots`` is ``10s``\nTry again in ``{error.retry_after:.2f}s``")
            await ctx.send(embed=cool)
        elif ctx.command.name == "duel":
            cool = discord.Embed(title="Slow it down",
                                 description=" ", color=0xa58fff)
            cool.add_field(
                name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.duel`` is ``5m``\nTry again in ``{error.retry_after:.2f}s``")
            await ctx.send(embed=cool)
        elif ctx.command.name == "fight":
            cool = discord.Embed(title="Slow it down",
                                 description=" ", color=0xa58fff)
            cool.add_field(
                name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.fight`` is ``30s``\nTry again in ``{error.retry_after:.2f}s``")
            await ctx.send(embed=cool)
    elif isinstance(error, discord.Forbidden):
        if ctx.command.name == "purge":
            error_msg = discord.Embed(
                title=" ", description=" ", color=0xffb12b)
            error_msg.add_field(
                name="Error", value="I'm missing the manage messages permission!\n_ _\n**Check the following:**\nAurora BOT Role permissions\nChannel permissions\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
            await ctx.send(embed=error_msg)
        else:
            error_msg = discord.Embed(
                title=" ", description=" ", color=0xffb12b)
            error_msg.add_field(
                name="Error", value="I'm missing the manage messages permission!\n_ _\n**Check the following:**\nAurora BOT Role permissions\nChannel permissions\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
            await ctx.send(embed=error_msg)
    elif isinstance(error, commands.CommandInvokeError):
        if ctx.command.name == "perm":
            error_msg = discord.Embed(
                title=" ", description=" ", color=0xffb12b)
            error_msg.add_field(
                name="Error", value="The output was more than 2000 characters, maybe try shortening your argument\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
            await ctx.send(embed=error_msg)
    elif isinstance(error, discord.HTTPException):
        if ctx.command.name == "perm":
            error_msg = discord.Embed(
                title=" ", description=" ", color=0xffb12b)
            error_msg.add_field(
                name="Error", value="The output was more than 2000 characters, maybe try shortening your argument\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
            await ctx.send(embed=error_msg)
    elif isinstance(error, commands.BadArgument):
        if ctx.command.name == "perm":
            error_msg = discord.Embed(
                title=" ", description=" ", color=0xffb12b)
            error_msg.add_field(
                name="Error", value="Space the numbers and try again\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
            await ctx.send(embed=error_msg)


db.commit()

bot.run(DISCORD_TOKEN)
