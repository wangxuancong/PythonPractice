from sklearn.svm import SVC,LinearSVC
from sklearn import linear_model
from PythonCoding.bit_cla.label import Label
from PythonCoding.bit_cla.func import Pulic_function as pf
import numpy as np
from sklearn.base import clone
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.model_selection import GridSearchCV





def data_prepare(window,ratio,class_num = 2 ):

    data = Label().main(window, ratio, class_num)

    train_data = np.array(data['train_data'])

    nsamples, nx, ny = train_data.shape

    train_dataset = train_data.reshape((nsamples, nx * ny))

    train_label = np.array(data['train_label'])

    test = np.array(data['test_data'])

    ns, nx, ny = test.shape

    test_dataset = test.reshape((ns,nx * ny))

    test_label = data['test_label']

    return train_dataset,train_label,test_dataset,test_label

def fit_model(model, X, y):

    local_model = clone(model)

    local_model.fit(X, y)

    return local_model

def evaluate_indicator(model,test_data,test_label):

    pred = model.predict(test_data)

    accuracy = metrics.accuracy_score(test_label,pred)

    precision = metrics.precision_score(test_label,pred)

    recall = metrics.recall_score(test_label,pred)

    roc_auc = metrics.roc_auc_score(test_label,pred)

    return accuracy,precision,recall,roc_auc



