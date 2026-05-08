# python-agent-shell

**Interactive Python REPL for SuperInstance fleet agents.**

A minimal, import-ready shell that gives agents PLATO integration, fleet-coordinate access, and constraint theory tools through a REPL you can pipe into any agent runtime.

## What It Is

Point any agent at this shell and it gets a live REPL with fleet utilities pre-loaded. No config. No setup. Just clone, install, and the agent starts talking.

## Quick Start

```bash
git clone https://github.com/SuperInstance/python-agent-shell
cd python-agent-shell
pip install -r requirements.txt

# Start the REPL
python3 src/shell.py [vessel-id]
```

The `vessel-id` arg sets which agent context the shell runs under (auto-detects if omitted).

```python
# Inside the shell
>>> eval_insight("check drift on batch-42")
>>> help()   # Show available fleet commands
>>> history  # Show command history
```

## What's Working

- Core REPL with `eval()` and `help()`
- Command history
- Fleet utility imports (PLATO, coordinate access, constraint tools)

## Architecture

```
src/
  shell.py       # Main REPL entry point
requirements.txt # Dependencies
```

## Part of the SuperInstance Fleet

This is a fleet utility — one of many tools that Cocapn agents pick up and use. See [SuperInstance](https://github.com/SuperInstance) for the full fleet.

## License

MIT
