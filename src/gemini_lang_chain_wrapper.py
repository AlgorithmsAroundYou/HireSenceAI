
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

class GeminiLangChainWrapper:

    def __init__(self, prompt_template):
        load_dotenv()
        os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_GEMINI_API_KEY")
        self.model="models/gemini-1.5-pro-latest"
        
        self.llm = ChatGoogleGenerativeAI(
            model=self.model,
            temperature=0.7
        )
        self.chain = prompt_template | self.llm

    def run(self, inputs: dict) -> str:
        try:
            response = self.chain.invoke(inputs)
            return response.content
        except Exception as e:
            return f"Error: {e}"
