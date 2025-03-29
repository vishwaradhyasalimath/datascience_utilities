import pandas as pd

def clean_dataframe(df, fill_na_value=0, drop_duplicates=True):
    """
    Utility function to clean a Pandas DataFrame by filling missing values and removing duplicates.
    
    :param df: Pandas DataFrame to clean
    :param fill_na_value: Value to replace NaN (default is 0)
    :param drop_duplicates: Boolean flag to remove duplicate rows (default is True)
    :return: Cleaned DataFrame
    """
    df_cleaned = df.copy()
    
    # Fill missing values
    df_cleaned.fillna(fill_na_value, inplace=True)
    
    # Remove duplicate rows if enabled
    if drop_duplicates:
        df_cleaned.drop_duplicates(inplace=True)
    
    return df_cleaned

# Example usage
if __name__ == "__main__":
    # Sample data
    data = {
        "Name": ["Alice", "Bob", "Charlie", "Alice", None],
        "Age": [25, None, 30, 25, 28],
        "Salary": [50000, 60000, None, 50000, 55000]
    }

    df = pd.DataFrame(data)
    
    print("Original DataFrame:")
    print(df, "\n")
    
    # Clean DataFrame
    cleaned_df = clean_dataframe(df, fill_na_value="N/A")
    
    print("Cleaned DataFrame:")
    print(cleaned_df)
