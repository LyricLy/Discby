import discord
import subprocess

from discord.ext import commands
from constants import info


class Meta:
    """Commands related to the bot itself."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def about(self, ctx):
        embed = discord.Embed(name=f"About {info.NAME}", description=info.ABOUT_TEXT)
        embed.add_field(name="Author", value=f"[{info.AUTHOR}]({info.AUTHOR_LINK})")
        embed.add_field(name="GitHub", value=info.GITHUB_LINK)
        embed.set_footer(text=f"{info.NAME} v{info.VERSION}")
        await ctx.send(embed=embed)

    async def on_message(self, message):
        if str(message.id) == self.bot.config["Dev"]["updatetrigger"]:
            subprocess.call(["git", "pull"])


def setup(bot):
    bot.add_cog(Meta(bot))
