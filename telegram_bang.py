#!/usr/bin/env python3
from telethon import TelegramClient, events, types
from colorama import Fore, Style, Back
from telethon import errors
from tqdm import tqdm
import configparser
import datetime
import asyncio
import sqlite3
from sqlite3 import Error
import time
import sys

# Reading configs
config = configparser.ConfigParser()
config.read("config.ini")
# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
api_hash = str(api_hash)

bot = TelegramClient(str(sys.argv[1]), api_id, api_hash)
count = 0

database = "gods_database.db"

@bot.on(events.NewMessage)
async def my_event_handler(event):    
    chat = await event.get_chat()
    await event.delete()  

    if isinstance(chat, types.Channel):
        if chat.username is not None:
            print(Back.WHITE + Fore.BLACK + "Message received on channel " + Fore.GREEN + chat.title + 
            Fore.BLACK + ", channel username " + Fore.GREEN + "@" + chat.username + Fore.WHITE +
            Style.RESET_ALL + "\nTried to be posted by " + str(sys.argv[1]) + " at " + 
            str(event.date) + "\nSucessfully deleted }:)")
        else:
            print(Back.WHITE + Fore.BLACK + "Message received on chat " + Fore.GREEN + str(chat.id) + 
            Style.RESET_ALL + "\nTried to be posted by " + str(sys.argv[1]) + " at " +
            str(event.date) + "\nSucessfully deleted }:)")
    elif isinstance(chat, types.User):
        print(Back.WHITE + Fore.BLACK + "Message received on chat " + Fore.GREEN + str(chat.id) +
         Style.RESET_ALL + "\nTried to be posted by " + str(sys.argv[1]) + " at " +
         str(event.date)+ "\nSucessfully deleted }:)")    
    elif isinstance(chat, types.Chat):
        print(Back.WHITE + Fore.BLACK + "Message received on group " + Fore.GREEN + str(chat.id) +
         Style.RESET_ALL + "\nTried to be posted by " + str(sys.argv[1]) + " at " + 
         str(event.date) + "\nSucessfully deleted }:)")    
    
    global count
    count += 1
    print(Back.WHITE + Fore.BLACK + "Message catched number " + str(count) + Style.RESET_ALL + "\n")
  
    global database
    conn = create_connection(database)
    conn.execute('UPDATE bots SET events = ? WHERE bot_token = ?', (count, str(sys.argv[1])))    
    conn.commit()
    conn.close()

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def create_bot(conn, bot):
    sql = """ INSERT INTO bots(bot_name,bot_token,events)
              VALUES(?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, bot)
    conn.commit()    
    return cur.lastrowid

async def main():  
    global database
    try:
        await bot.start(bot_token = str(sys.argv[1]))        
        if await bot.is_bot():
            me = await bot.get_me()                        
            for i in tqdm(range(0, 1), desc="Reading token " + str(sys.argv[2])):
                time.sleep(1)
            print(Fore.GREEN + "[+] Succesfully added " + str(sys.argv[1]) + " (" + str(me.username) +
            ")" + Style.RESET_ALL)
            print(Fore.GREEN + "[+] Token added to the God's Database" + Style.RESET_ALL)
            #Database bots filling
            conn = create_connection(database)   
            with conn:                
                create_bot(conn, ((str(me.username), str(sys.argv[1]), 0)))                                                     
        await bot.run_until_disconnected()

    # Token expired events
    except errors.AccessTokenExpiredError as e:
        for i in tqdm(range(0, 1), desc="Reading token " + str(sys.argv[2])):
            time.sleep(1)
        print(Fore.RED + "[-] " + str(sys.argv[1]) + " " + str(e) + Style.RESET_ALL +
        "\nSee runtime_auditlog.txt for more details")
        with open('runtime_auditlog.txt', 'a') as exp_log:
            exp_log.write(str(datetime.datetime.now(datetime.timezone.utc)) + ",[Expired]," + "Token " +
            str(sys.argv[1]) + " is already expired to read and process\n")
            exp_log.close()

    # Token revoked events    
    except errors.UnauthorizedError as e:
        print(Fore.RED + str(e) + "\n" + "Token " + str(sys.argv[1]) + " (" + str(me.username) + ") " +
        "revoked by scammer at " + str(datetime.datetime.now(datetime.timezone.utc)) + Style.RESET_ALL +
        "\nSee runtime_auditlog.txt for more details")
        with open('runtime_auditlog.txt', 'a') as rev_log:
            rev_log.write(str(datetime.datetime.now(datetime.timezone.utc)) + ",[Revoked]," + "Token " +
            str(sys.argv[1]) + " revoked by the scammer")   
            rev_log.close()

asyncio.run(main())