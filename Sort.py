#################
#Date: 3/28/22
#CS 446 Project 2
'''
FCFS: The first in first out scheduling algorithm is the easiest one to implement out of the 3.
It is used in batch systems and it is a non preemtive algorithm meaning it doesnt care about priority.
Without priority, processes with less execution time suffer and waiting time is often quite long.
It is implemented because it is simple and easy to understand. An example of this in use can be seen when 
buying tickets to the movies. You are given a ticket in a first come first serve basis.

'''

'''
Priority: The priority scheduling algorithm that we were asked to make was that of non preemtive measure.
This made it a little easier to implement. It is different from FCFS because it looks at priority when determining the order. It differs from SJF because it doesnt 
switch the process if a higher priority is available. In SJF if there is a process in the queue that has a smaller burst time it will pause the process executing
and swap it with the smaller burst time process. This is not the case for our priority non preemtive algorithm. The lack of 
preemtiveness makes the algorithm have a longer waitTime and slower turnaround times than SJF algorthims.
'''

'''
ShortestJobFirst: this is also known as shortest remaining time and we were asked to implement it in a preemtive way.
This algorithm is the fastest of the 3 with average turnaround times and lowest process wait times. Unlike the priority 
process scheduling algorithm, this algorithm looks and burst times and always puts the lowest burst time into execution even 
if there is another process already executing. This algorithm is very useful where process runtimes are known in advance. 
Although this algorithm is fast it can not implemented for CPU scheduling for the short term, this is because there is no specific 
method to predict the length of the upcoming CPU burst. This algorithm may cause very long turnaround times or starvation.
'''

import sys
#They are: PID, Arrival Time, Burst Time, and Priority.
###########
def main():
    content = []
    batchInt = []
    sortedArrival = []
    turnAround = []
    sortBurst = []
    if(len(sys.argv) == 3):
        try:
             with open(sys.argv[1]) as f:
                content = f.readlines()
                listNumPy = [x.strip().split(', ') for x in content]
                for i in range(0,len(listNumPy)):
                    batchInt.append([])
                for i in range(0,len(listNumPy)):
                    for x in range(0,len(listNumPy[i])):
                        batchInt[i].append(int(listNumPy[i][x]))
                sortedBatch = sorted(batchInt, key=lambda x: x[0]) #Sort by PID
                sortedBatch1 = sorted(batchInt, key=lambda x: x[1]) #Sort by arrival.

                for i in range(0,len(sortedBatch1)):
                    sortedArrival.append(int(sortedBatch1[i][1]))
                    sortBurst.append(int(sortedBatch1[i][2]))
                #If the 2nd argumanet matches fcfs
                if sys.argv[2] == 'FCFS':
                    pid, completion = FirstComeFirstServedSort(sortedBatch)
                    print("PID ORDER OF EXECUTION")
                    for i in range(0,len(pid)):
                        print(pid[i])
                    turnAround, turnAroundAvg = AverageTurnAround(completion, sortedArrival)
                    print(f"Average Turn Around Time: {turnAroundAvg}")
                    waitTime = AverageWait(turnAround, sortBurst)
                    print(f"Average Process Wait Time: {waitTime}")
                #If the 2nd argument mathches priority
                elif sys.argv[2] == 'Priority':
                    pid2, completion2, = PrioritySort(sortedBatch1) #pass in sorted by arrival array
                    print("PID ORDER OF EXECUTION:")
                    for i in range(0,len(pid2)):
                        print(pid2[i])
                    turnAround2, turnAroundAvg2 = AverageTurnAround(completion2, sortedArrival)
                    print(f"Average Turn Around Time: {turnAroundAvg2}")
                    waitTime2 = AverageWait(turnAround2, sortBurst)
                    print(f"Average Process Wait Time: {waitTime2}")

                elif sys.argv[2] == 'ShortestJobFirst':
                    pid3, completion3 = ShortestJobFirstSort(sortedBatch1)
                    print("PID ORDER OF EXECUTION:")
                    for i in range(0,len(pid3)):
                        print(pid3[i])
                    turnAround3, turnAroundAvg3 = AverageTurnAround(completion3, sortedArrival)
                    print(f"Average Turn Around Time: {turnAroundAvg3}")
                    waitTime3 = AverageWait(turnAround3, sortBurst)
                    print(f"Average Process Wait Time: {waitTime3}")
                else:
                    print("Your process scheduling options are FCFS, ShortestJobFirst, or Priority, and exit the program.")
        except:
            print("File Not Found")
    else:
        sys.exit()

