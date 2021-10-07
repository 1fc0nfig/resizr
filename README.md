# resizr

Lightweight image resize tool for UNIX based systems.

## Instalation:

Make sure you have [ffmpeg](https://www.ffmpeg.org/) installed!

linux:
```
apt install ffmpeg
```
Mac OS:
```
brew install ffmpeg
```

---
## Usage:
```
python3 resizr.py [-s source_directory] [--res 1920:1080] [-f png]
```

## Options:

- [-s] Source directory containing images. default: .
- [--res] Output file resolution. default: 1920x1080
- [-f] File extensions to loop over. default: png

## How it works?
The script loops over image files of different resolutions in source_directory and add black sides, either on top or bottom, depending on it's resolution, to each one.

Result is output directory with all images with same resolution, depending on --res option

### Example:
input image: 900x675
![input image](testin.jpg)
image output: 1920x1080
![output image : 1920x1080](testout.jpg)
