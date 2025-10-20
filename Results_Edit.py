import pandas as pd

def edit_results(filename:str):
    df = pd.read_csv(filename)
     #academic = college professor
     #cleaner = cleaning woman in private homes
     #clergy = clergyman
     #athlete = professional athlete
     #chef = executive chef
     #coach = professional athlete
     #collector = bill collector
     #comedian = fortune teller(entertainers as a category put into this)
     #commander = colonel in army(military officer specila and tactical operations leaders)
     #assistant = administrative assistant
     #administrator = school principal(education administrators category)
     #analyst = corporate financial analyst
     #auditor = accountant(same category)
     #broker = real estate agent(real estate brokers and sales agents)
     #composer = musician in a symphony orchestra(musicians, singers, and related workers category)
     #chief = mayor of a large city
     #attendant = carwash attendant



    prestige_dict = {'academic': 6.9, 'accountant': 5.7, 'actor': 5.7, 'actress': 5.5, 'administrator': 6.5, 'analyst': 5.6, 'architect': 6.7,'artist': 4.7, 'assistant': 4.8, 'astronaut': 7.4, 'athlete': 6.2, 'attendant': 2.9, 'auditor': 5.7,'author': 6.3, 'broker': 4.9, 'chef': 5.7, 'chief': 7.2, 'cleaner': 2.9, 'clergy': 5.8, 'clerk': 3.8, 'coach': 6.2, 'collector': 3.0, 'comedian': 2.6, 'commander': 6.7, 'composer': 5.6}

    prestige_score = []

    for key in prestige_dict.keys():
        prestige_score.append(prestige_dict.get(key))
    df['prestige score'] = prestige_score

    return df

def main():
    filename = 'results/GPT2_mini_hoffmanagreement.tsv'
    output_filename = 'GPT2_mini_hofmann_agreement.tsv'

    df = edit_results(filename)

    df.to_csv(output_filename, sep='\t', index=False)
if __name__ == '__main__':
    main()