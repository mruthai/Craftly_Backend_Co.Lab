# from openai import OpenAI


# Class Letter:
#     def __init__(self):
#         self.resume = []

#     def generate_prompt(resume, job_description, previous_cover_letter=None):
#         """
#         Create a prompt for the OpenAI API based on the given inputs.
#         """
#         # Construct a prompt that describes the task to the AI
#         prompt = (
#             "Create a professional cover letter based on the following information:\n"
#             "Resume:\n"
#             f"{resume}\n\n"
#             "Job Description:\n"
#             f"{job_description}\n\n"
#         )
#         if previous_cover_letter:
#             prompt += f"Previous Cover Letter:\n{previous_cover_letter}\n\n"
#         prompt += "Please write a cover letter that matches the job description, highlighting the relevant experience from the resume."

#         return prompt

#     def generate_cover_letter(self, resume, job_description, previous_cover_letter=None):
#         """
#         Generate a cover letter using the OpenAI API.
#         """
#         prompt = self.generate_prompt(resume, job_description, previous_cover_letter)

#         try:
#             # Call the OpenAI API using the prompt
#             response = openai.Completion.create(
#                 engine=Config.OPENAI_COMPLETIONS_ENGINE,
#                 prompt=prompt,
#                 max_tokens=1024,  # Adjust the number of tokens as needed
#                 api_key=Config.OPENAI_API_KEY
#             )
#             # Extract the generated text from the response
#             generated_text = response.choices[0].text.strip()
#             return generated_text
#         except Exception as e:
#             # If an error occurs, handle it (e.g., log the error, return a message to the user)
#             print(f"An error occurred: {e}")
#             return "I'm sorry, I wasn't able to generate the cover letter. Please try again later."

# Example usage:
# chat = Chat()
# cover_letter = chat.generate_cover_letter(user_resume, job_desc, previous_cover_letter)

