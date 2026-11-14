#!/usr/bin/env python
"""reducer.py"""
 
from itertools import groupby
from operator import itemgetter
import sys
 
def read_mapper_output(file, separator='\t'):
   for line in file:
       yield line.rstrip().split(separator, 1)
 
def main(separator='\t'):
   # input comes from STDIN (standard input)
   data = read_mapper_output(sys.stdin, separator=separator)
   
   all_counts = [] # list to hold everything before we sort
   
   # groupby groups multiple word-count pairs by word,
   # and creates an iterator that returns consecutive keys and their group:
   #   current_word - string containing a word (the key)
   #   group - iterator yielding all [current_word, count] items
   for current_word, group in groupby(data, itemgetter(0)):
       try:
            total_count = sum(int(count) for current_word, count in group)
            # append to the list instead of printing it here
            all_counts.append((current_word, total_count))
       except ValueError:
            # count was not a number, so silently discard this item
            pass
            
   # sort the list descending based on the count (index 1 in the tuple)
   all_counts.sort(key=lambda x: x[1], reverse=True)
   
   # print only the first 3 highest scores
   for current_word, total_count in all_counts[:3]:
       print ("%s%s%d" % (current_word, separator, total_count))
 
if __name__ == "__main__":
   main()
