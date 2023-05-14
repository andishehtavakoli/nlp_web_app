import spacy
import pandas as pd
import numpy as np


from src.ner import build_entity

TEXTS ="Net income was $9.4 million compared to the prior year of $2.7 million."




if __name__ == '__main__':

    df = build_entity(TEXTS)
    print(df.head())
