#!/usr/bin/python3
from googletrans import Translator
import sys
import functions as func

Dir = '/home/tsubu/repos/translation'
OutDir = Dir + '/result/'
InpDir = Dir + '/data/'

# 実行時の引数で読み込むファイルをしている
# main.py file_en.txt
args= sys.argv
if len(args) < 2:
    print('Command should be like')
    print('\"./main.py fileName\"')
else:
    # ファイルを開き、ラインを返す関数
    lines = func.openFileAndReadLines(InpDir, args[1])
    if lines is None:
        # ファイルが存在しなかった場合
        sys.exit(0)

    with open(OutDir + 'sampleResult.txt', 'w') as resultFile:
        for line in lines:
            translator = Translator()
            translated = translator.translate(line, dest="ja");
            print(line, file=resultFile) # English
            print(translated.text, file=resultFile) # Japanese
    resultFile.close
    print('finished')
