select *
from
(
select * from GroupPrac_COC  where DepressionScreening!='' and PQRS_Participation!=''
)
a
join
GroupPrac_PatientExp b
on
a.G_PAC_ID=b.G_PAC_ID
join
PhysicianCompare c
on
a.G_PAC_ID=c.G_PAC_ID
limit 20

create table physician as
select NPI,FirstName,LastName, a.G_PAC_ID as G_PAC_ID,Gender, Credential, MedSchool, GradYear, PrimarySpec, SecSpec1, SecSpec2, SecSpec3, SecSpec4, AllSecSpecs, NumGroupPracMembers, City, State, ZipCode, AcceptMedicareAssignment, ReportedQualityMeasures, UsedEHR, ParticipatedMedicareMaintenance, CommittedHeartHealth,PQRS_Participation, FluShot, PneumoniaVaccine, DepressionScreening, TobaccoScreening, BodyWeightScreening, BloodPressureScreening, BreastCancerScreening, ColorectalCancerScreening, CompareNewOldMed, ControlBP_InDiabetesPatients, ReduceHeartAttack, HeartFailurePatients, MedToImprovePumpingAction_HeartPatients,Y
from
(select NPI, FirstName,LastName, G_PAC_ID,Gender, Credential, MedSchool, GradYear, PrimarySpec, SecSpec1, SecSpec2, SecSpec3, SecSpec4, AllSecSpecs, NumGroupPracMembers, City, State, ZipCode, AcceptMedicareAssignment, ReportedQualityMeasures, UsedEHR, ParticipatedMedicareMaintenance, CommittedHeartHealth
from PhysicianCompare )a
join(select G_PAC_ID,
case when PQRS_Participation='Y' then 1 else 0 end as PQRS_Participation,
FluShot, PneumoniaVaccine, DepressionScreening, TobaccoScreening, BodyWeightScreening, BloodPressureScreening, BreastCancerScreening, ColorectalCancerScreening, CompareNewOldMed, ControlBP_InDiabetesPatients, ReduceHeartAttack, HeartFailurePatients, MedToImprovePumpingAction_HeartPatients
from GroupPrac_COC  where DepressionScreening!='' and PQRS_Participation!='') b
on
a.G_PAC_ID=b.G_PAC_ID
join
(select G_PAC_ID ,TimelyCare + Communication + PromoEdu + PatRating + Helpfulness + WorkingTogether + BetweenVisit + AttToMedCost as Y from GroupPrac_PatientExp group by G_PAC_ID) c
on
a.G_PAC_ID=c.G_PAC_ID

create table u_physician_raw as
select NPI,FirstName||' '||LastName as name,Gender, Credential, MedSchool, GradYear, PrimarySpec, SecSpec1, SecSpec2, SecSpec3, SecSpec4,AllSecSpecs, avg(NumGroupPracMembers), City, State, ZipCode, avg(AcceptMedicareAssignment) as AcceptMedicareAssignment, avg(ReportedQualityMeasures) as ReportedQualityMeasures, avg(UsedEHR) as UsedEHR, avg(ParticipatedMedicareMaintenance) as ParticipatedMedicareMaintenance, avg(CommittedHeartHealth) as CommittedHeartHealth,avg(PQRS_Participation) as PQRS_Participation, avg(FluShot) as FluShot, avg(PneumoniaVaccine) as PneumoniaVaccine, avg(DepressionScreening) as DepressionScreening, avg(TobaccoScreening) as TobaccoScreening, avg(BodyWeightScreening) as BodyWeightScreening, avg(BloodPressureScreening) as BloodPressureScreening, avg(BreastCancerScreening) as BreastCancerScreening, avg(ColorectalCancerScreening) as ColorectalCancerScreening, avg(CompareNewOldMed) as CompareNewOldMed, avg(ControlBP_InDiabetesPatients) as ControlBP_InDiabetesPatients, avg(ReduceHeartAttack) as ReduceHeartAttack, avg(HeartFailurePatients) as HeartFailurePatients, avg(MedToImprovePumpingAction_HeartPatients) as MedToImprovePumpingAction_HeartPatients,avg(Y) as Y
from physician
group by NPI,name,Gender,Credential,MedSchool, GradYear, PrimarySpec, SecSpec1, SecSpec2, SecSpec3, SecSpec4,AllSecSpecs
having count(distinct City)=1 and count(distinct State)=1 and count(distinct ZipCode)=1


