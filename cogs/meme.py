from discord.ext import commands
from aurora_secrets import *
from aurora_lists import *
import discord
import random

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


class Meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def meme(self, ctx):
        if not hasattr(self.bot, 'nextMeme'):
            self.bot.nextMeme = getmeme()

        name, url = self.bot.nextMeme
        embed0 = discord.Embed(title=name, color=random.choice(colors))
        embed0.set_image(url=url)

        await ctx.send(embed=embed0)

        self.bot.nextMeme = getmeme()


async def setup(bot):
    await bot.add_cog(Meme(bot))