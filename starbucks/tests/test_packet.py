from starbucks.command import Command as command

def test_packet_command_to_bytes():
  buf = command("HELLO", "WORLD").to_bytes()
  cmd = command.from_bytes(buf)

  assert(cmd.name == "HELLO")
  assert(cmd.args == ("WORLD",))
