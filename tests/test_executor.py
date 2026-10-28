"""Tests for the Executor Agent's retry logic."""

from __future__ import annotations

from unittest.mock import patch

from msi_engine.executor import ExecutorAgent
from msi_engine.models import WorkflowStep


@patch("msi_engine.executor.time.sleep")
def test_retries_on_transient_failure(mock_sleep, executor_agent: ExecutorAgent) -> None:
    """The ServiceNow mock is programmed to fail exactly once.
    This test proves the Executor retries and eventually succeeds."""
    step = WorkflowStep(
        system="servicenow",
        action="create_ticket",
        payload={"employee_name": "Jane Doe"}
    )

    result = executor_agent.execute_step(step)

    assert result.success is True
    assert result.attempts == 2  # Failed once, succeeded on 2nd try
    assert "ServiceNow" in result.output
    assert mock_sleep.call_count == 1  # Ensure it actually paused to wait


def test_fails_when_retries_exhausted(mock_apis) -> None:
    """If we set max_retries to 1, the Executor should fail immediately."""
    executor = ExecutorAgent(mock_apis, max_retries=1)
    step = WorkflowStep(
        system="servicenow",
        action="create_ticket",
        payload={"employee_name": "Jane Doe"}
    )

    result = executor.execute_step(step)

    assert result.success is False
    assert result.attempts == 1
    assert "503" in result.output
