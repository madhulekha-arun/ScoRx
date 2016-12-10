import math
import sqlite3
import numpy as np
import LinRegLearner as lrl
import RandomForest as rfl
import SVM as svml
from sklearn import linear_model
from sklearn import preprocessing  ## sklern is ML library-- preprocessing
print("Setting experiment values")

conn = sqlite3.connect('/Users/Madhu/Documents/Courses/DVA/project/fresh.db')

c = conn.cursor()

input = np.empty([0, 47])

for row in c.execute('SELECT * FROM final'):
    input = np.vstack([input, row])

# gender,credential
feature_list = [2, 4]
# gradyear,primary spec,
feature_list.extend(range(5, 7), )
# second
feature_list.extend([11], )
# state
feature_list.extend([13], )

feature_list.extend(range(16, 34), )

feature_list.extend(range(36, 47), )

inputX = input[:, feature_list]
inputY = input[:, 35]

inputX_f = np.ones(inputX.shape)
inputY_f = np.ones(inputY.shape)

encoding = preprocessing.LabelEncoder()  ## create label encoding object
# Gender
inputX[:, 0] = encoding.fit_transform(inputX[:, 0])
# Credential
inputX[:, 1] = encoding.fit_transform(inputX[:, 1])
# primary spec
inputX[:, 3] = encoding.fit_transform(inputX[:, 3])
# sec
inputX[:, 4] = encoding.fit_transform(inputX[:, 4])
# state
inputX[:, 5] = encoding.fit_transform(inputX[:, 5])
# form payment
inputX[:, 32] = encoding.fit_transform(inputX[:, 32])
# nature payment
inputX[:, 33] = encoding.fit_transform(inputX[:, 33])

print
inputX[5, :]