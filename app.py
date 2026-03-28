import time
import json

class EcoFlowAI:
    def __init__(self):
        self.laws_database = {
            "Regulation_42B": "Energy diversion must prioritize residential zones during peak hours (6 PM - 10 PM).",
            "Carbon_Limit_2026": "Industrial CO2 emissions cannot exceed 500kg per hour in urban sectors."
        }

    def analyst_agent(self, sensor_data):
        print("\n🔍 [Analyst Agent]: Scanning IoT Data feeds (UCI Smart Grid)...")
        time.sleep(1.5)
        # Logic to detect peak load
        if sensor_data['grid_load'] > 90:
            return {"status": "CRITICAL", "issue": "Grid Overload", "recommendation": "Divert 50MW from Industrial to Residential"}
        return {"status": "NORMAL", "issue": None, "recommendation": "Maintain flow"}

    def strategy_agent(self, proposal):
        print("⚖️  [Strategy Agent]: Accessing RAG Database for Environmental Law Compliance...")
        time.sleep(1.5)
        
        # Simulated RAG check against "Regulation_42B"
        applied_law = self.laws_database["Regulation_42B"]
        print(f"📖 [RAG Match Found]: {applied_law}")
        
        if "prioritize residential" in applied_law.lower():
            return {
                "decision": "APPROVED",
                "action_plan": f"Execute: {proposal['recommendation']}",
                "audit_trail": f"Validated against Regulation_42B. Priority: Residential."
            }
        return {"decision": "DENIED", "reason": "Policy mismatch"}

# --- RUNNING THE SYSTEM ---
if __name__ == "__main__":
    eco_system = EcoFlowAI()
    
    # Mock IoT Data Input
    current_metrics = {"grid_load": 95, "co2_level": 420}
    
    print("=== EcoFlow AI: Urban Sustainability Command Center ===")
    
    # Step 1: Analysis
    analysis = eco_system.analyst_agent(current_metrics)
    
    # Step 2: Strategy & Compliance Check
    if analysis['status'] == "CRITICAL":
        final_output = eco_system.strategy_agent(analysis)
        
        print("\n--- FINAL AGENTIC OUTPUT ---")
        print(f"Decision: {final_output['decision']}")
        print(f"Action: {final_output['action_plan']}")
        print(f"Audit Trail: {final_output['audit_trail']}")