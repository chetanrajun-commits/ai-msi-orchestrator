"""Mock Enterprise APIs.

Simulates a multi-vendor stack (SAP, ServiceNow, Salesforce). 
To demonstrate resilience, the ServiceNow mock is programmed to fail once
with a 503 Service Unavailable to test the Executor's retry logic.
"""

from __future__ import annotations

from typing import Any


class MockEnterpriseAPIs:
    def __init__(self) -> None:
        # Track failures to simulate transient network errors
        self.servicenow_failures = 1

    def call(self, system: str, action: str, payload: dict[str, Any]) -> tuple[bool, str]:
        """Simulates an API call. Returns a tuple of (success, output_message)."""
        name = payload.get("employee_name", "Unknown")

        if system == "sap":
            return True, f"SAP: Created employee record for {name}"
        
        elif system == "servicenow":
            if self.servicenow_failures > 0:
                self.servicenow_failures -= 1
                return False, "ServiceNow: 503 Service Unavailable (Transient Error)"
            return True, f"ServiceNow: Opened IT ticket for {name}"
        
        elif system == "salesforce":
            return True, f"Salesforce: Created user profile for {name}"
        
        return False, f"Unknown system: {system}"
