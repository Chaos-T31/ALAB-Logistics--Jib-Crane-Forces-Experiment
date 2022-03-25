# **************************************************************************************************************************************************************************************************** #
# *********************************************************************** 4.	To find the forces in the members of Jib Crane. ********************************************************************** #
# **************************************************************************************************************************************************************************************************** #
# -@ AmiLab


'''
Note-
    - **DATA VALIDATION EXCLUDED FOR BEING CHECKED AT THE TIME OF DATA INPUT**
    - All Testings have been logged into the terminal for future debuggings.
    - The Length of Jib, Tie and Post is/are considered to be in the same unit system.
'''


# ********************************************************************** Argument / Variable Declaration (for Testing purposes) ********************************************************************** #


n = 3                                                                                           # The Total Number of Observations been performed
init_reading = {'Jib': [1, 2, 3], 'Tie': [4, 5, 6]}                                             # The Initial Readings (without Weights)
final_reading = {'Jib': [10, 20, 30], 'Tie': [10, 20, 30]}                                      # The Final Readings (with Weights)
len_JC_membs = {'Jib': [5, 10, 15], 'Tie': [4, 8, 12], 'Post': [3, 6, 9]}                       # The Corresponding Lengths in the 3 Members 'Jib', 'Tie' & 'Post' of the Jib Crane
W = 1                                                                                           # The Weight Hung on the Jib Crane while performing the Readings


# **************************************************************************************** Section ends here **************************************************************************************** #


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #



# ******************************************************************* Calculations for the Forces in the Members of the Jib Crane ******************************************************************* #


from math import pi, acos, sin


def slNo(n):                                                 # For generating the Serial Numbers of the Observations
    return list(range(1, n + 1))

# Testing-
slno = slNo(n)
print(slno)


def observedForce(init_reading, final_reading, n):           # For calculating the Observed Force as: Observed Force = Final_Reading(F) - Initial_Reading(I)
    init_arms, final_arms = list(init_reading.keys()), list(final_reading.keys())
    return {'Jib': [final_reading[final_arms[0]][i] - init_reading[init_arms[0]][i] for i in range(n)], 'Tie':  [final_reading[final_arms[1]][i] - init_reading[init_arms[1]][i] for i in range(n)]}

# Testing-
print(observedForce(init_reading, final_reading, n))


def setScalingRatio(l1, l2):                                # For generating the 'Scaling Ratio' for the Members of the Jib Crane
    return f'{l1}:{l2}'

# Testing-
len_JC_membs = setScalingRatio(10, 2)
print(len_JC_membs)


def quantumScalar(len_JC_membs, scaling_ratio, n):          # For applying the 'Scaling Factor' obtained above for scaling the Members of the Jib Crane
    ante_quent = scaling_ratio.split(':')
    jib, tie, post = len_JC_membs.values()
    if scaling_ratio[-1] == 1:
        scaling_fact = float(ante_quent[0])
        return {'Jib': list(map(lambda j: int(j * scaling_fact) if int(j * scaling_fact) == j * scaling_fact else j * scaling_fact, jib)), 'Tie': list(map(lambda t: int(t * scaling_fact) if int(t * scaling_fact) == t * scaling_fact else t * scaling_fact, tie)), 'Post': list(map(lambda p: int(p * scaling_fact) if int(p * scaling_fact) == p * scaling_fact else p * scaling_fact, post))}
    else:
        scaling_fact = float(ante_quent[0]) / float(ante_quent[1])
        return {'Jib': list(map(lambda j: int(j * scaling_fact) if int(j * scaling_fact) == j * scaling_fact else j * scaling_fact, jib)), 'Tie': list(map(lambda t: int(t * scaling_fact) if int(t * scaling_fact) == t * scaling_fact else t * scaling_fact, tie)), 'Post': list(map(lambda p: int(p * scaling_fact) if int(p * scaling_fact) == p * scaling_fact else p * scaling_fact, post))}

# Testing-
scaled_forces = quantumScalar(len_JC_membs, '10:2', 3)
print(scaled_forces)


def forceAngles(scaled_forces, n):                          # For Calculating the Angles between Pair of 2 Forces
    return {'Jib': [pi / 2 for i in range(n)], 'Tie': [acos(scaled_forces['Post'][i] / scaled_forces['Jib'][i]) for i in range(n)], 'Post': [acos(scaled_forces['Tie'][i] / scaled_forces['Jib'][i]) for i in range(n)]}

# Testing-
angs = forceAngles({'Jib': [25.0, 50.0, 75.0], 'Tie': [20.0, 40.0, 60.0], 'Post': [15.0, 30.0, 45.0]}, 3)
print(angs)


def cal_Jib_N_Tie_Forces_PR(angs, wt_on_post_W, n):         # For Calculating the Forces P & R in the Members 'Jib' and 'Tie' of the Jib Crane
    return {'Jib': [(wt_on_post_W * sin(angs['Jib'][i])) / sin(angs['Post'][i]) for i in range(n)], 'Tie': [(wt_on_post_W * sin(angs['Tie'][i])) / sin(angs['Post'][i]) for i in range(n)]}

# Testing-
PR_Forces = cal_Jib_N_Tie_Forces_PR(angs, W, 3)
print(PR_Forces)


def calAvg(PR_Forces, n):                                   # For Calculating the Average of all the Readings for the Forces P & R in the Members 'Jib' and 'Tie' of the Jib Crane obtained above
    return {'Jib': sum(PR_Forces['Jib']) / n, 'Tie': sum(PR_Forces['Tie']) / n}

# Testing-
avg_PR_Forces = calAvg(PR_Forces, n)
print(avg_PR_Forces)


# ********************************************************************************* Section ends here *********************************************************************************************** #


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #




