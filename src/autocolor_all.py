# script to try to visually improve all images in the folder in which this script is executed using the autocolor bash script
# needs Python 3.x
# to get more help and to see needed parameters run: python3 autocolor_all.py -h

import subprocess # execute shell commands
import os # create directories, work with paths
import argparse # work with console arguments

# function tries to create a directory at the given path
# print success or failure
def create_dir(path: str) -> None:
    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)

# get console arguments given during the script start
def get_arguments() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="improve image quality of all images in a given directory using the 'autocolor' shell script", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-p", "--processed", type=str, default="/home/tim/esn/", help="path where the directory 'processed' should be created which is used to store the processed images")
    parser.add_argument("-i", "--images", type=str, default=os.getcwd(), help="path to the directory containing the images which should be processed; default is the directoy this script is in")
    parser.add_argument("-e", "--extensions", type=str, nargs="+", default=["png", "PNG", "jpg", "JPG", "jpeg"], help="give a list of file types which this script should process; files with other extensions will be ignored by this script")
    parser.add_argument("-a", "--autocolor", type=str, default="/home/tim/esn/scripts/autocolor", help="path to the 'autocolor' script")
    return parser.parse_args()

def main():
    # get console arguments
    args = get_arguments()

    # create the 'processed' directory if it doesn't already exist4
    assert os.path.exists(args.processed), "can*t create 'processed' directory; directory doesn't exist"
    args.processed = os.path.join(args.processed, "processed")
    create_dir(os.path.join(args.processed, "processed"))

    # replace all blank spaces in image dir name with underscores to avoid future complications
    dir_name = args.images.split("/")[-1].replace(" ", "_")

    # create directory to store processed images
    create_dir(os.path.join(args.processed, dir_name))

    # change all blank spaces in filenames to underscores (prevents errors while processing images with other scripts)
    for f in os.listdir(args.images):
        os.rename(os.path.join(args.images, f), os.path.join(args.images, f.replace(" ", "_")))

    # for each file call the autocolor shell script
    for f in os.listdir(args.images):
        if f.split(".")[-1] in args.extensions:
            print(f + " is being processed.")

            # create processed image name: replace dots and blank spaces in the filename and make it a jpg file
            processed_filename = "processed-" + "_".join(f.split(".")[:-1]).replace(" ", "_") + ".jpg"
            subprocess.call([args.autocolor, "-m", "gamma", "-c", "separate", os.path.join(args.images, f), os.path.join(args.processed, dir_name , processed_filename)])

if __name__ == "__main__":
    main()
