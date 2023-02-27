import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, RidgeCV, LassoCV, ElasticNetCV
from const import Constants
from utils import test_model, get_test, histograms, correlation, scatter


data = np.loadtxt("apartmentComplexData.txt", delimiter=",")
data = pd.DataFrame(data, columns=Constants.COLUMNS)

print("Column\t\t\tNull Count")
print(data.isna().sum())
print("----------------------------------------")

print("Duplicates: ", data.duplicated().sum())
print("----------------------------------------")

x_train, x_test, y_train, y_test = get_test(data,
                                            Constants.MEDIAN_COMPLEX_VALUE)

regress_model = LinearRegression()
regress_model.fit(x_train, y_train)

ridge_model = RidgeCV(alphas=[0.01, 0.1, 1, 10])
ridge_model.fit(x_train, y_train)

lasso_model = LassoCV(alphas=[0.01, 0.1, 1, 10])
lasso_model.fit(x_train, y_train)

elastic_net_model = ElasticNetCV(alphas=[0.01, 0.1, 1, 10])
elastic_net_model.fit(x_train, y_train)

test_model("Regress", regress_model, x_test, y_test)
test_model("Ridge", ridge_model, x_test, y_test)
test_model("Lasso", lasso_model, x_test, y_test)
test_model("Elastic Net", elastic_net_model, x_test, y_test)


#histograms(data, Constants)
#scatter(data, Constants)
#correlation(data, Constants.COLUMNS)
