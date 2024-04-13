from sklearn.datasets import load_breast_cancer
import pymongo
cancer = load_breast_cancer()
X=cancer.data
y=cancer.target
client=pymongo.MongoClient("mongodb://localhost:27017/")
db=client["breast_cancer"]
col=db["cancer"]
documents=[]
for i in range(len(cancer.data)):
    doc={
        'features':cancer.data[i].tolist(),
        'target':int(cancer.target[i]),
        'target_names':cancer.target_names[cancer.target[i]]
    }
    documents.append(doc)

col.insert_many(documents)