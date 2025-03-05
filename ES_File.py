#ES
import numpy as np

def ES(losses,alpha=None,VaR=None,use_PnL=False):
  if VaR is None:
    VaR=np.percentile(losses,100*alpha)
  es_value=np.mean(losses[losses>VaR]) if np.any(losses>VaR) else VaR
  return es_value

