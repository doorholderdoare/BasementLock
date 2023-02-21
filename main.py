import json
import discord
from discord.ext import commands
from discord import app_commands
from typing import Optional

with open('config.json', 'r') as f:
    config = json.load(f)

class abot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False

    async def on_ready(self):
        await tree.sync(guild=discord.Object(id=1071022755241279498))
        self.synced = True
        print('Bot is ready')

    async def on_member_join(self, member):
        print(f"{member.display_name} has joined the server")
        role = discord.utils.get(member.guild.roles, id=1074434567139754104)
        await member.add_roles(role)

bot = abot()
tree = app_commands.CommandTree(bot)
guild = guild=discord.Object(id=1071022755241279498)

@tree.command(name='nick', description='testing the bot', guild=guild)
@app_commands.checks.has_permissions(manage_nicknames=True)
async def self(interaction: discord.Interaction, member:discord.Member, *, nickname: Optional[str]):
    await member.edit(nick=nickname)
    await interaction.response.send_message(f'Changed nickname to {member.display_name}', ephemeral=True)


# @tree.command(name='bw', description='Bedwars Stats', guild=guild)
# async def self(interaction: discord.Interaction, ign:str):
    


@tree.error
async def on_app_command_error(interaction, error):
    if isinstance(error, app_commands.MissingPermissions):
        await interaction.response.send_message(error, ephemeral=True)
    else: raise error


bot.run(config['token'])