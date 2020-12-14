import os
import sys
import argparse
import pandas as pd

def getRuntimeArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_data_path', type=str, help='path of location to read the input data')
    parser.add_argument('--output_data_path', type=str, help='path of location to write the output data')
    args = parser.parse_args()
    return args


def main():
    # Get runtime arguments
    args = getRuntimeArgs()

    # Read data into pandas dataframe from input_data_path argument location
    df = pd.read_csv(os.path.join(args.input_data_path, 'german_credit_data.csv'))
    
    # Create output directory if it doesn't exist
    if not (args.output_data_path is None):
        os.makedirs(args.output_data_path, exist_ok=True)
    print('%s created' % args.output_data_path)

    # Write pandas dataframe to output_data_path argument location
    df.to_csv(os.path.join(args.output_data_path, 'output_german_credit_data.csv'))

if __name__ == '__main__':
    main()