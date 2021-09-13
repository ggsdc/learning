# Linear regression

This folder contais a small example of linear regression performed without any external library in python.

## How it works

### What is linear regression

Linear regression is a method for approximating a linear function between two variables. These variables can have a relationship or not, but applying a linear regression will try to finde the one that best fits both variables. For example the height of a child based on the height of its father.

It works better when the variables have a linear relationship between them, in cases where this is not the case we can use another types of regression, polynomial for example, or apply different treatments to the data, apply a logarithmic scale for example, to better fit a linear relationship between the two variables.

In the simplest case of linear regression, the one that we have here, we only have two variables. One variable is called the regressand, endogenous variable, response variable or dependent variable, this is the one that in the future we are going to forecast based on the observed values of the other variable, which are called regressors, exogenous variables, independent variables or features.

The main mathematical representation of the linear regression, with two variables, is as follows:

![equation](https://latex.codecogs.com/gif.latex?y%20%3D%20%5Cbeta_o%20&plus;%20%5Cbeta_1*x)

And the objective is to learn the parameters &beta;<sub>0</sub> and &beta;<sub>1</sub> to better approximate the value of the dependent variable *y* from the value of the independent variable *x*.

To achieve this we do it in the following steps:

1. Randomly initialize the values of &beta;<sub>0</sub> and &beta;<sub>1</sub>.
1. Computing the error between the real values of *y* and its estimated values. Normally we use the mean squared error (MSE).
1. Calculation the partial derivatives of the error function for &beta;<sub>0</sub> and &beta;<sub>1</sub>.
1. Updating the values of &beta;<sub>0</sub> and &beta;<sub>1</sub> based on the derivatives and the learning range.
1. Repeat from step 2 until the error is minimized.

#### The error function

This funtion is going to calculate the total error of our linear regression on our training set. For this example we are going to be using the mean squared error (MSE), which we are going to call *J*, which can be calculated with the following formula:

![equation](https://latex.codecogs.com/gif.latex?J%28%5Cbeta_0%2C%20%5Cbeta_1%29%20%3D%20%5Ctfrac%7B1%7D%7Bn%7D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%7B%28%5Cwidehat%7By%7D_i%20-%20y_i%29%5E2%7D)

There we can see that we are comapring the values between the predicted value of *y* and its real value. The predicted value is calculated with:

![equation](https://latex.codecogs.com/gif.latex?%5Cwidehat%7By%7D_i%20%3D%20%5Cbeta_0%20&plus;%20%5Cbeta_1*x_i)

Which gives us the following formula for the MSE:

![equation](https://latex.codecogs.com/gif.latex?J%28%5Cbeta_0%2C%20%5Cbeta_1%29%20%3D%20%5Ctfrac%7B1%7D%7Bn%7D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%7B%28%28%5Cbeta_0%20&plus;%20%5Cbeta_1*x_i%29%20-%20y_i%29%5E2%7D)

As we can see this error function depends both on the values of &beta;<sub>0</sub> and &beta;<sub>1</sub> so we can calculate the partial derivatives of said function by each of these parameters.

#### Calculating the derivatives

The calculation of the partial derivatives is a key step to afterwards updating the values of the parameters and improving the model.

Without entering in profound detail of how this derivatives are calculated, their values can be seen in the following formulas:

![equation](https://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20J%7D%7B%5Cpartial%20%5Cbeta_0%7D%20%3D%20%28%5Cwidehat%7By%7D_i%20-%20y_i%29)

![equation](https://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20J%7D%7B%5Cpartial%20%5Cbeta_1%7D%20%3D%20%28%5Cwidehat%7By%7D_i%20-%20y_i%29*x_i)

This two values will be the ones we need to minimize in order to better fit our model to the training data.

#### Updating the parameters of the model

With the values of the partial derivatives calculated we just need to update the parameters wit the following formulas:

![equation](https://latex.codecogs.com/gif.latex?%5Cbeta_0%20%3D%20%5Cbeta_0%20-%20%5Calpha%20%5Cfrac%7B%5Cpartial%20J%7D%7B%5Cpartial%20%5Cbeta_0%7D)

![equation](https://latex.codecogs.com/gif.latex?%5Cbeta_1%20%3D%20%5Cbeta_1%20-%20%5Calpha%20%5Cfrac%7B%5Cpartial%20J%7D%7B%5Cpartial%20%5Cbeta_1%7D)

The new value that appears in this formulas is &alpha; which is called the learning rate, if we set its value small its going to make the model have to take a lot of iterations until reaching the minimized values of the partial derivatives and with the risk of finding a local optimal point in the process, but if we set up its value too big, then the learning may never converge on the optimal values for the parameters.

## How it is set up

In this section we are going to see how the code is organized and how it works.

## Examples

In this section we are going to see the impact of different scenarios of input data and the value of the learning parameter.