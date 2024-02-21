import streamlit as st
from st_pages import add_page_title

st.title("📄 Project Proposal")

#Project Proposal

#Setup tabs
tab0, tab1, tab2, tab3, tab4, tab5 = st.tabs(["Presentation", "Introduction/Background", "Problem Definition", "Methods", "Potential Results and Discussion", "References"])

#Video Presentation
tab0.header("Presentation")
tab0.video("https://www.youtube.com/watch?v=KRKYY6XAhMI")

#Introduction/Background
tab1.header("Introduction/Background")
tab1.write("The real estate market is a significant component of the economy, influencing various sectors and directly affecting both buyers and sellers. Predicting housing prices accurately is crucial for making informed decisions. Previous studies have explored using machine learning algorithms to predict housing prices, demonstrating varying degrees of success. This proposal outlines a project aimed at developing a comprehensive ML model to predict housing prices accurately.")

tab1.subheader("Literature Review")
tab1.write("The application of ML algorithms in housing price prediction has seen varied approaches and successes. Research highlights the use of algorithms such as C4.5, RIPPER, Naive Bayesian, and AdaBoost in developing predictive models. One study analyzed 5359 townhouses in Fairfax County, Virginia, finding RIPPER to show superior accuracy among the tested algorithms [1]. Another significant approach involved a novel model using deep belief restricted Boltzmann machine (DRBM) and a nonmating genetic algorithm (NGA) for estimating sale prices, which addresses the limitations of backpropagation methods in handling complex pattern recognition [2]. Further, the effectiveness of advanced ML techniques, including decision forests and support vector machines, has been demonstrated in various studies, showing their potential in improving real estate price prediction models.")

tab1.subheader("Dataset Description")
tab1.write("The dataset consists of 79 explanatory variables describing nearly every aspect of residential homes in Ames, Iowa. This includes 36 quantitative and 43 categorical variables, covering information such as lot area, utilities, neighborhood, condition, overall quality, year built, and sale type. The dataset totals 1460 observations.")

tab1.subheader("Dataset Link")
tab1.write("The dataset is available on [Kaggle](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data).")

#Problem Definition
tab2.header("Problem Definition")
tab2.write("The project aims to employ ML algorithms to accurately predict housing prices, taking into account various influencing factors such as location, size, and property features. Accurate price prediction is vital for informed decision-making by stakeholders in the real estate market.")

#Methods
tab3.header("Methods")
tab3.subheader("Data Preprocessing Methods:")

list = ['**Principal Component Analysis (PCA)** for dimensionality reduction [3].', '**Handling Categorical Variables** with methods suitable for both ordinal and nominal variables.', 
        '**Uniform Manifold Approximation and Projection (UMAP)** for non-linear dimension reduction [4].']
s = ''
for i in list:
    s += "- " + i + "\n"
tab3.markdown(s)

tab3.subheader("Machine Learning Algorithms:")

list = ['**Linear Regression (Supervised)**: Utilizes scikit-learn and numpy, fitting for linear relationships [5].', 
        '**Support Vector Machines (Supervised)**: Utilizes sklearn.svm. This is effective in high-dimensional spaces and adaptable with different kernels [6].', 
        '**Decision Forest (Supervised)**: Employs TensorFlow Decision Forests and utilizes sklearn.ensemble.RandomForestClassifier, beneficial for tabular data with flexible hyperparameter tuning [7].',
        '**U-K-means clustering (Unsupervised)**: Utilizes sklearn.cluster.KMeans. Automatically finds the optimal number of clusters without initialization. Scales well to large datasets and can handle high-dimensional data [8].']
s = ''
for i in list:
    s += "- " + i + "\n"
tab3.markdown(s)

#Potential Results and Discussion
tab4.header("Potential Results and Discussion")
tab4.write("There are three quantitative metrics through which we can gauge our project success in accomplishing our goal: a robust machine learning pipeline that minimizes out-of-sample forecasting errors. Firstly, a successful model should result in a low Root-Mean-Squared-Error, indicating low magnitude and variability in prediction errors. Secondly, the Mean-Absolute-Error should be low, indicating predicted values are close to actual values on average. Lastly, it should show a high R-Squared value, indicating that the model captures a substantial amount of the variability in the target variable, given the features provided.")

#References
tab5.header("References")

list = ['B. Park and J. K. Bae, “Using machine learning algorithms for housing price prediction: The case of Fairfax County, Virginia housing data,” Expert Systems with Applications, vol. 42, no. 6, pp. 2928–2934, Apr. 2015, doi: https://doi.org/10.1016/j.eswa.2014.11.040.',
        'M. H. Rafiei and H. Adeli, “A Novel Machine Learning Model for Estimation of Sale Prices of Real Estate Units,” Journal of Construction Engineering and Management, vol. 142, no. 2, p. 04015066, Feb. 2016, doi: https://doi.org/10.1061/(asce)co.1943-7862.0001047.',
        'Z. Jaadi, “A Step by Step Explanation of Principal Component Analysis,” Built In, Sep. 04, 2019. https://builtin.com/data-science/step-step-explanation-principal-component-analysis',
        'S. Sivarajah, “Dimensionality Reduction for Data Visualization: PCA vs TSNE vs UMAP vs LDA,” Medium, Dec. 31, 2020. https://towardsdatascience.com/dimensionality-reduction-for-data-visualization-pca-vs-tsne-vs-umap-be4aa7b1cb29',
        '“1. Supervised learning — scikit-learn 0.21.3 documentation,” Scikit-learn.org, 2019. https://scikit-learn.org/stable/supervised_learning.html#supervised-learning',
        'scikit learn, “1.4. Support Vector Machines — scikit-learn 0.20.3 documentation,” Scikit-learn.org, 2018. https://scikit-learn.org/stable/modules/svm.html',
        '“House Prices Prediction using TFDF,” kaggle.com. https://www.kaggle.com/code/gusthema/house-prices-prediction-using-tfdf',
        'K. P. Sinaga and M.-S. Yang, “Unsupervised K-Means Clustering Algorithm,” IEEE Access, vol. 8, pp. 80716–80727, 2020, doi: https://doi.org/10.1109/access.2020.2988796.']
s = ''
index = 1
for i in list:
    s += "[" + str(index) + "] " + i + "\n\n"
    index+=1
tab5.markdown(s)

