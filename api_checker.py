import configparser

def check_config():
    # Reading configs
    config = configparser.ConfigParser()
    config.read("config.ini")
    # Setting configuration values
    api_id = config['Telegram']['api_id']
    api_hash = config['Telegram']['api_hash']
    api_hash = str(api_hash)

    if not api_id or not api_hash:        
        return False
    else:
        return True

check_config()