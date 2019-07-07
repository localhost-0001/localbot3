import discord
import config
import embeds
import splitter
import dictionaries
import copy
import sqlite3

def create(message, text, client, points=False, back=False, forward=False, done=False, exit=False):
