#!/usr/bin/env python

from pprint import pprint
import re
import sys
import math
import binascii


if __name__ == "__main__":

    with open('cipher.txt', 'r') as f:
        # Read the whole file at once
        data = f.read()
        print(data)
        #int(data, base=2)
        chunks, chunk_size = len(data), 8
        input = [int(data[i:i + chunk_size], base=2) for i in range(0, chunks, chunk_size)]
        print(input)
        f.close()

    with open('raw_plain.txt', 'w') as fout:
        for i in range(256):
            print("Using mask {}".format(i))
            temp = []
            avg = 0
            for letter in input:
                x = letter ^ i
                temp.append(x)
                #print("{}->{}".format(letter,x))
                avg = sum(temp)/len(temp)
                if avg < 32 or avg > 126:
                    #print("Failure!!\n")
                    del temp[:]
                    break
            print(temp)
            if len(temp) > 0:
                text = ''.join(chr(i) for i in temp)
                fout.write("----------------------------------Using mask {}----------------------------------\n".format(i))
                fout.write("{}\n\n".format(text))
        fout.close()
