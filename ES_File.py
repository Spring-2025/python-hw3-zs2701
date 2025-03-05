#ES
import numpy as np

def ES(losses,confidence=None,VaR=None,use_PnL=False):
  if VaR is None:
    VaR=np.percentile(losses,100*confidence)
  es_value=np.mean(losses[losses>VaR]) if np.any(losses>VaR) else VaR
  return es_value

np.random.seed(40)
u = np.random.uniform(0, 100, 100000)

es_confidence = ES(losses=u, confidence=0.8)
print('ES with confidence:', np.round(es_confidence, 0) == 90)

es_var = ES(losses=u, VaR=80)
print('ES with VaR:', np.round(es_var, 0) == 90)
