from discord.ext import commands 
import discord
import random
import datetime
import time
import os
from itertools import permutations

s_time = time.time()
intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix = ".", case_insensitive=True, intents=intents)

class Util(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
    
    @commands.command(aliases=['utility'])
    async def util(self, ctx):
        ut = discord.Embed(title= "UTILITY", description= "utility commands", color=0x878787)
        ut.add_field(name="🏓 ``.ping``", value=" Latency (ms)", inline=False)
        ut.add_field(name="📈️ ``.stats``", value="Displays ping, uptime, sever count")
        ut.add_field(name="📝 ``.perm <numbers>``", value="space your numbers", inline=False)
        ut.add_field(name="❌ ``.purge <number>``", value="clear messages", inline=False)
        ut.add_field(name="✏ ``.prefix (disabled cmd)``", value=".prefix <new prefix>", inline=False)
        ut.set_thumbnail(url="https://media.discordapp.net/attachments/807511480878497806/832286879713722374/aurora_util.png")
        ut.set_footer(text="Bot by Molecule")

        await ctx.send(embed=ut)
    @commands.command()
    async def ping(self, ctx):
        if bot.latency > 0.15:
            highping = discord.Embed(title=' ', description=" ")
            highping.add_field(name=f"🔴 {(round(bot.latency * 1000))} ms", value=" That's high ping right there ", inline=False)
            await ctx.send(embed=highping)
        elif bot.latency < 0.15:
            lowping = discord.Embed(title=' ', description=" ")
            lowping.add_field(name=f"🟢 {(round(bot.latency * 1000))} ms", value=" That's low ping right there ", inline=False)
            await ctx.send(embed=lowping)

    @commands.command()
    async def stats(self, ctx):
        c_time = time.time()
        diff = int(round(c_time - s_time))
        uptime = str(datetime.timedelta(seconds=diff))
        highping = discord.Embed(title=' ', description=" ")
        highping.add_field(name=f"Ping", value=f"{(round(bot.latency * 1000))} ms", inline=True)
        highping.add_field(name=f"Servers Count", value=f"{str(len(bot. guilds))} servers", inline=True)
        highping.add_field(name=f"Uptime", value=f"{uptime} ", inline=False)
        await ctx.send(embed=highping)

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_guild=True)
    @commands.bot_has_guild_permissions()
    async def purge(self, ctx, limit: int):
        if limit < 1:
            await ctx.send("bruh its impossible to delete that many messages")
        elif limit > 500:
            await ctx.send("you can only delete 500 or less at a time")
        else:
            await ctx.channel.purge(limit=limit + 1)
            await ctx.send(f'<a:8584_verified_blue:829373373640998922> **-** ``{limit}`` **messages have been deleted**', delete_after=4)

    @commands.command()
    async def perm(self, ctx, *nums: int):
        a = ""
        values = permutations(nums)
        for i in values:
            a += str(i)+"\n"
            p = discord.Embed(title="", description=("```"+a+"```"), colour=0x467553)
            p.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar_url)
            p.set_footer(text="if its blank then you probably forgot to type the numbers")
        await ctx.send(embed=p)

    @commands.command()
    async def prefix(self, ctx):
        noy = discord.Embed(title= "", description="", color=0xffb12b)
        noy.add_field(name="ERROR - DISABLED COMMAND", value="this command is disabled", inline=False)
        await ctx.send(embed=noy)


async def setup(bot):
    await bot.add_cog(Util(bot))