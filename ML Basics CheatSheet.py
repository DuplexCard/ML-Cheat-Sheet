### ML Basics CheatSheet ###



#_____ PANDAS _____#

    import pandas as pd
    # Summary Methods    
    .describe()
    .head()

    # Data insight
    .mean()
    .median()
    .max()
    .min()
    
    # Data retrieval
        # Index based data retrieval
        .iloc()
        # Name based data retrieval
        .loc()

    # Series of unique values
    .unique()

    # Mapping functions
    .map() #applied to column returning a series
    .apply() #applies to rows returning a dataFrame

    # Count occurrences of a value
    .value_counts()
    .size()
    .groupby('column').column.count()

    # Gets index of MAX value
    .idxmax()

    # Get sum of all trues in series
    .sum()
    

    # __ Grouping and Sorting __ #

        # Creates groups of the DataFrame
        .groupby('column')
        .groupby(['col1', 'col2'])
        
        # Runs all functions within the list for a set dataframe
        .agg()
        .agg([len, min, max])

        # Convert Multi index to single index
        .reset_index()
        # Multi Index resource https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html
        
        # Sort Data frame by a column
        .sort_values(by='colName')
        .sort_values(by=['colName1', 'colName2'])
        .sort_values(by='colName', ascending=False)
        
        # Sort by index number
        .sort_index()


   
    # __ Missing Values __ #
         
         # Get data type
         .dtype
         # Get null (NaN) or not null objects
        .isnull()
        .notnull()

        # Replace missing values
        .fillna() #needs to be stored back in with a declaration for permanent change
        .replace(arg1, arg2)

        # Get names of columns with missing values (for X_train_)
        cols_with_missing = [col for col in X_train.columns
                                if X_train[col].isnull().any()]

        # Drop columns with missing values
        reduced_X_train = X_train.drop(cols_with_missing, axis=1)
        reduced_X_valid = X_valid.drop(cols_with_missing, axis=1)
        

        # make new column indicating what will be imputed (modified imputation)
        for col in cols_with_missing:
            X_train_copy[col+"_was_missing"] = X_train_copy[col].isnull()
            X_valid_copy[col+"_was_missing"] = X_valid_copy[col].isnull()
            #replace x_train with x_train_copy below

        # imputation
        my_imputer = SimpleImputer() #https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html
        imputed_X_train = pd.DataFrame(my_imputer.fit_transform(X_train))
        imputed_X_valid = pd.DataFrame(my_imputer.transform(X_valid))
            # immutation removes column names so this is putting them back
        imputed_X_train.columns = X_train.columns
        imputed_X_vaild.columns = X_valid.columns

        
        # Convert type of value in series
        .astype()

        # Catagorical Values
           
            # Get list of categorical variables
                s = (X_train.dtypes == 'object')
                object_cols = list(s[s].index)

            # Make copy to avoid changing original data 
                label_X_train = X_train.copy()
                label_X_valid = X_valid.copy()

            # Apply label encoder to each column with categorical data (for 1D data use LabelEncoder instead of Ordinal)
                ordinaL_encoder = OrdinalEncoder()
                for col in object_cols:
                    label_X_train[col] = ordinaL_encoder.fit_transform(X_train[col])
                    label_X_valid[col] = ordinaL_encoder.transform(X_valid[col])


            # Apply one-hot encoder to each column with categorical data
                OH_encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
                OH_cols_train = pd.DataFrame(OH_encoder.fit_transform(X_train[object_cols]))
                OH_cols_valid = pd.DataFrame(OH_encoder.transform(X_valid[object_cols]))

            # One-hot encoding removed index; put it back
                OH_cols_train.index = X_train.index
                OH_cols_valid.index = X_valid.index

            # Remove categorical columns (will replace with one-hot encoding)
                num_X_train = X_train.drop(object_cols, axis=1)
                num_X_valid = X_valid.drop(object_cols, axis=1)

            # Add one-hot encoded columns to numerical features
                OH_X_train = pd.concat([num_X_train, OH_cols_train], axis=1)
                OH_X_valid = pd.concat([num_X_valid, OH_cols_valid], axis=1)



    # __ Renaming and Combining __ #
            
        # Change the name of a column
        .rename(columnsb={'arg1': 'arg2'})
        # Change the name of an index
        .rename(index={0: 'firstEntry', 1: 'secondEntry'})

        # Renames an Axis
        .rename_axis('arg1', axis='columns')
        .rename_axis('arg2', axis='rows')

        # Combining Data
        .concat() # "Smushes" together from the bottom, good formost columns identical
        .join()
            # Syntax for this is as such:
            # left = canadian_youtube.set_index(['title', 'trending_date'])
            # right = british_youtube.set_index(['title', 'trending_date'])
            # left.join(right, lsuffix='_CAN', rsuffix='_UK')
            
        
        .merge()