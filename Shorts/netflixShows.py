import pandas as pd
import pandas_profiling

nf_data = pd.read_csv('/Users/ian.salandy@ibm.com/downloads/netflix_titles.csv')

print(nf_data.sample())

