import numpy as np
from sklearn import linear_model
from sklearn import cross_validation
import matplotlib.pyplot as plt

class LinRegLearner(object):
    def __init__(self, verbose=False):
        pass

    def addEvidence(self, trainX, trainY,testX,testY):
        # Create linear regression object
        regr = linear_model.LinearRegression()

        v = np.ones(6)
        # Train the model using the training sets
        regr.fit(trainX, trainY)

        # The coefficients
        print('Coefficients: \n', regr.coef_)
        # The mean squared error
        print("Mean squared error: %.2f" % np.mean((regr.predict(testX) - testY) ** 2))
        # Explained variance score: 1 is perfect prediction
        print('Variance score: %.2f' % regr.score(testX, testY))

        # # Plot outputs
        # plt.scatter(testX, testY, color='black')
        # plt.plot(testX, regr.predict(testX), color='blue',
        #          linewidth=3)
        #
        # plt.xticks(())
        # plt.yticks(())
        #
        # plt.show()

        # print testX.shape
        # print testY.shape


if __name__ == "__main__":
    print
    "the secret clue is 'zzyzx'"