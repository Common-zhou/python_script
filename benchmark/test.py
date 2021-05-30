#coding=utf-8
import pandas as pd

if __name__ == '__main__':
    file = r'D:\social\SF1.tar\composite-merged-fk\dynamic\merge\Person.csv'
    df = pd.read_csv(file, sep="|")
    columns_name = df.columns.tolist()
    for i in range(0, len(columns_name)):
        old_column_name = columns_name[i]
        columns_name[i] = old_column_name.replace("_", "").lower()

    df.columns = columns_name
    df = df[["creationdate", "id"]]
    df.to_csv("test.csv", encoding="utf_8", index=False, sep="|")

    print(df.tail(10))
