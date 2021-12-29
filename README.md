## Simple script to help convert Nimbus notes to Simplenote.

### How to convert notes from Nimbus to Simplenote?
1. Download nimbusnote_to_simplenote.py
2. In Nimbus Note, select the file tab and click Export all note.
3. Select HTML and click export.
4. Open the created folder, you should see a folder named "All Notes" in it.
5. Run the script with the command below, adding at the end an additional argument with the path to the "All Notes" folder
```
py nimbusnote_to_simplenote.py 'C:\YOUR_PATH\All Notes'
```
6. Notes.json file should appear in the folder where nimbusnote_to_simplenote.py is located
7. Run Simplenote, select the file tab and click Import Notes... and select the notes.json file