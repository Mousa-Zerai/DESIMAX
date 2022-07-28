import numpy as np
    
def RoundDown(N_hh_composition_step1 = None,error = None): 
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