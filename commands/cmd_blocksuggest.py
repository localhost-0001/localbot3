import discord
import config
import excon
import sqlite3


conn = sqlite3.connect('sql.db')
c = conn.cursor()
id = "bdo"

perm = 4

async def ex(args, message, client, invoke):
    c.execute("SELECT * FROM bans WHERE id = '%s'" % (message.mentions[0].id))

    row = c.fetchone()

    if not row:
        sql = "INSERT INTO bans (id, banned) VALUES ('%s', '1')" % (message.mentions[0].id)
    else:
#        bans = bans.decode("utf-8")
        sql = "UPDATE bans SET banned = 1 WHERE id = '%s'" % (message.mentions[0].id)

    c.execute(sql)
    conn.commit()
    conn.close()
    await client.send_message(message.channel, "Well, end of file reached")
