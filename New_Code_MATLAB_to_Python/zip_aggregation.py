import numpy as np
    
def zip_aggregation(p_hh = None,occ_power = None,hh_zips = None,nocc = None,lightzip = None,lightload = None,wet_starts = None,wet_ends = None): 
    # Build the household ZIP model. The aggregate ZIP is obtained by a
# weighted summation of all household loads. First each user is aggregated
# and then lighting, heating, EVs and the user defined load are added.
    
    # Arguments:
#   p_hh (array) [W]: Active power demand profile of the household;
#   occ_power (cell [-]: DataStructure to hold the power profiles of every
#       household load for every occupant. This can be either active or
#       reactive power demand;
#   hh_zips (cell) [-]: ZIP models for each household appliance;
#   n_occ (int) [-]: The number of occupants in the household;
#   lightzip (array) [-]: ZIP models for lamps;
#   lightload (cell) [-]: Demand profile of each individual lamp;;
#   wet_starts (array) [min]: Start times of wet loads;;
#   wet_ends (array) [min]: End times of wet loads.
    
    # Returns:
#   agg_zip (array) [-]: Aggregate ZIP model of the household.
    
    agg_zip = np.zeros((1440,3))
    for user in np.arange(1,nocc+1).reshape(-1):
        for appliance in np.array([1,5,np.arange(7,26+1),np.arange(28,33+1)]).reshape(-1):
            p_app = occ_power[1,user](:,appliance)
            if sum(p_app) > 0:
                p_zip_model = hh_zips[appliance]
                agg_zip = agg_zip + np.abs(p_app) / p_hh * p_zip_model
        for appliance in np.array([4,6,27]).reshape(-1):
            if sum(occ_power[1,user](:,appliance)) > 0:
                if 4 == appliance:
                    idx = 1
                else:
                    if 6 == appliance:
                        idx = 2
                    else:
                        if 27 == appliance:
                            idx = 3
                wet_zip = np.zeros((1440,3))
                start_time = wet_starts(idx,user)
                end_time = wet_ends(idx,user)
                if start_time > end_time:
                    cycle = hh_zips[1,appliance].shape[1-1]
                    wet_zip[np.arange[1,end_time+1],:] = hh_zips[1,appliance](np.arange(cycle - end_time + 1,cycle+1),:)
                    wet_zip[np.arange[start_time,1440+1],:] = hh_zips[1,appliance](np.arange(1,cycle - end_time+1),:)
                else:
                    wet_zip[np.arange[start_time,end_time+1],:] = hh_zips[1,appliance]
                p_wet = np.abs(occ_power[1,user](:,appliance)) / p_hh
                agg_zip = agg_zip + bsxfun(times,wet_zip,p_wet)
    
    # lighting
    for light in np.arange(1,lightzip.shape[1-1]+1).reshape(-1):
        p_light = lightload[0](:,light)
        p_zip_model = lightzip(light,:)
        agg_zip = agg_zip + np.abs(p_light) / p_hh * p_zip_model
    
    # heating
    agg_zip = agg_zip + np.abs(occ_power[1,nocc + 2]) / p_hh * hh_zips[35]
    # EVs
    agg_zip = agg_zip + np.abs(occ_power[1,nocc + 3]) / p_hh * hh_zips[34]
    # Spare load space
    p_new = np.abs(occ_power[1,nocc + 4]) / p_hh
    agg_zip = agg_zip + bsxfun(times,hh_zips[36],p_new)
    return agg_zip
    
    return agg_zip