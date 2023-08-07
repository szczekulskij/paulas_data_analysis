from statistics import mean
from src.data_generator import get_data, add_bucket_AQ10_Score
from scipy.stats import ttest_rel as ttest_related
from scipy.stats import ttest_ind as ttest_not_related


def get_statistics_for_AQ10(grouping_interval):
    print(f"grouping_interval: {grouping_interval}")
    COLUMNS_TO_RUN_TT_TEST_ON = [
        # "Education",
        # "BUCKETED_Education",
        # "Gender",
        # "Handedness",
        "TextureScore",
        "PleasantnessSum",
        "WeightScore",
        "SummedUpScore",
        "FullGuessScore"
    ]
    df = get_data()
    # df = df.loc[df["Gender"] == "female"]
    # df = df.loc[df["Gender"] == "male"]

    # df = df.loc[df["Handedness"] == "left"]
    # df = df.loc[df["Handedness"] == "right"]
    df = add_bucket_AQ10_Score(df, grouping_interval)
    if len(grouping_interval) == 3:
        autismTypes = ["noAutism", "Autism"]
    elif len(grouping_interval) == 4:
        autismTypes = ["noAutism", "littleAutism", "Autism"]
    else : raise Exception("error nr 98127389")

    subDFs = []
    for autismType in autismTypes:
        subDFs.append(
            df.loc[df["BUCKETED_AQ10_Score"] == autismType]
        )
    for columnName in COLUMNS_TO_RUN_TT_TEST_ON:
        subList = []
        for subDf in subDFs:
            subList.append(list(subDf[columnName]))

        if len(subList) == 2:
            print(f"columnName: {columnName}")
            print(f"len left: {len(subList[0])}| len right: {len(subList[1])}")
            print(f"mean left: {round(mean(subList[0]),2)}| mean right: {round(mean(subList[1]),2)}")
            statistics, p_value = ttest_not_related(subList[0], subList[1], alternative = 'greater')
            print(f"p_value for alternative greater: {round(p_value,2)}")
            statistics, p_value = ttest_not_related(subList[0], subList[1], alternative = 'less')
            print(f"p_value for alternative less {round(p_value,2)}")

        elif len(subList) == 3:
            print(f"columnName: {columnName}")
            print(f"len left: {len(subList[0])} | len middle: {len(subList[1])} | len right: {len(subList[2])}")
            print(f"mean left: {round(mean(subList[0]),2)} | mean middle: {round(mean(subList[1]),2)} | mean right: {round(mean(subList[1]),2)}")
            statistics, p_value = ttest_not_related(subList[0], subList[1], alternative = 'greater')
            print(f"p_value for alternative greater (between 1st and 2nd entry): {round(p_value,2)}")
            statistics, p_value = ttest_not_related(subList[1], subList[2], alternative = 'greater')
            print(f"p_value for alternative greater (between 2nd and 3rd entry):: {round(p_value,2)}")

            print(f"len left: {len(subList[0])} | len middle: {len(subList[1])} | len right: {len(subList[2])}")
            print(f"mean left: {mean(subList[0])} | mean middle: {mean(subList[1])} | mean right: {mean(subList[1])}")
            statistics, p_value = ttest_not_related(subList[0], subList[1], alternative = 'less')
            print(f"p_value for alternative less (between 1st and 2nd entry): {round(p_value,2)}")
            statistics, p_value = ttest_not_related(subList[1], subList[2], alternative = 'less')
            print(f"p_value for alternative less (between 2nd and 3rd entry) : {round(p_value,2)}")
        else : raise Exception("error nr 12937261389")

        print("-------------------------------")
    print("\n")