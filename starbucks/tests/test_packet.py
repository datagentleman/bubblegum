from starbucks.command import Command

def test_packet_command_to_bytes():
  bytes = Command("Hello", "World").to_bytes()
  cmd   = Command.from_bytes(bytes)

  assert(cmd.name == "Hello")
  assert(cmd.args == ("World",))
