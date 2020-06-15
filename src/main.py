#!/usr/bin/python3
from googletrans import Translator
import sys

Dir = '/home/tsubu/repos/translation'
OutDir = Dir + '/result/'
InpDir = Dir + '/data/'

# 実行時の引数で読み込むファイルをしている
# main.py file_en.txt
args= sys.argv
if len(args) < 2:
    print('Command should be like')
    print('main.py textfile.txt')
else:
    print('open ' + InpDir + args[1])
    f = open(InpDir + args[1])
    lines = f.readlines()
    f.close()
    
    with open(OutDir + 'sampleResult.txt', 'w') as resultFile:
        for line in lines:
            translator = Translator()
            translated = translator.translate(line, dest="ja");
            print(line, file=resultFile) # English
            print(translated.text, file=resultFile) # Japanese
            print()
    resultFile.close
    print('finished')
