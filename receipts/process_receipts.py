import os
import glob
import json
import shutil

try:
    os.mkdir('./processed')
except OSError:
    print("processed directory already exists")

glob.glob('./new/receipt-[0-9]*.json')

subtotal = 0.0
num = 0

for path in glob.iglob('./new/receipt-[0-9]*.json'):
    with open(path) as f:
        content=json.load(f)
        subtotal += float(content['value'])
    destination = path.replace("new", "processed")
    shutil.move(path, destination)
    print(f"moved {path} to {destination}")

print(f"Receipt subtotal: ${round(subtotal, 2)}")
