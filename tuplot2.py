import argparse
import matplotlib.pyplot as plt
import pandas as pd
import re
from matplotlib import rc
rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})
# for Palatino and other serif fonts use:
# rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

tudfarben = {"blau": "#005AA9", "hellblau": "#0083CC", "tuerkis": "#009D81", "gruen": "#99C000", "gruengelb": "#C9D400",
             "gelb": "#FDCA00", "orange": "#F5A300", "orangerot": "#EC6500", "rot": "#E6001A", "lila": "#A60084", "lilablau": "#721085"}


parser = argparse.ArgumentParser(
    description="Obtain the names of the files to process from command line, split up into the core name, the numbers and the file extension. The defaults are av_cluster_radius_[35, 50, 75, 100].txt so if you just run the program with no arguments at all, it will do the standard plot. ")
parser.add_argument("-f",
                    "--fileprefix", help="The prefix of the file-series i.e. the actual file name.", default="av_cluster_radius_")

parser.add_argument("-F", "--filename",
                    help="Enter complete filenames manually. The label for the legend will be somehow derived from the filename.")
parser.add_argument("-e",
                    "--extension", help="File extension. Default is .txt.", default=".txt")
parser.add_argument("-n",
                    "--numbers",  nargs='+', help="The numbers that are contained in the filenames. Currently, exactly four are required.", default=["35", "50", "75", "100"])

parser.add_argument(
    "-x", "--xaxis", help="Set the title of the x-axis.", default="timestep")
parser.add_argument(
    "-y", "--yaxis", help="Set the title of the y-axis.", default="Radius")
parser.add_argument("-eb", "--errorbar",
                    help="Toggle the errorbars.", action="store_true")


parser.add_argument("--latex", help="Provide latex strings (space separated) to style the axis titles. The titles need to be entered surrounded by quotation marks to respect latex syntax.", nargs=2)

parser.add_argument("-ls", "--linestyle",
                    help="Set the linestyle of the plot. For example: dotted ..., loosely dotted . . ., dashed ---. Default is solid, which is just a continuous line.", default="solid")

args = parser.parse_args()
manual_filenames = args.filename
prefix = args.fileprefix
extension = args.extension
numbers = args.numbers
xtitle = args.xaxis
ytitle = args.yaxis
errorbars_on = args.errorbar
latex = args.latex
line = args.linestyle
# This requires that the default numbers are used. A more flexible solution will be added.
default_colors = dict.fromkeys(numbers)
default_colors[35] = tudfarben["rot"]
default_colors[50] = tudfarben["lila"]
default_colors[75] = tudfarben["orange"]
default_colors[100] = tudfarben["gruen"]

# Generate a list of filenames from the command line arguments. This only works with files that only differ in a number that is contained in them which is stored in list numbers. This seems like an inconvenient way of doing this, but it saves a lot of typing when using the program.
myfiles = [prefix + number +
           extension for number in numbers]
alldata = {}
for myfile, number in zip(myfiles, numbers):
    data = pd.read_csv(myfile, sep="\s\s\s\s\s\s",
                       header=None, names=["x", "y", "eb"], engine="python")

    alldata[number] = data


for key, value in alldata.items():
    if errorbars_on:
        plt.errorbar(value['x'], value['y'],
                     value['eb'], label="quench" + key, linestyle=line, color=default_colors[key])

    else:
        plt.plot(value['x'], value['y'],
                 label="quench " + key, linestyle=line, color=default_colors[key])


plt.legend(shadow=True)
if not latex:
    plt.xlabel(xtitle)
    plt.ylabel(ytitle)
else:
    plt.xlabel(latex[0])
    plt.ylabel(latex[1])
# plt.show()
print(latex)
plt.savefig(prefix + ".png")
