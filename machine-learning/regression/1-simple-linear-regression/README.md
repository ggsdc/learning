# Linear regression

This folder contais a small example of linear regression performed without any external library in python.

## How it works

### What is linear regression

Linear regression is a method for approximating a linear function between two variables. These variables can have a relationship or not, but applying a linear regression will try to finde the one that best fits both variables. For example the height of a child based on the height of its father.

It works better when the variables have a linear relationship between them, in cases where this is not the case we can use another types of regression, polynomial for example, or apply different treatments to the data, apply a logarithmic scale for example, to better fit a linear relationship between the two variables.

In the simplest case of linear regression, the one that we have here, we only have two variables. One variable is called the regressand, endogenous variable, response variable or dependent variable, this is the one that in the future we are going to forecast based on the observed values of the other variable, which are called regressors, exogenous variables, independent variables or features.

The main mathematical representation of the linear regression, with two variables, is as follows:

![equation](https://latex.codecogs.com/gif.latex?y%20%3D%20%5Cbeta_o%20&plus;%20%5Cbeta_1*x)

