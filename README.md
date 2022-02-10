# ESN Scripts

## src
directory containing the written scripts and other source files
* `autocolor`
    * script which automatically processes an image and tries to enhance its quality
    * does not need to be run individually or changed
    * use the `autocolor_all.py` script to enhance images
* `autocolor_all.py`
    * script that enhances the image quality of all images in a given directory
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
directory containing images used by the scripts
