#!/usr/bin/env python3
import sys
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

conn = sqlite3.connect('gods_database.db')
df = pd.read_sql_query("SELECT * from bots", conn)
plt.style.use('tableau-colorblind10')
fig, ax = plt.subplots(figsize=(8,4), dpi=144)

if sys.platform.startswith('win'):
    plt.get_current_fig_manager().window.geometry("+0+0")
elif sys.platform.startswith('linux'):
    plt.get_current_fig_manager().window.setGeometry(0, 0, 1700, 900)

fig.canvas.manager.set_window_title("The God's Dashbard of Telegram BigBang")

plt.subplots_adjust(bottom=0.1, left=0.205, right=0.945, top=0.866)

plt.xscale("symlog")
ax.xaxis.set_major_formatter(ScalarFormatter())

bar1 = ax.barh(df['bot_name'], df['events'], label="Messages gathered", height=0.5)
ax.set_ylabel("Malicious Bot Names", fontsize=5)
ax.legend(ncol=2, bbox_to_anchor=[1, 1.05], borderaxespad=0, frameon=False, fontsize='xx-small')
plt.xticks(fontsize=6)
plt.yticks(fontsize=6)

max_y_limit = max(df['id'])
if max_y_limit >= 30:
    ax.set_ylim(-0.5, 29.5)
else:
    ax.set_ylim(-0.5, max_y_limit)

ax.grid(which="major", axis='x', color='#DAD8D7', alpha=0.5, zorder=1)
ax.plot([0.205, 0.945], [.98, .98], transform=fig.transFigure, clip_on=False, color='#E3120B', linewidth=.7)
ax.add_patch(plt.Rectangle((0.205,.98), 0.04, -0.02, facecolor='#E3120B', transform=fig.transFigure, clip_on=False, linewidth = 0))

ax.text(x=0.205, y=.92, s="God's Dashboard", transform=fig.transFigure, ha='left', fontsize=14, weight='bold', alpha=.8)
ax.text(x=0.205, y=.88, s="Using malicious Telegram bots for good", transform=fig.transFigure, ha='left', fontsize=12, alpha=.8)

ax.text(x=0.212, y=0.04, s="Source: Telegram Big Bang's Database of God", transform=fig.transFigure, ha='left', fontsize=5, alpha=.7)
ax.text(x=0.212, y=0.02, s="Developed by: @avechuch0", transform=fig.transFigure, ha='left', fontsize=5, alpha=.7)
ax.text(x=0.425, y=0.02, s="Press 'p' or use the arrows icon to navigate on the chart if you have more than 30 bots monitored", transform=fig.transFigure, ha='left', fontsize=5, alpha=.7, color='#E3120B')

ax.bar_label(bar1, labels=[f'{e:,}' for e in df['events']], padding=3, color='black', fontsize=5) 

plt.rcParams["figure.autolayout"] = True
plt.show()

conn.close()