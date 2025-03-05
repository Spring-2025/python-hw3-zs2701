#VaR
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def VaR(r,confidence,principal=100):
  alpha=1-confidence
  var_percentile=np.percentile(r,alpha*100)
  VaR_value=abs(var_percentile)*principal
  return VaR_value

def percent_var(r,confidence):
  alpha=1-confidence
  plt.hist(r,bins=50,alpha=0.75)
  plt.show()

  out=np.percentile(r,(1-alpha)*100)
  return abs(out)

returns=np.random.normal(0,1,10000)
print(np.percentile(returns, 97.72))

r = np.random.normal(0.05, 0.03, 1000000)
probability2SD = norm.cdf(2)  # Probability under normal curve within 2 SD
my_confidence = probability2SD
my_percent_var = percent_var(r, my_confidence )
print(np.round(my_percent_var, 2) == 0.01)
