from chatterbot import ChatBot
from domain.train import get_bot_response


def run_terminal_chat(chatbot: ChatBot):
    """It initiates the cli session to interact with the chatbot."""
    print("Type 'exit' to end the conversation.")
    while True:
        try:
            user_input = input("user: ")
            if user_input.strip().lower() == 'exit':
                print("bot: Take care Bye!")
                break
            response = get_bot_response(chatbot, user_input)
            print(f"bot: {response}")
        except (KeyboardInterrupt, EOFError):
            print("\nbot: Conversation ended.")
            break
