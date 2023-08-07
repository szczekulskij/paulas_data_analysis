import pandas as pd 
def get_data():
    raw_data = pd.read_excel("data.xlsx")

    raw_data["Object1FullGuess"] = raw_data.apply(lambda row : 1 if (row["O1AssigTex_X_Rep"] + row["O1AssigSize_X_Rep"] + row["O1AssigWeight_X_Rep"]) == 3 else 0 , axis = 1)
    raw_data["Object2FullGuess"] = raw_data.apply(lambda row : 1 if (row["O2AssigTex_X_Rep"] + row["O2AssigSize_X_Rep"] + row["O2AssigWeight_X_Rep"]) == 3 else 0 , axis = 1)
    raw_data["Object3FullGuess"] = raw_data.apply(lambda row : 1 if (row["O3AssigTex_X_Rep"] + row["O3AssigSize_X_Rep"] + row["O3AssigWeight_X_Rep"]) == 3 else 0 , axis = 1)
    raw_data["Object4FullGuess"] = raw_data.apply(lambda row : 1 if (row["O4AssigTex_X_Rep"] + row["O4AssigSize_X_Rep"] + row["O4AssigWeight_X_Rep"]) == 3 else 0 , axis = 1)


    raw_data["TextureScore"] = raw_data["O1AssigTex_X_Rep"] + raw_data["O2AssigTex_X_Rep"] + raw_data["O3AssigTex_X_Rep"] + raw_data["O4AssigTex_X_Rep"]
    raw_data["SizeScore"] = raw_data["O1AssigSize_X_Rep"] + raw_data["O2AssigSize_X_Rep"] + raw_data["O3AssigSize_X_Rep"] + raw_data["O4AssigSize_X_Rep"]
    raw_data["WeightScore"] = raw_data["O1AssigWeight_X_Rep"] + raw_data["O2AssigWeight_X_Rep"] + raw_data["O3AssigWeight_X_Rep"] + raw_data["O4AssigWeight_X_Rep"]
    raw_data["SummedUpScore"] = raw_data["TextureScore"] + raw_data["SizeScore"] + raw_data["WeightScore"]
    raw_data["FullGuessScore"] = raw_data["Object1FullGuess"] + raw_data["Object2FullGuess"] + raw_data["Object3FullGuess"] +raw_data["Object4FullGuess"]

    raw_data["Gender"] = raw_data.apply(lambda row : "male" if row["Gender"] == 1 else "female", axis = 1)
    raw_data["Handedness"] = raw_data.apply(lambda row : "left" if row["Handedness"] == 1 else "right", axis = 1)
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
                "Participant_N", "Age", "Education", "Gender",
                "Handedness", "Self_ID", "AQ10_Score", "Hand_Cms", "Arm_Cms",

                # Score metrics
                "TextureScore", "SizeScore", "WeightScore", "SummedUpScore", 
                "FullGuessScore",
                # "Object1FullGuess", "Object2FullGuess", "Object3FullGuess", "Object4FullGuess"
                ]]   
    

    