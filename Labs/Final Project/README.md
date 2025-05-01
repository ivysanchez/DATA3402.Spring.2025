![](UTA-DataScience-Logo.png)


# Phishing Website Detection  Project

* **One Sentence Summary:** 
This repository holds an attempt to predict whether a website is legitimate or phishing using data from a Kaggle tabular classification challenge (https://www.kaggle.com/datasets/shashwatwork/web-page-phishing-detection-dataset/data).

## Overview
* **Tasks / challenge:** goal of this project is to develop a model that can effectively classify websites as either legitimate or phishing based on a set of features extracted from the website. This is crucial for online safety and security, as phishing attacks are a common threat.
* **Approach:** The approach involves data cleaning, preprocessing, and feature engineering to prepare the dataset for model training. Several machine learning models, including Logistic Regression, Decision Tree, Random Forest, Gradient Boosting, SVM, and XGBoost, are trained and evaluated. Hyperparameter tuning is performed to optimize the performance of the best-performing models. The project aims to achieve high accuracy, precision, recall, and F1 score in phishing website detection, with a focus on the F1 score. 
* **Summary of the performance achieved:** The XGBoost model, after hyperparameter tuning, achieved the highest F1 score of approximately 0.961, indicating a strong balance between precision and recall. This suggests the model is highly effective at identifying phishing websites while minimizing false alarms.

## Summary of Workdone


### Data
* Type: Input: CSV file containing website features and a target variable indicating phishing or legitimate status.
* Size: The original dataset had 11430 instances with 88 features.
* Instances (Train, Test, Validation Split): The data was split into an 80% training set and a 20% testing set, with no separate validation set used in this initial exploration.

#### Preprocessing / Clean up
* Missing values: The dataset contained no missing values.
* Inconsistencies: The 'status' column was converted to lowercase to ensure consistency.
* Categorical values: All categorical features were converted to numerical values using Label Encoding to be compatible with machine learning algorithms.
* Feature scaling: StandardScaler was applied to scale numerical features and improve model performance.
* Feature selection: Features with low importance (below a threshold of 0.02) based on Random Forest feature importance were removed to reduce dimensionality and potentially improve model performance.
* Feature engineering: New features were created to potentially capture more complex relationships within the data:
Interaction feature: 'page_rank_x_web_traffic'
Polynomial feature: 'google_index_squared' 
Combined feature: 'hyperlinks_ratio' 


#### Data Visualization
* Histograms and count plots were used to visualize the distribution of each feature, providing insights into the data characteristics and potential outliers. 
* A bar chart was generated to display the top 13 most important features identified by Random Forest feature importance.
* Bar charts were created to compare the performance of different models across key metrics.

### Problem Formulation
* Input: A set of features extracted from a website.
* Output: A binary classification (0 for legitimate, 1 for phishing).
* Models: Six different models were evaluated:
Logistic Regression
Decision Tree
Random Forest
Gradient Boosting
Support Vector Machine (SVM)
XGBoost
* Loss, Optimizer, other Hyperparameters: Default hyperparameters were initially used for each model. Hyperparameter tuning was performed on Random Forest and XGBoost using GridSearchCV to optimize the F1 score.

### Training

* Models were trained using scikit-learn and XGBoost libraries.
* Training times varied depending on the model complexity, with XGBoost taking the longest when doing hyperparameter tuning.
* Training curves were not explicitly generated in this analysis.
* Models were trained until convergence using default settings or until the best hyperparameters were found using GridSearchCV.
* No major difficulties were encountered other than long computational times.

### Performance Comparison
* Key performance metric(s): Accuracy, Precision, Recall, F1 Score, and ROC AUC were used to evaluate model performance. The F1 score was chosen as the primary metric for model selection due to its balance between precision and recall.
Show/compare results in one table:
Model
Accuracy
Precision
Recall
F1 Score
ROC AUC
Logistic Regression
0.922
0.934
0.909
0.921
0.977
Decision Tree
0.956
0.959
0.952
0.955
0.956
Random Forest
0.968
0.974
0.962
0.968
0.994
Gradient Boosting
0.965
0.966
0.964
0.965
0.993
SVM
0.957
0.971
0.942
0.956
0.991
XGBoost
0.971
0.975
0.967
0.971
0.995
XGBoost (Tuned)
0.972
0.976
0.968
0.972
0.995

* Show one (or few) visualization(s) of results: Bar charts were generated to compare model performance across different metrics.

### Conclusions
* Data preprocessing and feature engineering significantly improved the performance of all models, especially Logistic Regression.
* Random Forest and XGBoost consistently outperformed other models, achieving the highest scores across all metrics.
* Hyperparameter tuning further enhanced the performance of XGBoost, making it the best-performing model in this analysis.
* The final XGBoost model demonstrates high accuracy and a strong balance between precision and recall, making it suitable for phishing website detection.

### Future Work
* Explore more advanced feature engineering techniques to further improve model performance.
* Experiment with other machine learning algorithms, such as deep learning models, to see if they can achieve even better results.
Evaluate the model's performance on a larger and more diverse dataset to assess its generalization capabilities.

## How to reproduce results
To reproduce the results of this project, follow these steps:
* Download the dataset: Download the "Web Page Phishing Detection Dataset" from Kaggle (using the provided code).
Open the notebook: Open the provided notebook containing the code for data preprocessing, model training, and evaluation.
Run the code cells: Execute the code cells in the notebook sequentially to reproduce the results.
Resources:
Google Colab: Use Google Colab to run the code and leverage its computational resources.
Kaggle: Access the dataset and potentially explore other related datasets.

### Software Setup
* Required Packages: This project uses the following Python packages:
  * Standard Libraries:
   * pandas
   * numpy
   * matplotlib
   * seaborn
   * sklearn (scikit-learn)
* Additional Libraries:
   * kagglehub (For downloading the dataset from Kaggle)
   * xgboost


### Data
* The dataset used in this project, "Web Page Phishing Detection Dataset," is available on Kaggle. You can download it directly using the following code:
import kagglehub
path = kagglehub.dataset_download("shashwatwork/web-page-phishing-detection-dataset")
print("Path to dataset files:", path)
* Preprocessing:
The preprocessing steps are already included in the phishingdetection.ipynb notebook. Run the code cells related to data cleaning, feature scaling, feature selection, and feature engineering before training the models.

### Training
* To train the models:
  1. Open the phishingdetection.ipynb notebook.
  2. Run all cells up to the "Iterative Modeling" section.
  3. Execute the code in the "Iterative Modeling" and "Model Parameter Tuning" sections to train and evaluate different models and optimize hyperparameters.

#### Performance Evaluation
* To evaluate model performance:
  1. Ensure the models have been trained (by completing the training steps).
  2. Run the code cells in the "Iterative Modeling" and "Model Parameter Tuning" sections.These sections contain code to evaluate the models using various metrics like accuracy,precision, recall, F1 score, and ROC AUC, and display the results. You'll also find code for creating confusion matrices to visualize model performance.

