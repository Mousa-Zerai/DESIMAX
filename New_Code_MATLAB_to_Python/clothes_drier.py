import numpy as np
    
def clothes_drier(time_res = None,month = None,wm_end = None,p_cycle = None,q_cycle = None): 
    # Assign load cycle to a given instance of use of the clothes drier load.
# This function is dependent on a previous use of the washing machine load.
# If the washing machine load has previously been utilised then two sets of
# statistics are applied to define the clothes drier activity: one to
# determine if the load is used or not and another to set the start time of
# the appliance. If the load is used then the cycle is connected from the
# locally defined start time.
    
    # Arguments:
#   time_res (int) [min]: Simulation time step;
#   month (int) []:  Month of year;
#   wm_end (int) [min]: End time of the washing machine load;
#   p_cycle (array) [W]: Active power cycle of the appliance;
#   q_cycle (array) [var]: Reactive power cycle of the appliance.
    
    # Returns:
#   p (array) [W]: Active power profile of the clothes drier load;
#   q (array) [var]: Reactive power profile of the clothes drier load;
#   start_time (int) [min]: Start time of the load use;
#   end_time (int) [min]: End time of the load use.
    
    p = np.zeros((time_res,1))
    q = np.zeros((time_res,1))
    clothes_drier_prob1 = 0.235
    clothes_drier_prob2 = 0.308
    clothes_drier_delay_min = 5
    clothes_drier_delay_max = 120
    start_time = - 1
    end_time = - 1
    duration = p_cycle.shape[1-1]
    if (month > 5) and (month < 9):
        TDprob = clothes_drier_prob1
    else:
        TDprob = clothes_drier_prob2
    
    if np.random.rand(1) <= TDprob:
        start_time = wm_end + randi(np.array([clothes_drier_delay_min,clothes_drier_delay_max]))
        if start_time > time_res:
            start_time = start_time - time_res
        end_time = start_time - 1 + duration
        if end_time <= time_res:
            p[np.arange[start_time,end_time+1]] = p_cycle
            q[np.arange[start_time,end_time+1]] = q_cycle
        else:
            first_end = duration - (end_time - time_res)
            p[np.arange[start_time,time_res+1]] = p_cycle(np.arange(1,first_end+1))
            q[np.arange[start_time,time_res+1]] = q_cycle(np.arange(1,first_end+1))
            p[np.arange[1,end_time - time_res+1]] = p_cycle(np.arange(first_end + 1,duration+1))
            q[np.arange[1,end_time - time_res+1]] = q_cycle(np.arange(first_end + 1,duration+1))
            end_time = end_time - time_res
    
    return p,q,start_time,end_time
    