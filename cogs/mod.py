import discord
from discord.ext import commands
from datetime import timedelta
from discord import app_commands
from bot import MyBot

class Mod(commands.Cog):
    def __init__(self, bot:MyBot):
        self.bot = bot
    
    @app_commands.command()
    @app_commands.checks.has_permissions(kick_members=True)
    @app_commands.checks.bot_has_permissions(kick_members=True)
    async def kick(self,interaction:discord.Interaction,member:discord.Member,*,reason:str):
        """Kick a member from the server"""
        await member.kick(reason=reason)
        await interaction.response.send_message(f"{member.mention} has been kicked from the server for {reason}")
    
    @app_commands.command()
    @app_commands.checks.has_permissions(kick_members=True)
    @app_commands.checks.bot_has_permissions(kick_members=True)
    async def ban(self,interaction:discord.Interaction,member:discord.Member,*,reason:str):
        """Ban a member from the server"""
        await member.ban(reason=reason)
        await interaction.response.send_message(f"{member.mention} has been banned from the server for {reason}")

    @app_commands.command()
    @app_commands.checks.has_permissions(kick_members=True)
    async def warn(self, interaction:discord.Interaction, member:discord.Member,*,reason:str):
        """Warn a member"""
        await interaction.response.send_message(f"{member.mention} has been warned for {reason}")

    @app_commands.command()
    async def timeout(self, interaction:discord.Interaction, member:discord.Member,minutes:int,reason:str):
        """Timeout a member"""
        delta = timedelta(minutes=minutes)
        await member.timeout(delta, reason=reason)
        await interaction.response.send_message(f"{member.mention} has been timed out for {minutes} minutes for {reason}")

    @app_commands.command()
    @app_commands.checks.has_permissions(kick_members=True)
    async def dm(self, interaction:discord.Interaction, member:discord.Member,*,message:str):
        """Send a direct message to a member"""
        await member.send(message)  
        await interaction.response.send_message(f"Message sent to {member.mention}")

async def setup(bot:commands.Bot):
    await bot.add_cog(Mod(bot))


    
