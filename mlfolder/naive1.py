import pandas as pd
msg = pd.read_csv('naivecsv.csv', names=['message', 'label'])
print('The dimensions of the dataset',msg.shape[0])
msg['labelnum']=msg.label.map({'pos':1, 'neg':0})
X=msg.message
y=msg.labelnum
print(X)
print(y)
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(X, y)
print(xtest.shape)
print(xtrain.shape)
print(ytest.shape)
print(ytrain.shape)
from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
xtrain_dtm = count_vect.fit_transform(xtrain)
xtest_dtm=count_vect.transform(xtest)
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(xtrain_dtm,ytrain)
predicted = clf.predict(xtest_dtm)
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score
print('Accuracy metrics')
print('Accuracy of the classifer is',accuracy_score(ytest,predicted))
print('Confusion matrix')
print(confusion_matrix(ytest,predicted))
print('Recall and Precison ')
print(recall_score(ytest,predicted))
print(precision_score(ytest,predicted))


