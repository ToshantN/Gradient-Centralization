import os,time

print('Runing main.py for SGD')

os.system("python -W ignore main.py /home/yonghw/data/mini_imagenet/split_mini/ --model r50 --epochs 10 -b 128 --alg sgd   > /content/Gradient-Centralization/r50_b128_sgd.log")
os.system("python -W ignore main.py /home/yonghw/data/mini_imagenet/split_mini/ --model r50 --epochs 10-b 128 --alg sgdGC   > /content/Gradient-Centralization/r50_b128_sgdGC.log")
