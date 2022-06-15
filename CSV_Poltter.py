import math
import os
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import math

from matplotlib.ticker import ScalarFormatter

#My Module
import isDirNull

def CSV_Poltter(video_path, DataFrame, is_Check=True):
    basename_without_extension = os.path.splitext(os.path.basename(video_path))[0]
    result_folder_name = "Result"

    os.makedirs(f"./{result_folder_name}", exist_ok=True)
    os.makedirs(f"./{result_folder_name}/{basename_without_extension}", exist_ok=True)
    if(not is_Check):
        isDirNull.result_output_folder(f"./{result_folder_name}/{basename_without_extension}/Figure")

    fig = DataFrame.plot(x='frame', y='liquid_volume')
    fig.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
    y_min, y_max = fig.get_ylim()
    fig.set_ylim(0, y_max)
    plt.xlabel('Frame number', fontsize=16)
    plt.ylabel(r"Estimated volume of liquid [pixel$^3$]", fontsize=14)
    plt.minorticks_on()
    plt.grid(which = "major", axis = "x", color = "gray", alpha = 0.3,linestyle = "-")
    plt.grid(which = "both", axis = "y", color = "gray", alpha = 0.3,linestyle = "-")
    plt.savefig(f"./{result_folder_name}/{basename_without_extension}/Figure/{basename_without_extension}_LV.jpg")
    plt.close('all')
