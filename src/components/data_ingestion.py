import os
import sys
from src.exception import CustomException
from src.logger import logging

from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
import pandas as pd
from sklearn.model_selection import train_test_split

from dataclasses import dataclass

## intitialize the Data Ingestion configuration

@dataclass
class DataIngestionconfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')

## create the data ingestion class

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionconfig()

    def initiate_data_ingestion(self):
        logging.info('Data Ingestion method starts')

        try:
            df=pd.read_csv(os.path.join('notebooks/data','gemstone.csv'))
            logging.info('Dataset read as pandas Dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)

            logging.info('Raw data is created')

            train_set,test_set=train_test_split(df,test_size=0.30,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info('train_set and test_set are created')

            logging.info('Ingestion of Data is completed')

            return(
                self.ingestion_config.raw_data_path,
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )

        except Exception as e:
            logging.info('Exception occured at Data Ingestion Stage')
            raise CustomException(e,sys)

if __name__=="__main__":
    obj=DataIngestion()
    raw_data_imgestion=obj.initiate_data_ingestion()

    obj2=DataTransformation()
    train_arr,test_arr,obj_file_path=obj2.initaite_data_transformation(train_path=raw_data_imgestion[1],  # Provide the train data path
        test_path=raw_data_imgestion[2]  )
   
    obj3=ModelTrainer()
    print(obj3.initate_model_training(train_arr,test_arr))