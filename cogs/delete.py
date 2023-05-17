from discord.ext import commands
from aurora_secrets import *
from aurora_lists import *
import asyncio
import discord
import random

class Delete(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cursor = bot.cursor

    @commands.command()
    async def deletemydata(self, ctx):
        dmd = discord.Embed(color=random.choice(colors))
        dmd.add_field(name="Delete your info",
                    value=f"{ctx.author.mention} ARE YOU SURE YOU WANT TO CONTINUE?\nDoing this will get rid of all your info in our database\nType ``yes`` under ``10s`` to continue with the deletion")
        await ctx.send(embed=dmd)

        def check(message):

            return ctx.author == message.author and ctx.channel == message.channel

        try:

            ans = await self.bot.wait_for('message', check=check, timeout=10)

            if ans.author == ctx.message.author:
                if ans.content.lower() == "yes":
                    self.cursor.execute(
                        "delete from users where client_id = %s", [ctx.author.id])
                    db.commit()

                    await ctx.send(f"``🟢 SUCCESSFUL - {ctx.author.name} your data has been deleted``")
                else:
                    await ctx .send(f"``🔴 NOT SUCCESSFUL - {ctx.author.name} you failed to answer correctly``")
        except asyncio.TimeoutError:
            await ctx.send(f"``🔴 NOT SUCCESSFUL - {ctx.author.name} you failed to answer in time``")


async def setup(bot):
    await bot.add_cog(Delete(bot))