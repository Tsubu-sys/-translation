#!/usr/bin/python3
import os

def openFileAndReadLines(InpDir, fileName):
    # ファイルが存在するか確認する
    if not os.path.isfile(InpDir + fileName) :
        # 実行引数にファイル名がない場合(多分)
        print('Error: No such file')
        print('\"' + fileName + '\"')
        return None
    else:
        f = open(InpDir + fileName)
        lines = f.readlines()
        f.close()
        return lines
