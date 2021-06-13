import numpy as np
import pandas as pd

def get_spectrum_features(dfs, k):
    # get all possible motifs
    motifs = set()
    
    for df in dfs:
        for code in df['seq']:
            n = len(code)
            for i in range(n - k + 1):
                motifs.add(code[i:i + k])
    
    ret_dfs = []
    
    for df in dfs:
        df_data = []
        
        for code in df['seq']:
            motif_count = {}
            n = len(code)
            for i in range(n - k + 1):
                motif = code[i:i + k]
                motif_count[motif] = motif_count.get(motif, 0) + 1
                
            df_data.append(motif_count)
        
        motif_data = {}
        for motif in motifs:
            motif_col = []
            for motif_count in df_data:
                motif_col.append(motif_count.get(motif, 0))
            
            motif_data[motif] = motif_col
        
        ret_dfs.append(pd.DataFrame.from_dict(motif_data))
    
    return motifs, ret_dfs
        

def get_nonconstant_features(df1, df2):
    columns1 = set(df1.columns[df1.nunique() != 0])
    columns2 = set(df2.columns[df1.nunique() != 0])
    return list(columns1 & columns2)
