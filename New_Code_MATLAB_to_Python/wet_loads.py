import numpy as np
    
def wet_loads(time_res = None,activ = None,p_cycle = None,q_cycle = None,type_ = None): 
    # wet_loads  Assign wet load cycle to given instance of use. Two sets of
# statistics are applied to define the clothes drier activity: one to
# determine if the load is used or not and another to set the start time of
# the appliance. If the load is used then the cycle defined is connected
# from the locally defined start time.
    
    # Arguments:
#   time_res (int) [min]: Simulation time step;
#   activ (144x1) [-]: Activity profile of the load;
#   month (int) []:  Month of year;
#   p_cycle (array) [W]: Active power cycle of the appliance;
#   q_cycle (array) [var]: Reactive power cycle of the appliance;
#   type (int) [-]: Wet load type identifier. Allowed values: 1 =
#   dishwasher, 2 = washingmachine.
    
    # Returns:
#   p (t x 1) [W]: Active power profile of load;
#   q (t x 1) [var]: Reactive power profile of load;
#   start_time (int) [min]: Start time of load use;
#   end_time (int) [min]: End time of load use.
    
    if type_ == 1:
        use_prob = 0.4
        use_stats = np.array([0.171,0.327,0.529,0.822,1,1])
        b = 0
    else:
        if type_ == 2:
            use_prob = 1
            use_stats = np.array([0.235,0.414,0.634,0.871,1,1])
            b = - 1
        else:
            print('error')
    
    w = find(activ)
    cycle_length = len(p_cycle)
    p = np.zeros((time_res,1))
    q = np.zeros((time_res,1))
    start_time = - 1
    end_time = - 1
    time_period_start[1,1] = 37
    time_period_start[2,1] = 61
    time_period_start[3,1] = 85
    time_period_start[4,1] = 109
    time_period_start[5,1] = 133
    time_period_start[6,1] = 1
    time_period_end[1,1] = 60
    time_period_end[2,1] = 84
    time_period_end[3,1] = 108
    time_period_end[4,1] = 132
    time_period_end[5,1] = 144
    time_period_end[6,1] = 36
    time_shifts[1,1] = 360
    time_shifts[2,1] = 600
    time_shifts[3,1] = 840
    time_shifts[4,1] = 1080
    time_shifts[5,1] = 1320
    time_shifts[6,1] = 0
    if w.shape[1-1] == 1:
        w = w * 10
        w = w + randi(np.array([0,9]))
        if w > time_res:
            w = w - time_res
        b = w - 1 + cycle_length
        if b > time_res:
            first_end = cycle_length - (b - time_res)
            p[np.arange[w,time_res+1]] = p_cycle(np.arange(1,first_end+1))
            q[np.arange[w,time_res+1]] = q_cycle(np.arange(1,first_end+1))
            p[np.arange[1,b - time_res+1]] = p_cycle(np.arange(first_end + 1,cycle_length+1))
            q[np.arange[1,b - time_res+1]] = q_cycle(np.arange(first_end + 1,cycle_length+1))
            start_time = w
            end_time = b - time_res
        else:
            p[np.arange[w,b+1]] = p_cycle
            q[np.arange[w,b+1]] = q_cycle
            start_time = w
            end_time = b
    else:
        if w.shape[1-1] > 1:
            if np.random.rand(1) <= use_prob:
                use_flag = 0
                tz[1,1] = find(activ(np.arange(time_period_start(1),time_period_end(1)+1)))
                tz[2,1] = find(activ(np.arange(time_period_start(2),time_period_end(2)+1)))
                tz[3,1] = find(activ(np.arange(time_period_start(3),time_period_end(3)+1)))
                tz[4,1] = find(activ(np.arange(time_period_start(4),time_period_end(4)+1)))
                tz[5,1] = find(activ(np.arange(time_period_start(5),time_period_end(5)+1)))
                tz[6,1] = find(activ(np.arange(time_period_start(6),time_period_end(6)+1)))
                for k in np.arange(6,1+- 1,- 1).reshape(-1):
                    if tz[k,1].shape[1-1] > 1:
                        use_flag = 1
                    if use_flag == 1:
                        wstart = randsample(tz[k,1],1)
                        b = time_shifts(k) + wstart * 10 + randi(np.array([0,9])) - 1 + cycle_length
                        if b > time_res:
                            if b - cycle_length + 1 <= time_res:
                                end_ = cycle_length - (b - time_res)
                                p[np.arange[b - cycle_length + 1,time_res+1]] = p_cycle(np.arange(1,end_+1))
                                q[np.arange[b - cycle_length + 1,time_res+1]] = q_cycle(np.arange(1,end_+1))
                                p[np.arange[1,b - time_res+1]] = p_cycle(np.arange(end_ + 1,cycle_length+1))
                                q[np.arange[1,b - time_res+1]] = q_cycle(np.arange(end_ + 1,cycle_length+1))
                                start_time = b - cycle_length + 1
                                end_time = b - time_res
                            else:
                                p[np.arange[b - time_res - cycle_length + 1,b - time_res+1]] = p_cycle
                                q[np.arange[b - time_res - cycle_length + 1,b - time_res+1]] = q_cycle
                                start_time = b - time_res - cycle_length + 1
                                end_time = b - time_res
                        else:
                            p[np.arange[b - cycle_length,b - 1+1]] = p_cycle
                            q[np.arange[b - cycle_length,b - 1+1]] = q_cycle
                            start_time = b - cycle_length
                            end_time = b - 1
                        break
    
    return p,q,start_time,end_time
    