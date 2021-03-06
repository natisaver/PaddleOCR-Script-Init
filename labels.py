import os
import sys
import glob
import json

# change to directory of the script
os.chdir(sys.path[0])

# image file types allowed
endings = ['.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif']

# if labels.txt file doesnt exist create it, otherwise open it
with open('Label.txt', 'w') as f:
    # iterate through each JSON file in directory
    for i in glob.glob('*.json'):
        # Retrieve full 'image_Name' and extension
        file_Name = os.path.splitext(i)[0]
        for ends in endings:
            if glob.glob(file_Name+ends):
                image_Name = file_Name + ends
        # Open the JSON and edit key-value pairs
            # each templist is for one image
            # each tempdict is for one label/row in the image
            #to change key names from {'text': 'transcription', 'box': 'points'}
        with open(i, "r") as g:
            data = json.load(g)
            templist = []
            
            for row in data:
                tempdict = {'transcription': '', 'points': '', 'difficult': False}
                tempdict['transcription'] = row['text']
                x1, y1, x2, y2 = row['box']
                tempdict['points'] = [[x1, y1], [x1, y2], [x2, y2], [x2, y1]]
                templist.append(tempdict)
        # print(templist)
        # Convert the list to a JSON object and write to text file
        jsonString = json.dumps(templist)
        f.write(image_Name + '\t' + jsonString + '\n')
