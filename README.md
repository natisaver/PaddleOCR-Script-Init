# PaddleOCR-Script-Init
initialisation script for paddleocr model

### Where to put the scripts?
- *First locate your data directory containing annotated groundtruths with JSON files*
- e.g location: `C:\Users\username\xtract\project\data\your_data_dir\labels.py` or `C:\Users\username\gt`
- Place the script e.g `labels.py` into that same directory, with your e.g `image000.json` and `image000.jpg`
- Run the script to generate the relevant text file, e.g `Label.txt` file with the configurations

### What is the script `labels.py`?
- This script generates a summary of groundtruth information on each image, when we are doing end-to-end evaluation.
- This script generates a Label.txt file which is then used when we run the PaddleOCR Model for generating evaluation metrics of our model on the groundtruth data
- The Label.txt summarises all the json information of all the bounding boxes contained within an image, with its textual information, coordinates of box etc.
  - This script must be run before `C:\Users\username\xtract\tests\evaluation_tests\ocr_model_evaluation\test_ocr_model_evaluation.py` is runned.

### What is the script `trainData.py`?
- This script is used when we are trying to train an inference model.
- The first part of the script separates 2 folders, one for training data and one for validation data
- in a 70% to 30% split respectively, it then crops all full sized images by each of the bounding boxes and places the set into one of the folders
- The respect .txt files are also updated with the new cropped image name and textual information.
  - The path of these generated folders must be configured at `C:\Users\username\xtract\project\config\en_PP-OCRv3_rec.yml`.
  - This script must be run before `C:\Users\username\xtract\train.sh` is runned.

### What is the script `copyimagetextract.bat`?
- This script shifts files according to a list of files in a designated .txt file:
```text
image_000.jpg
image_001.jpg
```
- You have to indicate the source of the text file, followed by the from and to directories.
