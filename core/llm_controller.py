import yaml
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser

class LLMController:
    def __init__(self):
        # We use temperature=0 for strict, factual reasoning
        self.llm = ChatOllama(model="llama3", temperature=0,format="json")

    def _load_prompt(self, filename):
        with open(f"prompts/{filename}", "r") as f:
            config = yaml.safe_load(f)
        return ChatPromptTemplate.from_template(config["template"])

    def plan_search(self, user_query):
            prompt = self._load_prompt("planner.yaml")
            chain = prompt | self.llm | JsonOutputParser()
            
            try:
                return chain.invoke({"user_query": user_query})
            except Exception as e:
                # PRINT THE ERROR so we can see what happened
                print(f"❌ PLANNER ERROR: {e}") 
                return {"search_needed": False}

    def generate_answer(self, user_query, context):
        # 1. Load the "Analyst" Brain
        prompt = self._load_prompt("answer_engine.yaml")
        
        # 2. String output is fine here
        chain = prompt | self.llm | StrOutputParser()
        
        return chain.invoke({"user_query": user_query, "context": context})