from starbucks.command import Command as command
from starbucks.api     import PYTHON_API

def test_packet_command_to_bytes():
  command.COMMANDS = PYTHON_API

  buf = command("HELLO", "World").to_bytes()
  cmd = command.from_bytes(buf)

  assert(cmd.name == "HELLO")
  assert(cmd.args == ("World",))
