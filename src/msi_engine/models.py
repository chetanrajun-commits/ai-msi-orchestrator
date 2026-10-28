"""Domain models for the MSI Orchestrator."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class WorkflowStep:
    system: str
    action: str
    payload: dict[str, Any]


@dataclass
class WorkflowPlan:
    steps: list[WorkflowStep]


@dataclass
class StepResult:
    step: WorkflowStep
    success: bool
    output: str
    attempts: int = 1


@dataclass
class ExecutionReport:
    query: str
    plan: WorkflowPlan
    results: list[StepResult] = field(default_factory=list)
    overall_success: bool = False
