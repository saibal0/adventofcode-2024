import sys
import pandas as pd
import numpy as np
from collections import defaultdict

def run(file):
    file_content = pd.read_csv(file, delimiter='   ', names =['list1','list2'], engine='python')
    # print(file_content.head(1))
    
    # Question 1
    list_1 = sorted(file_content.list1.to_list())
    list_2 = sorted(file_content.list2.to_list())
    final_list = (abs(np.array(list_2) - np.array(list_1))).tolist()
    print("01. Answer: {}".format(sum(final_list)))

    # Question 2
    list_1 = file_content.list1.to_list()
    list_2 = file_content.list2.to_list()

    final_list = [var * list_2.count(var) for var in list_1]
    # print(final_list)
    print("02. Answer: {}".format(sum(final_list)))

if __name__ == '__main__':
    # print(sys.argv)
    file=sys.argv[1]
    run(file)