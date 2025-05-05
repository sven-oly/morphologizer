import csv

def convert_csv_to_dict(csv_file_path):
    cherokee_dict = {}
    
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            english_key = row['English'].strip()
            
            entry = {
                "pcs_syl": row['Present Continuous Syllabary'].strip(),
                "is_syl": row['Incompletive Syllabary'].strip(),
                "im_syl": row['Immediate Syllabary'].strip() if row['Immediate Syllabary'].strip() != "None" else None,
                "cs_syl": row['Completive Syllabary'].strip(),
                "isy_syl": row['Infinitive Syllabary'].strip() if row['Infinitive Syllabary'].strip() != "None" else None,
                "pcs_trans": row['Present Continuous Transcription'].strip(),
                "it_trans": row['Incompletive Transcription'].strip(),
                "imt_trans": row['Immediate Transcription'].strip() if row['Immediate Transcription'].strip() != "None" else None,
                "ct_trans": row['Completive Transcription'].strip(),
                "isy_trans": row['Infinitive Transcription'].strip() if row['Infinitive Transcription'].strip() != "None" else None,
                "transitivity": row['Transitivity'].strip(),
                "set": row['Set A or B'].strip(),
                "3rd_person": row['3rd person a/ka?'].strip(),
                "dict_entry": row['Dictionary Entry'].strip()
            }
            
            cherokee_dict[english_key] = entry
    
    return cherokee_dict

# Example usage
csv_path = '/Users/disha/Downloads/cherokee_database2.csv'
cherokee_data = convert_csv_to_dict(csv_path)

# Print the result (or save to a JSON file)
import json
print(json.dumps(cherokee_data, indent=2, ensure_ascii=False))