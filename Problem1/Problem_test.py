import Problem 
import torch
import csv
import sys
import numpy as np

PATH = "~/Testcase/Lab02/Problem1/"

def getAddress(x):
    return PATH + "ex" + str(x) + ".csv"

def test_Problem1():
    ## need to implement grading code
    ## test run example : ./Test.py 1
    for num in range(1,4):
        with open(getAddress(num), "r") as f:
            rdr = csv.reader(f)
            arr = [line for line in rdr][1:]

            train_data = arr[:-3]
            test_data = arr[-3:]
            
            ## process torch.Tensor and make comparsion
            ## Answer should be < 1% relative error.
            
            train_tensor = torch.FloatTensor(np.float_(train_data))
            x_train = train_tensor[:,0]
            train_label = train_tensor[:,1]
            w, b = Problem.train(x_train,train_label)
            
            test_tensor = torch.FloatTensor(np.float_(test_data))
            x_test = test_tensor[:,0]
            test_label = test_tensor[:,1]
            y = w*x_test+b
            
            error = 1e-1 * test_label

            assert(all(abs(test_label - y) < error)) 