import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(15, 2))
print(df.head(10))

df.to_csv('numpy.csv')