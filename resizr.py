import os
import sys
import shutil
import string
import subprocess

# default path
path = os.getcwd() + "/"

# default output resolution
ow = "1920"
oh = "1080"

# default file format
f = "png"

# args
for x in range(len(sys.argv)):

    # source directory
    if sys.argv[x] == '-s':
        try:
            path = sys.argv[x+1]
            if not os.path.isabs(path):
                path = os.getcwd() + "/" + path
                pass
            if not path.endswith("/"):
                path = path + "/"
        except Exception as e:
            print("Usage: python3 resize.py -s sourcedir [--res output_width:output_height] [-f png]")
            print(f"No source directory specified! going with default {path}")
            if not path.endswith("/"):
                path = path + "/"
            pass
        pass

    # output resolution
    if sys.argv[x] == "--res":
        try:
            res = sys.argv[x+1]
            res = res.split(":")
            ow = res[0]
            oh = res[1]
            pass
        except Exception as e:
            print("Usage: python3 resize.py -s sourcedir [--res output_width:output_height] [-f png]")
            print(f"No resolution specified, going with default {ow}:{oh}")
            pass
        pass

    # input file formats
    if sys.argv[x] == "-f":
        try:
            f = sys.argv[x+1]
            pass
        except Exception as e:
            print("Usage: python3 resize.py -s sourcedir [--res output_width:output_height] [-f png]")
            print(f"No output file format spicified, going with default {f}")
            pass
        pass
        pass

# create output directory in path
try:
    outdir = path + "resized/"
    os.mkdir(outdir)
    pass
except Exception as e:
    print(f"Could not create output directory! {e}")
    delete = input("Would you like to delete it? y/N : ")
    if delete == "y":
        try:
            shutil.rmtree(outdir)
            outdir = path + "resized/"
            os.mkdir(outdir)
            pass
        except Exception as e:
            print(f"Could not delete directory. {e}")
            raise
        pass
    else:
        quit()

# file extension to loop over
ext = "." + f

cnt = 0
for f in os.listdir(path):
    maxprog = len(os.listdir(path))
    if f.endswith(ext):
        # scale everything to ow:oh
        cnt += 1
        try:
            # update file
            inf = path + f
            outf = outdir + f

            # print progress
            print(f"[ {cnt} / {maxprog} ]Converting {inf} to {outf}")

            # command setting
            command = f'ffmpeg -i {inf} -vf scale={ow}:{oh}:force_original_aspect_ratio=decrease,pad={ow}:{oh}:(ow-iw)/2:(oh-ih)/2,setsar=1 {outf}'
            command = command.split(" ")

            # exec command
            subprocess.run(command)
            pass
        except KeyboardInterrupt as e:
            print(f"Quiting!")
            quit()
        pass
