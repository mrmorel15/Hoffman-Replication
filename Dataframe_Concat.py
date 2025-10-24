import pandas as pd
import csv



def main():
    files = ['/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_academic.tsv', 
             '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_accountant.tsv', 
             '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_actor.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_actress.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_administrator.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_analyst.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_architect.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_artist.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_assistant.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_astronaut.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_athlete.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_attendant.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_auditor.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_author.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_broker.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_chef.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_chief.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_cleaner.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_clergy.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_clerk.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_coach.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_collector.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_comedian.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_commander.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_composer.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_cook.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_counselor.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_curator.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_dentist.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_designer.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_detective.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_developer.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_diplomat.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_director.tsv',
             '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_doctor.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_drawer.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_driver.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_economist.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_editor.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_engineer.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_journalist.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_judge.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_landlord.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_minister.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_nurse.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_official.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_operator.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_psychiatrist.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_psychologist.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_researcher.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_singer.tsv',
             '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_student.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_surgeon.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_tailor.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_teacher.tsv',
            '/home/mmorel/NLPScholar/results/GPT2_large_hofmann_agreement_technician.tsv']
    #dfs = [pd.read_csv(f, sep='\t') for f in sorted(files)]
    dfs = []
    for f in sorted(files):
        try:
            df = pd.read_csv(f, sep='\t')
            if len(df.columns) == 1:
                print(f" File {f} only has one column! Check its formatting.")
            dfs.append(df)
        except Exception as e:
            print(f" Error reading {f}: {e}")
    combined = pd.concat(dfs, ignore_index=True)
    combined.to_csv("GPT2largeresults.tsv", sep='\t', index=False)
    
if __name__ == '__main__':
    main()