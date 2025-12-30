import os
import yaml
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser

# Load environment variables from .env file
load_dotenv()

class LLMController:
    def __init__(self):
        # We replace ChatOllama with ChatGroq
        # model="llama3-8b-8192" is free, fast, and smart
        self.llm = ChatGroq(
            temperature=0, 
            model_name="openai/gpt-oss-120b",
            api_key=os.getenv("API_KEY")
        )
        
        # We need a separate instance for JSON mode because Groq handles it differently
        self.json_llm = ChatGroq(
            temperature=0, 
            model_name="openai/gpt-oss-120b",
            api_key=os.getenv("API_KEY"),
            model_kwargs={"response_format": {"type": "json_object"}} # NATIVE JSON MODE
        )

    def _load_prompt(self, filename):
        with open(f"prompts/{filename}", "r") as f:
            config = yaml.safe_load(f)
        return ChatPromptTemplate.from_template(config["template"])

    def plan_search(self, user_query):
        prompt = self._load_prompt("planner.yaml")
        
        # Use the JSON-specific LLM instance
        chain = prompt | self.json_llm | JsonOutputParser()
        
        try:
            return chain.invoke({"user_query": user_query})
        except Exception as e:
            print(f"❌ PLANNER ERROR: {e}")
            return {"search_needed": False}

    def generate_answer(self, user_query, context):
        prompt = self._load_prompt("answer_engine.yaml")
        
        # Use the standard LLM instance for text generation
        chain = prompt | self.llm | StrOutputParser()
        
        return chain.invoke({"user_query": user_query, "context": context})