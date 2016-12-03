import math
import sqlite3
import numpy as np
import LinRegLearner as lrl
import RandomForest as rfl
import SVM as svml
from sklearn import linear_model



if __name__=="__main__":
    print("Setting experiment values")

    conn = sqlite3.connect('/Users/Madhu/Documents/Courses/DVA/project/docdata.db')

    c = conn.cursor()

    input=np.empty([0,47],dtype='float')

    for row in c.execute('SELECT * FROM sample'):
        input = np.vstack([input, row])

    feature_list=[5,12]
    feature_list.extend(range(16,34),)
    feature_list.extend(range(36,44),)

    inputX=input[:,feature_list]
    inputY=input[:,35]

    inputX_f=np.ones(inputX.shape)
    inputY_f=np.ones(inputY.shape)

    for i in range(0,inputX.shape[0]):
        for j in range(0, inputX.shape[1]):
            if(inputX[i,j]==''):
                inputX_f[i,j]=0.0
            else:
                inputX_f[i,j]=float(inputX[i,j])


    for i in range(0,inputY.shape[0]):
        inputY_f[i]=float(inputY[i])

    # compute how much of the data is training and testing
    train_rows = int(math.floor(0.6* inputX.shape[0]))
    test_rows = inputX.shape[0] - train_rows

    # separate out training and testing data
    trainX = inputX_f[:train_rows,:]
    trainY = inputY_f[:train_rows]
    testX = inputX_f[train_rows:,:]
    testY = inputY_f[train_rows:]

    # Linear Regression
    learner = lrl.LinRegLearner(verbose = True)
    learner.addEvidence(trainX,trainY,testX,testY)


    # Random Forest
    learner = rfl.RandomForest(verbose = True)
    learner.addEvidence(trainX,trainY,testX,testY)

    #SVM
    learner = svml.SupportVectorMachine(verbose=True)
    learner.addEvidence(trainX, trainY, testX, testY)
