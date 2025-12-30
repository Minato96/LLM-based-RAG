# LLM-Driven Reasoning Engine (Agentic RAG)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![LangChain](https://img.shields.io/badge/LangChain-v0.2-green)
![Groq](https://img.shields.io/badge/Groq-LPU_Inference-orange)
![Architecture](https://img.shields.io/badge/Architecture-Agentic-purple)

> **A latency-optimized, reasoning-first QA system that uses an LLM as a "Planner" to orchestrate information retrieval, ensuring grounded and verified answers.**

---

## Overview

Unlike traditional RAG systems that follow a linear pipeline:

~~~text
Search -> LLM -> Answer
~~~

this project implements an **Agentic Control Flow**, where the LLM acts as a planner that decides *if*, *when*, and *how* to retrieve information.

---

## Key Differentiators

- **Brain-First Architecture**  
  User intent is interpreted before any retrieval is triggered.

- **Sub-Second Latency**  
  Powered by Groq API (Llama 3) for near-instant reasoning.

- **Prompts-as-Code**  
  Prompts are stored in YAML, decoupling reasoning logic from Python.

- **Hallucination Control**  
  Answers must be grounded with citations or explicitly admit uncertainty.

---

## Architecture

The system follows a three-stage **Reasoning Loop**:

~~~mermaid
graph TD
    A[User Query] --> B[Stage 1: Planner]
    B -->|Simple| C[Direct Response]
    B -->|Complex| D[Stage 2: Tool Execution]
    D --> E[Retrieval Tool]
    E --> F[Stage 3: Reasoner]
    F --> G[Final Answer with Citations]
~~~

### Stage 1: Planner
- Analyzes user intent
- Determines whether retrieval is needed
- Emits structured JSON search plans

### Stage 2: Tool Execution
- Executes retrieval against the knowledge source
- Modular interface (FAISS / ChromaDB / Mock)

### Stage 3: Reasoner
- Synthesizes grounded answers
- Enforces no-hallucination constraints

---

## Tech Stack

| Component | Technology | Purpose |
|--------|-----------|--------|
| Orchestration | LangChain Core | Agent control flow |
| Inference | Groq API | Ultra-low-latency LPU inference |
| Model | Llama3-8B-8192 | Balanced reasoning |
| Prompt Config | YAML | Prompts-as-code |
| Secrets | python-dotenv | Environment isolation |

---

## Project Structure

~~~text
.
├── core/
│   ├── llm_controller.py
│   └── retrieval_tool.py
├── prompts/
│   ├── planner.yaml
│   └── answer_engine.yaml
├── data/
├── main.py
├── .env
└── requirements.txt
~~~

---

## Run

~~~bash
python main.py
~~~

---

## Author

**Charan**  
AI Engineer & Systems Architect
