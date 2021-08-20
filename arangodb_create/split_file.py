"""
将文件拆开 比如Place文件 拆分成Country、City
"""
import pandas as pd

# Organisation --> Company/University
# Place --> Continent/Country/City
path = "/data/sf1/resolve"

organisation_pd = pd.read_csv(path + "/Organisation.csv", sep="|", dtype=object)

company_ = organisation_pd.loc[organisation_pd[':LABEL'] == 'Company']
university_ = organisation_pd.loc[organisation_pd[':LABEL'] == 'University']

# 将 Organisation 选出来的存入csv
company_.drop(':LABEL', axis=1).to_csv(path + "/Company.csv", encoding="utf_8", index=False, sep="|")
university_.drop(':LABEL', axis=1).to_csv(path + "/University.csv", encoding="utf_8", index=False, sep="|")


place_pd = pd.read_csv(path + "/Place.csv", sep="|", dtype=object)
place_pd.loc[place_pd[':LABEL'] == 'Continent'].drop(':LABEL', axis=1).to_csv(path + "/Continent.csv", encoding="utf_8", index=False, sep="|")
place_pd.loc[place_pd[':LABEL'] == 'Country'].drop(':LABEL', axis=1).to_csv(path + "/Country.csv", encoding="utf_8", index=False, sep="|")
place_pd.loc[place_pd[':LABEL'] == 'City'].drop(':LABEL', axis=1).to_csv(path + "/City.csv", encoding="utf_8", index=False, sep="|")
