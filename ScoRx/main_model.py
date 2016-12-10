import math
import sqlite3
import numpy as np
import LinRegLearner as lrl
import RandomForest as rfl
import SVM as svml
from sklearn import linear_model
from sklearn import preprocessing  ## sklern is ML library-- preprocessing
import pandas as pd
import matplotlib.pyplot as plt


if __name__=="__main__":
    print("Setting experiment values")

    conn = sqlite3.connect('/Users/Madhu/Downloads/fresh.db')

    c = conn.cursor()

    input=np.empty([0,47])

    for row in c.execute('SELECT * FROM final'):
        input = np.vstack([input, row])

    #gender,credential
    feature_list = [2,4]
    #gradyear,primary spec,
    feature_list.extend(range(5,7), )
    #second
    feature_list.extend([11], )
    #state
    feature_list.extend([13], )
    # 16 | ReportedQualityMeasures | | 0 | | 0
    # 17 | UsedEHR | | 0 | | 0
    # 18 | ParticipatedMedicareMaintenance | | 0 | | 0
    # 19 | CommittedHeartHealth | | 0 | | 0
    # 20 | PQRS_Participation | | 0 | | 0
    # 21 | FluShot | | 0 | | 0
    # 22 | PneumoniaVaccine | | 0 | | 0
    # 23 | DepressionScreening | | 0 | | 0
    # 24 | TobaccoScreening | | 0 | | 0
    # 25 | BodyWeightScreening | | 0 | | 0
    # 26 | BloodPressureScreening | | 0 | | 0
    # 27 | BreastCancerScreening | | 0 | | 0
    # 28 | ColorectalCancerScreening | | 0 | | 0
    # 29 | CompareNewOldMed | | 0 | | 0
    # 30 | ControlBP_InDiabetesPatients | | 0 | | 0
    # 31 | ReduceHeartAttack | | 0 | | 0
    # 32 | HeartFailurePatients | | 0 | | 0
    # 33 | MedToImprovePumpingAction_HeartPatients | | 0 | | 0
    # 34 | Y | | 0 | | 0
    feature_list.extend(range(16,34),)
    # 36 | Total_Claim_Count | INT | 0 | | 0
    # 37 | Total_Day_Supply | INT | 0 | | 0
    # 38 | Total_Drug_Cost | INT | 0 | | 0
    # 39 | Bene_Count_Ge65 | INT | 0 | | 0
    # 40 | Total_Claim_Count_Ge65 | INT | 0 | | 0
    # 41 | Total_Day_Supply_Ge65 | INT | 0 | | 0
    # 42 | Total_Drug_Cost_Ge65 | INT | 0 | | 0
    # 43 | Total_Amount_of_Payment_USDollars | REAL | 0 | | 0
    # 44 | Form_of_Payment_or_Transfer_of_Value | TEXT | 0 | | 0
    # 45 | Nature_of_Payment_or_Transfer_of_Value | TEXT | 0 | | 0
    # 46 | MedSchoolRank | INT | 0 | | 0
    feature_list.extend(range(36,47),)

    inputX=input[:,feature_list]
    inputY=input[:,35]

    inputX_f=np.ones(inputX.shape)
    inputY_f=np.ones(inputY.shape)



    encoding = preprocessing.LabelEncoder()  ## create label encoding object
    inputX[:, 0] = encoding.fit_transform(inputX[:, 0])
    # Credential
    inputX[:, 1] = encoding.fit_transform(inputX[:, 1])
    # primary spec
    inputX[:, 3] = encoding.fit_transform(inputX[:, 3])
    # sec
    inputX[:, 4] = encoding.fit_transform(inputX[:, 4])
    # state
    inputX[:, 5] = encoding.fit_transform(inputX[:, 5])
    #form payment
    inputX[:, 32] = encoding.fit_transform(inputX[:, 32])
    #nature payment
    inputX[:, 33] = encoding.fit_transform(inputX[:, 33])



    for i in range(0,inputX.shape[0]):
        for j in range(0, inputX.shape[1]):
            if(inputX[i,j]==''):
                inputX_f[i,j]=0.0
            else:
                inputX_f[i,j]=float(inputX[i,j])


    for i in range(0,inputY.shape[0]):
        if (inputY[i] == ''):
            inputY_f[i] = 0.0
        else:
            inputY_f[i] = float(inputY[i])

    inputX_f[:, 2] = 2016-inputX_f[:, 2]

    print inputX_f.shape

    #print inputX[5,:]
    cols=['Gender','Credential','Experience','Primary Spec','Sec Spec','State',
    'ReportedQualityMeasures','UsedEHR','ParticipatedMedicareMaintenance','CommittedHeartHealth',
    'PQRS_Participation','FluShot','PneumoniaVaccine','DepressionScreening','TobaccoScreening',
    'BodyWeightScreening','BloodPressureScreening','BreastCancerScreening','ColorectalCancerScreening',
    'CompareNewOldMed','ControlBP_InDiabetesPatients','ReduceHeartAttack','HeartFailurePatients',
    'MedToImprovePumpingAction_HeartPatients',
    'Total_Claim_Count', 'Total_Day_Supply','Total_Drug_Cost','Bene_Count_Ge65','Total_Claim_Count_Ge65',
    'Total_Day_Supply_Ge65','Total_Drug_Cost_Ge65','Total_Amount_of_Payment_USDollars','Payment Form',
          'Payment Nature','MedSchoolRank']
    df = pd.DataFrame(inputX_f, columns=cols)


    # pd.options.display.mpl_style = 'default'
    # df.boxplot()
    #
    # cols = ['Total_Day_Supply', 'Total_Drug_Cost', 'Bene_Count_Ge65', 'Total_Claim_Count_Ge65', 'Total_Day_Supply_Ge65',
    #         'Total_Drug_Cost_Ge65', 'MedSchoolRank']
    # df1 = pd.DataFrame(inputX_f[:, [25, 26, 27, 28, 29, 30, 34]], columns=cols)

    # compute how much of the data is training and testing
    # train_rows = int(math.floor(0.6* inputX.shape[0]))
    # test_rows = inputX.shape[0] - train_rows
    #
    # # separate out training and testing data
    # trainX = inputX_f[:train_rows,:]
    # trainY = inputY_f[:train_rows]
    # testX = inputX_f[train_rows:,:]
    # testY = inputY_f[train_rows:]

    #std_scale = preprocessing.StandardScaler().fit(trainX)
    #trainX = std_scale.transform(trainX)
    #testX = std_scale.transform(testX)
    #     print trainX.shape
    #     lda = LDA(n_components=100)
    #     lda = lda.fit(trainX,trainY)
    #     trainX = lda.transform(trainX)
    #     testX = lda.transform(testX)
    #     print trainX.shape

    # # Linear Regression
    # learner = lrl.LinRegLearner(verbose = True)
    # learner.addEvidence(trainX,trainY,testX,testY)
    #
    #
    # # Random Forest
    # learner = rfl.RandomForest(verbose = True)
    # learner.addEvidence(trainX,trainY,testX,testY)
    #
    # #SVM
    # learner = svml.SupportVectorMachine(verbose=True)
    # learner.addEvidence(trainX, trainY, testX, testY)

    from pandas.tools.plotting import scatter_matrix

    scatter_matrix(df1, alpha=0.2, figsize=(6, 6), diagonal='kde')
