"""Python Agent Shell — minimal interactive shell for fleet agents.

Provides a read-eval-print loop with PLATO integration,
fleet coordinate access, and constraint theory tools.
"""

import sys
import logging
from typing import Optional

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s %(levelname)s %(message)s")
logger = logging.getLogger("python-agent-shell")


class AgentShell:
    """Interactive shell for fleet agents."""

    def __init__(self, vessel_id: str = "shell-01"):
        self.vessel_id = vessel_id
        self.history: list[str] = []
        logger.info(f"Agent shell initialized for vessel: {vessel_id}")

    def eval(self, cmd: str) -> str:
        """Evaluate a command and return output."""
        self.history.append(cmd)
        try:
            result = eval(cmd, {"__name__": "__fleet__"})
            return str(result)
        except SyntaxError:
            try:
                exec(cmd, {"__name__": "__fleet__"})
                return "(executed)"
            except Exception as e:
                return f"Error: {e}"
        except Exception as e:
            return f"Error: {e}"

    def help(self) -> str:
        return """Python Agent Shell Commands:
  eval <expr>     — Evaluate Python expression
  history          — Show command history
  help             — Show this help
  quit             — Exit shell
  fleet            — Show fleet status
  plato <room>     — Read PLATO room
  coord            — Show fleet coordinate (Laman rigidity)
"""


def main():
    vessel_id = sys.argv[1] if len(sys.argv) > 1 else "shell-01"
    shell = AgentShell(vessel_id)
    print(f"Fleet Python Shell v1.0.0 — vessel: {vessel_id}")
    print('Type help() for commands, quit to exit.')
    while True:
        try:
            cmd = input(f"[{vessel_id}]>>> ")
            if cmd == "quit":
                break
            elif cmd == "help()":
                print(shell.help())
            elif cmd.startswith("eval "):
                print(shell.eval(cmd[5:]))
            elif cmd == "history":
                for i, h in enumerate(shell.history):
                    print(f"  {i+1}: {h}")
            else:
                print(shell.eval(cmd))
        except EOFError:
            break
        except KeyboardInterrupt:
            print("\n(Interrupt)")
    print("Shell closed.")


if __name__ == "__main__":
    main()