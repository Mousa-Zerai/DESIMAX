import numpy as np
    
def appliance_population(time_res = None,n_occ = None,tv_stuff = None,settop_box = None,printer = None,music = None,router = None,phone = None,cooking = None,iron = None,vacuum = None,shower = None,dishwasher = None,washingmachine = None,clothesdrier = None,gamesconsole = None,computers = None,monitors = None,heating = None,cold_loads = None,ev = None): 
    # Generate household loads. Appliances are selected based on the ownership
# statistics defined in the input configuration files. Each appliance is
# assigned relevant electrical characteristics, which include: operating
# power, power factor, standby power and electrical load model.
# Auxililiary/dependent loads, e.g. computer monitors, are only assigned if
# the primary load is present. Loads with operating cycles, i.e. wet loads,
# are given a unique operating cycle to introduce further diversity in the
# appliance set. The power and duration of each stage of the operating
# cycle is selected from a uniform distribution from the given input data.
    
    # Arguments:
#   time_res (int) [min]: Simulation time step;
#   n_occ (int) [-]: The number of occupants in the household;
#   tv_stuff (array) [-]: TV load specification;
#   settop_box (array) [-]: Set-top box load specification;
#   printer (array) [-]: Printer load specification;
#   music (array) [-]: Music player load specification;
#   router (array) [-]: Router load specification;
#   phone (array) [-]: Phone load specification;
#   cooking (array) [-]: Cooking loads specification;
#   iron (array) [-]: Iron load specification;
#   vacuum (array) [-]: Vacuum cleaner load specification;
#   shower (array) [-]: Shower load specification;
#   dishwasher (array) [-]: Dishwasher load specification;
#   washingmachine (array) [-]: Washing machine load specification;
#   clothesdrier (array) [-]: Clothes drier load specification;
#   gamesconsole (array) [-]: Games console loads specification;
#   computers (array) [-]: Computer loads specification;
#   monitors (array) [-]: Monitor loads specification;
#   heating (array) [-]: Heating loads specification;
#   cold_loads (array) [-]: Cold loads specification;
#   ev (array) [-]: EV load specification.
    
    # Returns:
#   distr (cell) []: DataStructure to hold the active power characteristics
#       of household appliances;
#   distr_q (cell) []: DataStructure to hold the reactive power
#       characteristics of household appliances;
#   p_zips (cell) []: DataStructure to hold the active power ZIP models for
#       household appliances
#   q_zips (cell) []: DataStructure to hold the reactive power ZIP models
#       for household appliances
    
    # Initiliase this var here
    distr = cell(1,35)
    distr[0] = np.zeros((n_occ,1))
    distr[2] = distr[0]
    distr_q = cell(1,35)
    distr_q[0] = np.zeros((n_occ,1))
    distr_q[2] = distr_q[0]
    p_zips = cell(1,35)
    q_zips = cell(1,35)
    ## Wet loads
