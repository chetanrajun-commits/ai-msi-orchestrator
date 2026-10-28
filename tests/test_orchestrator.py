"""End-to-end test of the MSI Orchestrator."""

from __future__ import annotations

from msi_engine.orchestrator import Orchestrator


def test_full_pipeline_completes_successfully() -> None:
    orchestrator = Orchestrator()
    # We pass the natural language query.
    # The mock ServiceNow will fail once, retry, and the whole pipeline will exit 0.
    exit_code = orchestrator.run("Onboard new employee Jane Doe")
    
    assert exit_code == 0