create table u_physician as
select a.*,Bene_Count,Total_Claim_Count,Total_Day_Supply,Total_Drug_Cost,Bene_Count_Ge65,Total_Claim_Count_Ge65,Total_Day_Supply_Ge65,Total_Drug_Cost_Ge65,
Total_Amount_of_Payment_USDollars,Form_of_Payment_or_Transfer_of_Value,Nature_of_Payment_or_Transfer_of_Value
from
u_physician_raw a
join
(
select Npi,Bene_Count,Total_Claim_Count,Total_Day_Supply,Total_Drug_Cost,Bene_Count_Ge65,Total_Claim_Count_Ge65,Total_Day_Supply_Ge65,Total_Drug_Cost_Ge65
from Prescription
)b
on
a.NPI=b.Npi
join
(
select Physician_First_Name||' '||Physician_Last_Name as name,Total_Amount_of_Payment_USDollars,Form_of_Payment_or_Transfer_of_Value,Nature_of_Payment_or_Transfer_of_Value
from Payments
)c
on
a.name=c.name

create table physician_800_raw as
select a.*,DepressionScreening,TobaccoScreening,BodyWeightScreening,BloodPressureScreening,CompareNewOldMed,ReduceHeartAttack from
u_phycisian a join
( select * from IndEPPublicReporting_COC where DepressionScreening!=' ' or ) b
on a.NPI=b.NPI

create table u_physician_temp as
select a.*,Bene_Count,Total_Claim_Count,Total_Day_Supply,Total_Drug_Cost,Bene_Count_Ge65,Total_Claim_Count_Ge65,Total_Day_Supply_Ge65,Total_Drug_Cost_Ge65
from
u_physician_raw a
join
(
select Npi,Bene_Count,Total_Claim_Count,Total_Day_Supply,Total_Drug_Cost,Bene_Count_Ge65,Total_Claim_Count_Ge65,Total_Day_Supply_Ge65,Total_Drug_Cost_Ge65
from Prescription
)b
on
a.NPI=b.Npi

create table physician_final
as
select a.*,Total_Amount_of_Payment_USDollars,Form_of_Payment_or_Transfer_of_Value,Nature_of_Payment_or_Transfer_of_Value
from
u_physician_temp a
join
(
select Physician_First_Name||' '||Physician_Last_Name as name,Total_Amount_of_Payment_USDollars,Form_of_Payment_or_Transfer_of_Value,Nature_of_Payment_or_Transfer_of_Value
from Payments
)c
on
a.name=c.name


create table physician_final_clear
as
select *
from physician_final group by 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46,47;





Bene_Count,Total_Claim_Count,Total_Day_Supply,Total_Drug_Cost,Bene_Count_Ge65,Total_Claim_Count_Ge65,Total_Day_Supply_Ge65,Total_Drug_Cost_Ge65
Total_Amount_of_Payment_USDollars,Form_of_Payment_or_Transfer_of_Value,Nature_of_Payment_or_Transfer_of_Value

input=np.empty([0,47])

for row in c.execute('SELECT * FROM sample'):
	input = np.vstack([input, row])

inputX=input[:,feature_list]
inputY=input[:,35]



for i in range(0,inputX.shape[0]):
	for j in range(0, inputX.shape[1]):
		if(inputX[i,j]==''):
			inputX[i,j]=0.0
		else:
			inputX[i,j]=float(inputX[i,j])


train_rows = math.floor(0.6* inputX.shape[0])
test_rows = inputX.shape[0] - train_rows  # separate out training and testing data
trainX = inputX[:train_rows,:]
trainY = inputY[:train_rows]
testX = inputX[train_rows:,:]
testY = inputY[train_rows:]
  # Create linear regression object regr = linear_model.LinearRegression()  # Train the model using the training sets regr.fit(trainX, trainY)






