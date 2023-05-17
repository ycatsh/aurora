from discord.ext import commands
from aurora_secrets import *
from aurora_lists import *
import discord

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                join = discord.Embed(title="", description="Hello! Thanks for adding Aurora to your server 🤝️", color=0x2ea8ff)
                join.add_field(name="_ _", value="◇─────────────────────────────────◇")
                join.set_author(name="Aurora", icon_url="https://media.discordapp.net/attachments/807511480878497806/832503256118591498/Aurora.png")
                join.add_field(name="_ _", value="→ Do ``.help`` to check out all my commands and features\n_ _\n**Developer's Recommendation:**\n→ Run ``.rpg`` go on a quest, gamble and duel with friends\n→ Run ``.games`` mini games which are super fun to play\n→ Run ``.guess`` to test your knowledge on Anime/Geo/Star Wars\n_ _\n◇─────────────────────────────────◇", inline=False)
                join.add_field(name="_ _", value="[Join Aurora Support Server](https://discord.gg/G9vTrsV4aG)", inline=False)
                join.set_footer(text="Enjoy using the bot 👍 | Molecule")
                join.set_thumbnail(url="https://media.discordapp.net/attachments/807511480878497806/832503256118591498/Aurora.png")

                await channel.send(embed=join)
                
                break

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        error = getattr(error, 'original', error)

        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You can't do that :( ")

        elif isinstance(error, commands.MemberNotFound):
            error_msg = discord.Embed(title=" ", description=" ", color=0xffb12b)
            error_msg.add_field(name="Error", value="Please mention a user\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
            
            await ctx.send(embed=error_msg)

        elif isinstance(error, commands.MissingRequiredArgument):
            if ctx.command.name == "findnum":
                error_msg = discord.Embed(title=" ", description=" ", color=0xffb12b)
                error_msg.add_field(name="Error", value="please enter a valid number between 1 to 10 (not decimal)\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
                
                await ctx.send(embed=error_msg)

            elif ctx.command.name == "8ball":
                error_msg = discord.Embed(title=" ", description=" ", color=0xffb12b)
                error_msg.add_field(name="Error", value="please type down a message after the ``.8ball``\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
                
                await ctx.reply(embed=error_msg, mention_author=False)

            elif ctx.command.name == "dp":
                error_msg = discord.Embed(title=" ", description=" ", color=0xffb12b)
                error_msg.add_field(name="Error", value="please enter the number of items you want\nformat: ``.shop <item> <number>``\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
                
                await ctx.reply(embed=error_msg, mention_author=False)

            elif ctx.command.name == "hp":
                error_msg = discord.Embed(title=" ", description=" ", color=0xffb12b)
                
                error_msg.add_field(name="Error", value="please enter the number of items you want\nformat: ``.shop <item> <number>``\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
                await ctx.reply(embed=error_msg, mention_author=False)

            elif ctx.command.name == "vp":
                error_msg = discord.Embed(title=" ", description=" ", color=0xffb12b)
                error_msg.add_field(name="Error", value="please enter the number of items you want\nformat: ``.shop <item> <number>``\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
                
                await ctx.reply(embed=error_msg, mention_author=False)

            elif ctx.command.name == "slots":
                error_msg = discord.Embed(title=" ", description=" ", color=0xffb12b)
                error_msg.add_field(name="Error", value="please enter a valid amount to gamble with\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
                
                await ctx.reply(embed=error_msg, mention_author=False)

            else:
                error_msg = discord.Embed(title=" ", description=" ", color=0xffb12b)
                error_msg.add_field(name="Error", value="please enter the necessary arguments\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
                
                await ctx.send(embed=error_msg)

        elif isinstance(error, commands.CommandOnCooldown):
            if ctx.command.name == "meme":
                cool = discord.Embed(title="Slow it down", description=" ", color=0xa58fff)
                cool.add_field(name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.meme`` is ``1s``\nTry again in ``{error.retry_after:.2f}s``")
                
                await ctx.send(embed=cool)

            elif ctx.command.name == "highlow":
                cool = discord.Embed(title="Slow it down", description=" ", color=0xa58fff)
                cool.add_field(name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.highlow`` is ``10s``\nTry again in ``{error.retry_after:.2f}s``")
                
                await ctx.send(embed=cool)

            elif ctx.command.name == "anime":
                cool = discord.Embed(title="Slow it down", description=" ", color=0xa58fff)
                cool.add_field(name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.anime`` is ``5s``\nTry again in ``{error.retry_after:.2f}s``")
                
                await ctx.send(embed=cool)

            elif ctx.command.name == "geo":
                cool = discord.Embed(title="Slow it down", description=" ", color=0xa58fff)
                cool.add_field(name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.geo`` is ``5s``\nTry again in ``{error.retry_after:.2f}s``")
                
                await ctx.send(embed=cool)

            elif ctx.command.name == "sw":
                cool = discord.Embed(title="Slow it down", description=" ", color=0xa58fff)
                cool.add_field(name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.sw`` is ``5s``\nTry again in ``{error.retry_after:.2f}s``")
                
                await ctx.send(embed=cool)

            elif ctx.command.name == "shoot":
                cool = discord.Embed(title="Slow it down", description=" ", color=0xa58fff)
                cool.add_field(name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.shoot`` is ``3s``\nTry again in ``{error.retry_after:.2f}s``")
                
                await ctx.send(embed=cool)

            elif ctx.command.name == "kickball":
                cool = discord.Embed(title="Slow it down", description=" ", color=0xa58fff)
                cool.add_field(name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.kickball`` is ``3s``\nTry again in ``{error.retry_after:.2f}s``")
                
                await ctx.send(embed=cool)

            elif ctx.command.name == "bowl":
                cool = discord.Embed(title="Slow it down", description=" ", color=0xa58fff)
                cool.add_field(name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.bowl`` is ``3s``\nTry again in ``{error.retry_after:.2f}s``")
                
                await ctx.send(embed=cool)

            elif ctx.command.name == "hack":
                cool = discord.Embed(title="Slow it down", description=" ", color=0xa58fff)
                cool.add_field(name="⏪ ⏪ ⏪", value=f"don't hack people too much, Default cooldown for ``.hack`` is ``30s``\nTry again in ``{error.retry_after:.2f}s``")
                
                await ctx.send(embed=cool)

            elif ctx.command.name == "quest":
                cool = discord.Embed(title="Slow it down", description=" ", color=0xa58fff)
                cool.add_field(name="⏪ ⏪ ⏪", value=f"you have already hunted enough, Default cooldown for ``.quest`` is ``30s``\nTry again in ``{error.retry_after:.2f}s``")
                
                await ctx.send(embed=cool)

            elif ctx.command.name == "train":
                cool = discord.Embed(title="Slow it down", description=" ", color=0xa58fff)
                cool.add_field(name="⏪ ⏪ ⏪", value=f"you have already trained, Default cooldown for ``.train`` is ``45s``\nTry again in ``{error.retry_after:.2f}s``")
                
                await ctx.send(embed=cool)

            elif ctx.command.name == "dp":
                cool = discord.Embed(title="Slow it down", description=" ", color=0xa58fff)
                cool.add_field(name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.buy`` and ``.use`` is ``20s``\nTry again in ``{error.retry_after:.2f}s``")
                
                await ctx.send(embed=cool)

            elif ctx.command.name == "hp":
                cool = discord.Embed(title="Slow it down",description=" ", color=0xa58fff)
                cool.add_field(name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.buy`` and ``.use`` is ``20s``\nTry again in ``{error.retry_after:.2f}s``")
                
                await ctx.send(embed=cool)

            elif ctx.command.name == "vp":
                cool = discord.Embed(title="Slow it down",description=" ", color=0xa58fff)
                cool.add_field(name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.buy`` and ``.use`` is ``20s``\nTry again in ``{error.retry_after:.2f}s``")
                
                await ctx.send(embed=cool)

            elif ctx.command.name == "qg":
                cool = discord.Embed(title="Slow it down", description=" ", color=0xa58fff)
                cool.add_field(name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.buy`` and ``.use`` is ``20s``\nTry again in ``{error.retry_after:.2f}s``")
                
                await ctx.send(embed=cool)

            elif ctx.command.name == "eb":
                cool = discord.Embed(title="Slow it down", description=" ", color=0xa58fff)
                cool.add_field(name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.buy`` and ``.use`` is ``20s``\nTry again in ``{error.retry_after:.2f}s``")
                
                await ctx.send(embed=cool)

            elif ctx.command.name == "orb":
                cool = discord.Embed(title="Slow it down", description=" ", color=0xa58fff)
                cool.add_field(name="⏪ ⏪ ⏪", value=f"Default cooldown for this item\n``.buy`` - ``20s``\n``.use`` - ``3hr``\nTry again in ``{error.retry_after:.2f}s``")
                
                await ctx.send(embed=cool)

            elif ctx.command.name == "molecule":
                cool = discord.Embed(title="Slow it down", description=" ", color=0xa58fff)
                cool.add_field(name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.buy`` and ``.use`` is ``20s``\nTry again in ``{error.retry_after:.2f}s``")
                
                await ctx.send(embed=cool)

            elif ctx.command.name == "box":
                cool = discord.Embed(title="Slow it down",description=" ", color=0xa58fff)
                cool.add_field(name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.box`` is ``2m``\nTry again in ``{error.retry_after:.2f}s``")
                
                await ctx.send(embed=cool)

            elif ctx.command.name == "slots":
                cool = discord.Embed(title="Slow it down",description=" ", color=0xa58fff)
                cool.add_field(name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.slots`` is ``10s``\nTry again in ``{error.retry_after:.2f}s``")
                
                await ctx.send(embed=cool)

            elif ctx.command.name == "duel":
                cool = discord.Embed(title="Slow it down", description=" ", color=0xa58fff)
                cool.add_field(name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.duel`` is ``5m``\nTry again in ``{error.retry_after:.2f}s``")
                
                await ctx.send(embed=cool)

            elif ctx.command.name == "fight":
                cool = discord.Embed(title="Slow it down",description=" ", color=0xa58fff)
                cool.add_field(name="⏪ ⏪ ⏪", value=f"Default cooldown for ``.fight`` is ``30s``\nTry again in ``{error.retry_after:.2f}s``")
                
                await ctx.send(embed=cool)

        elif isinstance(error, discord.Forbidden):
            if ctx.command.name == "purge":
                error_msg = discord.Embed(title=" ", description=" ", color=0xffb12b)
                error_msg.add_field(name="Error", value="I'm missing the manage messages permission!\n_ _\n**Check the following:**\nAurora BOT Role permissions\nChannel permissions\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
                
                await ctx.send(embed=error_msg)

            else:
                error_msg = discord.Embed(title=" ", description=" ", color=0xffb12b)
                error_msg.add_field(name="Error", value="I'm missing the manage messages permission!\n_ _\n**Check the following:**\nAurora BOT Role permissions\nChannel permissions\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
                
                await ctx.send(embed=error_msg)

        elif isinstance(error, commands.CommandInvokeError):
            if ctx.command.name == "perm":
                error_msg = discord.Embed(title=" ", description=" ", color=0xffb12b)
                error_msg.add_field(name="Error", value="The output was more than 2000 characters, maybe try shortening your argument\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
                
                await ctx.send(embed=error_msg)

        elif isinstance(error, discord.HTTPException):
            if ctx.command.name == "perm":
                error_msg = discord.Embed(title=" ", description=" ", color=0xffb12b)
                error_msg.add_field(name="Error", value="The output was more than 2000 characters, maybe try shortening your argument\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
                
                await ctx.send(embed=error_msg)

        elif isinstance(error, commands.BadArgument):
            if ctx.command.name == "perm":
                error_msg = discord.Embed(title=" ", description=" ", color=0xffb12b)
                error_msg.add_field(name="Error", value="Space the numbers and try again\nSupport Server: [Join!](https://discord.gg/G9vTrsV4aG)")
                
                await ctx.send(embed=error_msg)


async def setup(bot):
    await bot.add_cog(Events(bot))