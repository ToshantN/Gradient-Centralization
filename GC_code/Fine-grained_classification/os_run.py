
import os,time

os.system("python -W ignore main.py /content/fgvc_aircraft/ --model r18p --epochs 10 -b 128 --alg sgd --dataset fgvc")
os.system("python -W ignore main.py /content/fgvc_aircraft/ --model r18p --epochs 10 -b 128 --alg sgdGC --dataset fgvc")
