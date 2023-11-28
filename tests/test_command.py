from bubblegum.command import Command

def test_command_from_to_bytes():
  cmd1 = Command('HELLO', 'CRUEL', 'WORLD')

  buf = cmd1.to_bytes()
  assert(buf() == b'\x05\x00\x00\x00HELLO\x02\x00\x00\x00\x05\x00\x00\x00CRUEL\x05\x00\x00\x00WORLD')
  
  cmd2 = Command.from_bytes(buf)
  assert(cmd2.name == cmd1.name)
  assert(cmd2.args == cmd1.args)