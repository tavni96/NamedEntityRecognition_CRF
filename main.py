from CRF_NER import CRF_NER
import pandas as pd

# Create Gazateer
gazetteer = pd.read_csv('gazetteer/gazateer.csv')
gazetteer = dict(zip(gazetteer['entities'].tolist(), gazetteer['categories'].tolist()))

# Get documents
documents = [str(x) for x in pd.read_csv('data/techCorpus.csv')['text'].tolist()][0:1000]

# Training Model
ner_crf = CRF_NER(gazetteer)
ner_crf.train(documents)

# Predictions
ner_crf.predict('Peter is looking to work for Google in Ireland where the Government is banning iphones')
