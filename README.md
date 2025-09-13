# Agent-as-Coder Challenge

This project implements an autonomous agent (`agent.py`) that generates custom bank statement parsers.

---

## Run Instructions

1. Clone this repo:
   ```bash
   git clone https://github.com/tbharati876/ai-agent-challenge.git
   cd ai-agent-challenge
2. Install dependencies
    ```bash
   pip install -r requirements.txt
3. Run the agent for ICICI
    ```bash
    python agent.py --target icici
4. Parser gets generated
    ```bash
    custom_parsers/icici_parser.py
5. Run tests
    ```bash
    pytest -q
---
Agent diagram

The agent follows a simple autonomous loop: it plans the next step, generates code for the parser, runs tests against the expected CSV, and if tests fail, it enters a self-correction loop with up to three retries. Once tests pass, the loop stops and the parser is finalized.
```bash
Plan → Generate parser → Run tests → Retry (≤3x) → Done 

   
   

