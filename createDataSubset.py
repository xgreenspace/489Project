import argparse
import os
import time
import regex as re

if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser(description='Create a subset of the full dataset')

    # Add the arguments
    parser.add_argument('--data', type=str, default='FullDataset', help='location of the data corpus')
    parser.add_argument('--output', type=str, default='subset_', help='location of the output data corpus')
    parser.add_argument('-s', '--size', type=int, default=10, help='size of the subset')

    # Execute the parse_args() method
    args = parser.parse_args()

    # Create the output directory and name it after the current time
    output_dir = os.path.join(args.output + time.strftime("%Y%m%d-%H%M%S"))
    os.makedirs(output_dir)
    
    # Within the output directory, create the subdirectories for the training, validation and test sets
    for subset in ['train', 'valid', 'test']:
        os.makedirs(os.path.join(output_dir, subset))

    # Find every file in the data/Real directory that has a filename containing "Left_index_finger.BMP"
    for i in range(args.size):
        
    
    

    

    


