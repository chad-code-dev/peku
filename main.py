from discord.ext import commands
import keep_alive
import os
import replit


def get_prefix(client, message):

    prefixes = ['!p ']    

    if not message.guild:
        prefixes = ['!p '] 

    return commands.when_mentioned_or(*prefixes)(client, message)


bot = commands.Bot(                                         
    command_prefix=get_prefix,
    description='just peku', 
    bot_owner_id=585905964675235841,
    case_insensitive=True                      
)


cogs = ['cogs.basic','cogs.embed']


@bot.event
async def on_ready():
    replit.clear()
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    for cog in cogs:
        bot.load_extension(cog)
    return

keep_alive.keep_alive()

bot.run(os.environ.get('TOKEN'), bot=True, reconnect=True)