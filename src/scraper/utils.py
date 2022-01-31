from scraper.constants import BDOCODEX_ITEM_URL


def build_bdo_codex_item_url(item_game_id: str) -> str:
    return f'{BDOCODEX_ITEM_URL}{item_game_id}/'


def sanitize_result_msg(resultMsg: str) -> list:
    """
    Converts response from API into a more readable list of data

    :param resultMsg: The `resultMsg` property of the API response
    """
    resultMsg = resultMsg.split('|')
    return [[int(s) for s in line.split('-') if len(s)] for line in resultMsg if len(line) > 0]
