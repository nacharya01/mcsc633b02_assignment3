from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


def train_chatbot_with_corpus(chatbot: ChatBot):
    """Trains the chatbot using the English corpus."""
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train("chatterbot.corpus.english")
    trainer.train("chatterbot.corpus.english.greetings")
    trainer.train("chatterbot.corpus.english.conversations")


def get_bot_response(chatbot: ChatBot, user_input: str) -> str:
    """Returns a response from the bot for a given user input."""
    return str(chatbot.get_response(user_input))