# app 3 is washing machine p col 6
# app 4 is tumble drier p col 27
# app5 is dishwasher p col 4
    wet_cycles = cell(3,1)
    wet_cycles_q = cell(3,1)
    for app in np.array(['dishwasher','washingmachine','clothesdrier']).reshape(-1):
        wetload = app[0]
        if 'dishwasher' == wetload:
            cycle_stages_power_min = dishwasher(:,1)
            cycle_stages_power_max = dishwasher(:,2)
            cycle_stages_duration_min = dishwasher(:,3)
            cycle_stages_duration_max = dishwasher(:,4)
            wet_model = dishwasher(:,np.arange(6,11+1))
            cycle_stages_pfs = dishwasher(:,5)
            n_stages = cycle_stages_pfs.shape
            app_id = 5
            app_id2 = 4
        else:
            if 'washingmachine' == wetload:
                cycle_stages_power_min = washingmachine(:,1)
                cycle_stages_power_max = washingmachine(:,2)
                cycle_stages_duration_min = washingmachine(:,3)
                cycle_stages_duration_max = washingmachine(:,4)
                wet_model = washingmachine(:,np.arange(6,11+1))
                cycle_stages_pfs = washingmachine(:,5)
                n_stages = cycle_stages_pfs.shape
                app_id = 3
                app_id2 = 6
            else:
                if 'clothesdrier' == wetload:
                    cycle_stages_power_min = clothesdrier(:,1)
                    cycle_stages_power_max = clothesdrier(:,2)
                    cycle_stages_duration_min = clothesdrier(:,3)
                    cycle_stages_duration_max = clothesdrier(:,4)
                    wet_model = clothesdrier(:,np.arange(6,11+1))
                    cycle_stages_pfs = clothesdrier(:,5)
                    n_stages = cycle_stages_pfs.shape
                    app_id = 4
                    app_id2 = 27
        wet_load_p = []
        wet_load_q = []
        wet_load_models = []
        x = 0
        for i in np.arange(1,n_stages+1).reshape(-1):
            stage_duration = randi(np.array([cycle_stages_duration_min(i),cycle_stages_duration_max(i)]))
            stage_power = randi(np.array([cycle_stages_power_min(i),cycle_stages_power_max(i)]))
            stage_pf = cycle_stages_pfs(i)
            stage_models = wet_model(i,:)
            stage_q_power = stage_power * np.tan(np.arccos(stage_pf))
            wet_load_p[np.arange[x + 1,x + stage_duration+1]] = stage_power
            wet_load_q[np.arange[x + 1,x + stage_duration+1]] = stage_q_power
            for j in np.arange(x + 1,x + stage_duration+1).reshape(-1):
                wet_load_models[j,:] = stage_models
            x = x + stage_duration
        wet_cycles[app_id - 2,1][:,1] = wet_load_p
        wet_cycles_q[app_id - 2,1][:,1] = wet_load_q
        # assign model to correct idx
        p_zips[app_id2] = wet_load_models(:,np.arange(1,3+1))
        q_zips[app_id2] = wet_load_models(:,np.arange(4,6+1))
    
    distr[16][1,1] = wet_cycles
    distr_q[16] = wet_cycles_q
    ## TV
    tv_type1_probability = tv_stuff(1,2)
    
    tv_type2_probability = tv_stuff(2,2)
    tv_type3_probability = tv_stuff(3,2)
    tv_type4_probability = tv_stuff(4,2)
    tv_type1_mean = tv_stuff(1,3)
    tv_type1_sigma = tv_stuff(1,4)
    tv_type1_min = tv_stuff(1,5)
    tv_type1_max = tv_stuff(1,6)
    tv_type1_pf = tv_stuff(1,7)
    tv_type1_standby_min = tv_stuff(1,8)
    tv_type1_standby_max = tv_stuff(1,9)
    tv_type1_p_zip[1,1] = tv_stuff(1,10)
    tv_type1_p_zip[1,2] = tv_stuff(1,11)
    tv_type1_p_zip[1,3] = tv_stuff(1,12)
    tv_type1_q_zip[1,1] = tv_stuff(1,13)
    tv_type1_q_zip[1,2] = tv_stuff(1,14)
    tv_type1_q_zip[1,3] = tv_stuff(1,15)
    tv_type2_mean = tv_stuff(2,3)
    tv_type2_sigma = tv_stuff(2,4)
    tv_type2_min = tv_stuff(2,5)
    tv_type2_max = tv_stuff(2,6)
    tv_type2_pf = tv_stuff(2,7)
    tv_type2_standby_min = tv_stuff(2,8)
    tv_type2_standby_max = tv_stuff(2,9)
    tv_type2_p_zip[1,1] = tv_stuff(2,10)
    tv_type2_p_zip[1,2] = tv_stuff(2,11)
    tv_type2_p_zip[1,3] = tv_stuff(2,12)
    tv_type2_q_zip[1,1] = tv_stuff(2,13)
    tv_type2_q_zip[1,2] = tv_stuff(2,14)
    tv_type2_q_zip[1,3] = tv_stuff(2,15)
    tv_type3_mean = tv_stuff(3,3)
    tv_type3_sigma = tv_stuff(3,4)
    tv_type3_min = tv_stuff(3,5)
    tv_type3_max = tv_stuff(3,6)
    tv_type3_pf = tv_stuff(3,7)
    tv_type3_standby_min = tv_stuff(3,8)
    tv_type3_standby_max = tv_stuff(3,9)
    tv_type3_p_zip[1,1] = tv_stuff(3,10)
    tv_type3_p_zip[1,2] = tv_stuff(3,11)
    tv_type3_p_zip[1,3] = tv_stuff(3,12)
    tv_type3_q_zip[1,1] = tv_stuff(3,13)
    tv_type3_q_zip[1,2] = tv_stuff(3,14)
    tv_type3_q_zip[1,3] = tv_stuff(3,15)
    tv_type4_mean = tv_stuff(4,3)
    tv_type4_sigma = tv_stuff(4,4)
    tv_type4_min = tv_stuff(4,5)
    tv_type4_max = tv_stuff(4,6)
    tv_type4_pf = tv_stuff(4,7)
    tv_type4_standby_min = tv_stuff(4,8)
    tv_type4_standby_max = tv_stuff(4,9)
    tv_type4_p_zip[1,1] = tv_stuff(4,10)
    tv_type4_p_zip[1,2] = tv_stuff(4,11)
    tv_type4_p_zip[1,3] = tv_stuff(4,12)
    tv_type4_q_zip[1,1] = tv_stuff(4,13)
    tv_type4_q_zip[1,2] = tv_stuff(4,14)
    tv_type4_q_zip[1,3] = tv_stuff(4,15)
    for i in np.arange(1,n_occ+1).reshape(-1):
        tv = np.random.rand(1)
        if tv <= tv_type1_probability:
            tv1_power = np.random.randn(1) * tv_type1_sigma + tv_type1_mean
            tv1_power[tv1_power < tv_type1_min] = tv_type1_min
            tv1_power[tv1_power > tv_type1_max] = tv_type1_max
            tv1_power_standby = randi(np.array([tv_type1_standby_min,tv_type1_standby_max]))
            tv1_q_power = tv1_power * np.tan(np.arccos(tv_type1_pf))
            tv1_q_power_standby = tv1_power_standby * np.tan(np.arccos(tv_type1_pf))
            distr[0][i,1] = tv1_power
            distr[0][i,3] = tv_type1_pf
            distr[2][i] = tv1_power_standby
            distr_q[0][i,1] = tv1_q_power
            distr_q[0][i,1] = tv1_q_power_standby
            p_zips[18 + i][np.arange[1,3+1]] = tv_type1_p_zip
            q_zips[18 + i][np.arange[1,3+1]] = tv_type1_q_zip
        else:
            if tv <= tv_type2_probability:
                tv2_power = np.random.randn(1) * tv_type2_sigma + tv_type2_mean
                tv2_power[tv2_power < tv_type2_min] = tv_type2_min
                tv2_power[tv2_power > tv_type2_max] = tv_type2_max
                tv2_power_standby = randi(np.array([tv_type2_standby_min,tv_type2_standby_max]))
                distr[0][i,1] = tv2_power
                distr[2][i,1] = tv2_power_standby
                distr[0][i,3] = tv_type2_pf
                tv2_q_power = tv2_power * np.tan(np.arccos(tv_type2_pf))
                tv2_q_power_standby = tv2_power_standby * np.tan(np.arccos(tv_type2_pf))
                distr_q[0][i,1] = tv2_q_power
                distr_q[2][i,1] = tv2_q_power_standby
                p_zips[18 + i][np.arange[1,3+1]] = tv_type2_p_zip
                q_zips[18 + i][np.arange[1,3+1]] = tv_type2_q_zip
            else:
                if tv <= tv_type3_probability:
                    tv3_power = np.random.randn(1) * tv_type3_sigma + tv_type3_mean
                    tv3_power[tv3_power < tv_type3_min] = tv_type3_min
                    tv3_power[tv3_power > tv_type3_max] = tv_type3_max
                    tv3_power_standby = randi(np.array([tv_type3_standby_min,tv_type3_standby_max]))
                    distr[0][i,1] = tv3_power
                    distr[2][i,1] = tv3_power_standby
                    tv3_q_power = tv3_power * np.tan(np.arccos(tv_type3_pf))
                    tv3_q_power_standby = tv3_power_standby * np.tan(np.arccos(tv_type3_pf))
                    distr[0][i,3] = tv_type3_pf
                    distr_q[0][i,1] = tv3_q_power
                    distr_q[2][i,1] = tv3_q_power_standby
                    p_zips[18 + i][np.arange[1,3+1]] = tv_type3_p_zip
                    q_zips[18 + i][np.arange[1,3+1]] = tv_type3_q_zip
                else:
                    tv4_power = np.random.randn(1) * tv_type4_sigma + tv_type4_mean
                    tv4_power[tv4_power < tv_type4_min] = tv_type4_min
                    tv4_power[tv4_power > tv_type4_max] = tv_type4_max
                    tv4_power_standby = randi(np.array([tv_type4_standby_min,tv_type4_standby_max]))
                    tv4_q_power = tv4_power * np.tan(np.arccos(tv_type4_pf))
                    tv4_q_power_standby = tv4_power_standby * np.tan(np.arccos(tv_type4_pf))
                    distr[0][i,1] = tv4_power
                    distr[0][i,3] = tv_type4_pf
                    distr[2][i] = tv4_power_standby
                    distr_q[0][i,1] = tv4_q_power
                    distr_q[2][i,1] = tv4_q_power_standby
                    p_zips[18 + i][np.arange[1,3+1]] = tv_type4_p_zip
                    q_zips[18 + i][np.arange[1,3+1]] = tv_type4_q_zip
    
    ## Set-top box
    set_top_box_power_min = settop_box(1,5)
    set_top_box_power_max = settop_box(1,6)
    set_top_box_standby_power_min = settop_box(1,8)
    set_top_box_standby_power_max = settop_box(1,9)
    set_top_box_pf = settop_box(1,7)
    set_top_box_p_zip[1,1] = settop_box(1,10)
    set_top_box_p_zip[1,2] = settop_box(1,11)
    set_top_box_p_zip[1,3] = settop_box(1,12)
    set_top_box_q_zip[1,1] = settop_box(1,13)
    set_top_box_q_zip[1,2] = settop_box(1,14)
    set_top_box_q_zip[1,3] = settop_box(1,15)
    set_top_box_power = randi(np.array([set_top_box_power_min,set_top_box_power_max]))
    set_top_box_standby_power = randi(np.array([set_top_box_standby_power_min,set_top_box_standby_power_max]))
    set_top_box_q_power = set_top_box_power * np.tan(np.arccos(set_top_box_pf))
    set_top_box_standby_q_power = set_top_box_standby_power * np.tan(np.arccos(set_top_box_pf))
    distr[3][1] = set_top_box_power
    distr[4][1] = set_top_box_standby_power
    distr_q[3][1] = set_top_box_q_power
    distr_q[4][1] = set_top_box_standby_q_power
    p_zips[23][np.arange[1,3+1]] = set_top_box_p_zip
    q_zips[23][np.arange[1,3+1]] = set_top_box_q_zip
    ## PCs and monitors
    pc_val1 = computers(1,2)
    laptop_val1 = computers(2,2)
    laptop_val2 = computers(3,2)
    laptop_val3 = computers(4,2)
    pc_load_mean = computers(1,16)
    
    pc_load_sigma = computers(1,17)
    
    pc_load_min = computers(1,18)
    
    pc_load_max = computers(1,19)
    
    pc_rated_power = computers(1,3)
    pc_standby_power_min = computers(1,8)
    pc_standby_power_max = computers(1,9)
    pc_p_zip = computers(1,np.arange(10,12+1))
    pc_q_zip = computers(1,np.arange(13,15+1))
    pc_power_factor = computers(1,7)
    for i in np.arange(1,n_occ+1).reshape(-1):
        if np.random.rand(1) > pc_val1:
            monitor = 1
            pc_load = np.random.randn(1) * pc_load_sigma + pc_load_mean
            pc_load[pc_load < pc_load_min] = pc_load_min
            pc_load[pc_load > pc_load_max] = pc_load_max
            pc_power = pc_load * pc_rated_power / 100
            distr[5][i,1] = pc_power
            distr[5][i,3] = pc_power_factor
            pc_standby_power = randi(np.array([pc_standby_power_min,pc_standby_power_max]))
            distr[6][i,1] = pc_standby_power
            pc_q_power = pc_power * np.tan(np.arccos(pc_power_factor))
            pc_q_power_standby = pc_standby_power * np.tan(np.arccos(pc_power_factor))
            distr_q[5][i,1] = pc_q_power
            distr_q[6][i,1] = pc_q_power_standby
            p_zips[7 + i][np.arange[1,3+1]] = pc_p_zip
            q_zips[7 + i][np.arange[1,3+1]] = pc_q_zip
        else:
            monitor = 0
            lap = np.random.rand(1)
            laptop_power_mean = 58
            laptop_power_sigma = 20
            if lap < laptop_val1:
                Plow = computers(2,5)
                Phigh = computers(2,6)
                Plow_standby = computers(2,8)
                Phigh_standby = computers(2,9)
                pf = computers(2,7)
                pc_p_zip = computers(2,np.arange(10,12+1))
                pc_q_zip = computers(2,np.arange(13,15+1))
            else:
                if lap < laptop_val2:
                    Plow = computers(3,5)
                    Phigh = computers(3,6)
                    Plow_standby = computers(3,8)
                    Phigh_standby = computers(3,9)
                    pf = computers(3,7)
                    pc_p_zip = computers(3,np.arange(10,12+1))
                    pc_q_zip = computers(3,np.arange(13,15+1))
                else:
                    Plow = computers(4,5)
                    Phigh = computers(4,6)
                    Plow_standby = computers(4,8)
                    Phigh_standby = computers(4,9)
                    pf = computers(4,7)
                    pc_p_zip = computers(4,np.arange(10,12+1))
                    pc_q_zip = computers(4,np.arange(13,15+1))
            laptop_power = np.random.randn(1) * laptop_power_sigma + laptop_power_mean
            laptop_power[laptop_power < Plow] = Plow
            laptop_power[laptop_power > Phigh] = Phigh
            laptop_standby_power = randi(np.array([Plow_standby,Phigh_standby]))
            distr[5][i,1] = laptop_power
            distr[5][i,3] = pf
            distr[6][i,1] = laptop_standby_power
            laptop_q_power = laptop_power * np.tan(np.arccos(pf))
            laptop_q_standby_power = laptop_standby_power * np.tan(np.arccos(pf))
            distr_q[5][i,1] = laptop_q_power
            distr_q[6][i,1] = laptop_q_standby_power
            p_zips[7 + i][np.arange[1,3+1]] = pc_p_zip
            q_zips[7 + i][np.arange[1,3+1]] = pc_q_zip
        if monitor == 1:
            monitor_val1 = monitors(1,2)
            if (np.random.rand(1) < monitor_val1):
                monitor_power_mean = monitors(1,3)
                monitor_power_sigma = monitors(1,4)
                monitor_power_min = monitors(1,5)
                monitor_power_max = monitors(1,6)
                monitor_standby_min = monitors(1,8)
                monitor_standby_max = monitors(1,9)
                monitor_pf = monitors(1,7)
                monitor_p_zip = monitors(1,np.arange(10,12+1))
                monitor_q_zip = monitors(1,np.arange(13,15+1))
            else:
                monitor_power_mean = monitors(2,3)
                monitor_power_sigma = monitors(2,4)
                monitor_power_min = monitors(2,5)
                monitor_power_max = monitors(2,6)
                monitor_standby_min = monitors(2,8)
                monitor_standby_max = monitors(2,9)
                monitor_pf = monitors(2,7)
                monitor_p_zip = monitors(2,np.arange(10,12+1))
                monitor_q_zip = monitors(2,np.arange(13,15+1))
            monitor_power = np.random.randn(1) * monitor_power_sigma + monitor_power_mean
            monitor_power[monitor_power < monitor_power_min] = monitor_power_min
            monitor_power[monitor_power > monitor_power_max] = monitor_power_max
            monitor_standby_power = randi(np.array([monitor_standby_min,monitor_standby_max]))
            distr[7][i,1] = monitor_power
            distr[8][i,1] = monitor_standby_power
            p_zips[11 + i][np.arange[1,3+1]] = monitor_p_zip
            q_zips[11 + i][np.arange[1,3+1]] = monitor_q_zip
            monitor_q_power = monitor_power * np.tan(np.arccos(monitor_pf))
            monitor_q_power_standby = monitor_standby_power * np.tan(np.arccos(monitor_pf))
            distr_q[7][i,1] = monitor_q_power
            distr_q[8][i,1] = monitor_q_power_standby
        else:
            distr[7][i,1] = 0
            distr[7][i,2] = 0
            distr[8][i,1] = 0
            distr_q[7][i,1] = 0
            distr_q[8][i,1] = 0
    
    ## Printers
    printer_on_min = printer(1,5)
    printer_on_max = printer(1,6)
    printer_standby_min = printer(1,8)
    printer_standby_max = printer(1,9)
    printer_pf = printer(1,7)
    printer_p_zip[1,1] = printer(1,10)
    printer_p_zip[1,2] = printer(1,11)
    printer_p_zip[1,3] = printer(1,12)
    printer_q_zip[1,1] = printer(1,13)
    printer_q_zip[1,2] = printer(1,14)
    printer_q_zip[1,3] = printer(1,15)
    printer_on_power = randi(np.array([printer_on_min,printer_on_max]))
    printer_standby_power = randi(np.array([printer_standby_min,printer_standby_max]))
    printer_on_q_power = printer_on_power * np.tan(np.arccos(printer_pf))
    printer_standby_q_power = printer_standby_power * np.tan(np.arccos(printer_pf))
    distr[21][1,1] = printer_on_power
    distr[21][1,2] = printer_standby_power
    distr_q[21][1,1] = printer_on_q_power
    distr_q[21][1,2] = printer_standby_q_power
    p_zips[16][np.arange[1,3+1]] = printer_p_zip
    q_zips[16][np.arange[1,3+1]] = printer_q_zip
    ## Music
    music_power_mean = music(1,3)
    music_power_sigma = music(1,4)
    music_power_min = music(1,5)
    music_power_max = music(1,6)
    music_standby_power_min = music(1,8)
    music_standby_power_max = music(1,9)
    music_pf = music(1,7)
    music_p_zip[1,1] = music(1,10)
    music_p_zip[1,2] = music(1,11)
    music_p_zip[1,3] = music(1,12)
    music_q_zip[1,1] = music(1,13)
    music_q_zip[1,2] = music(1,14)
    music_q_zip[1,3] = music(1,15)
    music_power = np.random.randn(1) * music_power_sigma + music_power_mean
    
    music_power[music_power < music_power_min] = music_power_min
    
    music_power[music_power > music_power_max] = music_power_max
    
    music_standby_power = randi(np.array([music_standby_power_min,music_standby_power_max]))
    music_on_q_power = music_power * np.tan(np.arccos(music_pf))
    music_standby_q_power = music_standby_power * np.tan(np.arccos(music_pf))
    distr[9][1] = music_power
    distr[10][1] = music_standby_power
    distr_q[9][1] = music_on_q_power
    distr_q[10][1] = music_standby_q_power
    p_zips[24][np.arange[1,3+1]] = music_p_zip
    q_zips[24][np.arange[1,3+1]] = music_q_zip
    ## Iron
    iron_power_mean = iron(1,3)
    iron_power_sigma = iron(1,4)
    iron_power_min = iron(1,5)
    iron_power_max = iron(1,6)
    iron_pf = iron(1,7)
    iron_p_zip[1,1] = iron(1,10)
    iron_p_zip[1,2] = iron(1,11)
    iron_p_zip[1,3] = iron(1,12)
    iron_q_zip[1,1] = iron(1,13)
    iron_q_zip[1,2] = iron(1,14)
    iron_q_zip[1,3] = iron(1,15)
    iron_power = np.random.randn(1) * iron_power_sigma + iron_power_mean
    
    iron_power[iron_power < iron_power_min] = iron_power_min
    
    iron_power[iron_power > iron_power_max] = iron_power_max
    
    iron_q_power = iron_power * np.tan(np.arccos(iron_pf))
    distr[11][1] = iron_power * 10
    distr_q[11][1] = iron_q_power * 10
    p_zips[7][np.arange[1,3+1]] = iron_p_zip
    q_zips[7][np.arange[1,3+1]] = iron_q_zip
    ## Vacuum cleaner
    vacuum_cleaner_val1 = 0.063
    vacuum_cleaner_val2 = 0.85
    vacuum_cleaner_combined = vacuum_cleaner_val1 * vacuum_cleaner_val2
    vacuum_cleaner_prob = vacuum(1,2)
    if np.random.rand(1) >= vacuum_cleaner_prob:
        vacuum_cleaner_mean = vacuum(1,3)
        vacuum_cleaner_power_sigma = vacuum(1,4)
        vacuum_cleaner_power_min = vacuum(1,5)
        vacuum_cleaner_power_max = vacuum(1,6)
        vacuum_cleaner_pf = vacuum(1,7)
        vacuum_cleaner_p_zip[1,1] = vacuum(1,10)
        vacuum_cleaner_p_zip[1,2] = vacuum(1,11)
        vacuum_cleaner_p_zip[1,3] = vacuum(1,12)
        vacuum_cleaner_q_zip[1,1] = vacuum(1,13)
        vacuum_cleaner_q_zip[1,2] = vacuum(1,14)
        vacuum_cleaner_q_zip[1,3] = vacuum(1,15)
        vacuum_cleaner_power = np.random.randn(1) * vacuum_cleaner_power_sigma + vacuum_cleaner_mean
        vacuum_cleaner_power[vacuum_cleaner_power < vacuum_cleaner_power_min] = vacuum_cleaner_power_min
        vacuum_cleaner_power[vacuum_cleaner_power > vacuum_cleaner_power_max] = vacuum_cleaner_power_max
        vacuum_cleaner_q_power = vacuum_cleaner_power * np.tan(np.arccos(vacuum_cleaner_pf))
        distr[12][1] = vacuum_cleaner_power * 100
        distr_q[12][1] = vacuum_cleaner_q_power * 100
        p_zips[5][np.arange[1,3+1]] = vacuum_cleaner_p_zip
        q_zips[5][np.arange[1,3+1]] = vacuum_cleaner_q_zip
    else:
        distr[12][1] = 0
        distr_q[12][1] = 0
    
    ## Router
    router_val = router(1,2)
    if np.random.rand(1) >= router_val:
        router_power_mean = router(1,3)
        router_power_sigma = router(1,4)
        router_power_min = router(1,5)
        router_power_max = router(1,6)
        router_pf = router(1,7)
        router_p_zip[1,1] = router(1,10)
        router_p_zip[1,2] = router(1,11)
        router_p_zip[1,3] = router(1,12)
        router_q_zip[1,1] = router(1,13)
        router_q_zip[1,2] = router(1,14)
        router_q_zip[1,3] = router(1,15)
        router_power = np.random.randn(1) * router_power_sigma + router_power_mean
        router_power[router_power < router_power_min] = router_power_min
        router_power[router_power > router_power_max] = router_power_max
        router_q_power = router_power * np.tan(np.arccos(router_pf))
        distr[13][1] = router_power
        distr_q[13][1] = router_q_power
        p_zips[25][np.arange[1,3+1]] = router_p_zip
        q_zips[25][np.arange[1,3+1]] = router_q_zip
    else:
        distr[13][1] = 0
        distr_q[13][1] = 0
    
    ## Electric shower
    shower_power_mean = shower(1,3)
    shower_power_sigma = shower(1,4)
    shower_power_min = shower(1,5)
    shower_power_max = shower(1,6)
    shower_pf = shower(1,7)
    shower_p_zip[1,1] = shower(1,10)
    shower_p_zip[1,2] = shower(1,11)
    shower_p_zip[1,3] = shower(1,12)
    shower_q_zip[1,1] = shower(1,13)
    shower_q_zip[1,2] = shower(1,14)
    shower_q_zip[1,3] = shower(1,15)
    shower_power = np.random.randn(1) * shower_power_sigma + shower_power_mean
    
    shower_power[shower_power < shower_power_min] = shower_power_min
    
    shower_power[shower_power > shower_power_max] = shower_power_max
    
    shower_power = 4000 + shower_power * 500
    shower_q_power = shower_power * np.tan(np.arccos(shower_pf))
    distr[14][1] = shower_power
    distr_q[14][1] = shower_q_power
    p_zips[0][np.arange[1,3+1]] = shower_p_zip
    q_zips[0][np.arange[1,3+1]] = shower_q_zip
    ## Cold loads
    cold_p = np.zeros((time_res / 10,6))
    cold_q = np.zeros((time_res / 10,6))
    t144 = np.arange(1,144+1)
    cold_var1 = 0.207
    cold_var2 = 0.244
    cold_var3 = 0.8
    cold_var4 = 0.31
    cold_var5 = 0.15
    cold_base_power = 9
    cold1_power_fixed = 30.2
    cold1_power_mean = cold_loads(1,3)
    cold1_power_sigma = cold_loads(1,4)
    cold1_power_min = cold_loads(1,5)
    cold1_power_max = cold_loads(1,6)
    cold1_pf = cold_loads(1,7)
    # Upright freezer
    cold2_power_mean = cold_loads(2,3)
    cold2_power_sigma = cold_loads(2,4)
    cold2_power_min = cold_loads(2,5)
    cold2_power_max = cold_loads(2,6)
    cold2_pf = cold_loads(2,7)
    #Chest freezer
    cold5_power_mean = cold_loads(3,3)
    cold5_power_sigma = cold_loads(3,4)
    cold5_power_min = cold_loads(3,5)
    cold5_power_max = cold_loads(3,6)
    cold5_pf = cold_loads(3,7)
    cold_p_zip = cold_loads(1,np.arange(10,12+1))
    cold_q_zip = cold_loads(1,np.arange(13,15+1))
    square_wave = square(t144 * 2 * pi * 0.3333,33.333)
    cold_cycle = (1 + square_wave) / 2
    if np.random.rand(1) <= cold_var1:
        # Number ONE
        cold_p[:,1] = np.transpose((cold_base_power + cold1_power_fixed * cold_cycle))
        cold_q[:,1] = cold1_power_fixed * cold_cycle * np.tan(np.arccos(cold1_pf))
    else:
        # Number TWO
        cold1_power = np.random.randn(1) * cold1_power_sigma + cold1_power_mean
        cold1_power[cold1_power < cold1_power_min] = cold1_power_min
        cold1_power[cold1_power > cold1_power_max] = cold1_power_max
        cold1_power = cold1_power - cold_base_power
        cold_p[:,1] = np.transpose((cold_base_power + cold1_power * cold_cycle))
        cold_q[:,1] = cold1_power * cold_cycle * np.transpose(np.tan(np.arccos(cold1_pf)))
    
    if np.random.rand(1) <= cold_var2:
        if np.random.rand(1) <= cold_var3:
            # Number THREE
            cold_p[:,1] = cold_p(:,1) + np.transpose((cold_base_power + cold1_power_fixed * cold_cycle))
            cold_q[:,1] = cold_q(:,1) + np.transpose((cold1_power_fixed * cold_cycle * np.tan(np.arccos(cold1_pf))))
        else:
            # Number FOUR
            cold1_power = np.random.randn(1) * cold1_power_sigma + cold1_power_mean
            cold1_power[cold1_power < cold1_power_min] = cold1_power_min
            cold1_power[cold1_power > cold1_power_max] = cold1_power_max
            cold1_power = cold1_power - cold_base_power
            cold_p[:,1] = cold_p(:,1) + np.transpose((cold_base_power + cold1_power * cold_cycle))
            cold_q[:,1] = cold_q(:,1) + np.transpose((np.multiply(cold1_power_fixed * cold_cycle,np.tan(np.arccos(cold1_pf)))))
    
    # Upright freezer
    if np.random.rand(1) <= cold_var4:
        cold2_power = np.random.randn(1) * cold2_power_sigma + cold2_power_mean
        cold2_power[cold2_power < cold2_power_min] = cold2_power_min
        cold2_power[cold2_power > cold2_power_max] = cold2_power_max
        cold2_power = cold2_power - cold_base_power
        cold_p[:,2] = np.transpose((cold_base_power + cold2_power * cold_cycle))
        cold_q[:,2] = cold2_power * cold_cycle * np.transpose(np.tan(np.arccos(cold2_pf)))
    
    # Chest Freezer
    if np.random.rand(1) <= cold_var5:
        cold5_power = np.random.randn(1) * cold5_power_sigma + cold5_power_mean
        cold5_power[cold5_power < cold5_power_min] = cold5_power_min
        cold5_power[cold5_power > cold5_power_max] = cold5_power_max
        cold5_power = cold5_power - cold_base_power
        cold_p[:,5] = np.transpose((cold_base_power + cold5_power * cold_cycle))
        cold_q[:,5] = cold5_power * cold_cycle * np.transpose(np.tan(np.arccos(cold5_pf)))
    
    frcycle = randperm(4) - 1
    for i in np.arange(1,3+1).reshape(-1):
        cold_p[:,i] = circshift(cold_p(:,i),np.array([frcycle(i),0]))
        cold_q[:,i] = circshift(cold_q(:,i),np.array([frcycle(i),0]))
    
    coldfactor = 1.06
    cold_p[:,np.arange[1,5+1]] = cold_p(:,np.arange(1,5+1)) * coldfactor
    cold_p[:,6] = np.sum(cold_p(:,np.arange(1,5+1)), 2-1)
    cold_q[:,6] = np.sum(cold_q(:,np.arange(1,5+1)), 2-1)
    # 10-min -> 1-min and save
    temp_adam = kron(cold_p(:,6),np.ones((10,1)))
    tempq_adam = kron(cold_q(:,6),np.ones((10,1)))
    distr[15][1,1][:,1] = temp_adam
    distr[15][1,1][:,2] = tempq_adam
    distr[15][1,2] = cold_p(:,:)
    distr[15][1,3] = cold_q(:,:)
    p_zips[26][np.arange[1,3+1]] = cold_p_zip
    q_zips[26][np.arange[1,3+1]] = cold_q_zip
    ## Cooking appliances
    
    cooking_powers = np.zeros((7,1))
    cooking_q_powers = np.zeros((7,1))
    # Oven
    cooking1_prob = cooking(1,1)
    cooking1_mean = cooking(1,2)
    cooking1_sigma = cooking(1,3)
    cooking1_min = cooking(1,4)
    cooking1_max = cooking(1,5)
    cooking1_pf = cooking(1,6)
    cooking1_p_zip[1,1] = cooking(1,9)
    cooking1_p_zip[1,2] = cooking(1,10)
    cooking1_p_zip[1,3] = cooking(1,11)
    cooking1_q_zip[1,1] = cooking(1,12)
    cooking1_q_zip[1,2] = cooking(1,13)
    cooking1_q_zip[1,3] = cooking(1,14)
    # Hob
    cooking2_prob = cooking(2,1)
    cooking2_mean = cooking(2,2)
    cooking2_sigma = cooking(2,3)
    cooking2_min = cooking(2,4)
    cooking2_max = cooking(2,5)
    cooking2_pf = cooking(2,6)
    cooking2_p_zip[1,1] = cooking(2,9)
    cooking2_p_zip[1,2] = cooking(2,10)
    cooking2_p_zip[1,3] = cooking(2,11)
    cooking2_q_zip[1,1] = cooking(2,12)
    cooking2_q_zip[1,2] = cooking(2,13)
    cooking2_q_zip[1,3] = cooking(2,14)
    # Hood
    cooking3_prob = cooking(3,1)
    cooking3_min = cooking(3,4)
    cooking3_max = cooking(3,5)
    cooking3_pf = cooking(3,6)
    cooking3_p_zip[1,1] = cooking(3,9)
    cooking3_p_zip[1,2] = cooking(3,10)
    cooking3_p_zip[1,3] = cooking(3,11)
    cooking3_q_zip[1,1] = cooking(3,12)
    cooking3_q_zip[1,2] = cooking(3,13)
    cooking3_q_zip[1,3] = cooking(3,14)
    # Microwave
    cooking4_prob = cooking(4,1)
    cooking4_mean = cooking(4,2)
    cooking4_sigma = cooking(4,3)
    cooking4_min = cooking(4,4)
    cooking4_max = cooking(4,5)
    cooking4_pf = cooking(4,6)
    cooking4_p_zip[1,1] = cooking(4,9)
    cooking4_p_zip[1,2] = cooking(4,10)
    cooking4_p_zip[1,3] = cooking(4,11)
    cooking4_q_zip[1,1] = cooking(4,12)
    cooking4_q_zip[1,2] = cooking(4,13)
    cooking4_q_zip[1,3] = cooking(4,14)
    # Kettle
    cooking5_prob = cooking(5,1)
    cooking5_mean = cooking(5,2)
    cooking5_sigma = cooking(5,3)
    cooking5_min = cooking(5,4)
    cooking5_max = cooking(5,5)
    cooking5_pf = cooking(5,6)
    cooking5_p_zip[1,1] = cooking(5,9)
    cooking5_p_zip[1,2] = cooking(5,10)
    cooking5_p_zip[1,3] = cooking(5,11)
    cooking5_q_zip[1,1] = cooking(5,12)
    cooking5_q_zip[1,2] = cooking(5,13)
    cooking5_q_zip[1,3] = cooking(5,14)
    # Toaster
    cooking6_prob = cooking(6,1)
    cooking6_mean = cooking(6,2)
    cooking6_sigma = cooking(6,3)
    cooking6_min = cooking(6,4)
    cooking6_max = cooking(6,5)
    cooking6_pf = cooking(6,6)
    cooking6_p_zip[1,1] = cooking(6,9)
    cooking6_p_zip[1,2] = cooking(6,10)
    cooking6_p_zip[1,3] = cooking(6,11)
    cooking6_q_zip[1,1] = cooking(6,12)
    cooking6_q_zip[1,2] = cooking(6,13)
    cooking6_q_zip[1,3] = cooking(6,14)
    # Food processor
    cooking7_prob = cooking(7,1)
    cooking7_mean = cooking(7,2)
    cooking7_sigma = cooking(7,3)
    cooking7_min = cooking(7,4)
    cooking7_max = cooking(7,5)
    cooking7_pf = cooking(7,6)
    cooking7_p_zip[1,1] = cooking(7,9)
    cooking7_p_zip[1,2] = cooking(7,10)
    cooking7_p_zip[1,3] = cooking(7,11)
    cooking7_q_zip[1,1] = cooking(7,12)
    cooking7_q_zip[1,2] = cooking(7,13)
    cooking7_q_zip[1,3] = cooking(7,14)
    if np.random.rand(1) > cooking1_prob:
        cooking1_power = np.round(np.random.randn(1) * cooking1_sigma + cooking1_mean)
        cooking1_power[cooking1_power < cooking1_min] = cooking1_min
        cooking1_power[cooking1_power > cooking1_max] = cooking1_max
        cooking1_q_power = cooking1_power * np.tan(np.arccos(cooking1_pf))
        cooking_powers[1,1] = cooking1_power
        cooking_q_powers[1,1] = cooking1_q_power
        p_zips[28][np.arange[1,3+1]] = cooking1_p_zip
        q_zips[28][np.arange[1,3+1]] = cooking1_q_zip
    
    if np.random.rand(1) > cooking2_prob:
        cooking2_power = np.round(np.random.randn(1) * cooking2_sigma + cooking2_mean)
        cooking2_power[cooking2_power < cooking2_min] = cooking2_min
        cooking2_power[cooking2_power > cooking2_max] = cooking2_max
        cooking2_q_power = cooking2_power * np.tan(np.arccos(cooking2_pf))
        cooking_powers[2,1] = cooking2_power
        cooking_q_powers[2,1] = cooking2_q_power
        p_zips[29][np.arange[1,3+1]] = cooking2_p_zip
        q_zips[29][np.arange[1,3+1]] = cooking2_q_zip
    
    if np.random.rand(1) > cooking3_prob:
        cooking3_power = randi(np.array([cooking3_min,cooking3_max]))
        cooking3_q_power = cooking3_power * np.tan(np.arccos(cooking3_pf))
        cooking_powers[3,1] = cooking3_power
        cooking_q_powers[3,1] = cooking3_q_power
        p_zips[33][np.arange[1,3+1]] = cooking3_p_zip
        q_zips[33][np.arange[1,3+1]] = cooking3_q_zip
    
    if np.random.rand(1) > cooking4_prob:
        cooking4_power = np.round(np.random.randn(1) * cooking4_sigma + cooking4_mean)
        cooking4_power[cooking4_power < cooking4_min] = cooking4_min
        cooking4_power[cooking4_power > cooking4_max] = cooking4_max
        cooking4_q_power = cooking4_power * np.tan(np.arccos(cooking4_pf))
        cooking_powers[4,1] = cooking4_power
        cooking_q_powers[4,1] = cooking4_q_power
        p_zips[30][np.arange[1,3+1]] = cooking4_p_zip
        q_zips[30][np.arange[1,3+1]] = cooking4_q_zip
    
    if np.random.rand(1) > cooking5_prob:
        cooking5_power = np.round(np.random.randn(1) * cooking5_sigma + cooking5_mean)
        cooking5_power[cooking5_power < cooking5_min] = cooking5_min
        cooking5_power[cooking5_power > cooking5_max] = cooking5_max
        cooking5_q_power = cooking5_power * np.tan(np.arccos(cooking5_pf))
        cooking_powers[5,1] = cooking5_power
        cooking_q_powers[5,1] = cooking5_q_power
        p_zips[31][np.arange[1,3+1]] = cooking5_p_zip
        q_zips[31][np.arange[1,3+1]] = cooking5_q_zip
    
    if np.random.rand(1) > cooking6_prob:
        cooking6_power = np.round(np.random.randn(1) * cooking6_sigma + cooking6_mean)
        cooking6_power[cooking6_power < cooking6_min] = cooking6_min
        cooking6_power[cooking6_power > cooking6_max] = cooking6_max
        cooking6_q_power = cooking6_power * np.tan(np.arccos(cooking6_pf))
        cooking_powers[6,1] = cooking6_power
        cooking_q_powers[6,1] = cooking6_q_power
        p_zips[32][np.arange[1,3+1]] = cooking6_p_zip
        q_zips[32][np.arange[1,3+1]] = cooking6_q_zip
    
    if np.random.rand(1) > cooking7_prob:
        cooking7_power = np.round(np.random.randn(1) * cooking7_sigma + cooking7_mean)
        cooking7_power[cooking7_power < cooking7_min] = cooking7_min
        cooking7_power[cooking7_power > cooking7_max] = cooking7_max
        cooking7_q_power = cooking7_power * np.tan(np.arccos(cooking7_pf))
        cooking_powers[7,1] = cooking7_power
        cooking_q_powers[7,1] = cooking7_q_power
    
    distr[17] = cooking_powers
    distr_q[17] = cooking_q_powers
    ## Phone
    phone_var = phone(1,2)
    phone_power_min = phone(1,5)
    phone_power_max = phone(1,6)
    phone_pf = phone(1,7)
    phone_p_zip[1,1] = phone(1,10)
    phone_p_zip[1,2] = phone(1,11)
    phone_p_zip[1,3] = phone(1,12)
    phone_q_zip[1,1] = phone(1,13)
    phone_q_zip[1,2] = phone(1,14)
    phone_q_zip[1,3] = phone(1,15)
    if np.random.rand(1) >= phone_var:
        phone_power = randi(np.array([phone_power_min,phone_power_max]))
        phone_q_power = phone_power * np.tan(np.cos(phone_pf))
        distr[22] = phone_power
        distr_q[22] = phone_q_power
    else:
        distr[22] = 0
        distr_q[22] = 0
    
    p_zips[17][np.arange[1,3+1]] = phone_p_zip
    q_zips[17][np.arange[1,3+1]] = phone_q_zip
    ## Games
    
    gamesconsole_var1 = gamesconsole(1,2)
    gamesconsole_var2 = gamesconsole_var1 + gamesconsole(2,2)
    gamesconsole_var3 = gamesconsole_var2 + gamesconsole(3,2)
    gamesconsole1_power = gamesconsole(1,3)
    gamesconsole1_pf = gamesconsole(1,7)
    gamesconsole1_p_zip = gamesconsole(1,np.arange(10,12+1))
    gamesconsole1_q_zip = gamesconsole(1,np.arange(13,15+1))
    gamesconsole2_power = gamesconsole(2,3)
    gamesconsole2_pf = gamesconsole(2,7)
    gamesconsole2_p_zip = gamesconsole(2,np.arange(10,12+1))
    gamesconsole2_q_zip = gamesconsole(2,np.arange(13,15+1))
    gamesconsole3_power = gamesconsole(3,3)
    gamesconsole3_pf = gamesconsole(3,7)
    gamesconsole3_p_zip = gamesconsole(3,np.arange(10,12+1))
    gamesconsole3_q_zip = gamesconsole(3,np.arange(13,15+1))
    gamecons = np.random.rand(1)
    if gamecons <= gamesconsole_var1:
        gamesconsole_power = gamesconsole1_power
        gamesconsole_pf = gamesconsole1_pf
        gamesconsole_q_power = gamesconsole_power * np.tan(np.arccos(gamesconsole_pf))
        gamesconsole_p_zip = gamesconsole1_p_zip
        gamesconsole_q_zip = gamesconsole1_q_zip
    else:
        if gamecons <= gamesconsole_var2:
            gamesconsole_power = gamesconsole2_power
            gamesconsole_pf = gamesconsole2_pf
            gamesconsole_q_power = gamesconsole_power * np.tan(np.arccos(gamesconsole_pf))
            gamesconsole_p_zip = gamesconsole2_p_zip
            gamesconsole_q_zip = gamesconsole2_q_zip
        else:
            gamesconsole_power = gamesconsole3_power
            gamesconsole_pf = gamesconsole3_pf
            gamesconsole_q_power = gamesconsole_power * np.tan(np.arccos(gamesconsole_pf))
            gamesconsole_p_zip = gamesconsole3_p_zip
            gamesconsole_q_zip = gamesconsole3_q_zip
    
    distr[23] = gamesconsole_power
    distr_q[23] = gamesconsole_q_power
    p_zips[18][np.arange[1,3+1]] = gamesconsole_p_zip
    q_zips[18][np.arange[1,3+1]] = gamesconsole_q_zip
    ## heating
    
    heating_ = np.zeros((3,1))
    storage_heating_ownership = heating(1,2)
    instant_heating_ownership = heating(2,2)
    tfeh = np.random.rand(1)
    if tfeh < storage_heating_ownership:
        heating_type = 2
        heating_mean = heating(2,3)
        heating_sigma = heating(2,4)
        heating_min = heating(2,5)
        heating_max = heating(2,6)
        heating_pf = heating(2,7)
        heating_p_zip = heating(2,np.arange(10,12+1))
        heating_q_zip = heating(2,np.arange(13,15+1))
    else:
        if tfeh < instant_heating_ownership + storage_heating_ownership:
            heating_type = 1
            heating_mean = heating(2,3)
            heating_sigma = heating(2,4)
            heating_min = heating(2,5)
            heating_max = heating(2,6)
            heating_pf = heating(2,7)
            heating_p_zip = heating(2,np.arange(10,12+1))
            heating_q_zip = heating(2,np.arange(13,15+1))
        else:
            heating_type = 0
            heating_mean = 0
            heating_min = 0
            heating_max = 0
            heating_sigma = 0
            heating_pf = 0
            heating_p_zip = np.array([0,0,0])
            heating_q_zip = np.array([0,0,0])
    
    heating_power = np.round(np.random.randn(1) * heating_sigma + heating_mean)
    
    heating_power[heating_power < heating_min] = heating_min
    
    heating_power[heating_power > heating_max] = heating_max
    
    heating_q_power = heating_power * np.tan(np.arccos(heating_pf))
    heating_[1,1] = heating_type
    heating_[2,1] = heating_power
    heating_[3,1] = heating_(2,1) * 4
    distr[35] = heating_
    distr_q[35] = heating_q_power
    p_zips[35][np.arange[1,3+1]] = heating_p_zip
    q_zips[35][np.arange[1,3+1]] = heating_q_zip
    ## Electric vehicle stuff
    ev_ownership = ev(1,2)
    
    if np.random.rand(1) < ev_ownership:
        ev_power_min = ev(1,5)
        ev_power_max = ev(1,6)
        ev_pf = ev(1,7)
        ev_charger_eff_min = ev(1,16)
        ev_charger_eff_max = ev(1,17)
        ev_p_zip[1,1] = ev(1,10)
        ev_p_zip[2,1] = ev(1,11)
        ev_p_zip[3,1] = ev(1,12)
        ev_q_zip[1,1] = ev(1,13)
        ev_q_zip[2,1] = ev(1,14)
        ev_q_zip[3,1] = ev(1,15)
        ev_battery_capacity_min = ev(1,20)
        ev_battery_capacity_max = ev(1,21)
        ev_battery_soc_mean = ev(1,18)
        ev_battery_soc_sigma = ev(1,19)
        ev_p_power = ev_power_min + (ev_power_max - ev_power_min) * np.random.rand(1)
        ev_battery_capacity = randi(np.array([ev_battery_capacity_min,ev_battery_capacity_max]))
        ev_q_power = ev_p_power * np.tan(np.arccos(ev_pf))
        ev_battery_soc = np.random.randn(1) * ev_battery_soc_sigma + ev_battery_soc_mean
        ev_charger_efficiency = ev_charger_eff_min + (ev_charger_eff_max - ev_charger_eff_min) * np.random.rand(1)
    else:
        ev_p_power = 0
        ev_battery_capacity = 0
        ev_q_power = 0
        ev_charger_efficiency = 0
        ev_battery_soc = 0
        ev_p_zip[np.arange[1,3+1]] = 0
        ev_q_zip[np.arange[1,3+1]] = 0
    
    distr[34][1,1] = ev_p_power
    distr[34][2,1] = ev_battery_capacity
    distr[34][3,1] = ev_battery_soc
    distr[34][4,1] = ev_charger_efficiency
    distr_q[34][1,1] = ev_q_power
    p_zips[34][np.arange[1,3+1]] = ev_p_zip
    q_zips[34][np.arange[1,3+1]] = ev_q_zip
    return distr,distr_q,p_zips,q_zips
    