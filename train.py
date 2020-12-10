import os
import sys
import argparse
import pandas as pd

from azureml.core import Run

def getRuntimeArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_data_path', type=str)
    parser.add_argument('--output_data_path', type=str)
    args = parser.parse_args()
    return args


def main():
    args = getRuntimeArgs()
    run = Run.get_context()

    # Read data into pandas dataframe from input_data argument location
    input_df = pd.read_csv(os.path.join(args.input_data, 'german_credit_data.csv'))
    
    # Write pandas dataframe to output_data argument location
    input_df.to_csv(os.path.join(args.output_data, 'output_german_credit_data.csv'))

if __name__ == "__main__":
    main()