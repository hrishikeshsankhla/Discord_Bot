import discord
from discord.ext import commands
import config


exts = [
    "cogs.mod",
    "cogs.welcomer"
]

class MyBot(commands.Bot):
    def __init__(self, command_prefix:str,intents:discord.Intents,**kwargs):
        super().__init__(command_prefix,intents=intents,**kwargs)

    async def setup_hook(self):
        for ext in exts:
            await self.load_extension(ext)
            print(f"{ext[5:]} cog loaded")

        await self.tree.sync()


    async def on_ready(self):
        print('Bot is ready')

        

if __name__ == "__main__":
    bot = MyBot(command_prefix="!",intents=discord.Intents.all())

    bot.run(config.DISCORD_TOKEN)
        


    






