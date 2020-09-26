import discord
from discord.ext import commands
import random
import bs4
import requests

client = commands.Bot(command_prefix=".")  # instance of Bot


@client.event  # the bot detects a specific activity. This happens when the user does something. NOT a direct interaction with the bot itself
async def on_ready():
    print("bot is ready")


@client.event
async def on_member_join(member):
    print(f"{member} has joined a server")


@client.event
async def on_member_remove(member):
    print(f"{member} has left a server")


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")


@client.command(aliases=["8ball"])
async def _8ball(ctx, *, question):
    response = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]

    await ctx.send(f"Question: {question}\nAnswer: {random.choice(response)}")


@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


# def remove(string):
#    return string.replace(" ", "+")


@client.command()
async def opgg(ctx, *, sum_name):

    replace_sum = sum_name.replace(" ", "+")
    res = requests.get("https://euw.op.gg/summoner/userName=" + replace_sum)
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    elems = soup.select(
        "#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose")

    res = elems[0].text.strip()

    await ctx.send(f"{res}")

    # Discord Token
client.run("")
