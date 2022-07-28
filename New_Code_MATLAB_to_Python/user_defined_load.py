import numpy as np
    
def user_defined_load(agg_size = None,data_dir = None,new_load_data = None,filename = None): 
    # Add a user defined load. Two different user definitions are accounted
# for: 1 - one load profile with power demand defined from uniform
# distribution and a set penetration level, 2 - multiple individual load
# profiles. The new loads are randomly allocated within the total
# population.
    
    # Args:
#   agg_size (int) [-]: The total number of households to be created.
#   data_dir (str) [-]: Path to the data directory.
#   new_load_data (array) [-]: Overview of the new load electrical data.
#   filename (str) [-]: Filename of load definition.
    
    # Returns:
#   new_load_locs (array) [-]: Household number to which the new load is
#      assigned.
#   new_load (cell) [-]: DataStructure to carry all new load electrical
#       characteristics.
    
    new_load_type = new_load_data(1)
    if new_load_type == 1:
        new_load_electrical_data = xlsread(strjoin(np.array([data_dir,filename]),''),'electrical','B3..I1442')
        # how many loads
        new_load_penetration = new_load_data(2)
        n_new_loads = np.round(agg_size * new_load_penetration)
        default_p = new_load_electrical_data(:,1)
        default_q = new_load_electrical_data(:,2)
        # make it fuzzy
        new_load_fuzzy_p_min = new_load_data(3)
        new_load_fuzzy_p_max = new_load_data(4)
        new_load_fuzzy_q_min = new_load_data(5)
        new_load_fuzzy_q_max = new_load_data(6)
        r_p = new_load_fuzzy_p_min + np.multiply((new_load_fuzzy_p_max - new_load_fuzzy_p_min),np.random.rand(n_new_loads,1))
        r_q = new_load_fuzzy_q_min + np.multiply((new_load_fuzzy_q_max - new_load_fuzzy_q_min),np.random.rand(n_new_loads,1))
        new_load = cell(n_new_loads,1)
        for i in np.arange(1,n_new_loads+1).reshape(-1):
            new_loads_data[:,1] = np.multiply(default_p,r_p(i))
            new_loads_data[:,2] = np.multiply(default_q,r_q(i))
            new_loads_data[:,np.arange[3,5+1]] = new_load_electrical_data(:,np.arange(3,5+1))
            new_loads_data[:,np.arange[6,8+1]] = new_load_electrical_data(:,np.arange(6,8+1))
            new_load[i] = new_loads_data
    else:
        if new_load_type == 2:
            __,sheets = xlsfinfo(strjoin(np.array([data_dir,'new_load_two.xlsx']),''))
            # find electrical sheets
            idx = strfind(sheets,'electrical')
            idx = find(not_(cellfun('isempty',idx)))
            n_new_loads = len(idx)
            new_load = cell(n_new_loads,1)
            i = 1
            for a in idx.reshape(-1):
                new_load[i] = xlsread(strjoin(np.array([data_dir,'new_load_two.xlsx']),''),sheets[a],'B2..I1441')
                i = i + 1
    
    # randomly assign to household
    new_load_locs = __builtint__.sorted(randperm(agg_size,n_new_loads))
    return new_load_locs,new_load
    
    return new_load_locs,new_load