import random
import discord
from discord.ext import commands
from src.signature import signmeC, signallC


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot: bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="Liste des commandes :", color=0x3498db)
        embed.add_field(name="quote", value="dit une citation", inline=False)
        embed.add_field(name="ping", value="ping le bot", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong")

    @commands.command()
    async def quote(self, ctx):
        quotes = open("data/quotes.txt", "r").readlines()
        choice = random.randint(0, len(quotes) - 1)
        await ctx.send(quotes[choice])

    @commands.command()
    async def signall(self, ctx):
        await signallC(ctx)

    @commands.command()
    async def signme(self, ctx):
        await signmeC(ctx)


async def setup(bot):
    await bot.add_cog(Commands(bot))
