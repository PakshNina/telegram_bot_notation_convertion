import os


class Settings:
    @property
    def BOT_TOKEN(self):
        api_key = os.getenv('NINAKO_NOTATION_BOT', '')
        return os.getenv('NINAKO_NOTATION_BOT', '')
