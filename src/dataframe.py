import asyncio
import pandas as pd
from werkzeug.datastructures import FileStorage


async def get_columns(file: FileStorage, sep:str) -> list:
    df = await read_file(file, sep)
    return list(df)


async def read_file(file: FileStorage, sep: str) -> pd.DataFrame:
    if file.split(".")[-1] in ("csv", "txt"):
        df = pd.read_csv(file, sep=sep)
    elif file.split(".")[-1] in ("xls", "xlsx"):
        df = pd.read_excel(file, dtype=str)
    else:
        df = pd.DataFrame()

    return df


async def merge(
    file_left: str,
    file_right: str,
    left_on: list,
    right_on: list,
    how:str,
    out_file: str,
    sep_left: str,
    sep_right: str
):

    df_left, df_right = await asyncio.gather(
        read_file(file_left, sep_left),
        read_file(file_right, sep_right)
    )

    df = pd.merge(df_left, df_right, left_on=left_on, right_on=right_on, how=how)
    df.to_excel(out_file, index=False)
