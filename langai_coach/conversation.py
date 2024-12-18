import openai

class ConversationPractice:
    def __init__(self, user):
        self.user = user
        openai.api_key = 'your-api-key'

    def start_session(self):
        prompt = input("Enter a topic to start a conversation: ")
        response = self.generate_response(prompt)
        print(f"\nAI: {response}")

    def generate_response(self, prompt):
        try:
            completion = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=100
            )
            return completion.choices[0].text.strip()
        except Exception as e:
            print(f"Error generating response: {e}")
            return "Sorry, there was an error processing your request."
