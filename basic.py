from discord.ext import commands
from datetime import datetime as d


class Basic(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='ping',
        description='The ping command',
        aliases=['p']
    )
    async def test_command(self, ctx):
        start = d.timestamp(d.now())


        msg = await ctx.send(content='Pinging')

        await msg.edit(content=f'Pong!\nOne message round-trip took {(d.timestamp(d.now())-start) * 1000}ms.')

        return

class Basic(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='beer',
        description='The beer command',
        aliases=['b']
    )
    async def test_command(self, ctx):
        start = d.timestamp(d.now())


        msg = await ctx.send(content='Using brain power')

        await msg.edit(content=f'I am not your slave')

        return

    @commands.command(
        name='say',
        description='The say command',
        aliases=['repeat', 'parrot'],
        usage='<text>'
    )
    async def say_command(self, ctx):
        msg = ctx.message.content

        prefix_used = ctx.prefix
        alias_used = ctx.invoked_with
        text = msg[len(prefix_used) + len(alias_used):]

        if text == '':

            await ctx.send(content='You need to specify the text!')

            pass
        else:

            await ctx.send(content=f"**{text}**")

            pass

        return


def setup(bot):
    bot.add_cog(Basic(bot))