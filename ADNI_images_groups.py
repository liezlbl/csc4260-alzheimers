import csv
import os
import shutil

# Task 1: Extract subject IDs from CSV and store them in a text file
def extract_ids_from_csv(csv_file, group, output_file):
    subject_ids = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Group'] == group:
                subject_ids.append(row['Subject'])

    with open(output_file, 'w') as outfile:
        for subject_id in subject_ids:
            outfile.write(subject_id + '\n')

# Task 2: Move folders based on IDs from the text file
def move_folders_by_ids(ids_file, source_dir, destination_dir):
    with open(ids_file, 'r') as file:
        for line in file:
            subject_id = line.strip()
            source_folder = os.path.join(source_dir, subject_id)
            if os.path.exists(source_folder):
                destination_folder = os.path.join(destination_dir, subject_id)
                shutil.move(source_folder, destination_folder)
                print(f"Moved folder '{subject_id}' to '{destination_folder}'.")

# move each subject ID folder to respective research group
groups = ['AD', 'CN', 'MCI']
source_directory = '/work/projects/csc4260-001-adni-2024s/lblaurel42/ADNI'
for group in groups:
    extract_ids_from_csv('ADNI1_Complete_3Yr_3T_3_25_2024.csv', group, f'{group.lower()}_subject_ids.txt')
    destination_directory = os.path.join('/work/projects/csc4260-001-adni-2024s/lblaurel42', group)  # path to group directory
    move_folders_by_ids(f'{group.lower()}_subject_ids.txt', source_directory, destination_directory)
