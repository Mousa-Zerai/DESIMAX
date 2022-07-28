import numpy as np
    
def check_device_sharing(current = None,n_occ = None,devicesharing = None): 
    # Check for device sharing and update activity profiles accordingly. For
# multiple occupancy households, there is a probability that certain
# appliances will be used by more than one occupant at any given time. The
# algorithm identifies every time period when multiple users have the same
# activity and uses the device sharing probability to determine if the
# activity is shared or not. If the activity is shared then the activity
# occurence is removed from the secondary user to avoid double counting of
# the load use.
    
    # Arguments:
#   current (array; 144, hh_size) [-]: Activity profile of the household
#       users.
#   n_occ (int) [-]: The number of occupants in the household.
#   devicesharing (array; 15, 144) [pu]: Array of probabilities of activity
#       sharing for the given user type.
    
    # Returns:
#   current (array; 144, hh_size) [-]: Updated activity profile of the
#       household users.
    
    # Generate random numbers
    a = 0
    b = 1
    r = a + np.multiply((b - a),np.random.rand(144,1))
    # Algorithm
    if n_occ == 2:
        # check activity five
        countuser15 = 0
        countuser25 = 0
        for tcheck5 in np.arange(1,144+1).reshape(-1):
            if current(tcheck5,1) == 5:
                countuser15 = countuser15 + 1
            if current(tcheck5,2) == 5:
                countuser25 = countuser25 + 1
        if (countuser15 >= countuser25):
            for tdelete5 in np.arange(1,144+1).reshape(-1):
                if current(tdelete5,2) == 5:
                    current[tdelete5,2] = 1
        else:
            if (countuser25 > countuser15):
                for tdelete5 in np.arange(1,144+1).reshape(-1):
                    if current(tdelete5,1) == 5:
                        current[tdelete5,1] = 1
        # check activity eight
        countuser18 = 0
        countuser28 = 0
        for tcheck8 in np.arange(1,144+1).reshape(-1):
            if current(tcheck8,1) == 8:
                countuser18 = countuser18 + 1
            if current(tcheck8,2) == 8:
                countuser28 = countuser28 + 1
        if (countuser18 >= countuser28):
            for tdelete8 in np.arange(1,144+1).reshape(-1):
                if current(tdelete8,2) == 8:
                    current[tdelete8,2] = 1
        else:
            if (countuser28 > countuser18):
                for tdelete8 in np.arange(1,144+1).reshape(-1):
                    if current(tdelete8,1) == 8:
                        current[tdelete8,1] = 1
        for t in np.arange(1,144+1).reshape(-1):
            if current(t,1) == current(t,2):
                activity = current(t,1)
                if activity == 1:
                    current[t,1] = 1
                else:
                    if activity == 3:
                        current[t,1] = 3
                    else:
                        if activity == 4:
                            current[t,2] = 1
                        else:
                            if activity == 5:
                                current[t,2] = 1
                            else:
                                if activity == 6:
                                    current[t,2] = 1
                                else:
                                    if activity == 7:
                                        current[t,2] = 1
                                    else:
                                        if activity == 8:
                                            current[t,2] = 1
                                        else:
                                            if activity == 9:
                                                current[t,2] = 1
                                            else:
                                                if activity == 16:
                                                    current[t,1] = 16
                                                else:
                                                    if r(t,1) <= devicesharing(activity,t):
                                                        current[t,2] = 1
    else:
        if n_occ == 3:
            # check activity five
            countuser15 = 0
            countuser25 = 0
            countuser35 = 0
            for tcheck5 in np.arange(1,144+1).reshape(-1):
                if current(tcheck5,1) == 5:
                    countuser15 = countuser15 + 1
                if current(tcheck5,2) == 5:
                    countuser25 = countuser25 + 1
                if current(tcheck5,3) == 5:
                    countuser35 = countuser35 + 1
            if (countuser15 >= countuser25) and (countuser15 >= countuser35):
                for tdelete5 in np.arange(1,144+1).reshape(-1):
                    if current(tdelete5,2) == 5:
                        current[tdelete5,2] = 1
                    if current(tdelete5,3) == 5:
                        current[tdelete5,3] = 1
            else:
                if (countuser25 >= countuser15) and (countuser25 >= countuser35):
                    for tdelete5 in np.arange(1,144+1).reshape(-1):
                        if current(tdelete5,1) == 5:
                            current[tdelete5,1] = 1
                        if current(tdelete5,3) == 5:
                            current[tdelete5,3] = 1
                else:
                    if (countuser35 >= countuser15) and (countuser35 >= countuser25):
                        for tdelete5 in np.arange(1,144+1).reshape(-1):
                            if current(tdelete5,1) == 5:
                                current[tdelete5,1] = 1
                            if current(tdelete5,2) == 5:
                                current[tdelete5,2] = 1
            #check activity eight
            countuser18 = 0
            countuser28 = 0
            countuser38 = 0
            for tcheck8 in np.arange(1,144+1).reshape(-1):
                if current(tcheck8,1) == 8:
                    countuser18 = countuser18 + 1
                if current(tcheck8,2) == 8:
                    countuser28 = countuser28 + 1
                if current(tcheck8,3) == 8:
                    countuser38 = countuser38 + 1
            if (countuser18 >= countuser28) and (countuser18 >= countuser38):
                for tdelete8 in np.arange(1,144+1).reshape(-1):
                    if current(tdelete8,2) == 8:
                        current[tdelete8,2] = 1
                    if current(tdelete8,3) == 8:
                        current[tdelete8,3] = 1
            else:
                if (countuser28 >= countuser18) and (countuser28 >= countuser38):
                    for tdelete8 in np.arange(1,144+1).reshape(-1):
                        if current(tdelete8,1) == 8:
                            current[tdelete8,1] = 1
                        if current(tdelete8,3) == 8:
                            current[tdelete8,3] = 1
                else:
                    if (countuser38 >= countuser18) and (countuser38 >= countuser28):
                        for tdelete8 in np.arange(1,144+1).reshape(-1):
                            if current(tdelete8,1) == 8:
                                current[tdelete8,1] = 1
                            if current(tdelete8,2) == 8:
                                current[tdelete8,2] = 1
            actcount = np.zeros((16,144))
            for t in np.arange(1,144+1).reshape(-1):
                for activity in np.arange(1,16+1).reshape(-1):
                    for users in np.arange(1,3+1).reshape(-1):
                        if current(t,users) == activity:
                            actcount[activity,t] = actcount(activity,t) + 1
                for activity in np.arange(1,15+1).reshape(-1):
                    if actcount(activity,t) == 2:
                        if devicesharing[2,1](activity,t) <= devicesharing[2,2](activity,t):
                            Prob[1,1] = devicesharing[2,1](activity,t)
                            Prob[1,2] = 1
                            Prob[2,1] = devicesharing[2,2](activity,t)
                            Prob[2,2] = 2
                        else:
                            Prob[1,1] = devicesharing[2,2](activity,t)
                            Prob[1,2] = 2
                            Prob[2,1] = devicesharing[2,1](activity,t)
                            Prob[2,2] = 1
                        if activity == 3:
                            current[t,1] = 3
                        else:
                            if activity == 16:
                                current[t,1] = 16
                            else:
                                if activity == 1:
                                    current[t,1] = 1
                                else:
                                    if activity == 2:
                                        current[t,1] = 2
                                    else:
                                        if current(t,1) == current(t,2):
                                            if r(t,1) <= Prob(1,1):
                                                if Prob(1,2) == 1:
                                                    current[t,2] = 1
                                            else:
                                                if r(t,1) <= Prob(1,1) + Prob(2,1):
                                                    if Prob(2,2) == 1:
                                                        current[t,2] = 1
                                        else:
                                            if current(t,1) == current(t,3):
                                                if r(t,1) <= Prob(1,1):
                                                    if Prob(1,2) == 1:
                                                        current[t,3] = 1
                                                else:
                                                    if r(t,1) <= Prob(1,1) + Prob(2,1):
                                                        if Prob(2,2) == 1:
                                                            current[t,3] = 1
                                            else:
                                                if current(t,2) == current(t,3):
                                                    if r(t,1) <= Prob(1,1):
                                                        if Prob(1,2) == 1:
                                                            current[t,3] = 1
                                                    else:
                                                        if r(t,1) <= Prob(1,1) + Prob(2,1):
                                                            if Prob(2,2) == 1:
                                                                current[t,3] = 1
                    if actcount(activity,t) == 3:
                        val1 = devicesharing[1,1](activity,t)
                        val2 = devicesharing[1,2](activity,t)
                        val3 = devicesharing[1,3](activity,t)
                        if val1 <= val2 and val1 <= val3 and val2 <= val3:
                            Prob[1,1] = devicesharing[1,1](activity,t)
                            Prob[1,2] = 1
                            Prob[2,1] = devicesharing[1,2](activity,t)
                            Prob[2,2] = 2
                            Prob[3,1] = devicesharing[1,3](activity,t)
                            Prob[3,2] = 3
                        else:
                            if val1 <= val2 and val1 <= val3 and val3 <= val2:
                                Prob[1,1] = devicesharing[1,1](activity,t)
                                Prob[1,2] = 1
                                Prob[2,1] = devicesharing[1,3](activity,t)
                                Prob[2,2] = 3
                                Prob[3,1] = devicesharing[1,2](activity,t)
                                Prob[3,2] = 2
                            else:
                                if val2 <= val1 and val2 <= val3 and val1 <= val3:
                                    Prob[1,1] = devicesharing[1,2](activity,t)
                                    Prob[1,2] = 2
                                    Prob[2,1] = devicesharing[1,1](activity,t)
                                    Prob[2,2] = 1
                                    Prob[3,1] = devicesharing[1,3](activity,t)
                                    Prob[3,2] = 3
                                else:
                                    if val2 <= val1 and val2 <= val3 and val3 <= val1:
                                        Prob[1,1] = devicesharing[1,2](activity,t)
                                        Prob[1,2] = 2
                                        Prob[2,1] = devicesharing[1,3](activity,t)
                                        Prob[2,2] = 3
                                        Prob[3,1] = devicesharing[1,1](activity,t)
                                        Prob[3,2] = 1
                                    else:
                                        if val3 <= val1 and val3 <= val2 and val1 <= val2:
                                            Prob[1,1] = devicesharing[1,3](activity,t)
                                            Prob[1,2] = 3
                                            Prob[2,1] = devicesharing[1,1](activity,t)
                                            Prob[2,2] = 1
                                            Prob[3,1] = devicesharing[1,2](activity,t)
                                            Prob[3,2] = 2
                                        else:
                                            if val3 <= val1 and val3 <= val2 and val2 <= val1:
                                                Prob[1,1] = devicesharing[1,3](activity,t)
                                                Prob[1,2] = 3
                                                Prob[2,1] = devicesharing[1,2](activity,t)
                                                Prob[2,2] = 2
                                                Prob[3,1] = devicesharing[1,1](activity,t)
                                                Prob[3,2] = 1
                        if activity == 1:
                            current[t,1] = 1
                        else:
                            if activity == 2:
                                current[t,1] = 2
                            else:
                                if activity == 3:
                                    current[t,1] = 3
                                else:
                                    if activity == 16:
                                        current[t,1] = 16
                                    else:
                                        if (current(t,1) == current(t,2)) and (current(t,1) == current(t,3)):
                                            if r(t,1) <= Prob(1,1):
                                                if Prob(1,2) == 1:
                                                    current[t,2] = 1
                                                    current[t,3] = 1
                                                else:
                                                    if Prob(1,2) == 2:
                                                        current[t,3] = 1
                                            else:
                                                if r(t,1) <= Prob(1,1) + Prob(2,1):
                                                    if Prob(2,2) == 1:
                                                        current[t,2] = 1
                                                        current[t,3] = 1
                                                    else:
                                                        if Prob(2,2) == 2:
                                                            current[t,3] = 1
                                                else:
                                                    if r(t,1) <= Prob(1,1) + Prob(2,1) + Prob(3,1):
                                                        if Prob(3,2) == 1:
                                                            current[t,2] = 1
                                                            current[t,3] = 1
                                                        else:
                                                            if Prob(3,2) == 2:
                                                                current[t,3] = 1
        else:
            if n_occ == 4:
                # check activity five
                countuser15 = 0
                countuser25 = 0
                countuser35 = 0
                countuser45 = 0
                for tcheck5 in np.arange(1,144+1).reshape(-1):
                    if current(tcheck5,1) == 5:
                        countuser15 = countuser15 + 1
                    if current(tcheck5,2) == 5:
                        countuser25 = countuser25 + 1
                    if current(tcheck5,3) == 5:
                        countuser35 = countuser35 + 1
                    if current(tcheck5,4) == 5:
                        countuser45 = countuser45 + 1
                if (countuser15 >= countuser25) and (countuser15 >= countuser35) and (countuser15 >= countuser45):
                    for tdelete5 in np.arange(1,144+1).reshape(-1):
                        if current(tdelete5,2) == 5:
                            current[tdelete5,2] = 1
                        if current(tdelete5,3) == 5:
                            current[tdelete5,3] = 1
                        if current(tdelete5,4) == 5:
                            current[tdelete5,4] = 1
                else:
                    if (countuser25 >= countuser15) and (countuser25 >= countuser35) and (countuser25 >= countuser45):
                        for tdelete5 in np.arange(1,144+1).reshape(-1):
                            if current(tdelete5,1) == 5:
                                current[tdelete5,1] = 1
                            if current(tdelete5,3) == 5:
                                current[tdelete5,3] = 1
                            if current(tdelete5,4) == 5:
                                current[tdelete5,4] = 1
                    else:
                        if (countuser35 >= countuser15) and (countuser35 >= countuser25) and (countuser35 >= countuser45):
                            for tdelete5 in np.arange(1,144+1).reshape(-1):
                                if current(tdelete5,1) == 5:
                                    current[tdelete5,1] = 1
                                if current(tdelete5,2) == 5:
                                    current[tdelete5,2] = 1
                                if current(tdelete5,4) == 5:
                                    current[tdelete5,4] = 1
                        else:
                            if (countuser45 >= countuser15) and (countuser45 >= countuser25) and (countuser45 >= countuser35):
                                for tdelete5 in np.arange(1,144+1).reshape(-1):
                                    if current(tdelete5,1) == 5:
                                        current[tdelete5,1] = 1
                                    if current(tdelete5,2) == 5:
                                        current[tdelete5,2] = 1
                                    if current(tdelete5,3) == 5:
                                        current[tdelete5,3] = 1
                # check activity eight
                countuser18 = 0
                countuser28 = 0
                countuser38 = 0
                countuser48 = 0
                for tcheck8 in np.arange(1,144+1).reshape(-1):
                    if current(tcheck8,1) == 8:
                        countuser18 = countuser18 + 1
                    if current(tcheck8,2) == 8:
                        countuser28 = countuser28 + 1
                    if current(tcheck8,3) == 8:
                        countuser38 = countuser38 + 1
                    if current(tcheck8,4) == 8:
                        countuser48 = countuser48 + 1
                if (countuser18 >= countuser28) and (countuser18 >= countuser38) and (countuser18 >= countuser48):
                    for tdelete8 in np.arange(1,144+1).reshape(-1):
                        if current(tdelete8,2) == 8:
                            current[tdelete8,2] = 1
                        if current(tdelete8,3) == 8:
                            current[tdelete8,3] = 1
                        if current(tdelete8,4) == 8:
                            current[tdelete8,4] = 1
                else:
                    if (countuser28 >= countuser18) and (countuser28 >= countuser38) and (countuser28 >= countuser48):
                        for tdelete8 in np.arange(1,144+1).reshape(-1):
                            if current(tdelete8,1) == 8:
                                current[tdelete8,1] = 1
                            if current(tdelete8,3) == 8:
                                current[tdelete8,3] = 1
                            if current(tdelete8,4) == 8:
                                current[tdelete8,4] = 1
                    else:
                        if (countuser38 >= countuser18) and (countuser38 >= countuser28) and (countuser38 >= countuser48):
                            for tdelete8 in np.arange(1,144+1).reshape(-1):
                                if current(tdelete8,1) == 8:
                                    current[tdelete8,1] = 1
                                if current(tdelete8,2) == 8:
                                    current[tdelete8,2] = 1
                                if current(tdelete8,4) == 8:
                                    current[tdelete8,4] = 1
                        else:
                            if (countuser48 >= countuser18) and (countuser48 >= countuser28) and (countuser48 >= countuser38):
                                for tdelete8 in np.arange(1,144+1).reshape(-1):
                                    if current(tdelete8,1) == 8:
                                        current[tdelete8,1] = 1
                                    if current(tdelete8,2) == 8:
                                        current[tdelete8,2] = 1
                                    if current(tdelete8,3) == 8:
                                        current[tdelete8,3] = 1
                actcount = np.zeros((16,144))
                for t in np.arange(1,144+1).reshape(-1):
                    for activity in np.arange(1,16+1).reshape(-1):
                        for users in np.arange(1,n_occ+1).reshape(-1):
                            if current(t,users) == activity:
                                actcount[activity,t] = actcount(activity,t) + 1
                    for activity in np.arange(1,15+1).reshape(-1):
                        if actcount(activity,t) == 2:
                            if devicesharing[3,1](activity,t) <= devicesharing[3,2](activity,t):
                                Prob[1,1] = devicesharing[3,1](activity,t)
                                Prob[1,2] = 1
                                Prob[2,1] = devicesharing[3,2](activity,t)
                                Prob[2,2] = 2
                            else:
                                Prob[1,1] = devicesharing[3,2](activity,t)
                                Prob[1,2] = 2
                                Prob[2,1] = devicesharing[3,1](activity,t)
                                Prob[2,2] = 1
                            if activity == 3:
                                current[t,1] = 3
                            else:
                                if activity == 16:
                                    current[t,1] = 16
                                else:
                                    if activity == 1:
                                        current[t,1] = 1
                                    else:
                                        if activity == 2:
                                            current[t,1] = 2
                                        else:
                                            if current(t,1) == current(t,2):
                                                if r(t,1) <= Prob(1,1):
                                                    if Prob(1,2) == 1:
                                                        current[t,2] = 1
                                                else:
                                                    if r(t,1) <= Prob(1,1) + Prob(2,1):
                                                        if Prob(2,2) == 1:
                                                            current[t,2] = 1
                                            else:
                                                if current(t,1) == current(t,3):
                                                    if r(t,1) <= Prob(1,1):
                                                        if Prob(1,2) == 1:
                                                            current[t,3] = 1
                                                    else:
                                                        if r(t,1) <= Prob(1,1) + Prob(2,1):
                                                            if Prob(2,2) == 1:
                                                                current[t,3] = 1
                                                else:
                                                    if current(t,1) == current(t,4):
                                                        if r(t,1) <= Prob(1,1):
                                                            if Prob(1,2) == 1:
                                                                current[t,4] = 1
                                                        else:
                                                            if r(t,1) <= Prob(1,1) + Prob(2,1):
                                                                if Prob(2,2) == 1:
                                                                    current[t,4] = 1
                                                    else:
                                                        if current(t,2) == current(t,3):
                                                            if r(t,1) <= Prob(1,1):
                                                                if Prob(1,2) == 1:
                                                                    current[t,3] = 1
                                                            else:
                                                                if r(t,1) <= Prob(1,1) + Prob(2,1):
                                                                    if Prob(2,2) == 1:
                                                                        current[t,3] = 1
                                                        else:
                                                            if current(t,2) == current(t,4):
                                                                if r(t,1) <= Prob(1,1):
                                                                    if Prob(1,2) == 1:
                                                                        current[t,4] = 1
                                                                else:
                                                                    if r(t,1) <= Prob(1,1) + Prob(2,1):
                                                                        if Prob(2,2) == 1:
                                                                            current[t,4] = 1
                                                            else:
                                                                if current(t,3) == current(t,4):
                                                                    if r(t,1) <= Prob(1,1):
                                                                        if Prob(1,2) == 1:
                                                                            current[t,4] = 1
                                                                    else:
                                                                        if r(t,1) <= Prob(1,1) + Prob(2,1):
                                                                            if Prob(2,2) == 1:
                                                                                current[t,4] = 1
                        if actcount(activity,t) == 3:
                            val1 = devicesharing[2,1](activity,t)
                            val2 = devicesharing[2,2](activity,t)
                            val3 = devicesharing[2,3](activity,t)
                            if val1 <= val2 and val1 <= val3 and val2 <= val3:
                                Prob[1,1] = devicesharing[2,1](activity,t)
                                Prob[1,2] = 1
                                Prob[2,1] = devicesharing[2,2](activity,t)
                                Prob[2,2] = 2
                                Prob[3,1] = devicesharing[2,3](activity,t)
                                Prob[3,2] = 3
                            else:
                                if val1 <= val2 and val1 <= val3 and val3 <= val2:
                                    Prob[1,1] = devicesharing[2,1](activity,t)
                                    Prob[1,2] = 1
                                    Prob[2,1] = devicesharing[2,3](activity,t)
                                    Prob[2,2] = 3
                                    Prob[3,1] = devicesharing[2,2](activity,t)
                                    Prob[3,2] = 2
                                else:
                                    if val2 <= val1 and val2 <= val3 and val1 <= val3:
                                        Prob[1,1] = devicesharing[2,2](activity,t)
                                        Prob[1,2] = 2
                                        Prob[2,1] = devicesharing[2,1](activity,t)
                                        Prob[2,2] = 1
                                        Prob[3,1] = devicesharing[2,3](activity,t)
                                        Prob[3,2] = 3
                                    else:
                                        if val2 <= val1 and val2 <= val3 and val3 <= val1:
                                            Prob[1,1] = devicesharing[2,2](activity,t)
                                            Prob[1,2] = 2
                                            Prob[2,1] = devicesharing[2,3](activity,t)
                                            Prob[2,2] = 3
                                            Prob[3,1] = devicesharing[2,1](activity,t)
                                            Prob[3,2] = 1
                                        else:
                                            if val3 <= val1 and val3 <= val2 and val1 <= val2:
                                                Prob[1,1] = devicesharing[2,3](activity,t)
                                                Prob[1,2] = 3
                                                Prob[2,1] = devicesharing[2,1](activity,t)
                                                Prob[2,2] = 1
                                                Prob[3,1] = devicesharing[2,2](activity,t)
                                                Prob[3,2] = 2
                                            else:
                                                if val3 <= val1 and val3 <= val2 and val2 <= val1:
                                                    Prob[1,1] = devicesharing[2,3](activity,t)
                                                    Prob[1,2] = 3
                                                    Prob[2,1] = devicesharing[2,2](activity,t)
                                                    Prob[2,2] = 2
                                                    Prob[3,1] = devicesharing[2,1](activity,t)
                                                    Prob[3,2] = 1
                            if activity == 1:
                                current[t,1] = 1
                            else:
                                if activity == 2:
                                    current[t,1] = 2
                                else:
                                    if activity == 3:
                                        current[t,1] = 3
                                    else:
                                        if activity == 16:
                                            current[t,1] = 16
                                        else:
                                            if (current(t,1) == current(t,2)) and (current(t,1) == current(t,3)):
                                                if r(t,1) <= Prob(1,1):
                                                    if Prob(1,2) == 1:
                                                        current[t,2] = 1
                                                        current[t,3] = 1
                                                    else:
                                                        if Prob(1,2) == 2:
                                                            current[t,3] = 1
                                                else:
                                                    if r(t,1) <= Prob(1,1) + Prob(2,1):
                                                        if Prob(2,2) == 1:
                                                            current[t,2] = 1
                                                            current[t,3] = 1
                                                        else:
                                                            if Prob(2,2) == 2:
                                                                current[t,3] = 1
                                                    else:
                                                        if r(t,1) <= Prob(1,1) + Prob(2,1) + Prob(3,1):
                                                            if Prob(3,2) == 1:
                                                                current[t,2] = 1
                                                                current[t,3] = 1
                                                            else:
                                                                if Prob(3,2) == 2:
                                                                    current[t,3] = 1
                                            else:
                                                if (current(t,1) == current(t,2)) and (current(t,1) == current(t,4)):
                                                    if r(t,1) <= Prob(1,1):
                                                        if Prob(1,2) == 1:
                                                            current[t,2] = 1
                                                            current[t,4] = 1
                                                        else:
                                                            if Prob(1,2) == 2:
                                                                current[t,4] = 1
                                                    else:
                                                        if r(t,1) <= Prob(1,1) + Prob(2,1):
                                                            if Prob(2,2) == 1:
                                                                current[t,2] = 1
                                                                current[t,4] = 1
                                                            else:
                                                                if Prob(2,2) == 2:
                                                                    current[t,4] = 1
                                                        else:
                                                            if r(t,1) <= Prob(1,1) + Prob(2,1) + Prob(3,1):
                                                                if Prob(3,2) == 1:
                                                                    current[t,2] = 1
                                                                    current[t,4] = 1
                                                                else:
                                                                    if Prob(3,2) == 2:
                                                                        current[t,4] = 1
                                                else:
                                                    if (current(t,1) == current(t,3)) and (current(t,1) == current(t,4)):
                                                        if r(t,1) <= Prob(1,1):
                                                            if Prob(1,2) == 1:
                                                                current[t,3] = 1
                                                                current[t,4] = 1
                                                            else:
                                                                if Prob(1,2) == 2:
                                                                    current[t,4] = 1
                                                        else:
                                                            if r(t,1) <= Prob(1,1) + Prob(2,1):
                                                                if Prob(2,2) == 1:
                                                                    current[t,3] = 1
                                                                    current[t,4] = 1
                                                                else:
                                                                    if Prob(2,2) == 2:
                                                                        current[t,4] = 1
                                                            else:
                                                                if r(t,1) <= Prob(1,1) + Prob(2,1) + Prob(3,1):
                                                                    if Prob(3,2) == 1:
                                                                        current[t,3] = 1
                                                                        current[t,4] = 1
                                                                    else:
                                                                        if Prob(3,2) == 2:
                                                                            current[t,4] = 1
                                                    else:
                                                        if (current(t,2) == current(t,3)) and (current(t,2) == current(t,4)):
                                                            if r(t,1) <= Prob(1,1):
                                                                if Prob(1,2) == 1:
                                                                    current[t,3] = 1
                                                                    current[t,4] = 1
                                                                else:
                                                                    if Prob(1,2) == 2:
                                                                        current[t,4] = 1
                                                            else:
                                                                if r(t,1) <= Prob(1,1) + Prob(2,1):
                                                                    if Prob(2,2) == 1:
                                                                        current[t,3] = 1
                                                                        current[t,4] = 1
                                                                    else:
                                                                        if Prob(2,2) == 2:
                                                                            current[t,4] = 1
                                                                else:
                                                                    if r(t,1) <= Prob(1,1) + Prob(2,1) + Prob(3,1):
                                                                        if Prob(3,2) == 1:
                                                                            current[t,3] = 1
                                                                            current[t,4] = 1
                                                                        else:
                                                                            if Prob(3,2) == 2:
                                                                                current[t,4] = 1
                        if actcount(activity,t) == 4:
                            val1 = devicesharing[1,1](activity,t)
                            val2 = devicesharing[1,2](activity,t)
                            val3 = devicesharing[1,3](activity,t)
                            val4 = devicesharing[1,4](activity,t)
                            if val1 <= val2 and val2 <= val3 and val3 <= val4:
                                Prob[1,1] = devicesharing[1,1](activity,t)
                                Prob[1,2] = 1
                                Prob[2,1] = devicesharing[1,2](activity,t)
                                Prob[2,2] = 2
                                Prob[3,1] = devicesharing[1,3](activity,t)
                                Prob[3,2] = 3
                                Prob[4,1] = devicesharing[1,4](activity,t)
                                Prob[4,2] = 4
                            else:
                                if val1 <= val2 and val2 <= val4 and val4 <= val3:
                                    Prob[1,1] = devicesharing[1,1](activity,t)
                                    Prob[1,2] = 1
                                    Prob[2,1] = devicesharing[1,2](activity,t)
                                    Prob[2,2] = 2
                                    Prob[3,1] = devicesharing[1,4](activity,t)
                                    Prob[3,2] = 4
                                    Prob[4,1] = devicesharing[1,3](activity,t)
                                    Prob[4,2] = 3
                                else:
                                    if val1 <= val3 and val3 <= val2 and val2 <= val4:
                                        Prob[1,1] = devicesharing[1,1](activity,t)
                                        Prob[1,2] = 1
                                        Prob[2,1] = devicesharing[1,3](activity,t)
                                        Prob[2,2] = 3
                                        Prob[3,1] = devicesharing[1,2](activity,t)
                                        Prob[3,2] = 2
                                        Prob[4,1] = devicesharing[1,4](activity,t)
                                        Prob[4,2] = 4
                                    else:
                                        if val1 <= val3 and val3 <= val4 and val4 <= val2:
                                            Prob[1,1] = devicesharing[1,1](activity,t)
                                            Prob[1,2] = 1
                                            Prob[2,1] = devicesharing[1,3](activity,t)
                                            Prob[2,2] = 3
                                            Prob[3,1] = devicesharing[1,4](activity,t)
                                            Prob[3,2] = 4
                                            Prob[4,1] = devicesharing[1,2](activity,t)
                                            Prob[4,2] = 2
                                        else:
                                            if val1 <= val4 and val4 <= val2 and val2 <= val3:
                                                Prob[1,1] = devicesharing[1,1](activity,t)
                                                Prob[1,2] = 1
                                                Prob[2,1] = devicesharing[1,4](activity,t)
                                                Prob[2,2] = 4
                                                Prob[3,1] = devicesharing[1,2](activity,t)
                                                Prob[3,2] = 2
                                                Prob[4,1] = devicesharing[1,3](activity,t)
                                                Prob[4,2] = 3
                                            else:
                                                if val1 <= val4 and val4 <= val3 and val3 <= val2:
                                                    Prob[1,1] = devicesharing[1,1](activity,t)
                                                    Prob[1,2] = 1
                                                    Prob[2,1] = devicesharing[1,4](activity,t)
                                                    Prob[2,2] = 4
                                                    Prob[3,1] = devicesharing[1,3](activity,t)
                                                    Prob[3,2] = 3
                                                    Prob[4,1] = devicesharing[1,2](activity,t)
                                                    Prob[4,2] = 2
                                                else:
                                                    if val2 <= val1 and val1 <= val3 and val3 <= val4:
                                                        Prob[1,1] = devicesharing[1,2](activity,t)
                                                        Prob[1,2] = 2
                                                        Prob[2,1] = devicesharing[1,1](activity,t)
                                                        Prob[2,2] = 1
                                                        Prob[3,1] = devicesharing[1,3](activity,t)
                                                        Prob[3,2] = 3
                                                        Prob[4,1] = devicesharing[1,4](activity,t)
                                                        Prob[4,2] = 4
                                                    else:
                                                        if val2 <= val1 and val1 <= val4 and val4 <= val3:
                                                            Prob[1,1] = devicesharing[1,2](activity,t)
                                                            Prob[1,2] = 2
                                                            Prob[2,1] = devicesharing[1,1](activity,t)
                                                            Prob[2,2] = 1
                                                            Prob[3,1] = devicesharing[1,4](activity,t)
                                                            Prob[3,2] = 4
                                                            Prob[4,1] = devicesharing[1,3](activity,t)
                                                            Prob[4,2] = 3
                                                        else:
                                                            if val2 <= val3 and val3 <= val1 and val1 <= val4:
                                                                Prob[1,1] = devicesharing[1,2](activity,t)
                                                                Prob[1,2] = 2
                                                                Prob[2,1] = devicesharing[1,3](activity,t)
                                                                Prob[2,2] = 3
                                                                Prob[3,1] = devicesharing[1,1](activity,t)
                                                                Prob[3,2] = 1
                                                                Prob[4,1] = devicesharing[1,4](activity,t)
                                                                Prob[4,2] = 4
                                                            else:
                                                                if val2 <= val3 and val3 <= val4 and val4 <= val1:
                                                                    Prob[1,1] = devicesharing[1,2](activity,t)
                                                                    Prob[1,2] = 2
                                                                    Prob[2,1] = devicesharing[1,3](activity,t)
                                                                    Prob[2,2] = 3
                                                                    Prob[3,1] = devicesharing[1,4](activity,t)
                                                                    Prob[3,2] = 4
                                                                    Prob[4,1] = devicesharing[1,1](activity,t)
                                                                    Prob[4,2] = 1
                                                                else:
                                                                    if val2 <= val4 and val4 <= val1 and val1 <= val3:
                                                                        Prob[1,1] = devicesharing[1,2](activity,t)
                                                                        Prob[1,2] = 2
                                                                        Prob[2,1] = devicesharing[1,4](activity,t)
                                                                        Prob[2,2] = 4
                                                                        Prob[3,1] = devicesharing[1,1](activity,t)
                                                                        Prob[3,2] = 1
                                                                        Prob[4,1] = devicesharing[1,3](activity,t)
                                                                        Prob[4,2] = 3
                                                                    else:
                                                                        if val2 <= val4 and val4 <= val3 and val3 <= val1:
                                                                            Prob[1,1] = devicesharing[1,2](activity,t)
                                                                            Prob[1,2] = 2
                                                                            Prob[2,1] = devicesharing[1,4](activity,t)
                                                                            Prob[2,2] = 4
                                                                            Prob[3,1] = devicesharing[1,3](activity,t)
                                                                            Prob[3,2] = 3
                                                                            Prob[4,1] = devicesharing[1,1](activity,t)
                                                                            Prob[4,2] = 1
                                                                        else:
                                                                            if val3 <= val1 and val1 <= val2 and val2 <= val4:
                                                                                Prob[1,1] = devicesharing[1,3](activity,t)
                                                                                Prob[1,2] = 3
                                                                                Prob[2,1] = devicesharing[1,1](activity,t)
                                                                                Prob[2,2] = 1
                                                                                Prob[3,1] = devicesharing[1,2](activity,t)
                                                                                Prob[3,2] = 2
                                                                                Prob[4,1] = devicesharing[1,4](activity,t)
                                                                                Prob[4,2] = 4
                                                                            else:
                                                                                if val3 <= val1 and val1 <= val4 and val4 <= val2:
                                                                                    Prob[1,1] = devicesharing[1,3](activity,t)
                                                                                    Prob[1,2] = 3
                                                                                    Prob[2,1] = devicesharing[1,1](activity,t)
                                                                                    Prob[2,2] = 1
                                                                                    Prob[3,1] = devicesharing[1,4](activity,t)
                                                                                    Prob[3,2] = 4
                                                                                    Prob[4,1] = devicesharing[1,2](activity,t)
                                                                                    Prob[4,2] = 2
                                                                                else:
                                                                                    if val3 <= val2 and val2 <= val1 and val1 <= val4:
                                                                                        Prob[1,1] = devicesharing[1,3](activity,t)
                                                                                        Prob[1,2] = 3
                                                                                        Prob[2,1] = devicesharing[1,2](activity,t)
                                                                                        Prob[2,2] = 2
                                                                                        Prob[3,1] = devicesharing[1,1](activity,t)
                                                                                        Prob[3,2] = 1
                                                                                        Prob[4,1] = devicesharing[1,4](activity,t)
                                                                                        Prob[4,2] = 4
                                                                                    else:
                                                                                        if val3 <= val2 and val2 <= val4 and val4 <= val1:
                                                                                            Prob[1,1] = devicesharing[1,3](activity,t)
                                                                                            Prob[1,2] = 3
                                                                                            Prob[2,1] = devicesharing[1,2](activity,t)
                                                                                            Prob[2,2] = 2
                                                                                            Prob[3,1] = devicesharing[1,4](activity,t)
                                                                                            Prob[3,2] = 4
                                                                                            Prob[4,1] = devicesharing[1,1](activity,t)
                                                                                            Prob[4,2] = 1
                                                                                        else:
                                                                                            if val3 <= val4 and val4 <= val1 and val1 <= val2:
                                                                                                Prob[1,1] = devicesharing[1,3](activity,t)
                                                                                                Prob[1,2] = 3
                                                                                                Prob[2,1] = devicesharing[1,4](activity,t)
                                                                                                Prob[2,2] = 4
                                                                                                Prob[3,1] = devicesharing[1,1](activity,t)
                                                                                                Prob[3,2] = 1
                                                                                                Prob[4,1] = devicesharing[1,2](activity,t)
                                                                                                Prob[4,2] = 2
                                                                                            else:
                                                                                                if val3 <= val4 and val4 <= val2 and val2 <= val1:
                                                                                                    Prob[1,1] = devicesharing[1,3](activity,t)
                                                                                                    Prob[1,2] = 3
                                                                                                    Prob[2,1] = devicesharing[1,4](activity,t)
                                                                                                    Prob[2,2] = 4
                                                                                                    Prob[3,1] = devicesharing[1,2](activity,t)
                                                                                                    Prob[3,2] = 2
                                                                                                    Prob[4,1] = devicesharing[1,1](activity,t)
                                                                                                    Prob[4,2] = 1
                                                                                                else:
                                                                                                    if val4 <= val1 and val1 <= val2 and val2 <= val3:
                                                                                                        Prob[1,1] = devicesharing[1,4](activity,t)
                                                                                                        Prob[1,2] = 4
                                                                                                        Prob[2,1] = devicesharing[1,1](activity,t)
                                                                                                        Prob[2,2] = 1
                                                                                                        Prob[3,1] = devicesharing[1,2](activity,t)
                                                                                                        Prob[3,2] = 2
                                                                                                        Prob[4,1] = devicesharing[1,3](activity,t)
                                                                                                        Prob[4,2] = 3
                                                                                                    else:
                                                                                                        if val4 <= val1 and val1 <= val3 and val3 <= val2:
                                                                                                            Prob[1,1] = devicesharing[1,4](activity,t)
                                                                                                            Prob[1,2] = 4
                                                                                                            Prob[2,1] = devicesharing[1,1](activity,t)
                                                                                                            Prob[2,2] = 1
                                                                                                            Prob[3,1] = devicesharing[1,3](activity,t)
                                                                                                            Prob[3,2] = 3
                                                                                                            Prob[4,1] = devicesharing[1,2](activity,t)
                                                                                                            Prob[4,2] = 2
                                                                                                        else:
                                                                                                            if val4 <= val2 and val2 <= val1 and val1 <= val3:
                                                                                                                Prob[1,1] = devicesharing[1,4](activity,t)
                                                                                                                Prob[1,2] = 4
                                                                                                                Prob[2,1] = devicesharing[1,2](activity,t)
                                                                                                                Prob[2,2] = 2
                                                                                                                Prob[3,1] = devicesharing[1,1](activity,t)
                                                                                                                Prob[3,2] = 1
                                                                                                                Prob[4,1] = devicesharing[1,3](activity,t)
                                                                                                                Prob[4,2] = 3
                                                                                                            else:
                                                                                                                if val4 <= val2 and val2 <= val3 and val3 <= val1:
                                                                                                                    Prob[1,1] = devicesharing[1,4](activity,t)
                                                                                                                    Prob[1,2] = 4
                                                                                                                    Prob[2,1] = devicesharing[1,2](activity,t)
                                                                                                                    Prob[2,2] = 2
                                                                                                                    Prob[3,1] = devicesharing[1,3](activity,t)
                                                                                                                    Prob[3,2] = 3
                                                                                                                    Prob[4,1] = devicesharing[1,1](activity,t)
                                                                                                                    Prob[4,2] = 1
                                                                                                                else:
                                                                                                                    if val4 <= val3 and val3 <= val1 and val1 <= val2:
                                                                                                                        Prob[1,1] = devicesharing[1,4](activity,t)
                                                                                                                        Prob[1,2] = 4
                                                                                                                        Prob[2,1] = devicesharing[1,3](activity,t)
                                                                                                                        Prob[2,2] = 3
                                                                                                                        Prob[3,1] = devicesharing[1,1](activity,t)
                                                                                                                        Prob[3,2] = 1
                                                                                                                        Prob[4,1] = devicesharing[1,2](activity,t)
                                                                                                                        Prob[4,2] = 2
                                                                                                                    else:
                                                                                                                        if val4 <= val3 and val3 <= val2 and val2 <= val1:
                                                                                                                            Prob[1,1] = devicesharing[1,4](activity,t)
                                                                                                                            Prob[1,2] = 4
                                                                                                                            Prob[2,1] = devicesharing[1,3](activity,t)
                                                                                                                            Prob[2,2] = 3
                                                                                                                            Prob[3,1] = devicesharing[1,2](activity,t)
                                                                                                                            Prob[3,2] = 2
                                                                                                                            Prob[4,1] = devicesharing[1,1](activity,t)
                                                                                                                            Prob[4,2] = 1
                            if activity == 1:
                                current[t,1] = 1
                            else:
                                if activity == 2:
                                    current[t,1] = 2
                                else:
                                    if activity == 3:
                                        current[t,1] = 3
                                    else:
                                        if activity == 16:
                                            current[t,1] = 16
                                        else:
                                            if current(t,1) == current(t,2) and current(t,1) == current(t,3) and current(t,1) == current(t,4):
                                                if r(t,1) <= Prob(1,1):
                                                    if Prob(1,2) == 1:
                                                        current[t,2] = 1
                                                        current[t,3] = 1
                                                        current[t,4] = 1
                                                    else:
                                                        if Prob(1,2) == 2:
                                                            current[t,3] = 1
                                                            current[t,4] = 1
                                                        else:
                                                            if Prob(1,2) == 3:
                                                                current[t,4] = 1
                                                else:
                                                    if r(t,1) <= Prob(1,1) + Prob(2,1):
                                                        if Prob(2,2) == 1:
                                                            current[t,2] = 1
                                                            current[t,3] = 1
                                                            current[t,4] = 1
                                                        else:
                                                            if Prob(2,2) == 2:
                                                                current[t,3] = 1
                                                                current[t,4] = 1
                                                            else:
                                                                if Prob(2,2) == 3:
                                                                    current[t,4] = 1
                                                    else:
                                                        if r(t,1) <= Prob(1,1) + Prob(2,1) + Prob(3,1):
                                                            if Prob(3,2) == 1:
                                                                current[t,2] = 1
                                                                current[t,3] = 1
                                                                current[t,4] = 1
                                                            else:
                                                                if Prob(3,2) == 2:
                                                                    current[t,3] = 1
                                                                    current[t,4] = 1
                                                                else:
                                                                    if Prob(3,2) == 3:
                                                                        current[t,4] = 1
                                                        else:
                                                            if r(t,1) <= (Prob(1,1) + Prob(2,1) + Prob(3,1) + Prob(4,1)):
                                                                if Prob(4,2) == 1:
                                                                    current[t,2] = 1
                                                                    current[t,3] = 1
                                                                    current[t,4] = 1
                                                                else:
                                                                    if Prob(4,2) == 2:
                                                                        current[t,3] = 1
                                                                        current[t,4] = 1
                                                                    else:
                                                                        if Prob(4,2) == 3:
                                                                            current[t,4] = 1
    
    return current
    
    return current