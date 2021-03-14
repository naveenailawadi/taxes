import pandas as pd
import os
import sys


# make a main function
def main(folder, export_filename):
    # read in all the files from the folder
    files = [f"{folder}/{file}" for file in os.listdir(folder)]

    # make a df for each file
    dfs = [pd.read_csv(file) for file in files]

    # merge the list of dfs
    combined_df = pd.concat(dfs)

    # export the combined df
    combined_df.to_csv(export_filename, index=False)


if __name__ == '__main__':
    folder = sys.argv[1]
    export_filename = sys.argv[2]

    main(folder, export_filename)
