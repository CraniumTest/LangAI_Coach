class User:
    def __init__(self):
        self.name = None
        self.language_level = None

    def setup_profile(self):
        self.name = input("Enter your name: ")
        self.language_level = input("Enter your current language proficiency level (e.g., Beginner, Intermediate, Advanced): ")
        print(f"Profile created for {self.name}, proficiency level: {self.language_level}")
