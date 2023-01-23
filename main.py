#!/usr/bin/env python3

import sys
import gzip

import src.map_io as io
import src.s01_map_info as mi

def main():
    with gzip.open(sys.argv[1], 'rb') as io.map_file:
        map_info = mi.parse_map_info()
        last_data = io.map_file.read()
    
    map_info["description"] = "I have now edited the description from here!"

    print(map_info)

    with gzip.open("output.h3m", 'wb') as io.out_file:
        mi.write_map_info(map_info)
        io.out_file.write(last_data)

if __name__ == "__main__":
    main()
