# MachineLearningVisualization


In my senior high school, I took a machine learning course online, but unfortunately didn't finish it. 
However, I was fascinated by how the mathematics of gradient descent worked for multivariable linear regression and I wanted to make a program on it.

This is that program that visualizes how graident decent works from a visual perspective, so that it makes more sense to people who don't understand it hopefully.

in the main class there is 2 variables:

function
- this is the mathmatical function that fits the data. 
- You can you should be able to use proper notation like x^2, but I only designed it to work for polynomials (I decided to build a interpreter that tries to understand the mathematical notation, and convert that to a numpy - representation and that alone was really tedious to implement, so I probably won't make it work for exponential logarithm functions or logarithmic regression)

data_file_location

- this is the file that points to a CSV file called data.csv, which stores random X and Y values.
- do you want to change the randomness? I did it I use that should be another file inside the program call dataModifier.py there should be some instructions on how you can make your own data points.x1c

When you open up the program there is two inputs

learning rate
- this is the amount that the function will change a.k.a. how much does a function take a step to the local optima.
- for ever for higher power polynomials I recommend that you choose a very small learning rate like 0.000000000001, otherwise, it will diverge to infinity.

number of iterations
- this tells you how many times are you going to perform the gradient, descent operation.
- is useful because you don't want to click the perform aggression button like 1000 times
- unfortunately, because my code isn't parallelized (runs on the GPU). You should probably use the values that are less than 10,000. Otherwise, the program may crash.


