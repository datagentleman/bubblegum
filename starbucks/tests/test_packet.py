from starbucks.command import Command

def test_packet_command_to_bytes():
  buf = Command("Hello", "World").to_bytes()
  cmd = Command.from_bytes(buf)

  assert(cmd.name == "Hello")
  assert(cmd.args == ("World",))
