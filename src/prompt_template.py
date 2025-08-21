
from langchain_core.prompts import ChatPromptTemplate

class PromptBuilder:

    @staticmethod
    def default_prompt():
        return ChatPromptTemplate.from_template(
            "You are a helpful assistant.\n\nQuestion: {question}"
        )
    
    @staticmethod
    def system_prompt():
        return """You are an AI assistant designed to help with HR recruitment and talent evaluation tasks.
                Your role is to analyze job descriptions and resumes, identify matches, and provide insights on candidate suitability.
                You should focus on skills, experience, and qualifications relevant to the job description.
                Always provide clear and concise recommendations based on the analysis.
                """

    @staticmethod
    def jd_resume_match_prompt():
        return ChatPromptTemplate.from_messages(
            [
            ("system", PromptBuilder.system_prompt()),
            ("human", """
            1. list all the skills in the job description
            2. list all the skills in the resume
            3. identify exact matches in skills or experience
            4. infer skills if they are implied through certifications or job roles
            5. list missing critical skills from the job description
            6. give a match percentage and short summary recommendation 

Job Description:
{job_description}

Resume:
{resume}

Instructions:
- Identify exact matches in skills or experience.
- Infer skills if they are implied through certifications or job roles.
- List missing critical skills from the job description.
- Give a match percentage and short summary recommendation.

Stricky provide the output in the following format:
Now, provide the result in this format:
Matched Skills:
Implied Skills:
Missing Skills:
Match Percentage:
Summary:
    """)]
        )