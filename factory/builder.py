from chatterbot import ChatBot


def build_chatbot() -> ChatBot:
    """Builds the chatbot."""
    return ChatBot(
        'TerminalBot',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri='sqlite:///db.sqlite3'
    )
