from discord.ext import commands 
import discord

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix = ".", case_insensitive=True, intents=intents)

class Rpg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.group(name="rpg", invoke_without_command=True)
    async def rpg(self, ctx):
        rpg = discord.Embed(title="RPG GAME (UNDER DEV)", description="The following are the commands which you can use\n **run ``.rpg info`` to learn more about the game**\n_ _", color=0x99ffd3)
        rpg.set_thumbnail(url="https://media.discordapp.net/attachments/807511480878497806/834121432849973288/rpg.png")
        rpg.add_field(name="_ _", value="_ _", inline = False)
        rpg.add_field(name="📈️ __MARKETPLACE__ (UNDER DEV)", value="``.market info`` ``.market`` ``.stocks``", inline = False)
        rpg.add_field(name="🎖️ __LEVELING__", value="``.quest`` ``.train`` ``.fight``", inline = True)
        rpg.add_field(name="_ _", value="_ _", inline=True)
        rpg.add_field(name="🗡️ __MULTIPLAYER__", value="``.duel``", inline = True)
        rpg.add_field(name="📂️ __PROGRESS__", value="``.profile`` ``.inv``", inline = True)
        rpg.add_field(name="_ _", value="_ _", inline=True)
        rpg.add_field(name="🛒️ __SHOPPING__", value="``.shop`` ``.buy`` ``.use``", inline = True)
        rpg.add_field(name="💸️ __GAMBLING__", value="``.highlow`` ``.slots``", inline = True)
        rpg.add_field(name="_ _", value="_ _", inline=True)
        rpg.add_field(name="📮️ __SETTINGS__", value="``.deletemydata``", inline = True)
        rpg.set_footer(text="First step to start playing, run .quest")
        await ctx.send(embed=rpg)

    @rpg.command(name="info")
    async def rpg_info(self, ctx):
        info = discord.Embed(title="RPG GAME INFO (UNDER DEV)", description="The main objective is to gain xp and levels to unlock various items and to move forward in the game\n**first ting you must do is go on your first adventure! run ``.quest``**", color=0x787878)
        info.add_field(name="__GAME FEATURES__", value="→ Earn COINS and XP with ``.quest`` ``.train``. Fight monsters with ``.fight``\n→ Check your data and progess with ``.profile``", inline = False)
        info.add_field(name="__MARKETPLACE__ (UNDER DEV)", value="→ Trade stocks of different hypothetical companies to earn money.\nrun ``.market info`` to learn more", inline = False)
        info.add_field(name="__SHOP INFO__", value="→ To buy items like weapons or potions use ``.shop``\n→The items can only be bought by COINS", inline = False)
        info.add_field(name="__GAMBLING__", value="→ To earn more money (coins) use ``.highlow`` ``.slots``\n→ You can only earn COINS not XP")
        info.add_field(name="__OTHER FEATURES__", value="→ Multiplayer\n To play with your friends: ``.duel``", inline = False)
        info.set_footer(text="Enjoy your time 👍")
        await ctx.send(embed=info)


async def setup(bot):
    await bot.add_cog(Rpg(bot))