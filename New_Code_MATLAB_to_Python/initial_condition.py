import numpy as np
    
def initial_condition(IC = None,r = None): 
    # Sets the initial condition of the user.
    
    # Arguments:
#   IC (array) [-]: Probability array of initial condititions;
#   r (float) [-]: A random number.
    
    # Returns:
#   stateone (int) [-]: Initial user activity state.
    
    for n in np.arange(1,16+1).reshape(-1):
        if r <= sum(IC(np.arange(1,n+1),1)):
            stateone = n
            break
    
    return stateone
    
    return stateone