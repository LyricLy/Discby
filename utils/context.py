from discord.ext import commands


class DiscbyContext(commands.Context):
    @property
    def dev(self):
        return str(self.guild.id) == self.bot.config["Dev"]["devguildid"]
