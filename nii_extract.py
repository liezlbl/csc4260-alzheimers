import os
import shutil

groups = ['AD', 'CN', 'MCI']

for group in groups:
    os.chdir(group)
    for subj in os.listdir():
        if os.path.isdir(subj):
            for root, dirs, files in os.walk(subj):
                for file in files:
                    if file.endswith('.nii'):
                        src = os.path.join(root, file)
                        dst = os.path.join(subj, file)  # Keep the original file name
                        shutil.move(src, dst)
    os.chdir('..')
