from infrastructure.setup import setup_django_environment
from factory.builder import build_chatbot
from domain.train import train_chatbot_with_corpus
from interface.cli import run_terminal_chat


def main():
    setup_django_environment()
    chatbot = build_chatbot()
    train_chatbot_with_corpus(chatbot)
    run_terminal_chat(chatbot)


if __name__ == "__main__":
    main()
