# In a small town the population is p0 = 1000 at the beginning of a year. 
# The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. 
# How many years does the town need to see its population greater or equal to p = 1200 inhabitants?

def nb_year(p0, percent, aug, p):
    percent = float(percent/100)
    counter, p_tmp = 1, int(p0 + p0*percent + aug)
    while p_tmp<p:
        counter += 1
        p_tmp += p_tmp*percent + aug
        p_tmp = int(p_tmp)
        if p_tmp>=p:
            break
        else:
            continue
    return counter