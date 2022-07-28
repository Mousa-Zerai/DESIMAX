import numpy as np
    
def electric_shower_loads(time_res = None,activ = None,rated_power = None,rated_q_power = None,ownership = None): 
    # Convert activity into Shower loads. Three sets of statistics are applied:
# one to determine if the load is used or not, another to set the start
# time of the appliance and another to set the duration.
    
    # Arguments:
#   time_res (int) [min]: Simulation time step.
#   activ (cell) [-]: DataStructure to hold the user activity profiles;
#   rated_power (float) [W]: Active power of the load;
#   rated_q_power (float) [var]: Reactive power of the load;
#   ownership (float) [-]: Ownership probability.
    
    # Returns:
#   p (array) [W]: Active power profile of the shower load;
#   q (array) [var]: Reactive power profile of the shower load.
    
    # initialise vars here
    p = np.zeros((time_res,1))
    q = np.zeros((time_res,1))
    duration_mean = 8
    
    duration_sigma = 2
    
    duration_min = 3
    
    duration_max = 15
    
    prob_bounds = np.array([[0,0.5],[0.5,0.6],[0.6,0.95],[0.95,1]])
    time_bounds = np.array([[31,60],[61,102],[103,144],[1,30]])
    if (np.random.rand(1) >= ownership):
        duration = np.round(np.random.randn(1) * duration_sigma + duration_mean)
        duration[duration < duration_min] = duration_min
        duration[duration > duration_max] = duration_max
        sh = np.random.rand(1)
        if (sh > prob_bounds(1,1) and sh <= prob_bounds(1,2)):
            sh2 = find(activ(np.arange(time_bounds(1,1),time_bounds(1,2)+1)))
            if not len(sh2)==0 :
                sh2start = randsample(sh2,1)
                start_time = (time_bounds(1,1) - 1) * 10 + sh2start * 10 + randi(np.array([0,9]))
                p[np.arange[start_time,start_time + duration - 1+1],1] = rated_power
                q[np.arange[start_time,start_time + duration - 1+1],1] = rated_q_power
        else:
            if (sh > prob_bounds(2,1) and sh <= prob_bounds(2,2)):
                sh2 = find(activ(np.arange(time_bounds(2,1),time_bounds(2,2)+1)))
                if not len(sh2)==0 :
                    sh2start = randsample(sh2,1)
                    start_time = (time_bounds(2,1) - 1) * 10 + sh2start * 10 + randi(np.array([0,9]))
                    p[np.arange[start_time,start_time + duration - 1+1],1] = rated_power
                    q[np.arange[start_time,start_time + duration - 1+1],1] = rated_q_power
            else:
                if (sh > prob_bounds(3,1) and sh <= prob_bounds(4,1)):
                    sh2 = find(activ(np.arange(time_bounds(3,1),time_bounds(3,2)+1)))
                    if not len(sh2)==0 :
                        sh2start = randsample(sh2,1)
                        l = (time_bounds(3,1) - 1) * 10 + sh2start * 10 + randi(np.array([0,9]))
                        if l + duration > time_res:
                            p[np.arange[l,time_res+1],1] = rated_power
                            p[np.arange[1,[l + duration - 1] - time_res+1],1] = rated_power
                            q[np.arange[l,time_res+1],1] = rated_q_power
                            q[np.arange[1,[l + duration - 1] - time_res+1],1] = rated_q_power
                        else:
                            p[np.arange[l,l + duration - 1+1],1] = rated_power
                            q[np.arange[l,l + duration - 1+1],1] = rated_q_power
                else:
                    sh2 = find(activ(np.arange(time_bounds(4,1),time_bounds(4,2)+1)))
                    if not len(sh2)==0 :
                        sh2start = randsample(sh2,1)
                        start_time = sh2start * 10 + randi(np.array([0,9]))
                        p[np.arange[start_time,start_time + duration - 1+1],1] = rated_power
                        q[np.arange[start_time,start_time + duration - 1+1],1] = rated_q_power
    
    return p,q
    