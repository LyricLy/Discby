# -*- coding: future_fstrings -*-

import aiohttp
import asyncio
import discord

from discord.ext import commands
from utils import context


class Discby(commands.Bot):
    def __init__(self, config, cogs=set(), *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.needed_extensions = cogs
        self.loaded_extensions = set()
        self.config = config
        self.session = aiohttp.ClientSession(loop=self.loop)
        self.loop.create_task(self.load_extensions(cogs))

    async def on_message(self, message):
        ctx = await self.get_context(message, cls=context.DiscbyContext)
        if self.config["Dev"].getboolean("devonly") and not ctx.dev:
            return
        await self.invoke(ctx)

    async def on_ready(self):
        print("Ready!")
        await self.wait_until_loaded()
        await self.change_presence(status=discord.Status.online)
        print("-----------------")

    async def on_connect(self):
        print(f"Connected as {self.user} (ID: {self.user.id})")
        await self.wait_until_loaded()
        await self.change_presence(status=discord.Status.idle)

    async def on_resume(self):
        await self.wait_until_loaded()
        await self.change_presence(status=discord.Status.online)

    async def load_extensions(self, extensions):
        for extension in extensions:
            await asyncio.sleep(0)
            try:
                self.load_extension(extension)
            except Exception as e:
                print(f'Error loading {extension}: "{type(e).__name__}: {e}"')
            else:
                self.loaded_extensions.add(extension)
        print("Loaded all extensions")

    async def wait_until_loaded(self):
        while self.needed_extensions < self.loaded_extensions:
            await asyncio.sleep(0)
