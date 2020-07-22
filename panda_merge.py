import pandas as pd

if __name__ == "__main__":
    br = '\n'
    data = {
        'emp_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Jason', 'Andy', 'Allen', 'Alice', 'Amy'],
        'last_name': ['Larkin', 'Jacob', 'A', 'AA', 'Jackson']}

    df_1 = pd.DataFrame(data, columns=['emp_id', 'first_name', 'last_name'])

    data = {
        'emp_id': ['4', '5', '6', '7'],
        'first_name': ['Brian', 'Shize', 'Kim', 'Jose'],
        'last_name': ['Alexander', 'Suma', 'Mike', 'G']}

    df_2 = pd.DataFrame(data, columns=['emp_id', 'first_name', 'last_name'])

    # Using concat
    df = pd.concat([df_1, df_2])
    print(df)
    print(br)
    # or
    # Using append
    print(df_1.append(df_2))
    print(br)
    # Join the two DataFrames along columns
    pd.concat([df_1, df_2], axis=1)

    # Merge two DataFrames based on the emp_id value
    # in this case only the emp_id's present in both tables will be joined
    pd.merge(df_1, df_2, on='emp_id')

    # Left join
    print(pd.merge(df_1, df_2, on='emp_id', how='left'))
    print(br)
    # Merge while adding a suffix to duplicate column names of both table
    print(pd.merge(df_1, df_2, on='emp_id', how='left', suffixes=('_left', '_right')))
    print(br)

    # Right join
    pd.merge(df_1, df_2, on='emp_id', how='right')
    print(br)
