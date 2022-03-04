import numpy as np 
import pickle 

# The goal angle
goal_deg = 48

# Degrees list
degrees = []
for i in range(1,90):
    degrees.append(i)

# Probabilities for each angle in "Degrees List"
equal = 1/89
prob = []
for i in range(1,90):
    prob.append(equal)
    
prob = np.array(prob)
degrees = np.array(degrees)

print(prob.sum())

def get_loc(array,value):
      a = np.where(array == value)
      return a[0]

vals = []
vals.append(14)
vals.append(18)
prev = 0 

# Probability change amount after each selection.
chn_mik = 0.0055555



def chn_prob(curr,prev):
    delta_n = abs((goal_deg+1) - curr)
    delta_prev = abs((goal_deg+1) - prev)
    index_cur = get_loc(degrees,curr)
    index_prev = get_loc(degrees,prev)
    print(index_cur)
    print(index_prev)
    if delta_n > delta_prev:
        if (prob[index_cur] - chn_mik)> 0 and (prob[index_prev] - chn_mik)> 0:
            prob[index_cur] -= chn_mik
            prob[index_prev] += chn_mik
    if delta_n < delta_prev:
        if (prob[index_cur] - chn_mik)> 0 and (prob[index_prev] - chn_mik)> 0:
            prob[index_cur] += chn_mik
            prob[index_prev] -= chn_mik
    if delta_n == 0:
        if (prob[index_cur] - chn_mik)> 0 and (prob[index_prev] - chn_mik)> 0:
            prob[index_cur] += chn_mik
            prob[index_prev] -= chn_mik
    if delta_prev == 0:
        if (prob[index_cur] - chn_mik)> 0 and (prob[index_prev] - chn_mik)> 0:
            prob[index_cur] -= chn_mik
            prob[index_prev] += chn_mik
        
do = 0
i = 0

val = np.amax(prob)
goal_probability = 0.985 # The goal probability value which the machine learning process terminate. 

# Training
while val < goal_probability:
    val = np.amax(prob)
    print("Try Number: "+str(i))
    cur = np.random.choice(degrees,p = prob)
    if do == 0:
        chn_prob(cur, vals[-2])
        do = 1
    if do == 1:
        chn_prob(cur, vals[-2])   
    vals.append(cur)
    i += 1
    

val = np.amax(prob)
goal_num = degrees[get_loc(prob, val)-1] 
print()
print("Reinforcement learning process ended")
print("The optimal angle to use to throw the ball is "+str(goal_num[0])+" degrees with a "+str(round((val*100),2))+"% probability.")

# Save the model
file = open("trained_model02.pkl","wb+")
pickle.dump(prob,file)
file.close()