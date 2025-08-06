import discord
from discord.ext import commands
from actions.task_runner import run_all_tasks

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def start(ctx):
    await ctx.send("🔍 Starting bug egg monitor...")
    from stock_checker.monitor import monitor
    monitor(callback=run_all_tasks)

bot.run(DISCORD_BOT_TOKEN)
