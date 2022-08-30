# power-plant-prediction

## A Problem description
In this project we will build a model to predict the electrical energy output of a Combined Cycle Power Plant, which uses a combination of gas turbines, steam turbines, and heat recovery steam generators to generate power.  We have a set of 9568 hourly average ambient environmental readings from sensors at the power plant which we will use in our model.

The columns in the data consist of hourly average ambient variables:
- Temperature (T) in the range 1.81°C to 37.11°C,
- Ambient Pressure (AP) in the range 992.89-1033.30 milibar,
- Relative Humidity (RH) in the range 25.56% to 100.16%
- Exhaust Vacuum (V) in the range 25.36-81.56 cm Hg
- Net hourly electrical energy output (PE) 420.26-495.76 MW (Target we are trying to predict)



## B For the problem described in the Project Topic section above, determine what type of machine learning approach is needed and select an appropriate output metric to evaluate performance in accomplishing the task:

1. We have a target which we want to predict -> machine learning approach: supervised learning.
2. Based on the features and the target I assume a linear relationship between features and target -> I choose a parametric algorithm
3. Our feature are continuous numbers as well as our target -> we face here a regression task
4. for regression tasks we use mean absolute error (MAE) and mean squared error (MSE)
5 in order to analyze how our model generalize the target for our test data set we additionally use the coefficient of determination (R^2)

## C Determine which possible features we may want to use in the model, and identify the different algorithms we might consider.

1. Temperature (AT) in the range 1.81°C to 37.11°C: higher temperature -> lower need of electricity to heat -> strong linear relationship between feature and target 

![Relationship between PE and AT](https://github.com/amo011235/power-plant-prediction/blob/main/data/AT-PE.png?raw=true)

2. Ambient Pressure (AP) in the range 992.89-1033.30 milibar: range of feature values very small and it seems that data is gathered on quite the same altitude above sea level. There is a relationship between PE and AP, but very low with a lot of outliers. Nevertheless we will use it as feature.

![Relationship between PE and AP](https://github.com/amo011235/power-plant-prediction/blob/main/data/AP-PE.png?raw=true)

3. Relative Humidity (RH) in the range 25.56% to 100.16%: poor relationship between feature and target. will not take this feature into account.

![Relationship between PE and RH](https://github.com/amo011235/power-plant-prediction/blob/main/data/RH-PE.png?raw=true)

4. Exhaust Vacuum (V) in the range 25.36-81.56 cm Hg: medium relationship between feature and target. 
![Relationship between PE and V](https://github.com/amo011235/power-plant-prediction/blob/main/data/V-PE.png?raw=true)

5. Net hourly electrical energy output (PE) 420.26-495.76 MW (Target we are trying to predict): our target

6. regression task with parametric relationship between features and target
7. baseline model: linear regression
8. second model: lasso regression with regularization for better model generalization


## D Split your data to create a test set to evaluate the performance of your final model.  Then, using your training set, determine a validation strategy for comparing different models - a fixed validation set or cross-validation. Depending on whether you are using Excel, Python or AutoML for your model building, you may need to manually split your data to create the test set and validation set / cross validation folds.
1. please see main.py for my code
2. in a nutshell: my validation strategy contains 5 Splits. 
3. for Lasso regression alpha determines the regularization strength. Alpha = 5 is chosen.

## E Use your validation approach to compare at least two different models (which may be either 1) different algorithms, 2) the same algorithm with different combinations of features, or 3) the same algorithm and features with different values for hyperparameters).  From among the models you compare, select the model with the best performance on your validation set as your final model.
1. please see main.py for my code
2. Cross validation scores for Linear Regression [0.91388442 0.9253434  0.92321194 0.91973593 0.91248973]
3. Cross validation scores for Lasse Regression [0.91226576 0.92136475 0.9188066  0.9157939  0.91132286] 

**-> validation scores very similar**

## F Evaluate the performance of your final model using the output metric you defined earlier.  
- MAE, MSE and R-Square for both models
### Linear Regression results
1. R Squared for Linear Regression: %.3f 0.9115407375636495
2. Mean squared error for Linear Regression: %.3f 25.801265800821458
3. Mean absolute error for Linear Regression: %.3f 3.877308782903797
### Linear Regression results
1. R Squared for Lasso Regression: %.3f 0.9101994870863179
2. Mean squared error for Lasso Regression: %.3f 26.192473675700715
3. Mean absolute error for Lasso Regression: %.3f 3.9377032100491074
### Final model
**-> Linear Regression**


