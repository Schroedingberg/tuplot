import pandas as pd
import argparse
from argparse import RawTextHelpFormatter
parser = argparse.ArgumentParser(
    description="Obtain the names of the files to process from command line",
    formatter_class=RawTextHelpFormatter)

parser.add_argument("-f", help="The file to process")
parser.add_argument(
    "-o", help="The output file. Default is input[:5]+norm.txt")
parser.add_argument(
    "-c", help="Columns to be normalized. Default is only the second one.(Index 1)", default=[1])
args = parser.parse_args()
f = args.f
o = args.o
c = args.c
data = pd.read_csv(f, sep=',',
                   engine='python', header=None)
normalised_data = data[1].apply(lambda x: (
    x - data[1].tail(1)) / (data[1][0] - data[1].tail(1)))
data[1] = normalised_data
data.to_csv(f.split(".")[0] + "norm.txt", sep=",")
