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
    for i in range(args.size + 1):
        # Create a regex to match the file names
        regex = re.compile(r'{}__(M|F)_Left_index_finger.BMP'.format(i))

        # Find the files that match the regex
        file_found = False
        for root, dirs, files in os.walk(args.data):
            for file in files:
                if regex.match(file):
                    # create directory for output
                    os.mkdir(os.path.join(output_dir, 'test', 'class_{}'.format(i)))
                    # Move the file to the output directory
                    shutil.copy(os.path.join(root, file), os.path.join(output_dir, 'test', 'class_{}'.format(i)))
                    file_found = True
                    break
            if file_found:
                break

    for i in range(args.size + 1):
        regex = re.compile(r'{}__(M|F)_Left_index_finger_(CR|CRh|Obl|Oblh|Zcut|Zcuth).BMP'.format(i))

        # Find the files that match the regex
        files_found = 0
        for root, dirs, files in os.walk(args.data + '/Altered'):
            for file in files:
                if regex.match(file):
                    # create directory for output
                    try:
                        os.mkdir(os.path.join(output_dir, 'train', 'class_{}'.format(i)))
                    except FileExistsError:
                        pass

                    # Move the file to the output directory
                    shutil.copy(os.path.join(root, file), os.path.join(output_dir, 'train', 'class_{}'.format(i)))
                    if "Medium" in root:
                        # Add an _M to the file name
                        os.rename(os.path.join(output_dir, 'train', 'class_{}'.format(i), file), os.path.join(output_dir, 'train', 'class_{}'.format(i), file[:-4] + "_M.BMP"))
                    if "Hard" in root:
                        # Add an _H to the file name
                        os.rename(os.path.join(output_dir, 'train', 'class_{}'.format(i), file), os.path.join(output_dir, 'train', 'class_{}'.format(i), file[:-4] + "_H.BMP"))
                    files_found += 1
                    if files_found == 6:
                        break
            if files_found == 6:
                break

    for i in range(args.size + 1):
        regex = re.compile(r'{}__(M|F)_Left_index_finger_(CR|Obl|Zcut).BMP'.format(i))

        # Find the files that match the regex
        files_found = 0
        for root, dirs, files in os.walk(args.data):
            for file in files:
                if regex.match(file):
                    # create directory for output
                    try:
                        os.mkdir(os.path.join(output_dir, 'valid', 'class_{}'.format(i)))
                    except FileExistsError:
                        pass
                    # Copy the file to the output directory and rename it
                    shutil.copy(os.path.join(root, file), os.path.join(output_dir, 'valid', 'class_{}'.format(i)))
                    if "Medium" in root:
                        # Add an _M to the file name
                        os.rename(os.path.join(output_dir, 'valid', 'class_{}'.format(i), file), os.path.join(output_dir, 'valid', 'class_{}'.format(i), file[:-4] + "_M.BMP"))
                    if "Hard" in root:
                        # Add an _H to the file name
                        os.rename(os.path.join(output_dir, 'valid', 'class_{}'.format(i), file), os.path.join(output_dir, 'valid', 'class_{}'.format(i), file[:-4] + "_H.BMP"))
                    files_found += 1
                    if files_found == 3:
                        break
            if files_found == 3:
                break

                
        
        
    
    

    

    


