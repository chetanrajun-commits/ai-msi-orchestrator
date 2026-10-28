# AI-Led MSI Orchestrator

> An AI-led Master Systems Integrator (MSI) orchestrator that parses natural language and executes resilient multi-step workflows across mock enterprise APIs.

[![CI](https://github.com/chetanrajun-commits/ai-msi-orchestrator/actions/workflows/ci.yml/badge.svg)](https://github.com/chetanrajun-commits/ai-msi-orchestrator/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Ruff](https://img.shields.io/badge/lint-ruff-orange.svg)](https://github.com/astral-sh/ruff)

---

## The Problem

Large enterprises have fragmented technology stacks. A simple business request—like onboarding a new employee—requires a human (or a brittle script) to create a record in SAP, open an IT ticket in ServiceNow, and provision a Salesforce profile. 

If one of those systems goes down (a 503 error), the whole process breaks, leaving the employee half-onboarded and IT scrambling to fix it. 

This repository is a **reference implementation** of the fix: an AI-led Master Systems Integrator (MSI). It uses an LLM-style Intent Agent to translate natural language into a structured multi-step workflow, and a resilient Executor Agent to run those steps across the enterprise stack with built-in retry logic.

## What it does

1. **Intent Agent:** Parses the natural language request (e.g., *"Onboard new employee Jane Doe"*), extracts the entities, and generates a strictly typed `WorkflowPlan`.
2. **Executor Agent:** Iterates through the plan and calls the respective enterprise APIs. It implements exponential backoff to gracefully handle transient network failures.
3. **Resilience Demo:** The mock ServiceNow API is intentionally programmed to fail on the first attempt with a `503 Service Unavailable`, proving the orchestrator's ability to retry and recover without human intervention.

---

## Demo

Because this is a deterministic CLI, you can watch the MSI engine parse the request, hit a failure, and self-heal:

```bash
msi-engine run --query "Onboard new employee Jane Doe"
