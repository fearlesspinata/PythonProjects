import glob

receipts = glob.glob('./new/receipt-[0-9]*.json')

number=0

print(len(receipts))
