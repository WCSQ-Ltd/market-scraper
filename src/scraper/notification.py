import discord

from scraper.settings import DISCORD_WEBHOOK_URL


def notify_user_of_hits(hits: list):
    """
    I'm too lazy to configure a bot, so we'll use webhooks for now LOL
    """
    message = []
    wh = discord.Webhook.from_url(
        DISCORD_WEBHOOK_URL,
        adapter=discord.RequestsWebhookAdapter()
    )

    for item in hits:
        msg = f'**+{item["item_level"]} {item["name"]}** is waiting to be listed at **{item["time_to_list"]}**.\n'
        message.append(msg)

    wh.send(''.join(message))
