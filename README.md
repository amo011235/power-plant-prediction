# power-plant-prediction

## For the problem described in the Project Topic section above, determine what type of machine learning approach is needed and select an appropriate output metric to evaluate performance in accomplishing the task:

- We have a target which we want to predict -> machine learning approach: supervised learning.
- Based on the features and the target I assume a linear relationship between features and target -> I choose a parametric algorithm
- Our feature are continuous numbers as well as our target -> we face here a regression task
- for regression tasks we use mean absolute error (MAE) and mean squared error (MSE)
- in order to analyze how our model generalize the target for our test data set we additionally use the coefficient of determination (R^2)

# Determine which possible features we may want to use in the model, and identify the different algorithms we might consider.

- Temperature (T) in the range 1.81°C to 37.11°C: higher temperature -> lower need of electricity to heat -> strong linear relationship between feature and target 

- Ambient Pressure (AP) in the range 992.89-1033.30 milibar: range of feature values very small and it seems that data is gathered on quite the same altitude above sea level. There is a relationship between PE and AP, but very low with a lot of outliers. Nevertheless we will use it as feature.

- Relative Humidity (RH) in the range 25.56% to 100.16%: poor relationship between feature and target. will not take this feature into account.

- Exhaust Vacuum (V) in the range 25.36-81.56 cm Hg: medium relationship between feature and target. 

- Net hourly electrical energy output (PE) 420.26-495.76 MW (Target we are trying to predict): our target

- regression task with parametric relationship between features and target
- baseline model: linear regression
- second model: ridge regression with regularization for better model generalization


# Split your data to create a test set to evaluate the performance of your final model.  Then, using your training set, determine a validation strategy for comparing different models - a fixed validation set or cross-validation. Depending on whether you are using Excel, Python or AutoML for your model building, you may need to manually split your data to create the test set and validation set / cross validation folds.
- please see main.py for my code
- in a nutshell: The validation strategy contains 5 Splits:

Use your validation approach to compare at least two different models (which may be either 1) different algorithms, 2) the same algorithm with different combinations of features, or 3) the same algorithm and features with different values for hyperparameters).  From among the models you compare, select the model with the best performance on your validation set as your final model.
- please see main.py for my code
- Cross validation scores for Linear Regression [0.91388442 0.9253434  0.92321194 0.91973593 0.91248973]
- Cross validation scores for Lasse Regression [0.91226576 0.92136475 0.9188066  0.9157939  0.91132286]
- validation scores very similar

# Evaluate the performance of your final model using the output metric you defined earlier.  
## Linear Regression results
- MAE, MSE and R-Square for both models
- R Squared for Linear Regression: %.3f 0.9115407375636495
- Mean squared error for Linear Regression: %.3f 25.801265800821458
- Mean absolute error for Linear Regression: %.3f 3.877308782903797
## Linear Regression results
- R Squared for Lasso Regression: %.3f 0.9101994870863179
- Mean squared error for Lasso Regression: %.3f 26.192473675700715
- Mean absolute error for Lasso Regression: %.3f 3.9377032100491074
## Final model
- Linear Regression


