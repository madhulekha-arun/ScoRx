import numpy as np
from hmmlearn.hmm import GaussianHMM
from itertools import permutations
from scipy.linalg import norm
from hmmlearn import hmm
import math
from datetime import datetime
from numpy import genfromtxt
import pandas as pd
import sqlite3
import numpy as np


if __name__=="__main__":
    print("Setting experiment values")

    conn = sqlite3.connect('/Users/Madhu/Documents/Courses/DVA/project/docdata.db')

    c = conn.cursor()

    input=np.empty([0,47])

    for row in c.execute('SELECT * FROM sample'):
        input = np.vstack([input, row])


    #input_file='/Users/Madhu/Documents/Courses/DVA/project/master_table.csv'

    #input=genfromtxt(input_file, delimiter='|')
    #input=input[1:,:]
    #outputarr = np.empty([31,12])

    #orders_df = pd.read_csv(input_file, index_col=id, na_values=['nan'])

    print input