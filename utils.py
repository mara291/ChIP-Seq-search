from pybedtools import BedTool
import os

def jaccard_index(a_file, b_file):
    a = BedTool(a_file).sort()
    b = BedTool(b_file).sort()
    result = a.jaccard(b)
    return result['jaccard']

def compare_data(uploaded_file, data_dir='data/', top_n=3):
    scores = []
    for fname in os.listdir(data_dir):
        if fname.endswith(".bed"):
            ref_path = os.path.join(data_dir, fname)
            score = jaccard_index(uploaded_file, ref_path)
            scores.append((fname, score))
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:top_n]
