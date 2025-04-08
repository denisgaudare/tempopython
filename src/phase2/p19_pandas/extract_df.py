
import pandas as pd
import numpy as np


df = pd.read_csv("data.csv", date_format="", parse_dates=["date","naissance"], usecols=["id", "date", "value"])
