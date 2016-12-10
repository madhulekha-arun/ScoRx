# ScoRx
DVA Project - Generate Medic Score for Doctors and create recommendations for patients 

This repo contains the code for modelling the scoRx for each physician. There are 3 models that we have tried. 
Random Forest
SVM
Linear Regression

In order to run it we need a connection to be made to an sqlite database that contains the master table. This master table is formed from combining many data sources which is listed at the bottom of this document. All of that need to be downloaded and the sql script to create tables (ScoRx/ScoRx/scripts/sql/create_tables.sql) which is part of this repo needs to be run. After that the main script (ScoRx/ScoRx/master_table.sql) needs to be run which will create the master table.

Once the data set up is completed, we can run the main python script () which will perform all the feature creation, selection, model running. The dependencies are already imported, therefore no further process is required.





