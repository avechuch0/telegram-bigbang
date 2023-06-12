[![Actively Maintained](https://img.shields.io/badge/Maintenance%20Level-Actively%20Maintained-green.svg)](https://gist.github.com/cheerfulstoic/d107229326a01ff0f333a1d3476e068d)

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/avechuch0)

![pic](https://github.com/avechuch0/telegram-bigbang/blob/main/images/header.png)
# Telegram-Bigbang
*"Bring collections of malicious bots on Telegram from the depths of darkness to the radiance of light to annoy scammers"*

This is just an extension of the fifth use case designed for my other tool https://github.com/avechuch0/telegram-hitbackscammer/. This new tool monitors your collections of malicious Telegram bots that are the part of Phishing kits, once a victim trips into the Phishing trap, deletes the stolen data, resulting in annoyance of cyberthreat actors and prevents a fraud/data leakage likelihood.

# How it works
"Elementary, my dear Watson"... the program reads a list of malicious Telegram bots you feed, and puts all of them in listening mode using the Telegram API to prevent data theft and mitigate fraud.

### This is the analogy
*"An instance of **Big** creates an instance of **Bang** for **each bot** to be monitored. It creates a collection of bots actively listening for any information send by a victim of different Phishing campaigns, and delete it immediately, screwing up attackers' intentions".*

* You just need to fill the "bot_tokens_list.txt" or any other file you want with malicious Telegram bot tokens (One per line). The more tokens you have, the more people you protect.
* And then run ```python3 .\telegram_big.py bot_tokens_list.txt```

To get the telemetry of events, or to put it simply, how many people you have saved with this program, you can run the "God's Dashboard" - a bar's chart which presents the events gathered and deleted by each bot under your control.
* To run the God's Dashboard, in other terminal use ```python3 .\gods_dashboard.py```

### How the God's Dashboard looks
This chart has been designed to  check and visually display the events gathered by each bot after running the "Big Bang." The data is retrieved from the "God's Database", a sqlite3 database designed to store the events.

```python3 .\gods_dashboard.py```

![pic](https://github.com/avechuch0/telegram-bigbang/blob/main/images/chart_example.png)

# Requirements
* Python 3 - Use the the latest or a recent version
* Internet Connection (You are going to interact with Telegram's servers)

# Getting started
1. Download / clone the repo
2. Install required packages: ```pip3 install -r requirements.txt``` or ```pip install -r requirements.txt``` 
3. Get the Telegram API keys (api_id and api_hash) following the instructions here: https://core.telegram.org/api/obtaining_api_id
4. Set the API keys in your config.ini file
5. Take the bot_tokens_list.txt or any other file and fill with the malicious Telegram bot tokens (one per line)found on Phishing campaigns, threat hunting/intelligence activities, and other stuff linked to combat cybercrime in Telegram.
6. You're ready to go, run the main script ```python3 .\telegram-big.py bot_tokens_list.txt``` for Linux or ```python .\telegram-big.py bot_tokens_list.txt``` if you use Windows. Note that you can use any file filled by Telegram bot tokens, I left the one in the project just to help you :)

# Please read this carefully
When you run the tool, take into account the following. A Python thread would be created for each Telegram's token in your list used to run telegram-big.py, so **this tool would consume a considerable RAM memory space if you want to monitor hundreds/thousands of bots**. The amount of memory space required is not excessive, but I want to bring this to your attention, especially if you have a significant number of bots. Please proceed with caution by monitoring the RAM levels carefully.


In *NIX systems, after stopping a program using Ctrl-C or by closing the Terminal, wipe manually the RAM to ensure the memory is cleared. Supposing there are no other Python3 scripts running, use the following command in Ubuntu flavors (e.g., Kali Linux) to clean the RAM:

```killall python3```

If you want to see the different instances created by telegram-big.py:

```ps aux | grep python3```

After killing all the processes, you should not see the threads created by this tool at time of execution.

# The role of this tool in the cybersecurity landscape
This software, along with telegram-hitbackscammer, is a response from a "blue perspective" to address the increasing abuse of Telegram by threat actors for Phishing campaigns in the evolving landscape. For more information about this trend, see the following studies articles:
* **Abuse of Telegram Bots Rises 800% in 2022** - https://cofense.com/blog/abuse-telegram-bots-rises-800/
* **Malicious email campaigns abusing Telegram bots rise tremendously in Q1 2023, surpassing all of 2022 by 310%** - https://cofense.com/blog/malicious-email-campaigns-abusing-telegram-bots-rise-tremendously-in-q1-2023-surpassing-all-of-2022-by-310/

# FAQ
### 1. Is my identity would be pwned, or found by the scammer/phisher?

Nope, the attackers won't have any information about you. Remember, you are using their own bot for all operations; on the other hand, the communication takes place between the bot and Telegram through the API.

### 2. On which operating systems can this tool run?

Any system (Win/*NIX). You only need Python3 and the requirements of the tool to run it.

### 3. How to find malicious Telegram bots?

Well, this entirely depends on your phishing/smishing analysis skills, intelligence, and threat hunting approaches. This tool is designed to assist various roles in the infosecurity space, including individuals and companies that are exposed to the current Telegram phishing ecosystem, in disrupting malicious operations until takedown measures are implemented.

Hope this tool can help you, as the trend of cyber attacks with abusing Telegram Bots will still be rising in 2023.

# Contact
Twitter: [@avechuch0](https://twitter.com/avechuch0)