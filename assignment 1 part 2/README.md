Name of the assignment : Assignment 1 Part 2 

================================================

Date of submission : 02/04/2024

================================================

Instructions on how to run the code : 

For the problem 3, I had to build a polynomial regression model from scratch using stochastic gradient descent. First, I generated some fake sinusoidal data to test it out. Then I transformed the data into polynomial features with a degree of 3 - this lets the model learn nonlinear relationships. After that came the fun part - implementing SGD! I iterated through 1000 epochs, each time using the learning rate of 0.01 to update the model parameters towards minimizing the loss function. I plotted the loss over time, and you could see it decreasing as SGD converged to a solution. Finally, I compared my model's predictions to the original sinusoidal data, and the fit looked pretty good! 

For Question 4, we took the basic Stochastic Gradient Descent (SGD) setup from Question 3, which aimed at fitting a curve to data points that resemble a sine wave, and then we spiced things up by adding two advanced techniques called Momentum and Adam. These are like turbo boosts for our basic SGD, making it smarter and faster in finding the best curve. Imagine you're trying to roll a ball down a hill to find the lowest point, Momentum helps by pushing the ball to keep rolling faster in the right direction, while Adam is like having an intelligent navigation system that adjusts the speed and direction based on the terrain. We programmed these enhancements to see which one gets to the bottom of the hill (or finds the best curve) the quickest.

ensure you have a Python environment with numpy and matplotlib installed.


================================================

Instructions on how to run any tests (if applicable):

For Question 3, you are implementing a Stochastic Gradient Descent (SGD) algorithm for a polynomial regression problem, aiming to fit a model to data that follows a sinusoidal pattern. To run the test, ensure your script or notebook includes the functions for generating synthetic data, transforming these into polynomial features (with a degree of M=3), and applying the SGD algorithm.

For Question 4, the task extends Question 3's SGD by incorporating Momentum and Adam optimizations. To test these enhancements:

Momentum: Set the learning rate to 0.01, the momentum coefficient (γ) to 0.9 and run for 1000 epochs. This approach adds velocity to the parameter updates, potentially accelerating convergence.

Adam: Use a learning rate of 0.01, β1=0.9, β2=0.999, and ϵ=1e−8, over 1000 epochs. Adam adjusts the learning rate based on first and second moment estimates of the gradients, aiming for efficient and stable convergence.

Execute each algorithm separately and compare their performance through loss vs. epoch plots.


================================================

Instructions on how to run any notebook (if applicable) : N/A