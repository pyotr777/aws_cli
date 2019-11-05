#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import subprocess
import argparse
from datetime import datetime, timedelta
from io import StringIO
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
from matplotlib.ticker import MultipleLocator, LinearLocator, MaxNLocator


# Plot grid on the axis ax
def drawGrid(ax, ticks=5, minor_ticks=5):
    # if ystep is not None:
    # minorLocatorY = MultipleLocator(ystep / minor_ticks)
    # majorLocatorY = MultipleLocator(ystep)
    steps = np.arange(1, 10, 100)
    majorLocatorY = MaxNLocator(ticks, steps=steps)
    minorLocatorY = MaxNLocator(minor_ticks * ticks, steps=steps)
    ax.yaxis.set_minor_locator(minorLocatorY)
    ax.yaxis.set_major_locator(majorLocatorY)

    ax.grid(which='minor', linestyle=':', linewidth=.5, alpha=.5)
    ax.grid(which="major", ls=":", alpha=0.25, color="black")


parser = argparse.ArgumentParser()
parser.add_argument(
    "--options",
    default="",
    nargs=argparse.REMAINDER,
    help=
    "Options for describe-spot-price-history command. https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-spot-price-history.html"
)
parser.add_argument("--days", default=1, type=int, help="Show history for this number of days.")
parser.add_argument("--os", default=None, type=str, help="Filter by OS")
args = parser.parse_args()

options = " ".join(args.options)
# Start time set to 1 day before now
if "start-time" not in options:
    starttime = datetime.today() - timedelta(days=args.days)
    options += " --start-time {}".format(starttime.isoformat())

command = "aws ec2 describe-spot-price-history {}".format(options)
print(command)
proc = subprocess.Popen(command.split(" "), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=0, shell=False)
output = ""
for line in iter(proc.stdout.readline, b''):
    line = line.decode('utf-8')
    output += line
    print(line.strip("\n"))

df = pd.read_csv(StringIO(output), sep="\t", header=None, names=["type", "reg", "inst", "OS", "price", "date"])
df["date"] = df["date"].astype("datetime64")

# Filter by OS if provided
if args.os is not None:
    df = df[df["OS"].str.contains(args.os, case=False)]

# print(df.head())

register_matplotlib_converters()

fg = sns.FacetGrid(
    df,
    hue="reg",
    col="inst",
    row="OS",
    height=5,
    aspect=1.1,
    margin_titles=True,
    sharex=True,
    sharey=False,
)
g = fg.map(plt.plot, "date", "price", lw=1, alpha=1, ms=3, marker="o", fillstyle="full",
           markerfacecolor="#ffffff").add_legend()

axes = g.axes
for i, row in enumerate(axes):
    for j, column in enumerate(row):
        ax = axes[i, j]
        # Define the date format
        ax.set_xticklabels(ax.get_xticklabels(), rotation=65, horizontalalignment='right')
        date_form = DateFormatter("%d %H:%M")
        ax.xaxis.set_major_formatter(date_form)
        drawGrid(ax, ticks=7, minor_ticks=10.)

fig_file = "spot_prices.pdf"
plt.savefig(fig_file, bbox_inches="tight")
print("Saved plot to", fig_file)
