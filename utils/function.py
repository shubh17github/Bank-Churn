import json
import pickle
import config
import numpy as np

class bank():
    def __init__(self,CreditScore,Geography,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary):
        self.CS=CreditScore
        self.Geography=Geography
        self.Gender=Gender
        self.Age=Age
        self.Tenure=Tenure
        self.Balance=Balance
        self.NumOfProducts=NumOfProducts
        self.HasCrCard=HasCrCard
        self.IsActiveMember=IsActiveMember
        self.EstimatedSalary=EstimatedSalary


    def load_model(self):
        with open(config.model_file_path,'rb') as file:
            self.model=pickle.load(file)

        with open(config.col_dict_path,'r') as file:
            self.col_dict=json.load(file)

    def predict(self):
        self.load_model()
        array=np.zeros(len(self.col_dict['column']))

        array[0]=self.CS
        array[1]=self.Geography
        array[2]=self.Gender
        array[3]=self.Age
        array[4]=self.Tenure
        array[5]=self.Balance
        array[6]=self.NumOfProducts
        array[7]=self.HasCrCard
        array[8]=self.IsActiveMember
        array[9]=self.EstimatedSalary

        result=self.model.predict([array])

        return result[0]
        




      

    


    
