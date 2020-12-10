import os
import sys
import argparse
import pandas as pd

def getRuntimeArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_data_path', type=str)
    parser.add_argument('--output_data_path', type=str)
    args = parser.parse_args()
    return args


def main():
    args = getRuntimeArgs()

    # Read data into pandas dataframe from input_data argument location
    input_df = pd.read_csv(os.path.join(args.input_data_path, 'german_credit_data.csv'))
    
    # Write pandas dataframe to output_data argument location
    input_df.to_csv(os.path.join(args.output_data_path, 'output_german_credit_data.csv'))

if __name__ == "__main__":
    main()