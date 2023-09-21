# Machine Learning Visualization README

## Introduction
During my senior year of high school, I embarked on an online machine learning course. Although I didn't complete the course, I was deeply intrigued by the mathematics behind gradient descent, especially in the context of multivariable linear regression. This program is a visualization tool designed to demystify gradient descent, making it more accessible to those unfamiliar with the concept.

## Prerequisites
Ensure you have the following libraries installed:
- `numpy`
- `tkinter`
- `matplotlib`

## Configuration
Within the main class, there are two key variables:

### 1. `function`
- Represents the mathematical function tailored to fit the data.
- While the program supports standard notation like `x^2`, it's primarily designed for polynomial functions. I've incorporated an interpreter to translate mathematical notation into a format compatible with `numpy`. However, due to the complexity of this task, the program currently does not support exponential or logarithmic functions.

### 2. `data_file_location`
- Points to a CSV file named `data.csv` containing random X and Y values.
- If you wish to modify the randomness of the data, refer to the `dataModifier.py` file within the program. This file contains guidelines on customizing your data points.

## Usage
Once you're familiar with the main class variables, you can proceed to run the program. Upon execution, you'll encounter input boxes for:

### 1. `learning rate`
- Dictates the magnitude of change in the function, essentially determining the step size towards the local optima.
- For higher-degree polynomials, it's advisable to opt for a minuscule learning rate, such as `0.000000000001`, to prevent divergence to infinity.

### 2. `number of iterations`
- Specifies the number of times the gradient descent operation will be executed.
- This feature is particularly handy, eliminating the need to repetitively click the "perform regression" button.
- Given that the code isn't parallelized and doesn't leverage GPU capabilities, it's recommended to keep this value below 10,000 to prevent potential program crashes.

## Getting Started
If you're new to machine learning, don't hesitate to experiment with the program. Play around with different configurations and aim to minimize the cost function. have fun!
