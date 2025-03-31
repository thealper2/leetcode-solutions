import pandas as pd

def analyze_dna_patterns(samples: pd.DataFrame) -> pd.DataFrame:
    def check_patterns(sequence):
        return {
            'has_start': int(sequence.startswith('ATG')),
            'has_stop': int(sequence[-3:] in {'TAA', 'TAG', 'TGA'}),
            'has_atat': int('ATAT' in sequence),
            'has_ggg': int('GGG' in sequence)
        }

    patterns = samples['dna_sequence'].apply(check_patterns).apply(pd.Series)
    return pd.concat([samples, patterns], axis=1)