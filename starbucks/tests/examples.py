from starbucks.datasets import Dataset

def test_datasets_ls():
  for ds in Dataset.ls(): print(ds.name)