import discord
import config
import excon
import sqlite3

id = "bdo"



perm = 4

async def ex(args, message, client, invoke):
    conn = sqlite3.connect('sql.db')
    c = conn.cursor()
    c.execute("SELECT * FROM bans WHERE id = '%s'" % (message.mentions[0].id))

    row = c.fetchone()

    if not row:
        sql = "INSERT INTO bans (id, banned) VALUES ('%s', '0')" % (message.mentions[0].id)
    else:
#        bans = bans.decode("utf-8")
        sql = "UPDATE bans SET banned = 0 WHERE id = '%s'" % (message.mentions[0].id)

    c.execute(sql)
    conn.commit()
    conn.close()
    await client.send_message(message.channel, "Well, end of file reached")
