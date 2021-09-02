# Import necessary libraries 
import numpy as np
import streamlit as st
import utilities

# Set a title 
st.title("My Streamlit App")

# Add text to the app 
st.write("""

## Explore different classifiers

Change the **classifer** or the **dataset** on the left to see how different models perform. 

""")

# Add a select box widget to the side 
dataset_name = st.sidebar.selectbox("Select Dataset", ("Iris", "Breast Cancer", "Wine"))

classifier = st.sidebar.selectbox("Select Classifiers", ("KNN", "SVM", "Random Forest"))

scaling = st.sidebar.checkbox("Scaling?")

# Get the data 
X, y = utilities.get_dataset(dataset_name)
st.write("Shape of the data:", X.shape)
st.write("Number of Classes:", len(np.unique(y)))

# Add parameters to the UI based on the classifier
params = utilities.add_parameter_ui(classifier)

# Get our classifier with the correct classifiers 
clf = utilities.get_classifier(classifier, params)

# Check if scaling is required 
if scaling:
	X = utilities.scale_data(X)

# Make predictions and get accuray 
accuracy = utilities.classification(X, y, clf)
st.write("**Classifer:** ", classifier)
st.write("**Accuracy:** ", accuracy)

# Plot the components of the data 
utilities.plot_data(X, y)