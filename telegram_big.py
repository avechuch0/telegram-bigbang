#!/usr/bin/env python3
import api_checker
import subprocess
import sys
import time
import datetime
import sqlite3
from sqlite3 import Error
from colorama import Fore, Back, Style

header = '''
___________________________________________________________________________________________________________________________________

                                                                                                     ~~~~~~~~~$
████████╗███████╗██╗     ███████╗ ██████╗ ██████╗  █████╗ ███╗   ███╗                              /~~~~~~~~~~~~~
╚══██╔══╝██╔════╝██║     ██╔════╝██╔════╝ ██╔══██╗██╔══██╗████╗ ████║                             /~~~//~~~$~~~~~~~~
   ██║   █████╗  ██║     █████╗  ██║  ███╗██████╔╝███████║██╔████╔██║                             (*/      \/~~~~~~~~~~~
   ██║   ██╔══╝  ██║     ██╔══╝  ██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║                              |__      \&)~~~~~~~~~~~$
   ██║   ███████╗███████╗███████╗╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║                              (@   )   ###~~~~~~~~~
   ╚═╝   ╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝                              |%  ) #####~~~~~~~~~~~$
                                                                       Alpha                        (** ######~/~~
        ██████╗ ██╗ ██████╗ ██████╗  █████╗ ███╗   ██╗ ██████╗           |                        /  (# ##/)      _________________
        ██╔══██╗██║██╔════╝ ██╔══██╗██╔══██╗████╗  ██║██╔════╝           |                       %|%¨ \ #~$       | By @avechuch0 |
        ██████╔╝██║██║  ███╗██████╔╝███████║██╔██╗ ██║██║  ███╗   Cyber_/:\_Deception~֊֊֊.~~~°°/        $          
        ██╔══██╗██║██║   ██║██╔══██╗██╔══██║██║╚██╗██║██║   ██║         \:/  `--~〰֊֊, 〰〰                 (\ #
        ██████╔╝██║╚██████╔╝██████╔╝██║  ██║██║ ╚████║╚██████╔╝          |          `~^֊^   ..   ,..:\          
        ╚═════╝ ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ v1.0      |             (/:|(〰~~-〰        `^
        "Bring collections of malicious bots on Telegram from          Omega            \\_%             `〰〰〰
   the depths ofdarkness to the radiance of light to annoy scammers"
___________________________________________________________________________________________________________________________________'''

big_completed = '''
 +-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+-+-+-+ 
 |B|I|G| |B|A|N|G| |C|O|M|P|L|E|T|E|D| 
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ 
 |    \    /                 \   /   | 
 |     \OO/         \    /  booooom  | 
 |     (Big)         \OO/    /   \   | 
 |      / \         (Bang)           | 
 |     /   \          /\\             | 
 |                   /  \\            | 
 |B|O|T|S| |I|N| |M|O|N|I|T|O|R|I|N|G| 
 The malicious bots are now in control 
   All of them are in listening mode
 +-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+-+
 See log file runtime_auditlog.txt
 for troubleshooting.
  
   ** Leave this terminal opened **
 Run gods_dashboard.py in other shell
 to get the telemetry of events\n '''

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def clean_database():
    conn = sqlite3.connect("gods_database.db")
    cur = conn.cursor()
    # Purge the bots' table
    cur.execute("DELETE FROM bots")
    conn.commit()
    conn.close()

def create_database():
    database = "gods_database.db"

    sql_create_bots_table = """ CREATE TABLE IF NOT EXISTS bots (
                                    id integer PRIMARY KEY,
                                    bot_name text NOT NULL,
                                    bot_token text NOT NULL,
                                    events integer
                                ); """

    conn = create_connection(database)
    if conn is not None:                
        # Create the bots table        
        create_table(conn, sql_create_bots_table)
    else:
        print("Error! Cannot create the database connection.")  

def create_table(conn, create_table_sql):
    try:
        cur = conn.cursor()
        # Check of bots' table exists
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='bots'")
        result = cur.fetchone()        
        if result:
            clean_database() # Cleaning the table on each execution
        else:
            cur.execute(create_table_sql)
    except Error as e:
        print(e)

def big_bang(bot_tokens):
    with open("runtime_auditlog.txt", "w") as log:
        log.write(str(datetime.datetime.now(datetime.timezone.utc)) + ",[NewSession],New session of Telegram-bigbang created\n")
        print("\nNew session of Telegram-bigbang created - " + str(datetime.datetime.now(datetime.timezone.utc)))
        log.close()
    tokens = open(bot_tokens, "r")        
    print("Starting...")
    bots_number = len(tokens.readlines())
    print(Fore.GREEN + "[+] Processing " + str(bots_number) + " bots" + Style.RESET_ALL)    
    tokens.close()   
    time.sleep(3)    
    os_type = True
    python_ver = ""
    if sys.platform.startswith('win'):
        os_type = True
        python_ver = "python"   
    elif sys.platform.startswith('linux'):
        os_type = False
        python_ver = "python3"

    tokens = open(bot_tokens, "r") 
    for line_number, token in enumerate(tokens):           
        process = subprocess.Popen([python_ver, 'telegram_bang.py'] + [str(token.strip()),str(line_number+1)], shell=os_type)   
        time.sleep(2)
    time.sleep(5)
    print(Fore.WHITE + big_completed.ljust(50) + Style.RESET_ALL)
    tokens.close()

    audit = open("runtime_auditlog.txt", "r")
    number_bots_error = int(len(audit.readlines())) - 1
    print(Fore.GREEN + "Bots in current monitoring by Telegram Big Bang " + str(bots_number - number_bots_error) + "\n" + Style.RESET_ALL)    
    audit.close()

def main():
    if(len(sys.argv) < 2):
        print("Usage: python3 {} telegram_bot_tokens_file".format(sys.argv[0]) + "\n")
    else:
        bots_list = sys.argv[1]        
        create_database()
        big_bang(bots_list)   

if __name__ == "__main__":
    print(Fore.WHITE + header + Style.RESET_ALL)
    if api_checker.check_config():
        main()             
    else:
        print("".ljust(2) + ":( \n  Please check the config.ini file and fill the api_id and api_hash values.")
        print("".ljust(2) + "Go to https://my.telegram.org/auth to get your Telegram's keys.")
        sys.exit(0)    
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Closing Telegram-bigbang...\n")        
        sys.exit(0)