import discord
import time
from discord.ext import commands

class customDC:
    def __init__(self, bot):
        self.bot = bot
		
    @commands.command()
    async def mine(self, ctx):
        for i in range(10):
            await ctx.message.edit(content='!mine')
            time.sleep(61)
def setup(bot):
    bot.add_cog(T3CHCmds(bot))
