import numpy as np
    
def round_hh_composition(N_hh_composition_step1 = None,error = None,type_ = None): 
    # Round the household composition numbers to equal
# the total population size.
    
    # Arguments:
#   N_hh_composition_step1 (array) [-]: Unrounded values;
#   error (num) [-]: Size of the difference between the unrounded values
#       and the defined aggregate size;
#   type (int) [-]: Identify if the unrounded values are over or under the
#       defined aggregate size.
    
    # Returns:
#   N_hh_final (array) [-]: Corrected values.
    
    dim = N_hh_composition_step1.shape
    j = 1
    for i in np.arange(1,dim(1)+1).reshape(-1):
        A_temp[np.arange[j,j + dim[2] - 1+1]] = N_hh_composition_step1(i,:)
        j = j + dim(2)
    
    integ = np.zeros((1,dim(1) * dim(2)))
    A = np.zeros((1,dim(1) * dim(2)))
    for x in np.arange(1,(dim(1) * dim(2))+1).reshape(-1):
        integ[1,x] = int(np.floor(A_temp(1,x)))
        A[1,x] = A_temp(1,x) - integ(1,x)
    
    A[2,:] = np.arange(1,(dim(1) * dim(2))+1)
    if type_ == 1:
        __,I = __builtint__.sorted(A(1,:))
        B = A(:,I)
        n = 0
        for m in np.arange(1,(dim(1) * dim(2))+1).reshape(-1):
            if n < error:
                if B(1,m) >= 0.5:
                    B[1,m] = 0
                    n = n + 1
            else:
                break
    else:
        if type_ == 2:
            __,I = __builtint__.sorted(A(1,:),'descend')
            B = A(:,I)
            n = 0
            for m in np.arange(1,(dim(1) * dim(2))+1).reshape(-1):
                if n < error:
                    if B(1,m) <= 0.5:
                        if B(2,m) != np.array([3,4,5,9,10,15]):
                            B[1,m] = 1
                            n = n + 1
                else:
                    break
        else:
            print('errore')
    
    for z in np.arange(1,(dim(1) * dim(2))+1).reshape(-1):
        if 1 == B(2,z):
            N_hh_final[1,1] = B(1,z)
        else:
            if 2 == B(2,z):
                N_hh_final[1,2] = B(1,z)
            else:
                if 3 == B(2,z):
                    N_hh_final[1,3] = B(1,z)
                else:
                    if 4 == B(2,z):
                        N_hh_final[1,4] = B(1,z)
                    else:
                        if 5 == B(2,z):
                            N_hh_final[1,5] = B(1,z)
                        else:
                            if 6 == B(2,z):
                                N_hh_final[2,1] = B(1,z)
                            else:
                                if 7 == B(2,z):
                                    N_hh_final[2,2] = B(1,z)
                                else:
                                    if 8 == B(2,z):
                                        N_hh_final[2,3] = B(1,z)
                                    else:
                                        if 9 == B(2,z):
                                            N_hh_final[2,4] = B(1,z)
                                        else:
                                            if 10 == B(2,z):
                                                N_hh_final[2,5] = B(1,z)
                                            else:
                                                if 11 == B(2,z):
                                                    N_hh_final[3,1] = B(1,z)
                                                else:
                                                    if 12 == B(2,z):
                                                        N_hh_final[3,2] = B(1,z)
                                                    else:
                                                        if 13 == B(2,z):
                                                            N_hh_final[3,3] = B(1,z)
                                                        else:
                                                            if 14 == B(2,z):
                                                                N_hh_final[3,4] = B(1,z)
                                                            else:
                                                                if 15 == B(2,z):
                                                                    N_hh_final[3,5] = B(1,z)
                                                                else:
                                                                    if 16 == B(2,z):
                                                                        N_hh_final[4,1] = B(1,z)
                                                                    else:
                                                                        if 17 == B(2,z):
                                                                            N_hh_final[4,2] = B(1,z)
                                                                        else:
                                                                            if 18 == B(2,z):
                                                                                N_hh_final[4,3] = B(1,z)
                                                                            else:
                                                                                if 19 == B(2,z):
                                                                                    N_hh_final[4,4] = B(1,z)
                                                                                else:
                                                                                    if 20 == B(2,z):
                                                                                        N_hh_final[4,5] = B(1,z)
    
    z = 1
    for a in np.arange(1,dim(1)+1).reshape(-1):
        for b in np.arange(1,dim(2)+1).reshape(-1):
            N_hh_final[a,b] = N_hh_final(a,b) + integ(1,z)
            z = z + 1
    
    N_hh_final = np.round(N_hh_final)
    return N_hh_final