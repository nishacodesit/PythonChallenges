"""Dice may not have any memory, but apparently the roulette wheel at the Learn Challenge Casino does. You’ve received a tip-off that the wheel has some exploitable bias where the probability of landing on a given number changes depending on the number previously landed on. Analyze a list containing a history of roulette spins.
Return a dictionary where the keys are numbers on the roulette wheel, and the values are dictionaries mapping numbers on the wheel to probabilities, such that `d[n1][n2]` is an estimate of the probability that the next spin will land on n2, given that the previous spin landed on n1.
"""

def conditional_roulette_probs(history):
    """
    Example:
    conditional_roulette_probs([1, 3, 1, 5, 1])
    {1: {3: 0.5, 5: 0.5},
       3: {1: 1.0},
       5: {1: 1.0}
      }
    """

    print ("History is ", history)

    count = {}
    for i, num in enumerate(history) :
        if i == (len(history) - 1):
            break

        if num not in count.keys():
            count[num] = {}
            count[num][history[i+1]] = 1
        else :
            if history[i+1] in count[num].keys():
                count[num][history[i+1]] += 1
            else :
                count[num][history[i+1]] = 1

    prob = {}
    for key in count.keys():
        prob[key] = {}
        nexts = count[key]
        total = sum(nexts.values())
        for nxt_key in nexts.keys():
            prob_nxt = (nexts[nxt_key] / total)
            prob[key][nxt_key] = prob_nxt


    #for key in count.keys():
        #print ("COUNT---", key, " ", count[key])
    for key in prob.keys():
        print ("probability of ", prob[key], " after ", key)


    return prob

conditional_roulette_probs([1,2,5,1,2,4,2,5])
conditional_roulette_probs([1,1,1,1])
conditional_roulette_probs([1,3,1])
