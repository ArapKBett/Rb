import discord
from discord.ext import commands
from config import DISCORD_BOT_TOKEN, SEND_TO, CHANNEL_ID, ADMIN_USER_ID
from actions.task_runner import run_all_tasks

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

async def send_update(msg: str):
    if SEND_TO == "channel":
        channel = bot.get_channel(CHANNEL_ID)
        if channel:
            await channel.send(msg)
    elif SEND_TO == "dm":
        user = await bot.fetch_user(ADMIN_USER_ID)
        if user:
            await user.send(msg)

@bot.event
async def on_ready():
    print(f"✅ Bot logged in as {bot.user}")
    await send_update("🤖 Bot is now online and ready.")

@bot.command()
async def start(ctx):
    await send_update("🔍 Starting Bug Egg monitor...")
    
    from stock_checker.monitor import monitor

    def callback():
        import asyncio
        asyncio.run_coroutine_threadsafe(send_update("🐣 Bug Egg is in stock! Running automation..."), bot.loop)
        run_all_tasks()
        asyncio.run_coroutine_threadsafe(send_update("✅ All tasks completed."), bot.loop)

    monitor(callback=callback)
