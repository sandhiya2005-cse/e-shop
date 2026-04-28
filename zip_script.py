import os
import zipfile

with zipfile.ZipFile('ecom_project.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
    # Add files
    if os.path.exists('run.bat'):
        zipf.write('run.bat')
    if os.path.exists('__init__.py'):
        zipf.write('__init__.py')

    for d in ['backend', 'frontend']:
        for root, _, files in os.walk(d):
            if '__pycache__' in root: continue
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path)

print("Zip completed.")
