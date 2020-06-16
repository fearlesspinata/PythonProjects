#!/usr/bin/env python3.8

import argparse
print("""
        maintained by:
        ___________                 .__                       __________.__               __          
        \_   _________ _____ _______|  |   ____   ______ _____\______   |__| ____ _____ _/  |______  
         |    ___/ __ \\\__  \\\_  __ |  | _/ __ \ /  ___//  ___/|     ___|  |/    \\\__  \\\   __\\__  \\  
         |     \\\  ___/ / __ \|  | \|  |_\  ___/ \___ \ \___ \ |    |   |  |   |  \/ __ \|  |  / __ \_
         \___  / \___  (____  |__|  |____/\___  /____  /____  >|____|   |__|___|  (____  |__| (____  /
             \/      \/     \/                \/     \/     \/                  \/     \/          \/ 
                """)
# build the parser
parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')

args = parser.parse_args()

with open(args.filename) as f:
    lines = f.readlines()
    lines.reverse()

    if args.limit:
        lines = lines[:args.limit]

    for line in lines:
        print(line.strip()[::-1])


# parse the arguments

# read the file, reverse the contents and print
