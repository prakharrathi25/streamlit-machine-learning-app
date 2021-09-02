''' File which contains the utility functions needed for the application '''
# Import libraries 
import pandas as pd 
import streamlit as st
import matplotlib.pyplot as plt 

from sklearn import datasets
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC 
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler

# Function to get the datasets 
def get_dataset(name):
	'''
		Function which returns the features as X 
		and targets as y based on the dataset name
		ARGS: dataset name
		RETURNS: Features and Labels
	'''

	if name == "Iris":
		data = datasets.load_iris()
	elif name == "Breast Cancer":
		data = datasets.load_breast_cancer()
	else: 
		data = datasets.load_wine() 

	# Get data and targets 
	X = data.data
	y = data.target
	return X, y

# Function to scale the data 
def scale_data(X):
	scaler = MinMaxScaler()
	X = scaler.fit_transform(X)
	return X

# Function to add UI characterstics for each classifier
def add_parameter_ui(clf_name): 

	'''
		Classifier_name --> Classifier parameters
	'''

	params = dict()
	
	if clf_name == 'KNN':
		# Add a k manipulation sidebar
		K = st.sidebar.slider("K", 1, 15)
		params['K'] = K 

	elif clf_name == 'SVM':
		C = st.sidebar.slider("C", 0.01, 10.0)
		params['C'] = C 

	else: 
		max_depth = st.sidebar.slider("Max Depth", 2, 12)
		n_estimators = st.sidebar.slider("N Estimators", 1, 100)
		params['max_depth'] = max_depth
		params['n_estimators'] = n_estimators

	return params

# Function which returns the classifier with correct parameters
def get_classifier(clf_name, params):

	if clf_name == 'KNN':
		clf = KNeighborsClassifier(n_neighbors=params['K'])

	elif clf_name == 'SVM':
		clf = SVC(C=params['C'])
	else: 
		clf = RandomForestClassifier(n_estimators=params['n_estimators'], 
									 max_depth=params['max_depth'], random_state=42)
	return clf

# Perform Classfication and return the accuracy 
def classification(X, y, clf):

	# Split the data 
	X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.2, random_state=42)

	clf.fit(X_train, y_train)
	preds = clf.predict(X_test)

	acc = accuracy_score(y_true=y_test, y_pred=preds)

	return acc

# Plot the data on a two dimenstion place using decomposition 
def plot_data(X, y):
	pca = PCA(2)
	x_projected = pca.fit_transform(X)

	X1 = x_projected[:, 0]
	X2 = x_projected[:, 1]

	fig = plt.figure()
	plt.title("")
	plt.scatter(X1, X2, c=y, alpha=0.8, cmap="viridis")
	plt.xlabel("Principal Component 1")
	plt.ylabel("Principal Component 2")
	plt.colorbar()

	# Plot using streamlit 
	st.pyplot(fig)