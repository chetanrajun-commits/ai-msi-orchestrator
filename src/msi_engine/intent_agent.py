"""Intent Agent.

Simulates an LLM that parses a natural language request and translates it
into a structured, multi-step API workflow across the enterprise stack.
"""

from __future__ import annotations

import re

from .models import WorkflowPlan, WorkflowStep


class IntentAgent:
    def parse(self, query: str) -> WorkflowPlan:
        # Extract the employee name from the query using Regex
        # e.g., "Onboard new employee Jane Doe" -> "Jane Doe"
        name = "Unknown"
        match = re.search(r"employee\s+([A-Za-z]+\s+[A-Za-z]+)", query)
        if match:
            name = match.group(1)

        # Simulate LLM generating the multi-system API sequence
        return WorkflowPlan(
            steps=[
                WorkflowStep(
                    system="sap", 
                    action="create_employee", 
                    payload={"employee_name": name}
                ),
                WorkflowStep(
                    system="servicenow", 
                    action="create_ticket", 
                    payload={"employee_name": name}
                ),
                WorkflowStep(
                    system="salesforce", 
                    action="create_user", 
                    payload={"employee_name": name}
                )
            ]
        )
