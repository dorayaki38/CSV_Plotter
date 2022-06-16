import math
import os
from numpy.core.shape_base import stack
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
import tkinter.filedialog

from matplotlib.ticker import ScalarFormatter
from pandas.core.frame import DataFrame

#My Module
import isDirNull

class CSV_Poltter:
	def csv_poltter(self, file_path: str = None, is_Check: bool =True):
		print("csv_poltter")
		while not file_path:
			file_path = self._open_folder()

		# 保存フォルダの作成と確認
		result_folder_name = "Result"
		basename_without_extension = os.path.splitext(os.path.basename(file_path))[0]
		os.makedirs(f"./{result_folder_name}", exist_ok=True)
		os.makedirs(f"./{result_folder_name}/{basename_without_extension}", exist_ok=True)
		if(not is_Check):
			isDirNull.result_output_folder(f"./{result_folder_name}/{basename_without_extension}/Figure")

		# データの読み込み
		dataframe: DataFrame = pd.read_csv(file_path)
		axes_x_name = self._ask_which_data_to_use(dataframe, "x")
		axes_y_name = self._ask_which_data_to_use(dataframe, "y")
		
		fig  = dataframe.plot(x = axes_x_name, y = axes_y_name)
		fig.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
	
		# y軸のリミットを設定
		fig.set_ylim(self._cal_ylim(fig))

		# ラベル設定
		plt.xlabel('Frame number', fontsize=16)
		plt.ylabel(r"Estimated volume of liquid [pixel$^3$]", fontsize=14)
	
		# グリッド設定
		plt.minorticks_on()
		plt.grid(which = "major", axis = "x", color = "gray", alpha = 0.3,linestyle = "-")
		plt.grid(which = "both", axis = "y", color = "gray", alpha = 0.3,linestyle = "-")
	
		# 保存
		path_savefig = f"./{result_folder_name}/{basename_without_extension}/{basename_without_extension}_{axes_y_name}.jpg"
		plt.savefig(path_savefig)
		print(f"{path_savefig} にグラフを保存しました。")
		plt.close('all')


	def _open_folder(self) -> str:
		print("グラフ化するCSVファイルを選んでください")
		file_type = [('CSVファイル', '*.csv'),('CSVファイル', '*.txt')]
		
		root = tkinter.Tk()
		
		file_path = None
		file_path = tkinter.filedialog.askopenfilename(filetypes = file_type, initialdir = ".")

		root.destroy()
		return file_path

	def _cal_ylim(self, fig, y_min: float = 0, y_max: float = 0) -> (float, float):
		# 元データによってy軸の基準を変える。
		y_min_raw, y_max_raw = fig.get_ylim()
		
		if not y_min != 0:
			if y_min_raw > 0:
				y_min = 0
			else:
				y_min = y_min_raw

		if not y_max != 0:
			if y_max_raw < 0:
				y_max = 0
			else:
				y_max = y_max_raw * 1.1 # 上限ギリギリだと見にくいので10%のマージン

		return y_min, y_max

	def _ask_which_data_to_use(self, dataframe: DataFrame, axis: str) -> str:
		headers = list(dataframe.columns.values)
		
		print(f"Q : どの列を {axis} 軸に設定しますか。")
		index_count: int = 0
		for i, header in enumerate(headers):
			print(f"{i} : {headers[i]}")
			index_count += 1

		select: int = -1
		while select < 0 or index_count - 1 < select:
			try:
				select = int(input('インデックスを指定してください: '))
			except:
				print("整数で入力してください。")
		print(f"{axis} 軸に{headers[select]} を設定しました。")
		return str(headers[select])

if __name__ == '__main__':
	poltter = CSV_Poltter()
	poltter.csv_poltter()
