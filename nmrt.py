from sys import *
from os import *
from time import *
from subprocess import *

def bd(idir):

    files = listdir(idir)
    for file in files:
        fn = file.split(".")[0]
        mkdir("_extracted/" + fn)
        Popen("quickbms.exe decompress.bms " + idir + "/" + file + " _extracted/" + fn)
        sleep(1)
        Popen("quickbms.exe decompress.bms _extracted/" + fn + "/" + fn + ".arc _extracted/" + fn)

def d(file):
    fn = file.split(".")[0]
    mkdir("_extracted/" + fn)
    Popen("quickbms.exe decompress.bms " + file + " _extracted/" + fn)
    sleep(1)
    Popen("quickbms.exe decompress.bms _extracted/" + fn + "/" + fn + ".arc _extracted/" + fn)