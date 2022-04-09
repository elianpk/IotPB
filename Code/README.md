## Code
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
Code.
|   README.md
|
+---DataPrep
|       csv_file.csv
|       generator.py
|       preprocess.ipynb
|
\---Operationalization
    +---app
    |       aws.py
    |       main.py
    |       settings.py
    |       shadow_control.py
    |       shadow_view.js
    |
    \---certificates
        +---elian
        |       room.cert.pem
        |       room.private.key
        |       room.public.key
        |       root-CA.crt
        |
        \---shadow
                room.cert.pem
                room.private.key
                room.public.key
                root-CA.crt
```