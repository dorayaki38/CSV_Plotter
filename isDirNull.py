import os
import shutil

def result_output_folder(filePath):
	while not os.listdir(filePath) == []:
		inputvalue = input("結果出力先フォルダには既にファイルがあるようです。\n続行する場合はyを、既存のファイルを全て消して続行するにはrを押してください。")
		if inputvalue == 'y':
			break
		if inputvalue == 'r':
			shutil.rmtree(filePath)
			os.mkdir(filePath)
			break