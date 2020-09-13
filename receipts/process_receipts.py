import os
import glob
import json
import shutil

try:
    os.mkdir('./processed')
except OSError:
    print("processed directory already exists")

receipts = glob.glob('./new/receipt-[0-9]*.json')

subtotal = 0.0
num = 0

for path in receipts:
    with open(path) as f:
        content=json.load(f)
        subtotal += float(content['value'])
    destination = path.replace("new", "processed")
    shutil.move(path, destination)
    print(f"moved {path} to {destination}")

print("Receipt subtotal: $%.2f" % subtotal)
