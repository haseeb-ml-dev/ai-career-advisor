# job_matcher/matcher.py

import torch
import pickle
from sentence_transformers import SentenceTransformer, util

# Load model once
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load precomputed embeddings
with open("data/job_embeddings.pkl", "rb") as f:
    job_titles, job_descriptions, job_embeddings = pickle.load(f)

def match_resume_to_jobs(resume_text, top_n=5):
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)

    similarities = util.cos_sim(resume_embedding, job_embeddings)[0]
    top_indices = torch.topk(similarities, k=top_n).indices.tolist()

    matches = []
    for idx in top_indices:
        matches.append((job_titles[idx], job_descriptions[idx], float(similarities[idx])))

    return matches
