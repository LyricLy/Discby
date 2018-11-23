import discord
import io

from discord.ext import commands
from PIL import Image


class Fun:
    """Random commands for fun."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hotornot(self, ctx, member: discord.Member = None):
        """Returns if something is hot, or not."""
        member = member or ctx.author
        url = member.avatar_url_as(format="png")
        async with self.bot.session.get(url) as resp:
            raw = await resp.read()
        img = Image.open(io.BytesIO(raw))
        data = img.convert("HSV").getdata(2)  # only the value

        heat = ((sum(data) / len(data)) / 255) * 10
        bar = "🔥" * int(heat) + "⬛" * (10 - int(heat))

        embed = discord.Embed(title="Not" if heat < 5 else "Hot", description=" ".join(bar))
        embed.set_footer(text=f"{heat:.2f} / 10")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Fun(bot))
