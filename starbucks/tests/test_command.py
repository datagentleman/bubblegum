from starbucks.command import Command

def test_command_from_to_bytes():
  cmd1 = Command('HELLO', 'CRUEL', 'WORLD')
  
  buf = cmd1.to_bytes()
  assert(buf.data() == b'\x00\x05HELLO\x00\x02\x00\x02\x00\x05CRUEL\x00\x05WORLD')
  
  cmd2 = Command.from_bytes(buf)
  assert(cmd2.name == cmd1.name)
  assert(cmd2.args == cmd1.args)