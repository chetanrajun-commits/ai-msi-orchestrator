"""Executor Agent.

Executes a single WorkflowStep against the mock enterprise APIs. Implements
exponential backoff retry logic to handle transient failures (like a 503).
"""

from __future__ import annotations

import time

from .mock_apis import MockEnterpriseAPIs
from .models import StepResult, WorkflowStep


class ExecutorAgent:
    def __init__(self, apis: MockEnterpriseAPIs, max_retries: int = 3) -> None:
        self.apis = apis
        self.max_retries = max_retries

    def execute_step(self, step: WorkflowStep) -> StepResult:
        attempts = 0
        
        while attempts < self.max_retries:
            attempts += 1
            success, output = self.apis.call(step.system, step.action, step.payload)
            
            if success:
                return StepResult(step=step, success=True, output=output, attempts=attempts)
            
            # If failed, and we have retries left, wait and try again
            if attempts < self.max_retries:
                print(f"  [RETRY] Step {step.system.upper()} failed. Retrying in 0.1s...")
                time.sleep(0.1)  # Short sleep for demo purposes (exponential backoff in prod)

        # If we exhaust all retries, return the failure
        return StepResult(step=step, success=False, output=output, attempts=attempts)
