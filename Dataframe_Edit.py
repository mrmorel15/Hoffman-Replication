import pandas as pd
import csv

def edit_dataframe(pred_filename: str, eval_filename:str):
    df = pd.read_csv(pred_filename, sep='\t')
    dataframe = pd.read_csv(eval_filename, sep='\t')
    
    max_wordpos_sent = df.groupby('sentid')['wordpos'].max().reset_index()
    max_wordpos_sent = max_wordpos_sent.rename(columns={'wordpos': 'ROI'})

    roi_map = max_wordpos_sent.set_index('sentid')['ROI']

    dataframe['ROI'] = dataframe['sentid'].map(roi_map)
    
    return dataframe


def main():
    pred_filename = '/home/mmorel/NLPScholar/predictions/GPT2_large_agreement_.tsv'
    eval_filename = '/home/mmorel/NLPScholar/AAE_SAE_MP_drawer.tsv'
    output_filename = 'AAE_SAE_large_drawer_with_ROI.tsv'
    df = edit_dataframe(pred_filename, eval_filename)
    
    df.to_csv(output_filename, sep='\t', index=False)
if __name__ == '__main__':
    main()