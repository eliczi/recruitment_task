import pandas as pd
import re

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    if not re.fullmatch(r'[a-zA-Z_]+', new_column):
        return pd.DataFrame()

    if not re.fullmatch(r'[a-zA-Z_+\-*\s]+', role):
        return pd.DataFrame()

    potential_cols = re.sub(r'[+\-*]', ' ', role).split()
    for col in potential_cols:
        if not re.fullmatch(r'[a-zA-Z_]+', col) or col not in df.columns:
            return pd.DataFrame()

    try:
        new_df = df.copy()
        result = new_df.eval(role)
        new_df[new_column] = result
        return new_df
    except Exception:
        return pd.DataFrame()