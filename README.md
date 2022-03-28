# CS446_Assignment_2
 
Directions

There is a test batchfile for assignment 2 part 1 in Files -> ProgrammingAssignments. Each line of the batchfile contains 4 comma separated values. They are: PID, Arrival Time, Burst Time, and Priority. PID is the process id. Arrival time is the time since the process arrived in the ready queue. Burst time is the amount of time required to fully execute the process on the CPU. Priority should only be used by the priority scheduling algorithm, and it decides which process should run first if more than one process arrives at the same time. Let's look at a simplified example of the batchfile:

1, 0, 20, 2

3, 0, 50, 1

7, 9, 4, 3

2, 10, 12, 4


Your program should consist of at least 6 functions: Main, FirstComeFirstServedSort, ShortestJobFirstSort, PrioritySort, AverageTurnaround, and AverageWait. Please note that the way Python implements main (Links to an external site.) is different than the way that C or C++ implements it. Below, I provide the general description of each of the functions. You will notice that these descriptions are much less comprehensive than the first assignment. This is because I would like you to begin working on implementing algorithms from a general description (much like you would in an interview).
