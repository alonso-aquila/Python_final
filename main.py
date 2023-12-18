# This is final task Python web branch final_task

import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame(random.sample(['human', 'robot'] * 10, 20), columns={'Essence'})
data.head()
