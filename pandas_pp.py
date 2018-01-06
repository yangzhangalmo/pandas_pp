def multi_value_counts(df, cols):
    ''' Return object containing counts of unique values for multiple columns.
    Args:
        df: pandas dataframe
        cols: the name of columns that need to be counted
    Returns:
        counts: Series

    Example:
        df = pd.DataFrame([[1, 2], [1, 3], [2, 3], [1, 3]])
        cols = [0, 1]
        print multi_value_counts(df, cols)
        
        df = pd.DataFrame([[1, 2, 2], [1, 3, 4], [2, 3, 4], [1, 3, 2]])
        cols = [0, 2]
        print multi_value_counts(df, cols)
        
        df = pd.DataFrame([[1, 2, 2], [1, 3, 4], [2, 3, 4], [1, 3, 2]], columns=['cispa', 'epfl', 'stanford'])
        cols = ['cispa', 'stanford']
        print multi_value_counts(df, cols)
    '''

    df_copy = df.copy()
    
    df_copy['temp_combine'] = ''
    
    for c in cols:
        if c == cols[0]:
            df_copy['temp_combine'] = df_copy[c].apply(str)
        else:
            df_copy['temp_combine'] = df_copy['temp_combine']+'_'+df_copy[c].apply(str)
    return df_copy.temp_combine.value_counts()


