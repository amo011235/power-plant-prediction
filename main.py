import pandas
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.model_selection import cross_val_score
from sklearn import metrics
import matplotlib.pyplot as plt

from sklearn.metrics import mean_squared_error, r2_score

def main():
    df = pandas.read_csv('data/CCPP_data.csv')
    ## Poor relationship between feature RH and target PE. Not using RH.
    df_X = df[['AT','V','AP']] ## my features
    df_y = df[['PE']] ## my targets
    ## Test data size = 15%
    X_train, X_test, y_train, y_test = train_test_split(df_X,df_y, test_size=0.15)

    ## Usage of Linear Regression and Lasso Regression as models
    regr_linear = linear_model.LinearRegression()
    ## For Lasso regression alpha determines the regularization strength. A high strength is chosen.
    regr_lasso = linear_model.Lasso(alpha=5)
    ## Validation strategy contains 5 Splits
    scores_linear = cross_val_score(regr_linear, X_train,y_train,cv=5)
    scores_lasso = cross_val_score(regr_lasso, X_train,y_train,cv=5)
    print('Cross validation scores for Linear Regression', scores_linear)
    print('Cross validation scores for Lasse Regression', scores_lasso)

    
    model_linear = regr_linear.fit(X_train, y_train)
    model_lasso = regr_lasso.fit(X_train, y_train)

    linear_infer = model_linear.predict(X_test)
    lasso_infer = model_lasso.predict(X_test)

    ## for regression task we use mean absolute error (MAE) and mean squared error (MSE)
    ## in order to analyze how our model generalize the target for our test data set we additionally use the coefficient of determination (R^2)
    r2_linear = metrics.r2_score(y_test, linear_infer)
    mse_linear = metrics.mean_squared_error(y_test, linear_infer)
    mae_linear = metrics.mean_absolute_error(y_test, linear_infer)

    print('R Squared for Linear Regression: %.3f', r2_linear)
    print('Mean squared error for Linear Regression: %.3f', mse_linear)
    print('Mean absolute error for Linear Regression: %.3f', mae_linear)

    r2_lasso = metrics.r2_score(y_test, lasso_infer)
    mse_lasso = metrics.mean_squared_error(y_test, lasso_infer)
    mae_lasso = metrics.mean_absolute_error(y_test, lasso_infer)

    print('R Squared for Lasso Regression: %.3f', r2_lasso)
    print('Mean squared error for Lasso Regression: %.3f', mse_lasso)
    print('Mean absolute error for Lasso Regression: %.3f', mae_lasso)

if __name__ == "__main__":
    main()
    print('DONE')