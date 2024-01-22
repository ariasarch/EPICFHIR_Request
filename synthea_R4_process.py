import json
import os
import pandas as pd

check = ["Label", "%BASOS", "%EOS", "ABDOMINAL PAIN", "ADD ON DIFFERENTIA", "ALC (ABSOLUTE LYMPHOCYTE COUNT) _ EXTERNA",
        "AMB REFERRAL TO INTERVENTIONAL RADIOLOGY", "AMB REFERRAL TO PEDIATRIC GASTROENTEROLOGY",
        "ANC (ABSOLUTE NEUTROPHIL COUNT) _ EXTERNA", "Abdominal Infection", "Abdominal abscess", "Abdominal bloating",
        "Abdominal cramping", "Abdominal discomfort", "Abdominal distension (gaseous)",
        "Abdominal migraine_ not intractable", "Abdominal or pelvic swelling_ mass or lump_ unspecified site",
        "Abdominal pain", "Abdominal pain in female", "Abdominal pain in female patient", "Abdominal pain in male",
        "Abdominal pain through to back", "Abdominal pain_ acute", "Abdominal pain_ chronic_ epigastric",
        "Abdominal pain_ chronic_ generalized", "Abdominal pain_ epigastric", "Abdominal pain_ generalized",
        "Abdominal pain_ left lower quadrant", "Abdominal pain_ left upper quadrant",
        "Abdominal pain_ other specified site", "Abdominal pain_ periumbilic",
        "Abdominal pain_ right lower quadrant", "Abdominal pain_ right upper quadrant",
        "Abdominal pain_ unspecified abdominal location", "Abdominal pain_ unspecified location",
        "Abdominal pain_ unspecified site", "Abdominal tenderness", "Abdominal tenderness absent",
        "Abnormal electrocardiogram (ECG) (EKG)", "Abnormal electroencephalogram (EEG)", "Abnormal electromyogram (EMG)",
        "Abnormal findings on diagnostic imaging of other abdominal regions_ including retroperitoneum",
        "Abnormal mammogram_ unspecified", "Absence of nausea and vomiting", "Acute abdominal pain",
        "Allergy status to sulfonamides", "Allergy to sulfonamide", "Anxiety", "Anxiety and depression",
        "Anxiety disorder", "Anxiety disorder due to known physiological condition", "Anxiety disorder_ unspecified",
        "Anxiety disorder_ unspecified type", "Anxiety state_ unspecified", "Asleep", "Audiogram Date",
        "Audiogram Specific Frequency Field Hz", "Audiogram Specific Frequency Type", "Audiogram Time", "BASOS",
        "BCHO OPC GASTROENTEROLOGY", "Back pain", "Bacterial Culture_ Urine w/ gram stain",
        "Bacterial Culture_ Urine w/o gram stain", "Benign neoplasm of stomach", "Bloating", "CALCIUM REPLACEMEN",
        "CELL COUNT AND  DIFFERENTIAL_ BODY FLUI", "CELL COUNT AND DIFFERENTIAL_ CSF",
        "COMPLETE BLOOD COUNT WITH DIFFERENTIA", "CSF gram stain method", "CYTOLOGY_ NON_GYNECOLOGIC (DELIVER SPECIMEN TO PATHOLOGY)",
        "Calcium_ and magnesium_containing product", "Chronic abdominal pain", "Chronic generalized abdominal pain",
        "Circadian rhythm sleep disorder_ unspecified", "Comatose", "Confusion", "Constipation", "Constipation_ unspecified",
        "Constipation_ unspecified constipation type", "Cyclic vomiting syndrome",
        "Cyclic vomiting syndrome_ intractability of vomiting not specified_ presence of nausea not specified",
        "Cyclical vomiting_ in migraine_ intractable", "Cyclical vomiting_ in migraine_ not intractable",
        "DERMATOPATHOLOGY", "DIFFERENTIA", "DIFFERENTIAL_ MANUAL (EXTERNAL LAB)", "DISCHARGE REFERRAL TO GASTROENTEROLOGY",
        "Depression", "Depression_ unspecified depression type", "Diarrhea", "Diarrhea and vomiting", "Diarrhea not present",
        "Diarrhea_ unspecified", "Diarrhea_ unspecified type", "Difficulty sleeping", "Disease of stomach and duodenum_ unspecified",
        "Disorders of magnesium metabolism", "Disorientation", "Disorientation_ unspecified", "Dyspepsia and other specified disorders of function of stomach",
        "Dysuria", "EOSINOPHIL ABS COUNT _ EXTERNA", "EOS_ BF", "EOS_ CSF", "Electromyogram abnormal",
        "Encounter for screening mammogram for malignant neoplasm of breast", "Endoscopy of stomach",
        "Epigastric abdominal pain", "FECAL WHITE BLOOD CELL EXA", "FINE NEEDLE ASPIRATION (DELIVER SPECIMEN TO PATHOLOGY)",
        "Family history of diabetes mellitus", "Family history of epilepsy and other diseases of the nervous system",
        "Family history of ischemic heart disease",
        "Family history of ischemic heart disease and other diseases of the circulatory system",
        "Family history of malignant neoplasm of breast", "Family history of malignant neoplasm of digestive organs",
        "Family history of malignant neoplasm of gastrointestinal tract", "Family history of malignant neoplasm of liver",
        "Family history of malignant neoplasm of other genital organs", "Family history of malignant neoplasm of other organs or systems",
        "Family history of malignant neoplasm of ovary", "Family history of malignant neoplasm_ unspecified",
        "Family history of other diseases of the digestive system", "Family history of other endocrine_ nutritional and metabolic diseases",
        "Family history of other mental and behavioral disorders", "Family history of other specified malignant neoplasm",
        "Family history of stroke", "Family history of stroke (cerebrovascular)", "Family history with explicit context pertaining to father",
        "Family history with explicit context pertaining to mother", "Family history with explicit context pertaining to sister",
        "Fever", "Fever and chills", "Fever and other physiologic disturbances of temperature regulation", "Fever in pediatric patient",
        "Fever presenting with conditions classified elsewhere", "Fever with chills", "Fever_ unspecified", "Fever_ unspecified fever cause",
        "Functional abdominal pain syndrome", "GASTROENTEROLOGY SV", "GYNECOLOGIC AND ANAL CYTOLOGY THIN PREP (DELIVER SPECIMEN TO PATHOLOGY)",
        "Generalized Anxiety Disorder", "Generalized abdominal pain", "HEMATOPATHOLOGY", "HYPERTENSION", "Hallucinations",
        "Hallucinations_ unspecified", "Hemangioma of intra_abdominal structures", "Hernia of abdominal wall",
        "Hernia of unspecified site of abdominal cavity without mention of obstruction or gangrene",
        "Hypersomnia with sleep apnea_ unspecified", "Hypertension", "Hyponatremia", "INTERVENTIONAL RADIOLOGY",
        "IP CONSULT FOR NEURORADIOLOGY PROCEDUR", "IP CONSULT TO GASTROENTEROLOGY", "IP CONSULT TO INTERVENTIONAL RADIOLOGY",
        "IP CONSULT TO PEDIATRIC GASTROENTEROLOGY", "Ileus (CMS code)", "Ileus_ unspecified (CMS code)",
        "Inadequate sleep hygiene", "Increased sweating", "Infection with microorganisms resistant to penicillins",
        "Insomnia", "Insomnia_ unspecified", "Insomnia_ unspecified type", "Intractable abdominal pain",
        "Intractable cyclical vomiting with nausea", "Intractable nausea and vomiting",
        "Intractable vomiting with nausea_ unspecified vomiting type", "Intravenous pyelogram (procedure)", "LYMPHOCYTE ANTIGEN STIMULATION",
        "LYMPHOCYTE MITOGEN STIMULATION", "LYMPHOCYTE SUBSETS", "LYMPHOCYTE SUBSETS_ T/B/NK_CELL QUANTITATION FOR PERIPHER BLOOD (INC. CBC DIFFERENTIAL)",
        "Localization_related (focal) (partial) epilepsy and epileptic syndromes with complex partial seizures_ with intractable epilepsy",
        "Localization_related (focal) (partial) epilepsy and epileptic syndromes with complex partial seizures_ without mention of intractable epilepsy",
        "Localization_related (focal) (partial) epilepsy and epileptic syndromes with simple partial seizures_ with intractable epilepsy",
        "Localization_related (focal) (partial) epilepsy and epileptic syndromes with simple partial seizures_ without mention of intractable epilepsy",
        "Localization_related (focal) (partial) symptomatic epilepsy and epileptic syndromes with complex partial seizures_ intractable_ without status epilepticus (CMS code)",
        "Localization_related (focal) (partial) symptomatic epilepsy and epileptic syndromes with complex partial seizures_ not intractable_ without status epilepticus (CMS code)",
        "Localization_related (focal) (partial) symptomatic epilepsy and epileptic syndromes with simple partial seizures_ intractable_ without status epilepticus (CMS code)",
        "Localization_related (focal) (partial) symptomatic epilepsy and epileptic syndromes with simple partial seizures_ not intractable_ without status epilepticus (CMS code)",
        "Long term (current) use of antibiotics", "Lower abdominal pain", "Lower abdominal pain_ unspecified",
        "MAGNESIUM SALTS REPLACEMEN", "MELATONIN 1 MG TABLE", "MELATONIN 1 MG/ML ORAL SUS", "MELATONIN 10 MG TABLE",
        "MELATONIN 3 MG TABLE", "MELATONIN 5 MG TABLE", "MONOCYTE ABS COUNT _ EXTERNA",
        "Major depressive disorder_ recurrent episode_ severe_ without mention of psychotic behavior",
        "Major depressive disorder_ recurrent severe without psychotic features (CMS code)", "Malignant neoplasm of stomach",
        "Memory loss", "Morbid (severe) obesity due to excess calories (CMS code)", "Muscle weakness (generalized)",
        "Muscle weakness of limb", "NEOSTIGMINE METHYLSULFATE 1 MG/ML INJECTION SOLUTION",
        "NEOSTIGMINE METHYLSULFATE 1 MG/ML INTRAVENOUS SOLUTION", "NEUTROPHIL CYTOPLASMIC ANTIBODIES",
        "NEUTROPHIL OXIDATIVE INDEX", "Nausea", "Nausea _ vomiting", "Nausea alone", "Nausea and vomiting",
        "Nausea and vomiting in adult", "Nausea and vomiting_ intractability of vomiting not specified_ unspecified vomiting type",
        "Nausea vomiting and diarrhea", "Nausea with vomiting", "Nausea with vomiting_ unspecified", "Nausea without vomiting",
        "Nausea_ vomiting_ and diarrhea", "Neck pain", "Nicotine dependence_ cigarettes_ uncomplicated", "No nausea",
        "Non_intractable cyclical vomiting with nausea",
        "Non_intractable vomiting with nausea_ unspecified vomiting type",
        "Nonspecific (abnormal) findings on radiological and other examination of abdominal area_ including retroperitoneum",
        "Nonspecific (abnormal) findings on radiological and other examination of genitourinary organs",
        "Nonspecific abnormal electrocardiogram (ECG) (EKG)",
        "ONDANSETRON HCL (PF) 4 MG/2 ML INJECTION SOLUTION",
        "ONDANSETRON HCL 2 MG/ML INTRAVENOUS SOLUTION", "ONDANSETRON HCL 4 MG TABLE",
        "ONDANSETRON HCL 4 MG/5 ML ORAL SOLUTION", "ONDANSETRON HCL 8 MG TABLE", "OSA (obstructive sleep apnea)",
        "OXYCODONE 10 MG TABLE", "OXYCODONE 15 MG TABLE", "OXYCODONE 30 MG TABLE", "OXYCODONE 5 MG CAPSUL",
        "OXYCODONE 5 MG TABLE", "OXYCODONE 5 MG/5 ML ORAL SOLUTION",
        "OXYCODONE ER 10 MG TABLET_CRUSH RESISTANT_EXTENDED RELEASE 12 HR",
        "OXYCODONE ER 10 MG TABLET_EXTENDED RELEASE_12 HR",
        "OXYCODONE ER 20 MG TABLET_CRUSH RESISTANT_EXTENDED RELEASE 12 HR", "OXYCODONE SCREEN_ URIN",
        "OXYCODONE_ACETAMINOPHEN 10 MG_325 MG TABLE", "OXYCODONE_ACETAMINOPHEN 5 MG_325 MG TABLE",
        "Obstructive sleep apnea", "Obstructive sleep apnea (adult) (pediatric)", "Other sleep disorders",
        "PINEAL HORMONE AGENTS", "Paresthesia", "Paresthesia of skin", "Procedures on the stomach", "RADIOLOGY",
        "RADIOLOGY OUTSIDE IMAGES_ OFFICIAL REA", "Recurrent abdominal pain", "Relapsing Fever",
        "Respiratory Depression", "Restlessness", "Right sided abdominal pain", "SURGICAL PATHOLOGY",
        "Scoliosis (and kyphoscoliosis)_ idiopathic", "Seizure disorder (CMS code)", "Seizures", "Seizures (CMS code)",
        "Serum sodium measurement", "Sinus Tachycardia", "Surgical pathology procedure", "Sweating", "Symptom severe",
        "TEMPORARY TRACHEOSTOMY", "Tachycardia", "Tachycardia_ unspecified", "Tremor", "US ABDOMEN COMPLETE (RADIOLOGY PERFORMED)",
        "US ABDOMEN COMPLETE WITH DOPPLER (RADIOLOGY PERFORMED)", "Unspecified abdominal pain",
        "Unspecified severe protein_calorie malnutrition (CMS code)",    "Upper abdominal pain", "abdominal discomfort", "abdominal pain", "abdominal swelling", "antibiotics",
        "busulfan", "dilaudid", "docusate", "docusate sodium", "duloxetine", "ferrous sulfate", "gram stain",
        "hydromorphone", "magnesium", "magnesium oxide", "magnesium sulfate", "melatonin", "morphine sulfate",
        "nausea", "nausea and vomiting", "no vomiting", "normal sleep and appetite", "ondansetron", "oxycodone",
        "penicillins", "polyethylene glycol", "polyethylene glycols", "program", "propranolol", "rubs", "severe",
        "severe abdominal pain", "severe pain", "severely", "sleep", "sleeping", "sleepy", "sodium", "sodium cation",
        "sodium chloride", "sonogram", "stomach", "sulfate", "vomiting", "Age", "Male", "Female",
        "ACETAMINOPHEN 10 MG/ML IV (ADULT)", "ACETAMINOPHEN 10 MG/ML IV (PEDI)", "ACETAMINOPHEN 160 MG/5 ML (5 ML) ORAL SUSPENSION",
        "ACETAMINOPHEN 160 MG/5 ML ORAL LIQUI", "ACETAMINOPHEN 1_000 MG/100 ML (10 MG/ML) INTRAVENOUS SOLUTION",
        "ACETAMINOPHEN 300 MG_CODEINE 30 MG TABLE", "ACETAMINOPHEN 325 MG TABLE", "ACETAMINOPHEN 325 MG/10.15 ML ORAL SOLUTION",
        "ACETAMINOPHEN 500 MG GELCA", "ACETAMINOPHEN 500 MG TABLE", "ACETAMINOPHEN 650 MG RECTAL SUPPOSITORY",
        "ACETAMINOPHEN 650 MG/20.3 ML ORAL SOLUTION", "ACETAMINOPHEN 80 MG CHEWABLE TABLE", "ACETAMINOPHEN ADULT 2 G DAILY MAXIMU",
        "ACETAMINOPHEN ADULT 4 G DAILY MAXIMU", "ACETAMINOPHEN CUSTOM ADULT DAILY MAXIMU", "ACETAMINOPHEN LEV",
        "ACETAMINOPHEN STANDARD PEDIATRIC DAILY MAXIMU", "ANALGESIC/ANTIPYRETICS_ SALICYLATES",
        "ANALGESIC/ANTIPYRETICS_NON_SALICYLA", "ANALGESICS", "ANALGESICS_ NON_OPIOI", "ANALGESIC_NON_SALICYLATE_BARBITURATE_XANTHINE COMB",
        "ANTIHYPERTENSIVES_ ACE INHIBITORS", "ANTIHYPERTENSIVES_ ANGIOTENSIN RECEPTOR ANTAGONIS",
        "ANTIHYPERTENSIVES_ SYMPATHOLYTI", "ANTIHYPERTENSIVES_ VASODILATORS", "ANTI_ANXIETY DRUGS", "ANTI_ANXIETY _ BENZODIAZEPINES",
        "Acetaminophen", "Aggressive behavior", "Agitation", "Alanine transaminase", "Analgesics", "Atelectasis", "BACK PAIN",
        "CALCIUM 600 + D(3) ORAL", "CALCIUM ACETATE(PHOSPHATE BINDERS) 667 MG CAPSUL",
        "CALCIUM CARBONATE 200 MG CALCIUM (500 MG) CHEWABLE TABLE", "CALCIUM CARBONATE 500 MG (1_250 MG)_VITAMIN D3 200 UNIT TABLE",
        "CALCIUM CARBONATE 500 MG CALCIUM (1_250 MG) TABLE", "CALCIUM CHANNEL BLOCKING AGENTS",
        "CALCIUM CHLORIDE 100 MG/ML (10 %) INTRAVENOUS SOLUTION", "CALCIUM CHLORIDE 100 MG/ML (10 %) INTRAVENOUS SYRING",
        "CALCIUM CITRATE 315 MG CALCIUM_VITAMIN D3 6.25 MCG (250 UNIT) TABLE", "CALCIUM CITRATE ORAL",
        "CALCIUM GLUCONATE 1 GRAM/50 ML IN DEXTROSE 5% IV", "CALCIUM GLUCONATE IVPB 1 GRAM (MINI_BAG PLUS)", "CALCIUM ORAL",
        "CALCIUM _ EXTERNA", "CLONAZEPAM 0.5 MG TABLE", "CLONAZEPAM 1 MG TABLE", "Calcium _ External", "Calcium oxalate crystals",
        "Chills (without fever)", "Chronic pain", "Chronic pain associated with significant psychosocial dysfunction",
        "Chronic pain disorder", "Chronic pain due to trauma", "Chronic pain syndrome", "Chronic pelvic pain in female", "DIARRHEA",
        "DIZZINESS", "DULOXETINE 20 MG CAPSULE_DELAYED RELEAS", "DULOXETINE 30 MG CAPSULE_DELAYED RELEAS",
        "DULOXETINE 60 MG CAPSULE_DELAYED RELEAS", "Depressed mood", "Depressive disorder", "Depressive disorder_ not elsewhere classified",
        "Diastolic B", "Dizziness", "Dizziness and giddiness", "Dysarthria", "Dysarthria and anarthria", "Dyspepsia", "Dysplasia",
        "EPIGASTRIC PAIN", "Edema_ unspecified", "Eosinophil Abs Count _ External", "Eosinophil Abs Ct", "Epigastric pain",
        "FATIGU", "FERRITIN", "FEV", "Fatigue", "Fatigue_ unspecified type", "Febrile convulsions (simple)_ unspecified",
        "Ferritin", "Generalized aches and pains", "Generalized anxiety disorder", "Hernia", "Hypertensive disease",
        "MAGNESIUM OXIDE 400 MG (241.3 MG MAGNESIUM) TABLE", "Major Depressive Disorder",
        "Major depressive disorder_ recurrent episode_ unspecified", "Major depressive disorder_ recurrent_ unspecified (CMS code)",
        "Major depressive disorder_ single episode_ unspecified", "Mental Orientation", "Mental Status", "Mental disorders",
        "Mental disorders of mother_ antepartum", "Mental state", "Morbid obesity (CMS code)", "NAUSEA",
        "ONDANSETRON 4 MG DISINTEGRATING TABLE", "ONDANSETRON 8 MG DISINTEGRATING TABLE", "OPIOID ANALGESIC AND NON_SALICYLATE ANALGESICS",
        "OPIOID ANALGESICS", "OPIOID ANALGESIC_ ANESTHETIC ADJUNCT AGENTS", "OPIOID ANTAGONISTS",
        "OPIOID ANTITUSSIVE_EXPECTORANT COMBINATION", "OPIOID WITHDRAWAL THERAPY AGENTS_ OPIOID_TY", "Opioid", "Opioid withdrawal",
        "Opioids", "Other chronic pain", "Other fatigue", "Other specified hypotension", "PAIN _ CHRONIC SV",
        "Pain and tenderness", "SLEEP DISORDER MZ", "Sleep Apnea Syndromes", "Sleeplessness", "VANCOMYCIN 1 G IVPB (VIAL_MATE)",
        "VANCOMYCIN 1250 MG/300 ML D5W IVPB (PREMIX)", "VANCOMYCIN 1500 MG/305 ML D5W IVPB (PREMIX)", "VANCOMYCIN 50 MG/ML ORAL SOLN",
        "VANCOMYCIN 750 MG IVPB (VIAL_MATE)", "VANCOMYCIN ANTIBIOTICS AND DERIVATIVES", "VANCOMYCIN LEV", "Vancomycin", "acetaminophen",
        "analgesia", "bloating", "calcium ion", "depression", "drowsy", "fatigued", "fevers", "insomnia", "mental status"
]

json_directory = '/Users/ariasarch/Downloads/synthea_sample_data_fhir_latest'

# List all JSON files in the directory
json_files = [f for f in os.listdir(json_directory) if f.endswith('.json')]

# Dictionary to store the count of each string in each file
count_dict = {}
len_check = len(check)
len_json = len(json_files)

for i, json_file_name in enumerate(json_files):
    print(f'On file {i} of {len_json}')

    # Create the full path to the JSON file
    json_file_path = os.path.join(json_directory, json_file_name)

    # Open the JSON file for reading
    with open(json_file_path, 'r') as json_file:
        # Parse the JSON data into a Python dictionary
        data = json.load(json_file)

    # Format data
    formatted_data = json.dumps(data, indent=2)

    # Initialize count for this file
    count_dict[json_file_name] = {}

    # Check and count each string in 'check'
    for j, string in enumerate(check):
        count = formatted_data.count(string)
        count_dict[json_file_name][string] = count

df = pd.DataFrame.from_dict(count_dict, orient='index')
excel_filename = 'output.xlsx'

# Export the DataFrame to an Excel file
df.to_excel(excel_filename, engine='openpyxl')

print(f"DataFrame exported as '{excel_filename}'")