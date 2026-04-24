
## Purpose

### Model equilibrium relationships
from statsmodels.tsa.vector_ar.vecm import VECM

def run_vecm(data):
    model = VECM(data, k_ar_diff=1, coint_rank=1)
    return model.fit()
