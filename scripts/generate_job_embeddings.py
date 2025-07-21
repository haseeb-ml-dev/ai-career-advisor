# scripts/generate_job_embeddings.py

import pandas as pd
from sentence_transformers import SentenceTransformer
import pickle

# Load your dataset
df = pd.read_csv("data/job_descriptions.csv")
job_titles = df.iloc[:, 1]
job_descriptions = df.iloc[:, 2]

# Encode with SBERT
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(list(job_descriptions), convert_to_tensor=True)

# Save both titles and embeddings
with open("data/job_embeddings.pkl", "wb") as f:
    pickle.dump((list(job_titles), list(job_descriptions), embeddings), f)

print("✅ Job embeddings saved!")
