import pandas as pd
import numpy as np

if __name__ == "__main__":
    df = pd.DataFrame({'Name': ['jack', 'jane', 'jack', 'jane', 'jack', 'jane', 'jack', 'jane'],
                       'State': ['SFO', 'SFO', 'NYK', 'CA', 'NYK', 'NYK', 'SFO', 'CA'],
                       'Grade': ['A', 'A', 'B', 'A', 'C', 'B', 'C', 'A'],
                       'Age': np.random.uniform(24, 50, size=8),
                       'Salary': np.random.uniform(3000, 5000, size=8), })

    # by state and name find mean age for each grade

    print(pd.pivot_table(df, values='Age', index=['State', 'Name'],
                         columns=['Grade']))
