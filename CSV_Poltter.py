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
    # �ۑ��t�H���_�̍쐬�Ɗm�F
    result_folder_name = "Result"
    basename_without_extension = os.path.splitext(os.path.basename(video_path))[0]
    os.makedirs(f"./{result_folder_name}", exist_ok=True)
    os.makedirs(f"./{result_folder_name}/{basename_without_extension}", exist_ok=True)
    if(not is_Check):
        isDirNull.result_output_folder(f"./{result_folder_name}/{basename_without_extension}/Figure")

    # �f�[�^�̓ǂݍ���
    fig = DataFrame.plot(x='frame', y='liquid_volume')
    fig.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
    

    # ���f�[�^�ɂ����y���̊��ς���B
    y_min_raw, y_max_raw = fig.get_ylim()
    
    if y_min_raw > 0:
        y_min = 0
    else:
        y_min = y_min_raw

    if y_max_raw < 0:
        y_max = 0
    else:
        y_max = y_max_raw

    fig.set_ylim(y_min, y_max)

    # ���x���ݒ�
    plt.xlabel('Frame number', fontsize=16)
    plt.ylabel(r"Estimated volume of liquid [pixel$^3$]", fontsize=14)
    
    # �O���b�h�ݒ�
    plt.minorticks_on()
    plt.grid(which = "major", axis = "x", color = "gray", alpha = 0.3,linestyle = "-")
    plt.grid(which = "both", axis = "y", color = "gray", alpha = 0.3,linestyle = "-")
    
    # �ۑ�
    plt.savefig(f"./{result_folder_name}/{basename_without_extension}/Figure/{basename_without_extension}_LV.jpg")
    plt.close('all')
