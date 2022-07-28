# Top level code for bringing all functions together
import numpy as np
import matplotlib.pyplot as plt
clear
# Define directory locations here. EXAMPLE:
# base_dir = 'C:\Users\user\Documents\MATLAB\DESIMAX\code\';
base_dir = 'C:\\Users\\user\\Documents\\MATLAB\\DESIMAX\\code\\'

data_dir = fullfile(base_dir,'..\\\\data\\\\')
save_dir = fullfile(base_dir,'..\\\\output\\\\')
# User defined load
user_load_name = 'new_load_one.xlsx'
# Heavy lifting here
scipy.io.loadmat(fullfile(data_dir,'irradiancedata.mat'))
scipy.io.loadmat(fullfile(data_dir,'TM.mat'))
scipy.io.loadmat(fullfile(data_dir,'IC.mat'))
scipy.io.loadmat(fullfile(data_dir,'Sharing.mat'))
scipy.io.loadmat(fullfile(data_dir,'DesTemp.mat'))
tv_data = xlsread(strjoin(np.array([data_dir,'ce_ict.xlsx']),''),'tv','A4..O7')
settop_box_data = xlsread(strjoin(np.array([data_dir,'ce_ict.xlsx']),''),'box','A4..O4')
router_data = xlsread(strjoin(np.array([data_dir,'ce_ict.xlsx']),''),'router','A4..O4')
phone_data = xlsread(strjoin(np.array([data_dir,'ce_ict.xlsx']),''),'phone','A4..O4')
gamesconsole_data = xlsread(strjoin(np.array([data_dir,'ce_ict.xlsx']),''),'gamesconsole','A4..O6')
computer_data = xlsread(strjoin(np.array([data_dir,'ce_ict.xlsx']),''),'computer','A4..S7')
monitor_data = xlsread(strjoin(np.array([data_dir,'ce_ict.xlsx']),''),'monitor','A4..O5')
printer_data = xlsread(strjoin(np.array([data_dir,'ce_ict.xlsx']),''),'printer','A4..O4')
music_data = xlsread(strjoin(np.array([data_dir,'ce_ict.xlsx']),''),'music','A4..O4')
cooking_data = xlsread(strjoin(np.array([data_dir,'cooking_loads.xlsx']),''),'cooking','A4..O10')
iron_data = xlsread(strjoin(np.array([data_dir,'misc_loads.xlsx']),''),'iron','A4..O4')
vacuum_data = xlsread(strjoin(np.array([data_dir,'misc_loads.xlsx']),''),'vacuum','A4..O4')
shower_data = xlsread(strjoin(np.array([data_dir,'misc_loads.xlsx']),''),'shower','A4..O4')
dishwasher_data = xlsread(strjoin(np.array([data_dir,'wet_loads.xlsx']),''),'dishwasher','B3..L18')
washingmachine_data = xlsread(strjoin(np.array([data_dir,'wet_loads.xlsx']),''),'washingmachine','B3..L27')
clothesdrier_data = xlsread(strjoin(np.array([data_dir,'wet_loads.xlsx']),''),'clothesdrier','B3..L31')
heating_data = xlsread(strjoin(np.array([data_dir,'heating_loads.xlsx']),''),'heating','A4..O5')
cold_load_data = xlsread(strjoin(np.array([data_dir,'cold_loads.xlsx']),''),'cold','A4..O6')
ev_load_data = xlsread(strjoin(np.array([data_dir,'ev_loads.xlsx']),''),'ev','A4..U4')
lighting_load_data = xlsread(strjoin(np.array([data_dir,'lighting_loads.xlsx']),''),'lighting','A4..O10')
general_configuration = xlsread(strjoin(np.array([data_dir,'general.xlsx']),''),'general','B2..B4')
composition = xlsread(strjoin(np.array([data_dir,'general.xlsx']),''),'composition','B3..G7')
user_behaviour = xlsread(strjoin(np.array([data_dir,'general.xlsx']),''),'user_behaviour','B2..B4')
# Define configurable variables here

Day = general_configuration(1)
Month = general_configuration(2)
N_hh = general_configuration(3)
# load a new load profile
new_load_data = xlsread(strjoin(np.array([data_dir,user_load_name]),''),'statistics','A3..F3')
new_load_locs,new_loads = user_defined_load(N_hh,data_dir,new_load_data,user_load_name)
# The user types are randomly allocated within the aggregate
User_type_percent[1,1] = user_behaviour(1)
User_type_percent[1,2] = user_behaviour(2)
User_type_percent[1,3] = user_behaviour(3)
hh_type = hh_user_type(User_type_percent,N_hh)
## Convert the hh composition into absolute values
# This code is required to round up/down to ensure that the rounded result
# of the percentage composition multiplied by the aggregate size returns a
# value which is equal to the defined aggregate size

