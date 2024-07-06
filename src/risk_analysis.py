import numpy as np

def risk_analysis(simul_nums, threshold=0):
    # Ensure npvs is a numpy array of numbers, extracting the first element if it's a tuple
    npvs = np.array([x for x in simul_nums])

    # Calculate the probability and expected loss
    prob = prob_exceeding(npvs, threshold)
    loss = expected_loss(npvs, threshold)
    
    return prob, loss

def prob_exceeding(npvs, threshold):
    # Calculate the probability of npvs exceeding the threshold
    prob = np.mean(npvs > threshold)
    print(f"Probability of Exceeding Threshold ({threshold}): {prob:.2%}")

    return prob

def expected_loss(npvs, threshold):
    # Calculate the expected loss for values below the threshold
    losses = npvs[npvs < threshold]
    if losses.size == 0:
        expected_loss = 0
    else:
        expected_loss = np.mean(losses)
    
    
    print(f"Expected Loss: -${abs(expected_loss)}")
    #print(f"Expected Loss: -${abs(expected_loss):,.2f}")

    return expected_loss