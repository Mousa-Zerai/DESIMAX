import numpy as np
    
def activity_profile_generation(n_occ = None,n_working = None,day = None,agg_size = None,TM = None,IC = None,Sharing = None): 
    # Generate household occupant activity profiles.
    
    # Arguments:
#   n_occ (int) [-]: The number of occupants in the household;
#   n_working (int) [-]: The number of working occupants in the household;
#   day (int) [-]: Day identifier;
#   agg_size (int) [-]: The total number of households to be created;
#   TM (cell) [-]: DataStructure to hold the transition matrix
#       probabilities;.
#   IC (cell) [-]: DataStructure to hold the transition matrix
#       probabilities;
#   Sharing (cell) [-]: DataStructure to hold the transition matrix
#       probabilities.
    
    # Returns:
#   profiles (cell) [-]: DataStructure to hold the user activity profiles;
#   hh_occ (array) [-]: DataStructure to hold the overall household
#      occupancy data.
    
    # Generate all random numbers
    a = 0
    b = 1
    
    rtot = a + np.multiply((b - a),np.random.rand(144,agg_size * n_occ))
    # Get transition matrix, initial conditions and sharing probabilities
    transition_matrix = TM[1,n_occ][n_working + 1,day]
    initial_conditions = IC[1,n_occ][n_working + 1,day]
    if n_occ > 1:
        device_sharing = Sharing[1,n_occ][1,n_working + 1][1,day]
    
    # Initiate return vars
    profiles = cell(agg_size,1)
    hh_occ = np.zeros((144,agg_size))
    # Algorithm
    if n_occ == 1:
        for e in np.arange(1,agg_size+1).reshape(-1):
            current = np.zeros((144,1))
            UserProfile = np.zeros((144,17))
            rv = rtot(1,e)
            r = rtot
            nextvalue = initial_condition(initial_conditions,rv)
            current[1,1] = nextvalue
            UserProfile[1,current[1,1]] = UserProfile(1,current(1,1)) + 1
            if ((UserProfile(1,2) == 1) or (UserProfile(1,15) == 1) or (UserProfile(1,16) == 1)):
                UserProfile[1,17] = UserProfile(1,17) + 0
            else:
                UserProfile[1,17] = UserProfile(1,17) + 1
            for d in np.arange(1,143+1).reshape(-1):
                CurrentMatrix = cell2mat(transition_matrix(d))
                var = current(d,1)
                for nextvar in np.arange(1,16+1).reshape(-1):
                    if r(d + 1,e) <= sum(CurrentMatrix(var,np.arange(1,nextvar+1))):
                        current[d + 1,1] = nextvar
                        UserProfile[d + 1,current[d + 1,1]] = UserProfile(d + 1,current(d + 1,1)) + 1
                        if ((UserProfile(d + 1,2) == 1) or (UserProfile(d + 1,15) == 1) or (UserProfile(d + 1,16) == 1)):
                            UserProfile[d + 1,17] = UserProfile(d + 1,17) + 0
                        else:
                            UserProfile[d + 1,17] = UserProfile(d + 1,17) + 1
                        break
            profiles[e][1,1] = UserProfile
            hh_occ[:,e] = UserProfile(:,17)
    else:
        randomcounter = 1
        for n in np.arange(1,agg_size+1).reshape(-1):
            current = np.zeros((144,n_occ))
            for e in np.arange(1,n_occ+1).reshape(-1):
                rv = rtot(1,randomcounter)
                r = rtot(:,randomcounter)
                nextvalue = initial_condition(initial_conditions,rv)
                current[1,e] = nextvalue
                for d in np.arange(1,143+1).reshape(-1):
                    CurrentMatrix = cell2mat(transition_matrix(d))
                    var = current(d,e)
                    for nextvar in np.arange(1,16+1).reshape(-1):
                        if r(d + 1,1) <= sum(CurrentMatrix(var,np.arange(1,nextvar+1))):
                            current[d + 1,e] = nextvar
                            break
                randomcounter = randomcounter + 1
            current = check_device_sharing(current,n_occ,device_sharing)
            for b in np.arange(1,n_occ+1).reshape(-1):
                UserProfile = np.zeros((144,17))
                for t in np.arange(1,144+1).reshape(-1):
                    UserProfile[t,current[t,b]] = UserProfile(t,current(t,b)) + 1
                    if ((UserProfile(t,2) == 1) or (UserProfile(t,15) == 1) or (UserProfile(t,16) == 1)):
                        UserProfile[t,17] = UserProfile(t,17) + 0
                    else:
                        UserProfile[t,17] = UserProfile(t,17) + 1
                profiles[n][b,1] = UserProfile
                hh_occ[:,n] = hh_occ(:,n) + UserProfile(:,17)
    
    return profiles,hh_occ
    