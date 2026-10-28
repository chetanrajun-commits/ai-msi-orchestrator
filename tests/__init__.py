"""Shared fixtures for the MSI Orchestrator test suite."""

from __future__ import annotations

import pytest

from msi_engine.executor import ExecutorAgent
from msi_engine.intent_agent import IntentAgent
from msi_engine.mock_apis import MockEnterpriseAPIs


@pytest.fixture
def mock_apis() -> MockEnterpriseAPIs:
    return MockEnterpriseAPIs()


@pytest.fixture
def intent_agent() -> IntentAgent:
    return IntentAgent()


@pytest.fixture
def executor_agent(mock_apis: MockEnterpriseAPIs) -> ExecutorAgent:
    return ExecutorAgent(mock_apis, max_retries=3)
