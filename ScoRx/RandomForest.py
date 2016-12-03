import numpy as np
from sklearn import linear_model
from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from sklearn import cross_validation

class RandomForest(object):
    def __init__(self, verbose=False):
        pass

    def addEvidence(self, trainX, trainY,testX,testY):

        rf = RandomForestClassifier(n_estimators=100, criterion='gini', max_depth=10, min_samples_split=5, verbose=0,
                                    random_state=0)  ## create RF object
        scores = cross_validation.cross_val_score(rf, trainX, trainY, scoring='accuracy',
                                                  cv=3)  ##scoring='mean_squared_error'
        rf_model = rf.fit(trainX, trainY)  ## Train the model for 2013
        print scores  ## Cross validation score

        # print rf_model.score(testX, testY)

        # The coefficients
        # print('Coefficients: \n', rf.coef_)
        # The mean squared error
        print("Mean squared error: %.2f" % np.mean((rf.predict(testX) - testY) ** 2))
        # Explained variance score: 1 is perfect prediction
        print('Variance score: %.2f' % rf.score(testX, testY))

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