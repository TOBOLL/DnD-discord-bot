import discord
import response


async def send_message(message, user_message):
    try:
        response_for_user = response.handle_response(user_message)
        await message.channel.send(response_for_user)
    except Exception as e:
        print(e)


def run_discord_bot():
    token = open('token.txt', 'r').readline()
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_message(message):
        if message.author == client.user or str(message.channel) != "bot":
            return

        await send_message(message, str(message.content))

    @client.event
    async def on_ready():
        print("Bot is running")

    client.run(token)
