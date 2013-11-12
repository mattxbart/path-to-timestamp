import sys, os
import time
import datetime

def make_tuple(time_dirs):
    parts = []
    for part in time_dirs:
        try:
            part = int(part)
            parts.append(part)
        except ValueError:
            print "'%s' not a valid integer for time conversion" % part
            return []
    return tuple(parts)

def make_time(f, formats=["%m%d%y", "%m%d%Y"]):

    for format in formats:
        try:
            return time.mktime(time.strptime(f[:len(format)], format))
        except ValueError:
            continue
        

def run(path):

    for base, dirs, files in os.walk(path):
        for f in files:
            struct = make_time(f)
            if struct:
                print struct
                os.utime(os.path.join(base, f), (struct, struct,))
                print os.path.join(base, f), struct

        



if __name__ == "__main__":
    
    run(sys.argv[1])
