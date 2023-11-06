from starbucks.api     import PYTHON_API
from starbucks.command import Command as command

def test_command_from_to_bytes():
  command.COMMANDS = PYTHON_API
  cmd1 = command('HELLO', 'CRUEL', 'WORLD')

  buf = cmd1.to_bytes()
  assert(buf.data() == b'\x05\x00HELLO\x02\x00\x00\x02\x05\x00CRUEL\x05\x00WORLD')
  
  cmd2 = command.from_bytes(buf)
  assert(cmd2.name == cmd1.name)
  assert(cmd2.args == cmd1.args)