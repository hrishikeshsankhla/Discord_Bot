import discord
from discord.ext import commands
from discord import app_commands
from bot import MyBot
import json

class Welcome(commands.Cog):
    def __init__(self, bot:MyBot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member:discord.Member):
        with open('./data.json', 'r') as f:
            records = json.load(f)

        try :
            channel_id = records[str(member.guild_id)]
        except KeyError:
            return
        channel = self.bot.get_channel(int(channel_id))
        if not channel:
            return 
        await channel.send(f'Welcome {member.mention}!.You are {member.guild.member_count}th membert of our server')

    @app_commands.command()
    async def welcome(self, interaction:discord.Interaction):
        with open("./data.json","r") as f:
            records = json.load(f)
        
        records[str(interaction.guild_id)] = str(interaction.channel_id)
        with open("./data.json","w") as f:
            json.dump(records, f)
        
        await interaction.response.send_message(f"Success! {interaction.channel.mention} is your welcome channel.")
    

async def setup(bot:commands.Bot):
    await bot.add_cog(Welcome(bot))


    
