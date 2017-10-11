import pandas as pd
data = pd.read_csv("data_fileCRDC2013_14.csv",encoding="Latin-1")
data["total_enrollment"] = data["TOT_ENR_M"] + data["TOT_ENR_F"]
array = ["SCH_ENR_HI_M","SCH_ENR_HI_F","SCH_ENR_AM_M","SCH_ENR_AM_F","SCH_ENR_AS_M","SCH_ENR_AS_F","SCH_ENR_HP_M","SCH_ENR_HP_F","SCH_ENR_BL_M","SCH_ENR_BL_F","SCH_ENR_WH_M","SCH_ENR_WH_F","SCH_ENR_TR_M","SCH_ENR_TR_F"]
enr = {}
for val in array:
    enr[val] = data[val].sum()
    
all_enrollment = data["total_enrollment"].sum()

print(enr)
print("#############################")
print(all_enrollment)
print("#############################")
per_enr = {}
for val in enr:
    per_enr[val] = enr[val] / (all_enrollment) * 100
    
print(per_enr)
    

