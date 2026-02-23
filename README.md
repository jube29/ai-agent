# Claude Code at home

A minimal AI agent in Python, built as part of the [CodeCrafters](https://codecrafters.io/challenges/claude-code) challenge.

## What it does

Sends a prompt to an LLM via OpenRouter, executes tool calls in a loop until the model is done, prints the final answer.

## Tools

| Tool | Description |
|---|---|
| `Read` | Read file contents |
| `Write` | Create or overwrite a file |
| `Bash` | Execute a shell command |

## Project structure

```
app/
├── main.py    # CLI entry point
├── agent.py   # Conversation loop
└── tools.py   # Tool definitions and handlers
```
