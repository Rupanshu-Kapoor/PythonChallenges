def minWaitingTime(patient: list[int], time: list[int]) -> int:
    """
    :param patient:  list of patients to be treated
    :param time: time taken to treat ith patient
    :return: Total wating time for the last patient
    """
    waiting_time = 0
    # created array of 0 to check if patient is treated, if treated mark it 1
    treated = [0 for x in range(len(patient))]

    for i in range(len(patient)):
        min_index = 0
        # defined initial min Time to be +ve infinity so that every other time will be lower than it
        tmin = float("inf")

        for j in range(len(patient)):
            # checking if patient is not treated and his treatment time is less than last tmin
            if treated[j] == 0 and time[j] < tmin:
                min_index = j
                tmin = time[j]

        # making patient with min treatment time from all left patient as treated
        treated[min_index] = 1
        waiting_time += tmin
    # subtracting last patient treatment time from total waiting time as we only need
    # the waiting time for last patient
    return waiting_time-tmin

print(minWaitingTime([1,2,3,4,5], [10,15,7,13,3]))