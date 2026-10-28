"""Tests for the Intent Agent."""

from __future__ import annotations

from msi_engine.intent_agent import IntentAgent


def test_parses_employee_name(intent_agent: IntentAgent) -> None:
    plan = intent_agent.parse("Onboard new employee Jane Doe")
    
    assert len(plan.steps) == 3
    assert plan.steps[0].system == "sap"
    assert plan.steps[0].payload["employee_name"] == "Jane Doe"
    assert plan.steps[1].system == "servicenow"
    assert plan.steps[2].system == "salesforce"


def test_handles_unknown_name(intent_agent: IntentAgent) -> None:
    plan = intent_agent.parse("Onboard a new person")
    
    assert plan.steps[0].payload["employee_name"] == "Unknown"
