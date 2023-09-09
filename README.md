# MachineLearningVisualization


In my senior high school, I took a machine learning course online, but unfortunately didn't finish it. 
However, I was fascinated by how the mathematics of gradient descent worked for multivariable linear regression and I wanted to make a program on it.

This is that program that visualizes how graident decent works from a visual perspective, so that it makes more sense to people who don't understand it hopefully.


When you open up the program there is two inputs

learning rate
- this is the amount that the function will change a.k.a. how much does a function take a step to the local optima.
- for ever for higher power polynomials I recommend that you choose a very small learning rate like 0.000000000001, otherwise, it will diverge to infinity.

number of iterations
- this tells you how many times are you going to perform the gradient, descent operation.
- is useful because you don't want to click the perform aggression button like 1000 times
- unfortunately, because my code isn't parallelized (runs on the GPU). You should probably use the values that are less than 10,000. Otherwise, the program may crash.


