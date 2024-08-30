import discord
from discord.ext import commands
from discord import app_commands
from bot import MyBot

class ErrorCog(commands.Cog):
    def __init__(self, bot:MyBot):
        self.bot = bot

    async def on_app_command_error(
            self, interaction:discord.Interaction,error: app_commands.AppCommandError
    ):
        ...

    @commands.Cog.listener()
    async def on_command_error(
        self, ctx:commands.Context,error:commands.CommandError
    ):
        if isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send(f"Missing required argument - (error.param.name)")
    


async def setup (bot:commands.Bot):
    await bot.add_cog(ErrorCog(bot))