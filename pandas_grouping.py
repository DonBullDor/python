import pandas as pd
import numpy as np

if __name__ == "__main__":
    df = pd.DataFrame({'Name': ['jack', 'jane', 'jack', 'jane', 'jack', 'jane', 'jack', 'jane'],
                       'State': ['SFO', 'SFO', 'NYK', 'CA', 'NYK', 'NYK', 'SFO', 'CA'],
                       'Grade': ['A', 'A', 'B', 'A', 'C', 'B', 'C', 'A'],
                       'Age': np.random.uniform(24, 50, size=8),
                       'Salary': np.random.uniform(3000, 5000, size=8), })

    print(df)
    # Note that the columns are ordered automatically in their alphabetic order
    # for custom order please use below code
    # df = pd.DataFrame(data, columns = ['Name', 'State', 'Age','Salary'])
    # Find max age and salary by Name / State
    # with the group by, we can use all aggregate functions such as min, max, mean, count, cumsum
    print(df.groupby(['Name', 'State']).max())
