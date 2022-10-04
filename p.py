import discord

#insert token here
token = "TOKEN"

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.author)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
    
    if message.channel.name == 'enter channel':
        if user_message.lower() == '!hello':
            await message.channel.send(f'Hello {username}')
            return
        elif username.lower() == '!ping':
            await message.channel.send(f'Pong!')
            return
        elif user_message.lower() == '!random_number':
            response = f'random number is: {random.randrange(100010121)}'
            await message.channel.send(response)
            return

client.run(token)
