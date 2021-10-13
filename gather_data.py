import os
import pandas as pd

def gather_files():
    files_list = [f for f in os.listdir("data") if f.endswith(".csv")]
    return files_list

def concat_files(filenames):
    dfs = []
    for filename in filenames:
        df = pd.read_csv(os.path.join("data", filename), index_col=None, header=0)
        dfs.append(df)
    res = pd.concat(dfs, axis=0, ignore_index=True)
    return res

if __name__ == "__main__":
    list_files = gather_files()
    df = concat_files(list_files)
    df.to_csv(os.path.join("data", "full_data.csv"))

