from starbucks.datasets import Dataset
import starbucks.commands as commands

def test_datasets_ls():
  for ds in Dataset.ls(): print(f'\ndataset: {ds.name}')


def test_stream_data():
  print(commands.stream(['iris/iris.csv']))