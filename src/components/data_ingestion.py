import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from pymongo import MongoClient

@dataclass
class DataIngestionconfig:
    train_data_path=os.path.join('artifacts','train.csv')
    test_data_path=os.path.join('artifacts','test.csv')
    raw_data_path=os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionconfig()
    
    def initiateDataIngestion(self):
        logging.info('Data ingestion started!')

        try:
            logging.info('Setting connection with MongoDB')
            client=MongoClient('mongodb://localhost:27017/')
            db=client['breast_cancer']
            col=db['cancer']
            logging.info('Connection done and collection intialised!')
            cur=col.find({})
            data=list(cur)
            logging.info('Data fetched from MongoDB')
            df=pd.DataFrame(data)
            
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info('Dataset saved in csv')

            train_set,test_set=train_test_split(df,test_size=0.3,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,Header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,Header=True)
            logging.info('Train and test datasets saved!')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )


        except Exception as e:
            logging.info('Error occured in Data Ingestion')
