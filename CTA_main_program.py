# Benchmarking test on 5 algorithms
# As part of submission for Computational Thinking With Algorithms 
# Author: Katie O'Brien G00398250


# Credit: https://www.angela1c.com/projects/cta_benchmarking/ctabenchmarkingproject
#         https://docs.python.org/3/library/time.html#time.time
#         https://medium.com/@morganjonesartist/color-guide-to-seaborn-palettes-da849406d44f
#         https://www.programiz.com/dsa/radix-sort#:~:text=In%20this%20tutorial%2C%20you%20will,to%20their%20increasing%2Fdecreasing%20order.


# Importing requisite modules and libraries 
import random
import time
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import algorithms

import matplotlib.pyplot as plt


# Defining a function for benchmarking
def benchmarking(algorithms, Sizes, runs):
    # Creating some output variables
    elapsed_times = [] # holding the times for each run- this should end up with 10 elapsed times for each algorithm
    input_size =[] # holding array size used for each run
    curr_run =[] # records the current run the algorithm is on
    algo =[] # holds the name of the current sorting algorithm


    # for each of the 5 sorting algorithms 
    for algo_name in algorithms:
        print(f"Running {algo_name}")        
        # for each array size in the size array
        for size in Sizes:
            # this runs 10 times for each size for each sort type
            for run in range(runs):
                # generating random arrays
                x = [random.randint(0,100) for i in range(size)]
                # selecting the sorting algorithm to use
                algorithm = algorithms[algo_name]
                # start_time will return the current time on the machine, which is measured in seconds from Unix Epoch 
                start_time = time.time()
                # running the actual algorithm using the array and runs specified above 
                algorithm(x)
                # Timestamps the time that the algorithm ended. 
                end_time = time.time()
                # To get the time elapsed in miliseconds, which is more appropriate for benchmarking, * the response by 1,000
                time_elapsed = (end_time - start_time)* 1000 

                # recording the results of current test to the results array
                elapsed_times.append(time_elapsed)               
                # recording the current run number (from 1 to 10)
                curr_run.append(run+1)
                # recording the current input size to the size array
                input_size.append(size)
                # recording the name of the current sorting algorithm 
                algo.append(algo_name) 

    # outputting a dataframe with the raw times for each trial             
    df = pd.DataFrame({"Name":algo, "Size":input_size, "Times":elapsed_times, "trialNo":curr_run})
    return df

# Defining a function to take the output of the benchmarking function and calculate the averages 
def mean_sorts(df):
    # using the Size column of the dataframe as the index
    df.set_index('Size', inplace=True)
    # calculating the averages for each sorting algorithm at each input size
    means = (df.iloc[:, 0:2].groupby(['Name','Size']).mean()).round(3)
    # unstacking the dataframe to get the desired format for the output to the console
    return means.unstack()

# defining a function to plot the averages on a graph
def plot_averages(df2):
     # setting the plot sizing and style
    plt.rcParams["figure.figsize"]=(16,8)
    sns.set(style= "darkgrid")
    # using the dataframe for plotting
    df2.T.plot(lw=2, colormap="brg_r", marker='.', markersize=10, 
         title='Benchmarking Sorting Algorithms - Average Times')
    # Setting x and y labels
    plt.ylabel("Run time in milliseconds")
    plt.xlabel("Input Size")
    # Saving plot to machine
    plt.savefig('sort-plot1.png', bbox_inches='tight')

# defining a function to export the results to csv
def export_results(times, means):
    
    times.to_csv('Raw_time_data' + '.csv')
    means.to_csv('Averages' + '.csv')

# calling the main program
if __name__ == "__main__":
    # Algorithms to be used- function code is available in a seperate script
    algorithms = {"MergeSort":algorithms.mergesort,"QuickSort":algorithms.quicksort, "CountingSort": algorithms.countingsort}
    # providing the sizes for the arrays to be sorted    
   
    array_sizes = [100,250,500,750,1000,1250,2500]

    # calling the benchmarking function
    results = benchmarking(algorithms, array_sizes, 10)

    print("The run time for each of the sorting algorithms have been measured 10 times and the averages of these runs for each algorithm and input size are as follows \n ")
    # creating a dataframe to store the averages from the benchmarking
    df2=  mean_sorts(results)
    df2.rename_axis(None, inplace=True)
    # drop one of the multi-index levels
    df2.columns = df2.columns.droplevel()
    # print the results to the console
    print(df2)
    # call the plotting function
    plot_averages(df2)
    # export the results to csv
    export_results(results, df2)