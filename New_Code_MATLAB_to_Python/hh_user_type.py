import numpy as np
    
def hh_user_type(user_type_pu = None,agg_size = None): 
    # Randomly distribute user behaviour.
    
    # Arguments:
#   user_type_pu (array) [-]: Proportion of each user type in the aggregate
#       population;
#   agg_size (int) [-]: The total number of households to be created.
    
    # Returns:
#   hh_type (array) [-]: Type of each husehold.
    
    User_type = np.multiply(user_type_pu,agg_size)
    User_type_step2 = np.round(User_type)
    User_type_step3 = sum(sum(User_type_step2))
    if User_type_step3 > agg_size:
        error = User_type_step3 - agg_size
        U_hh_final = RoundDown(User_type,error)
    else:
        if User_type_step3 < agg_size:
            error = agg_size - User_type_step3
            U_hh_final = RoundUp(User_type,error)
        else:
            U_hh_final = User_type_step2
    
    N = agg_size
    r = randperm(N)
    count = 1
    hh_type = np.zeros((N,1))
    for a in np.arange(1,N+1).reshape(-1):
        index = r(1,a)
        if count <= (U_hh_final(1,1)):
            hh_type[index,1] = 0
            count = count + 1
        else:
            if count <= (U_hh_final(1,2) + U_hh_final(1,1)):
                hh_type[index,1] = 1
                count = count + 1
            else:
                hh_type[index,1] = 2
                count = count + 1
    
    return hh_type
    
    return hh_type