N_hh_composition_percent = composition
N_hh_composition_step1 = np.multiply(N_hh_composition_percent,N_hh)
N_hh_composition_step2 = np.round(N_hh_composition_step1)
N_hh_composition_step3 = sum(sum(N_hh_composition_step2))
if N_hh_composition_step3 > N_hh:
    error = N_hh_composition_step3 - N_hh
    N_hh_final = round_hh_composition(N_hh_composition_step1,error,1)
else:
    if N_hh_composition_step3 < N_hh:
        error = N_hh - N_hh_composition_step3
        N_hh_final = round_hh_composition(N_hh_composition_step1,error,2)
    else:
        N_hh_final = N_hh_composition_step2

# Get irradiance
irr = irradiance(:,Month)
## Run the code

time_res = 1440
active_power = np.zeros((time_res,N_hh))
reactive_power = np.zeros((time_res,N_hh))
p_zip_models = cell(N_hh,1)
q_zip_models = cell(N_hh,1)
c = 1
for HHsize in np.arange(1,4+1).reshape(-1):
    for Working in np.arange(0,HHsize+1).reshape(-1):
        N = N_hh_final(HHsize,Working + 1)
        if N > 0:
            profiles,hh_occ = activity_profile_generation(HHsize,Working,Day,N,TM,IC,Sharing)
            for b in np.arange(1,N+1).reshape(-1):
                distr,distr_q,pzips,qzips = appliance_population(time_res,HHsize,tv_data,settop_box_data,printer_data,music_data,router_data,phone_data,cooking_data,iron_data,vacuum_data,shower_data,dishwasher_data,washingmachine_data,clothesdrier_data,gamesconsole_data,computer_data,monitor_data,heating_data,cold_load_data,ev_load_data)
                APower,RePower,LightPower,LightZIPS,LightQZIPS,individual_light_q,wet_starts,wet_ends = activity_to_power(time_res,profiles[b],Month,Day,hh_type(b,1),lighting_load_data,DesTemp,irr,hh_occ(:,b),distr,distr_q,HHsize)
                # check for new load definitions
                if ismember(c,new_load_locs):
                    new_load_idx = find(new_load_locs == c)
                    pzips[36] = new_loads[new_load_idx](:,np.arange(3,5+1))
                    qzips[36] = new_loads[new_load_idx](:,np.arange(6,8+1))
                    APower[1,HHsize + 4] = new_loads[new_load_idx](:,1)
                    RePower[1,HHsize + 4] = new_loads[new_load_idx](:,2)
                else:
                    APower[1,HHsize + 4] = np.zeros((1440,1))
                    RePower[1,HHsize + 4] = np.zeros((1440,1))
                    pzips[36] = np.zeros((1,3))
                    qzips[36] = np.zeros((1,3))
                # Sum all household appliances
                P_HH = np.zeros((1440,1))
                Q_HH = np.zeros((1440,1))
                for j in np.arange(1,HHsize + 4+1).reshape(-1):
                    P_HH = P_HH + np.sum(APower[1,j], 2-1)
                    Q_HH = Q_HH + np.sum(RePower[1,j], 2-1)
                # get zip model of the household
                p_zip = zip_aggregation(P_HH,APower,pzips,HHsize,LightZIPS,LightPower[1,18][1,1],wet_starts,wet_ends)
                q_zip = zip_aggregation(P_HH,RePower,qzips,HHsize,LightQZIPS,np.array([individual_light_q]),wet_starts,wet_ends)
                # sort data into global vars
                active_power[:,c] = P_HH
                reactive_power[:,c] = Q_HH
                p_zip_models[c,1] = p_zip
                q_zip_models[c,1] = q_zip
                c = c + 1

P_aggr = np.sum(active_power, 2-1)
Q_aggr = np.sum(reactive_power, 2-1)
t = np.transpose(np.array([np.arange(0,24 - 24 / time_res+24 / time_res,24 / time_res)]))
plt.plot(t,P_aggr)
hold('on')
plt.plot(t,Q_aggr,'red')
save(fullfile(save_dir,'active_power_profiles.mat'),'active_power','P_aggr')
save(fullfile(save_dir,'reactive_power_profiles.mat'),'reactive_power','Q_aggr')
save(fullfile(save_dir,'active_power_load_models.mat'),'p_zip_models')
save(fullfile(save_dir,'reactive_power_load_models.mat'),'q_zip_models')