# ESN Scripts

## src
directory containing the written scripts and other source files
* `autocolor`
    * script which automatically processes an image and tries to enhance its quality
    * does not need to be run individually or changed
    * use the `autocolor_all.py` script to enhance images
* `autocolor_all.py`
    * script that enhances the image quality of all images in a given directory
    * standard image extensions that are processed: png, PNG, jpg, JPG, jpeg
    * needs the `autocolor` script to work properly
    * to get further help call `python3 autocolor_all.py -h`
* `watermark`
    * simple shell script that puts a watermark on all images in the same directory as the script
    * path to watermark has to be set in the script before execution
    * if not executable run `sudo chmod +x watermark` first
* `remove-unmarked`
    * remove all files in the directory containing this script whose names don't contain the string "marked-"
    * simplifies clean-up after watermarking
    * if nor executable run `sudo chmod +x remove-unmarked` first

## img 
directory containing images used by the scripts, e.g. the watermark

## example workflow
* download folder of unprocessed images
* process images
    * script can be run like `python3 autocolor_all.py -p "path to directory for processed images" -i "path to folder containing unprocessed images" -a "path to autocolor script" (-e extension1 extension2 extension3 ...)`
    * example (with extension list): `python3 autocolor.py -p "~/esn" -i "~/images/event_x" -a "~/scripts/autocolor" -e png jpg JPG PNG`
    * example (without extension list): `python3 autocolor.py -p "~/esn" -i "~/images/event_x" -a "~/scripts/autocolor"`
* watermark the processed images
    * execute the `watermark` script in the directory containing the processed images: `./watermark`
* clean up the directory conatining the processed and watermarked images
    * e.g. execute `./remove-unmarked` to remove ALL files not containing "marked-" in their file name
* upload folder containing processed and watermarked images