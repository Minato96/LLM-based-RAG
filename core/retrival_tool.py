class RetrievalTool:
    def __init__(self):
        # In a real system, you would initialize FAISS/Chroma here.
        # For Project 2, we simulate the "Perfect Retrieval" to test the LLM's reasoning.
        self.mock_db = {
            "budget": "The Q3 Project Budget was approved at $1.5M. (Source: Finance_Doc_A)",
            "timeline": "The project timeline is delayed by 2 weeks due to API failures. (Source: Tech_Report_B)",
            "policy": "Remote work policy requires VPN access for all employees. (Source: HR_Policy_V2)"
        }

    def search(self, queries):
        """
        Input: List of search strings (from the Planner)
        Output: Aggregated context string
        """
        print(f"   🔍 TOOL IN USE: Searching for {queries}...")
        
        results = []
        # Simple simulation logic
        for q in queries:
            for key, content in self.mock_db.items():
                if key in q.lower():
                    results.append(content)
        
        if not results:
            return "No relevant documents found in the database."
            
        return "\n".join(results)