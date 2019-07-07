import discord
import random

id = "gundam"

async def ex(args, message, client, invoke):
    embed=discord.Embed(title="Discord", url="https://discord.gg/rsaNa3x", colour=0xe74c3c)
    embed.set_author(name="LOCALBOT", url="https://discordapp.com/oauth2/authorize/?permissions=2146958591&scope=bot&client_id=421691975155056640", icon_url="https://i.imgur.com/E8GIP3I.png")
    embed.set_thumbnail(url="https://yt3.ggpht.com/-310LKwfseck/AAAAAAAAAAI/AAAAAAAAAAA/3oXd3OARMkQ/s200-mo-c-c0xffffffff-rj-k-no/photo.jpg")
    embed.add_field(name="WARNING!", value="GET BINGED", inline=True)
    embed.set_footer(text="by localthehost.")
    if random.randint(0,100) == 2:
        await client.send_message(message.channel, "<@346554178975301632>", embed=embed)
    else:
        embed=discord.Embed(title="Discord", url="https://discord.gg/rsaNa3x", colour=0xe74c3c)
        embed.set_author(name="LOCALBOT", url="https://discordapp.com/oauth2/authorize/?permissions=2146958591&scope=bot&client_id=421691975155056640", icon_url="https://i.imgur.com/E8GIP3I.png")
        embed.set_thumbnail(url="https://yt3.ggpht.com/-310LKwfseck/AAAAAAAAAAI/AAAAAAAAAAA/3oXd3OARMkQ/s200-mo-c-c0xffffffff-rj-k-no/photo.jpg")
        embed.add_field(name="WARNING!", value="You tried....", inline=True)
        embed.set_footer(text="by localthehost.")
        await client.send_message(message.channel, embed=embed)
