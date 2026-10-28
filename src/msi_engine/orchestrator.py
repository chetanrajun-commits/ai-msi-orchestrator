"""Orchestrator.

Wires the Intent Agent and Executor Agent into a single pipeline.
"""

from __future__ import annotations

from .executor import ExecutorAgent
from .intent_agent import IntentAgent
from .mock_apis import MockEnterpriseAPIs


class Orchestrator:
    def __init__(self) -> None:
        self.intent_agent = IntentAgent()
        self.apis = MockEnterpriseAPIs()
        self.executor = ExecutorAgent(self.apis, max_retries=3)

    def run(self, query: str) -> int:
        print(f"[ORCHESTRATOR] Received natural language query: '{query}'")
        
        # 1. Parse Intent
        print("[INTENT]       Parsing workflow plan...")
        plan = self.intent_agent.parse(query)
        print(f"[INTENT]       Generated {len(plan.steps)}-step plan.")
        
        for i, step in enumerate(plan.steps, 1):
            print(f"[INTENT]         Step {i}: {step.system.upper()} -> {step.action}")

        # 2. Execute Plan
        print("\n[EXECUTOR]     Beginning execution...")
        all_success = True
        
        for i, step in enumerate(plan.steps, 1):
            print(f"[EXECUTOR]     Executing Step {i}/{len(plan.steps)}: {step.system.upper()}")
            result = self.executor.execute_step(step)
            
            if result.success:
                print(f"[EXECUTOR]     ✅ {result.output} (Attempts: {result.attempts})")
            else:
                print(f"[EXECUTOR]     ❌ FAILED after {result.attempts} attempts: {result.output}")
                all_success = False
                break  # Stop the workflow if a critical step fails

        # 3. Conclusion
        if all_success:
            print("\n[ORCHESTRATOR] ✅ Workflow completed successfully across all systems.")
            return 0
        else:
            print("\n[ORCHESTRATOR] ❌ Workflow failed.")
            return 1
