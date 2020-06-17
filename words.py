#!/usr/bin/env python3.8
import argparse

parser = argparse.ArgumentParser(description='Wordfinder')
parser.add_argument('word')

args = parser.parse_args()

words = open("/usr/share/dict/words")
word_lines = words.readlines()
matches = []

for word in word_lines:
    if args.word in word:
        matches.append(word.strip())

print(matches)
