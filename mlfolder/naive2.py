import pandas as pd
msg = pd.read_csv('naivecsv.csv', names=['message', 'label'])
print('The dimensions of the dataset',msg.shape[0])
msg['labelnum']=msg.label.map({'pos':1, 'neg':0})


X=msg.message
y=msg.labelnum
from sklearn.model_selection import train_test_split
Xtrain, Xtest, ytrain, ytest= train_test_split(X, y)
from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
Xtrain_dtm = count_vect.fit_transform(Xtrain)
Xtest_dtm=count_vect.transform(Xtest)

df=pd.DataFrame(Xtrain_dtm.toarray(), columns=count_vect.get_feature_names_out())
print(df[0:5])

from sklearn.naive_bayes import MultinomialNB
clf=MultinomialNB()
clf.fit(Xtrain_dtm,ytrain)
pred=clf.predict(Xtest_dtm)

for doc, p in zip(Xtrain, pred):
    p='pos' if p==1 else 'neg'
    print("%s->%s"%(doc,p))

from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score
print('Accuracy Metrics:\n')
print('Accuracy: ',accuracy_score(ytest, pred))
print('Recall: ',recall_score(ytest, pred))
print('Precision:',precision_score(ytest,pred))
print('Confusion Matrix: \n', confusion_matrix(ytest,pred))