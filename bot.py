import discord
from discord.ext import commands
import config
from datetime import timedelta

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!",intents=intents)

@bot.event
async def on_ready():
   
    await bot.load_extension('cogs.mod')
    print("Moderation cog loaded")
    print('Bot is ready')
    await bot.tree.sync()

@bot.event
async def on_message(msg: discord.Message):
    content = msg.content
    if not msg.channel.id == 1264976698496254075:
        print('Wrong channel')
        return 

    if content =="hello":
        await msg.reply("hi!")
    
    await bot.process_commands(msg)

@bot.event
async def on_guild_channel_create(channel:discord.abc.GuildChannel):
    print('Channel created')
    print(channel.name)



@bot.event
async def on_guild_role_create(role:discord.Role):
    print('Role created')
    print(role.name)

@bot.event
async def on_guild_role_delete(role:discord.Role):
    print('Role deleted')
    print(role.name)



@bot.tree.command()
async def ping(interaction: discord.interactions):
    await interaction.response.send_message("Pong!",ephemeral = True)

@bot.tree.command()
async def embed(inter:discord.Interaction,title:str,message:str):
    embed = discord.Embed(title=title,description=message,color=0x00FFB3)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/1264976698496254075/1277566656855412796/856151dc-93d5-4dd5-bfe3-d9ac680a48e1.jpeg?ex=66cda22b&is=66cc50ab&hm=7f2b79921fcd4fd3aa189b8e5e715726b3e9fb3419b6262f7cde13a480aa3842&"
    )
    embed.set_image(
        url="https://cdn.discordapp.com/attachments/1264976698496254075/1277565405333819494/2997.jpg?ex=66cda100&is=66cc4f80&hm=3734f03479bf92d5569e1516de3ba7031e5e89dd5e975567329727664d454873&"
    )
    embed.set_footer(
        text="Footer Message",
        icon_url=""
    )
    embed.add_field(name="Field 1",value="Value 1",inline=True)
    embed.add_field(name="Field 2",value="Value 2",inline=True)
    embed.add_field(name="Field 3",value="Value 3",inline=True)

    await inter.response.send_message(embed=embed,ephemeral=True)

@bot.tree.command()
@commands.has_permissions(manage_messages=True)
@commands.bot_has_permissions(manage_messages=True)
async def clear(interaction:discord.Interaction,amount:int):
    await interaction.response.defer(thinking=True,ephemeral=True)
    await interaction.channel.purge(limit=amount)
    await interaction.followup.send(f"Deleted {amount} messages.",ephemeral=True)


@clear.error
async def on_error(interactions:discord.Interaction,error:commands.CommandError):
    if isinstance(error,commands.MissingPermissions):
        await interactions.response.send_message(
            "You don't have the required permissions to use this command.",ephemeral=True
            )
    elif isinstance(error,commands.BotMissingPermissions):
        await interactions.response.send_message(
            "I don't have the required permissions to use this command.",ephemeral=True
        )   











bot.run(config.DISCORD_TOKEN)
