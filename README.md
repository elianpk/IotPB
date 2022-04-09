# Room Temperature IOT

## Dependencies
``` cmd
python -m venv venv
.\venv\Scripts\activate or source venv/bin/activate
pip install -r requirements.txt
npm install
```
## Run Notebooks
``` cmd
jupyter notebook
```
## Run Sensor linux
``` cmd
cd ./Code/Operationalization
python||python3 ./app/main
```

## Run device shadow view
``` cmd
cd ./Code/Operationalization
node ./app/shadow_view.js
```

## Control device shadow
``` cmd
cd ./Code/Operationalization
python ./app/shadow_control.py on
python ./app/shadow_control.py off
```

## Folder Structure 
``` cmd
room-temperature.
|   
|   
+---Code
|   |   README.md
|   |   
|   \---DataPrep
|       |   preprocess.ipynb
|       |
|       \---.ipynb_checkpoints
|               preprocess-checkpoint.ipynb
|
+---Data
|   |   README.md
|   |
|   +---Processed
|   |       room_temp_prepdata.csv
|   |
|   \---Raw
|           room_temp_rawdata.csv
|
\---Docs
        README.md
```