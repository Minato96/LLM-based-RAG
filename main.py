from core.llm_controller import LLMController
from core.retrival_tool import RetrievalTool

def run_reasoning_engine():
    # 1. Initialize Components
    brain = LLMController()
    tools = RetrievalTool()
    
    print("🤖 AI Reasoning Engine Initialized. (Type 'exit' to quit)")
    
    while True:
        query = input("\nUser: ")
        if query.lower() == "exit": break
        
        # --- STAGE 1: PLANNING ---
        print("   🧠 Analyzing query...")
        plan = brain.plan_search(query)
        
        if plan.get("search_needed"):
            # --- STAGE 2: TOOL EXECUTION ---
            search_terms = plan["queries"]
            context = tools.search(search_terms)
            
            # --- STAGE 3: REASONING ---
            print("   🤔 Reading documents and reasoning...")
            answer = brain.generate_answer(query, context)
            
            print(f"\n{answer}")
        else:
            print("   🤖 I can answer that directly: Hello! How can I help with your project?")

if __name__ == "__main__":
    run_reasoning_engine()