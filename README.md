# Advanced-Python

Gabi Turner

Programming Language: Python

Date: Oct. 5 2023

Description: This repository was designed to show an understanding of how to use python and be able to use libraries to load data, create arrays, and create visualizations from the given data.

Files needed: 

No files are needed for the first task

tit_test.csv 
tit_train.csv

These two files are needed just for the second task because I concatenated the data together to be able to create the visualizations

Required Packages:

pandas: to load the data

matplotlib: to create graphs such as histrograms, bar graphs, and line graphs

numpy: to create arrays

seaborn: to create histograms and the boxplot

Execution:

Task 1: 
1. create a Fibonacci sequence that creates a numpy array for the program
2. create a variable X to have 20 values of fib. numbers
3. recreate an array from part 3 of the second assignment where one array is quotient of fib. numbers and the other is the difference of numbers from the fib. numbers
4. the plot all 3 series into a graph; I used a line graph to represent the 3 series

Task 2:

1. Load tit_test and tit_train files into the python program and concatenate them together
2. use .describe() to get the statistical summary of the data frame
3. create a histogram using matplotlib to get the distribution of ages
4. for the second histrogram, use seaborn to show the distribution of age and the survival rate of the passengers; otherwise matplotlib overlaps the graphs together without a clear visualization of the distribution
5. Calculate the survival rate of the sum of the concatenated data then divided by the total passengers
6. then create a bar graph of the survival rate; I used matplotlib, but you can also use seaborn
7. Then group the data by sex to create a bar graph the shows the survival rate based on the genders of the passengers
8. Use seaborn to create a boxplot of survival rate of passengers based on the class.

