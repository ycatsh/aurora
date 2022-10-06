from discord.ext import commands 
import discord
import random
from aurora_lists import colors
import praw 

reddit = praw.Reddit(client_id = "id", client_secret= "secret", username = "your_username", password = "your password", user_agent = "your_useragent", check_for_async=False)

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix = ".", case_insensitive=True, intents=intents)

class Meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command(pass_context=True)
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def meme(self, ctx):
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


async def setup(bot):
    await bot.add_cog(Meme(bot))

