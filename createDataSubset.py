import argparse
import os
import time
import regex as re
import shutil

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

    # Move (size)__(M|F)_Left_index_finger.BMP files from the data directory to the output directory
    for i in range(args.size):
        # Create a regex to match the file names
        regex = re.compile(r'{}__(M|F)_Left_index_finger.BMP'.format(i))

        # Find the files that match the regex
        for root, dirs, files in os.walk(args.data):
            for file in files:
                if regex.match(file):
                    # Move the file to the output directory
                    shutil.copy(os.path.join(root, file), os.path.join(output_dir, 'test'))
        
        
    
    

    

    


