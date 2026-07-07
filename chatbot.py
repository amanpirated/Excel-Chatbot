from google import genai
from config import GEMINI_API_KEY

class ChatBot:
    def __init__(self):
        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )
    def build_prompt(self, contexts, query):
        context = "\n\n".join(contexts)
        prompt = f"""
You are an HR assistant.
Answer ONLY from the context.
Context
{context}
Question
{query}
"""
        return prompt
    
    def ask(self, contexts, query):
        prompt = self.build_prompt(
            contexts,
            query
        )
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text