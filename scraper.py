import pandas as pd

data = pd.read_html('https://en.wikipedia.org/wiki/Roswell,_Georgia')

print(len(data))
print(data[2])