from starbucks.dataset import Dataset
from starbucks.worker  import Worker

import starbucks.commands as commands

def test_datasets_ls():
  for ds in Dataset.ls(): print(f'\ndataset: {ds.name}')


def test_stream_data():
  commands.stream(['iris/iris.csv'])
  

def test_worker_ls():
  print([name.rstrip('.py') for name in Worker.ls()])
  