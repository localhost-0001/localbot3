import discord
import config

id = "faq"

async def ex(args, message, client, invoke):
    embed=discord.Embed(title="Discord", url=config.invite, colour=0xe74c3c)
    embed.set_author(name=config.name, url=config.botinv, icon_url=config.leftlogoembed)
    embed.set_thumbnail(url=config.embedthumbnail)
    embed.add_field(name="WARNING!", value="PLEASE READ THE FAQ AND RULES", inline=True)
    embed.set_footer(text="by raidrix.")
    await client.send_message(message.channel, embed=embed)
