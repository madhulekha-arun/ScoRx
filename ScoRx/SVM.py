import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt
from sklearn import cross_validation

class SupportVectorMachine(object):
    def __init__(self, verbose=False):
        pass

    def addEvidence(self, trainX, trainY,testX,testY):
        lin_svm = svm.LinearSVC(C=1.0, class_weight=None, dual=True, fit_intercept=True,
                                intercept_scaling=1, loss='squared_hinge', max_iter=1000,
                                multi_class='ovr', penalty='l2', random_state=None, tol=0.0001,
                                verbose=0)

        scores = cross_validation.cross_val_score(lin_svm, trainX, trainY, scoring='accuracy',
                                                  cv=3)  ##scoring='mean_squared_error'
        svm_model = lin_svm.fit(testX, testY)  ## Train the model for 2013
        print scores  ## Cross validation score

        # print rf_model.score(testX, testY)

        # The coefficients
        # print('Coefficients: \n', rf.coef_)
        # The mean squared error
        print("Mean squared error: %.2f" % np.mean((lin_svm.predict(testX) - testY) ** 2))
        # Explained variance score: 1 is perfect prediction
        print('Variance score: %.2f' % lin_svm.score(testX, testY))


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