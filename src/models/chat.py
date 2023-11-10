# src/models/chat.py
from openai import OpenAI
# from ..keys import OPENAI_API_KEY
from src.config import Config

class Chat:
    def __init__(self):
        """Initialize the Chat class."""
        self.conversation_history = []

    def get_ai_answer(self, query: str = None):
        """Generate a response to a user-inputted query using OpenAI's GPT-3.5 Turbo."""
        if not query:
            return "I'm sorry, I didn't receive any input. Could you please repeat your question?"

        if query.strip().lower() == "clear history":
            self.conversation_history.clear()
            return "Conversation history has been cleared."

        self.conversation_history.append({"role": "user", "content": query})
        
        try:
            client = OpenAI(
                # Set your API key here
                # api_key=OPENAI_API_KEY
                api_key=Config.OPENAI_API_KEY
            )

            chat_completion = client.chat.completions.create(
                messages=self.conversation_history,  # Pass the entire conversation history
                model="gpt-3.5-turbo",
            )

            message = chat_completion.choices[0].message.content
            self.conversation_history.append({"role": "assistant", "content": message})
            return message
        except Exception as e:
            print(f"An error occurred while generating a response: {e}")
            self.conversation_history.clear()
            return "There was an issue generating a response. Please try again later."


        

    # @staticmethod
    # def generate_prompt(resume, job_description, previous_cover_letter=None):
    #     """
    #     Create a prompt for the OpenAI API based on the given inputs.
    #     """
    #     # Construct a prompt that describes the task to the AI
    #     prompt = (
    #         "Create a professional cover letter based on the following information:\n"
    #         "Resume:\n"
    #         f"{resume}\n\n"
    #         "Job Description:\n"
    #         f"{job_description}\n\n"
    #     )
    #     if previous_cover_letter:
    #         prompt += f"Previous Cover Letter:\n{previous_cover_letter}\n\n"
    #     prompt += "Please write a cover letter that matches the job description, highlighting the relevant experience from the resume."

    #     return prompt

    # def generate_cover_letter(self, resume, job_description, previous_cover_letter=None):
    #     """
    #     Generate a cover letter using the OpenAI API.
    #     """
    #     prompt = self.generate_prompt(resume, job_description, previous_cover_letter)

    #     try:
    #         # Call the OpenAI API using the prompt
    #         response = openai.Completion.create(
    #             engine=Config.OPENAI_COMPLETIONS_ENGINE,
    #             prompt=prompt,
    #             max_tokens=1024,  # Adjust the number of tokens as needed
    #             api_key=Config.OPENAI_API_KEY
    #         )
    #         # Extract the generated text from the response
    #         generated_text = response.choices[0].text.strip()
    #         return generated_text
    #     except Exception as e:
    #         # If an error occurs, handle it (e.g., log the error, return a message to the user)
    #         print(f"An error occurred: {e}")
    #         return "I'm sorry, I wasn't able to generate the cover letter. Please try again later."

# Example usage:
# chat = Chat()
# cover_letter = chat.generate_cover_letter(user_resume, job_desc, previous_cover_letter)

