import csv
import pandas as pd

read_file = pd.read_csv (r'LR-draft.txt')
read_file.to_csv (r'LR_draft.csv', index=None)