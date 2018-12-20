import numpy as np
import pandas as pd
import scipy.stats as ss


def create_combined_vector(assessment_file):
    comb_df = pd.read_csv(assessment_file)

    # Seperate out vectors
    days = [0 for i in range(len(comb_df.values))]
    trend = comb_df['trend'].values
    close = comb_df['adjusted_close'].values

    # Resize and normalize
    days = days[1:]
    trend = ss.zscore(trend[1:])
    close = ss.zscore(np.diff(close))

    return (trend, close, days)


# Generate combined vecotr ready for ingestion by the
# Granger Causality function (days used for later graph)



(trend, close, days) = create_combined_vector(filename)
combined_vector = []
for i in range(len(trend)):
    combined_vector.append((trend[i], close[i]))