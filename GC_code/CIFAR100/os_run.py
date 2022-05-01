
import os,time

#cifar100 sgd & sgdGCC

print("Running main.py with SGD")
os.system("python  main.py --lr 0.1 --wd 0.0005 --alg sgd --epochs 10  --model r50 > /content/Gradient-Centralization/r50_lr11_wd45_sgd.log")

print("Running main.py with SGDGC")
os.system("python  main.py --lr 0.1 --wd 0.0005 --alg sgdGC --epochs 10  --model r50 > /content/Gradient-Centralization/r50_lr11_wd45_sgdGC.log")
