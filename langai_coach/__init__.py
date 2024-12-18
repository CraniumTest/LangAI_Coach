from .curriculum import Curriculum
from .conversation import ConversationPractice
from .user import User

class LangAICoach:
    def __init__(self):
        self.user = User()

    def start(self):
        print("Welcome to LangAI Coach!")
        self.user.setup_profile()

        curriculum = Curriculum(self.user)
        conversation = ConversationPractice(self.user)

        while True:
            choice = input("\nChoose an option: \n1. View Curriculum \n2. Practice Conversation \n3. Exit\n")
            if choice == '1':
                curriculum.display_path()
            elif choice == '2':
                conversation.start_session()
            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
