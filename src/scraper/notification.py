from datetime import datetime

import discord

from scraper.settings import DISCORD_WEBHOOK_URL

wh = discord.Webhook.from_url(
    DISCORD_WEBHOOK_URL,
    adapter=discord.RequestsWebhookAdapter()
)


def notify_channel_of_hits(hits: list):
    """
    I'm too lazy to configure a bot, so we'll use webhooks for now LOL
    """
    message = []

    for item in hits:
        msg = f'**+{item["item_level"]} {item["name"]}** is waiting to be listed at **{item["time_to_list"]}**.\n'
        message.append(msg)

    wh.send(''.join(message))


def notify_channel_heartbeat(run_count: int):
    wh.send(f'Heartbeat check, runs: {run_count}')
