import discord
import config
import random

id = "ping"

async def ex(args, message, client, invoke):
    lennys = [
    "( ͡° ͜ʖ ͡°)", "( ͡° ͜ʖ ͡°)", "(☭ ͜ʖ ☭)", "(ᴗ ͜ʖ ᴗ)", "( ° ͜ʖ °)", "(⟃ ͜ʖ ⟄)", "( ‾ ʖ̫ ‾)", "(͠≖ ͜ʖ͠≖)", "( ͡° ʖ̯ ͡°)", "ʕ ͡° ʖ̯ ͡°ʔ", "( ͡° ل͜ ͡°)", "( ͠° ͟ʖ ͡°)"
    ]
    embed=discord.Embed(title="Discord", url=config.invite, color=0x2ecc71)
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
    embed.set_thumbnail(url=config.embedthumbnail)
    embed.add_field(name="Your lenny face!", value=random.choice(lennys), inline=True)
    embed.set_footer(text=config.by)
    await client.send_message(message.channel, embed=embed)
