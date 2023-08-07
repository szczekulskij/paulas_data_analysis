
from numpy import mean
import pandas as pd 
def get_data():
    raw_data = pd.read_excel("data.xlsx")

    raw_data["Object1FullGuess"] = raw_data.apply(lambda row : 1 if (row["O1AssigTex_X_Rep"] + row["O1AssigSize_X_Rep"] + row["O1AssigWeight_X_Rep"]) == 3 else 0 , axis = 1)
    raw_data["Object2FullGuess"] = raw_data.apply(lambda row : 1 if (row["O2AssigTex_X_Rep"] + row["O2AssigSize_X_Rep"] + row["O2AssigWeight_X_Rep"]) == 3 else 0 , axis = 1)
    raw_data["Object3FullGuess"] = raw_data.apply(lambda row : 1 if (row["O3AssigTex_X_Rep"] + row["O3AssigSize_X_Rep"] + row["O3AssigWeight_X_Rep"]) == 3 else 0 , axis = 1)
    raw_data["Object4FullGuess"] = raw_data.apply(lambda row : 1 if (row["O4AssigTex_X_Rep"] + row["O4AssigSize_X_Rep"] + row["O4AssigWeight_X_Rep"]) == 3 else 0 , axis = 1)
    raw_data["PleasantnessSum"] = raw_data.apply(lambda row : mean(row["O1_Pleasantness"] + row["O2_Pleasantness"] + row["O3_Pleasantness"] +row["O4_Pleasantness"]), axis = 1)
    raw_data["selfIdentyfing"] = raw_data.apply(lambda row : "noSpecialIlnesses" if row["Self_ID"] == 6 else "SpecialIlness" , axis = 1)

    raw_data["TextureScore"] = raw_data["O1AssigTex_X_Rep"] + raw_data["O2AssigTex_X_Rep"] + raw_data["O3AssigTex_X_Rep"] + raw_data["O4AssigTex_X_Rep"]
    raw_data["SizeScore"] = raw_data["O1AssigSize_X_Rep"] + raw_data["O2AssigSize_X_Rep"] + raw_data["O3AssigSize_X_Rep"] + raw_data["O4AssigSize_X_Rep"]
    raw_data["WeightScore"] = raw_data["O1AssigWeight_X_Rep"] + raw_data["O2AssigWeight_X_Rep"] + raw_data["O3AssigWeight_X_Rep"] + raw_data["O4AssigWeight_X_Rep"]
    # raw_data["SummedUpScore"] = raw_data["TextureScore"] + raw_data["SizeScore"] + raw_data["WeightScore"]
    # remove size score
    raw_data["SummedUpScore"] = raw_data["TextureScore"] +  raw_data["WeightScore"]
    raw_data["FullGuessScore"] = raw_data["Object1FullGuess"] + raw_data["Object2FullGuess"] + raw_data["Object3FullGuess"] +raw_data["Object4FullGuess"]

    raw_data["Gender"] = raw_data.apply(lambda row : "male" if row["Gender"] == 1 else "female", axis = 1)
    raw_data["Handedness"] = raw_data.apply(lambda row : "left" if row["Handedness"] == 1 else "right", axis = 1)
    # Add another way to looking at Education
    raw_data["BUCKETED_Education"] = raw_data.apply(lambda row : 
                                        "UG" if int(row["Education"]) in [1,2,3] else \
                                        "gradNHigher" if row["Education"] in [4,5] else \
                                        "Other"
                                        ,axis=1)

    raw_data["Education"] = raw_data.apply(lambda row : 
                                           "UG1" if row["Education"] == 1 else \
                                           "UG2" if row["Education"] == 2 else \
                                           "UG3" if row["Education"] == 3 else \
                                           "PhD" if row["Education"] == 4 else \
                                           "postGrad" if row["Education"] == 5 else \
                                           "Other"
                                           ,axis=1)

    return raw_data.copy(deep = True)\
                [[
                # Metrics for checking correlation
                "Participant_N", "Age", "Education", "BUCKETED_Education", "Gender",
                "Handedness", "Self_ID", "AQ10_Score", "Hand_Cms", "Arm_Cms", "selfIdentyfing",

                # Score metrics
                "TextureScore", "SizeScore", "WeightScore", "SummedUpScore", 
                "FullGuessScore", "PleasantnessSum"
                ]]   
    

    
# Add a new (bucketed) column for grouping AQ_10_Score
def add_bucket_AQ10_Score(df, grouping_interval):
    '''
    grouping_interval like [0,4,7,10]
    '''
    # Check
    if 0 not in grouping_interval or 10 not in grouping_interval: raise Exception("len(grouping_interval) has to be either 3 or 4, and has to incldue 0 and 10")
    if len(grouping_interval)==3:
        def row_func(int):
            if int <=grouping_interval[1]: return "noAutism"
            else : return "Autism"
    elif len(grouping_interval)==4:
        def row_func(int):
            if int <=grouping_interval[1]: return "noAutism"
            elif int <=grouping_interval[2]: return "littleAutism"
            else : return "Autism"
    else: 
        raise Exception("len(grouping_interval) has to be either 3 or 4, and has to incldue 0 and 10")
    df["BUCKETED_AQ10_Score"] = df.apply(lambda row : row_func(row["AQ10_Score"]), axis = 1)
    return df