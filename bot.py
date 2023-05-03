import discord
from discord.ext import commands

import response

token = open('token.txt', 'r').readline()
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)


async def send_message(message, user_message):
    try:
        response_for_user = response.handle_response(user_message)
        await message.channel.send(response_for_user)
    except Exception as e:
        print(e)


def run_discord_bot():
    @client.event
    async def on_message(message):
        message_content_string = str(message.content)
        if message.author == client.user or str(message.channel) != "bot":
            return

        if message_content_string[0] != '!':
            await send_message(message, message_content_string)
        else:
            await client.process_commands(message)

    @client.command(name='clear', help='this command will clear 15 msgs')
    async def clear(ctx):
        await ctx.channel.purge(limit=25)

    @client.event
    async def on_ready():
        print("Bot is running")

    client.run(token)
