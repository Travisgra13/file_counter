import os
import sys

def main(argv):
    num_of_files = len(os.listdir(argv[0]))
    print("Number of files in " + argv[0] + " is " + str(num_of_files))
    sys.exit(num_of_files)


if __name__ == '__main__':
    main(sys.argv[1:])
