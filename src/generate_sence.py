
from src.prompt_template import PromptBuilder
from src.gemini_lang_chain_wrapper import GeminiLangChainWrapper
from src.openai_lang_chain_wrapper import OpenAILangChainWrapper

class GenerateSence:

    def __init__(self):
        print("🧠 Generating hiring scene...")
        self.prompt = PromptBuilder.jd_resume_match_prompt()
        self.gemini = GeminiLangChainWrapper(self.prompt)
        self.openai = OpenAILangChainWrapper(self.prompt)     

    def generate_hire_sence(self, resumeContent, job_description):
        """Generate a hiring scene based on job description and resume."""
        inputs = {}
        inputs["job_description"] = job_description
        inputs["resume"] = resumeContent        
        # Generate the hiring scene
        result = self.openai.run(inputs)
        return result
        #print("🧠 Hiring scene generated successfully!")