import re
from telegram.exceptions import UnreadablePattern


def get_numbers_from_telegram_string(conversion_string: str) -> list:
    if re.match('\d+\D+\d+\D+\d+', conversion_string):
        return re.split('\D+', conversion_string)
    if re.match('\d+', conversion_string):
        return [conversion_string, None, None]
    raise UnreadablePattern('Could not parse number')
