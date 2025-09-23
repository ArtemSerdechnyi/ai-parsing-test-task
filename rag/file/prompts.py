def build_match_columns_prompt(columns_data: list[dict], target_columns: tuple[str, ...]) -> str:
    prompt = f"""
        You are an assistant helping to identify relevant columns in a dataset.

        Target column names: {target_columns}

        For each provided column, decide if it matches (or is a synonym/close variation of) 
        one of the target names. 

        Rules:
        - Return a list of ColumnMatch objects.
        - Always include a short 'reason' for why you marked is_match true or false.
        - is_match must be strictly boolean.
        - target_column_name a target column name corresponding to the column

        Columns to analyze:
        {columns_data}
    """
    return prompt
