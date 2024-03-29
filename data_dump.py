import pymongo
import pandas as pd 
import json


client = pymongo.MongoClient("mongodb+srv://Rahul7898:7898913258@cluster0.5ypoism.mongodb.net/?retryWrites=true&w=majority")


DATA_FILE_PATH = "/config/workspace/insurance.csv.2"
DATABASE_NAME =   "INSURANCE"
COLLECTION_NAME = "INSURANCE_PROJECT"


if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Row and columns:{df.shape}")

    #convert dataframe to json so that we can dump these records in mongo db
    df.reset_index(drop=True , inplace = True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])


    #insert converted json record to mongo db
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
