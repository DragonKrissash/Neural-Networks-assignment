from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder
from sklearn.pipeline import Pipeline 
from sklearn.compose import ColumnTransformer
import sys,os
from dataclasses import dataclass
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
from src.utils import save_obj

@dataclass
class DataTransformationConfig:
    preprocessor_ob_file_path=os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self) -> None:
        self.data_transformation_config=DataTransformationConfig()

    def get_transformation_object(self):
        try:
            logging.info('Data transformation initiated!')
            num_col=['mean radius', 'mean texture', 'mean perimeter', 'mean area',
       'mean smoothness', 'mean compactness', 'mean concavity',
       'mean concave points', 'mean symmetry', 'mean fractal dimension',
       'radius error', 'texture error', 'perimeter error', 'area error',
       'smoothness error', 'compactness error', 'concavity error',
       'concave points error', 'symmetry error',
       'fractal dimension error', 'worst radius', 'worst texture',
       'worst perimeter', 'worst area', 'worst smoothness',
       'worst compactness', 'worst concavity', 'worst concave points',
       'worst symmetry', 'worst fractal dimension']
            
            logging.info('Pipeline Initiated')

            num_pipe=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='mean')),
                    ('scaler',StandardScaler())
                ]
            )

            preprocessor=ColumnTransformer([
                ('num_pipe',num_pipe,num_col)
            ])

            logging.info('Pipeline completed!')
            return preprocessor

        except Exception as e:
            logging.info('Error occured in Data transformation pipeline')
            raise CustomException(e,sys) 
    
    def initiate_data_transformation(self,train_data_path,test_data_path):
        try:
            logging.infor('Reading train and test data path for data transformation')
            train_df=pd.read_csv(train_data_path)
            test_df=pd.read_csv(test_data_path)
            logging.info('Obtaining the processor')
            preprocessor_obj=self.get_transformation_object()
            target_col='malignant', 'benign'


        except Exception as e:
            logging.info('Error occured in initiating data transformation')
            raise CustomException(e,sys)

    