import sys
import argparse

from pathlib import Path

def encode(filename, toPng):

    filein = open(filename, "rb")
    data = bytearray(filein.read())

    if toPng:
        data[0] = 0x89
    else:
        data[0] = 0xED

    ext = ".png" if toPng else ".psm"
    
    pFilename = Path(filename)
    
    filenameout = pFilename.parent / (pFilename.stem + ext)
    
    fileout = open(filenameout, "wb")

    fileout.write(data)

    fileout.close()
    filein.close()

    return

if __name__ == "__main__":


    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-d", "--decode", help="Convert .psm file into a .png file", action="store_true")
    group.add_argument("-e", "--encode", help="Convert .png file into a .psm file", action="store_true")
    parser.add_argument("file", help="the file to work with, either a .png or a .psm")
    args = parser.parse_args()

    if args.decode:
        encode(args.file, True)
    elif args.encode:
        encode(args.file, False)
    else:
        parser.print_usage()