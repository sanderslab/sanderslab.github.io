#!/usr/bin/env python
# Optimize sizes for images/videos displayed in table format
# Author: David Young, 2020

import os
import sys

import pandas as pd


def main(path, max_width, group_col="Age"):
    """Optimize sizes of images or videos displayed in a table format,
    assuming that items in the same group will be displayed in the same row
    with a uniform height maximized for the allowed width.

    Takes a CSV file with a columns for grouping, Height, and Width.
    Items in the same group will be given a uniform height, with widths
    adjusted to keep the same aspect ratio while maximizing the allowed
    dimensions. Outputs a CSV with columns appended for the new height
    and width.

    Args:
        path (str): Path to CSV.
        max_width (int): Maximum width.
        group_col (str): Name of grouping column; defaults to "Age".

    Returns:

    """
    df = pd.read_csv(path)
    print(df)
    ages = df[group_col]
    resized = {}
    for age in ages.unique():
        atlases = df.loc[ages == age]
        # max height is limited by minimum height fitting within max width
        hts = (atlases["Height"] * max_width).div(atlases["Width"])
        ht = min(hts)
        # adjust widths to this uniform height
        widths = (atlases["Width"] * ht).div(atlases["Height"])
        resized.setdefault("Height_new", []).extend([ht] * len(atlases))
        resized.setdefault("Width_new", []).extend(widths)
    df = pd.concat([df, pd.DataFrame(resized)], axis=1)
    df.to_csv("{}_resized{}".format(*os.path.splitext(path)))


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Please supply args in the format: python optimize_size "
              "path max_width")
        sys.exit(1)
    main(sys.argv[1], int(sys.argv[2]))
