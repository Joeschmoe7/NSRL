# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import datetime

currentDate = datetime.datetime.now().strftime("%m-%d-%Y")

fileName = r"D:\Hashes\NSRL\IOS.txt"
saveFileName = r"D:\IOS-converted_" + currentDate + ".txt"

df = pd.read_csv(fileName, dtype={"SHA-1": "string", "MD5": "string", "CRC32": "string", "Filename": "string", "FileSize": "string", "Product Code": "string", "OpSystemCode": "string", "SpecialCode": "string"})            
df["MD5"] = df["MD5"].drop_duplicates()
df1 = df["MD5"]
df1 = df1.dropna()

np.savetxt(saveFileName, df1.values, fmt='%s')
