import cogs
import discord

from configparser import ConfigParser
from constants import info
from discord.ext import commands
from utils import bot


parser = ConfigParser()
parser.read("config.ini")

discby = bot.Discby(command_prefix=commands.when_mentioned_or("ly!"),
                    status=discord.Status.dnd,
                    cogs=cogs.get_extensions() | {"jishaku"},
                    config=parser,
                    description=info.ABOUT_TEXT)

discby.run(parser["Auth"]["token"])