########################################
def FirstComeFirstServedSort(batchData):
    count = 0
    cumsum = 0
    sortedCompleteDone = []
    sortedComplete = []
    sortedPID = []
    sortedBatch = sorted(batchData, key=lambda x: x[1])# Sort by arrival.

    for i in sortedBatch:# 1 and 3 return
        sortedPID.append(int(sortedBatch[count][0]))
        sortedComplete.append(int(sortedBatch[count][2]))
        count += 1

    #Add all the previous elements to current
    for x in sortedComplete:
        cumsum += x
        sortedCompleteDone.append(cumsum)

    return sortedPID, sortedCompleteDone

####################################
def ShortestJobFirstSort(batchData): 
    time = 0 #Keeps track of the time remaining.
    pid = 0
    pidList = []
    arrivalTime = []
    completionDone = []
    sortedProcess = sorted(batchData, key=lambda x: x[1]) #Sort the PID sorted batchdata with burst data now

    for x in sortedProcess:
        if x[1] not in arrivalTime and x[1] != 0:
            arrivalTime.append(x[1])                       
    #iterate to the end of the lists
    while len(sortedProcess) != 0:
        while len(arrivalTime) != 0:
            arrived = []
            notArrived = []

            if not pidList or sortedProcess[pid][0] != pidList[-1]:          
                pidList.append(sortedProcess[pid][0])
            
            sortedProcess[pid][2] -= (arrivalTime[0] - time)
            time = arrivalTime[0]
            if sortedProcess[pid][2] <= 0:                                  
                completionDone.append(sortedProcess[pid][2] + time)
            if sortedProcess[pid][2] < 0:
                time += sortedProcess[0][2]
            if sortedProcess[pid][2] >= 0:
                del arrivalTime[0]
            if sortedProcess[pid][2] <= 0:                                            
                del sortedProcess[0]

            for i in sortedProcess:
                if i[1] <= time:
                    arrived.append(i)
                elif i[1] > time:
                    notArrived.append(i)

            arrived = sorted(arrived, key=lambda x: x[2])

            if len(arrived) == 0:
                time = arrivalTime[0]
            else:
                arrived.extend(notArrived)
                sortedProcess = arrived

        sortedProcess = sorted(sortedProcess, key=lambda x: x[2])

        if sortedProcess[pid][0] != pidList[-1]:
            pidList.append(sortedProcess[pid][0])
        else:
            time += sortedProcess[pid][2]
            completionDone.append(time)
            del sortedProcess[0]
    return pidList, completionDone

############################
def PrioritySort(batchData):
    count = 0
    count2 = 0
    cumsum = 0
    sortedArrival = []
    sortedPriority = []
    sortedPID = []
    sortedBurst = []
    sortedBurstDone = []
    for i in batchData:# 1 and 3 return
        sortedArrival.append(int(batchData[count][1]))
        sortedPID.append(int(batchData[count][0]))
        sortedBurst.append(int(batchData[count][2]))
        count += 1

    for x in range(len(batchData)):# 1 and 3 return
        sortedPriority.append(int(batchData[count2][3]))
        if(sortedArrival[x - 1] == sortedArrival[x]):# check to see if the arrivals are the same.
            if(sortedPriority[x - 1] > sortedPriority[x]):# Check to see if the priority is in the right position.
                sortedPID[x - 1], sortedPID[x] = sortedPID[x], sortedPID[x - 1]
                sortedBurst[x - 1], sortedBurst[x] = sortedBurst[x], sortedBurst[x - 1]
            elif(sortedPriority[x - 1] == sortedPriority[x]):
                if sortedPID[x - 1] > sortedPID[x]:
                    sortedPID[x - 1], sortedPID[x] = sortedPID[x], sortedPID[x - 1]
                    sortedBurst[x - 1], sortedBurst[x] = sortedBurst[x], sortedBurst[x - 1]
                else:
                    pass
        count2 += 1
    for y in sortedBurst:
        cumsum += y
        sortedBurstDone.append(cumsum)
    return sortedPID, sortedBurstDone

##########################################################
def AverageWait(processTurnaroundTimes, processBurstTime):
    count = 0
    wait = []
    waitTime = 0
    #Iterate through burst times
    for i in range(0,len(processBurstTime)):
        wait.append((processTurnaroundTimes[count] - processBurstTime[count]))
        waitTime += (wait[count])/len(processTurnaroundTimes)
        count += 1
    return waitTime

###################################################################
def AverageTurnAround(processCompletionTimes, processArrivalTimes):
        turnAround = []
        turnAroundAvg = 0
        count = 0
        #iterate through arrivalTimes
        for i in range(0,len(processArrivalTimes)):
            turnAround.append(processCompletionTimes[count] - processArrivalTimes[count])
            turnAroundAvg += turnAround[count]/len(processArrivalTimes)
            count += 1
        return turnAround, turnAroundAvg

######
main()