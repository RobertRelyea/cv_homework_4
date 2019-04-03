import sympy
import numpy as np
import matplotlib.pyplot as plt
import pdb

def solvel2(R_val,l1_val,K_val):
    l2 = sympy.symbols('l2')
    equation = (l1_val*l2) - K_val*((l1_val + l2)**2)
    l2_vals = sympy.solve([sympy.Eq(equation, R_val)], [l2])
    return l2_vals

def getl2(R_val, l1_vals, K_val):
    pos_arr, neg_arr = [], []
    for l1_val in l1_vals:
        l2_vals = solvel2(R_val, l1_val, K_val)
        neg_arr.append(l2_vals[0])
        if len(l2_vals) > 1:
            pos_arr.append(l2_vals[1])
    return pos_arr, neg_arr

l1_vals = np.arange(0.0, 50.0, 0.5)

R_vals = [0.5, 10, 40]
K_vals = [0.05] * 3

for (R, K) in zip(R_vals, K_vals):
    pos_arr, neg_arr = getl2(R, l1_vals, K)

    plt.scatter(l1_vals, neg_arr)
    plt.title("R = " + str(R) + ", K = " + str(K))
    plt.xlabel('Lambda1')
    plt.xlim(0,50)
    plt.ylabel('Lambda2')
    plt.ylim(0,50)
    plt.grid()
    plt.show()
    ans = input("Good fig?")
    if ans == 'y' or ans == 'Y':
        plt.savefig('R{}K{}.png'.format(R, K))
