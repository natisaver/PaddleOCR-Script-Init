import os
import sys
import glob
import json

# change to directory of the script
os.chdir(sys.path[0])

# image file types allowed
endings = ['.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif']

# if labels.txt file doesnt exist create it, otherwise open it
with open('labels.txt', 'w') as f:
    # iterates JSON files 
    for i in glob.glob('*.json'):
        # Retrieve 'image_Name'
        file_Name = os.path.splitext(i)[0]
        for ends in endings:
            if glob.glob(file_Name+ends):
                image_Name = file_Name + ends
        # Open the JSON and edit key-value
        names_key = {'text': 'transcription', 'box': 'points'}
        with open(i, "r") as g:
            data = json.load(g)
            templist = []
            tempdict = {'transcription': '', 'points': '', 'difficult': False}
            for row in data:
                for old_name in row:
                    if old_name == 'text':
                        tempdict['transcription'] = row[old_name]
                    elif old_name == 'box':
                        x1, y1, x2, y2 = row[old_name]
                        tempdict['points'] = [[x1, y1], [x1, y2], [x2, y2], [x2, y1]]
                templist.append(tempdict)
        # print(templist)
        # Convert the list to a JSON object and write to text file
        jsonString = json.dumps(templist)
        f.write(image_Name + '\t' + jsonString + '\n')
