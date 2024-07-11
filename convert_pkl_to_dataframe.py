import pandas as pd

# 加载.pkl文件中的数据到DataFrame
data = pd.read_pickle('tracks.pkl')

# 显示DataFrame
print(data)
