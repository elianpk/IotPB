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
|   .gitignore
|   package-lock.json
|   package.json
|   README.md
|   requirements.txt
|   TDSP
|   TDSP.png
|
+---Code
|   |   README.md
|   |
|   +---DataPrep
|   |       csv_file.csv
|   |       generator.py
|   |       preprocess.ipynb
|   |
|   \---Operationalization
|       +---app
|       |       aws.py
|       |       main.py
|       |       settings.py
|       |       shadow_control.py
|       |       shadow_view.js
|       |
|       \---certificates
|           +---elian
|           |       room.cert.pem
|           |       room.private.key
|           |       room.public.key
|           |       root-CA.crt
|           |
|           \---shadow
|                   room.cert.pem
|                   room.private.key
|                   room.public.key
|                   root-CA.crt
|
+---Data
|   |   README.md
|   |
|   +---Modeling
|   |       SensorData.csv
|   |
|   +---Processed
|   |       room_temp_prepdata.csv
|   |
|   \---Raw
|           room_temp_rawdata.csv
|
\---Docs
    |   README.md
    |
    +---DataReport
    |       data-dictionary.ipynb
    |
    \---Project
            Charter.ipynb
```