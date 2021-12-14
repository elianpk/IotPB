# IotPB
IoT Infnet Project

## Rodar o Projeto
``` cmd
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```
## Estrutura das pastas
``` cmd
IOTPB.
|   
|   
+---Code
|   |   README.md
|   |   
|   \---DataPrep
|       |   PreprocessamentoPB.ipynb
|       |
|       \---.ipynb_checkpoints
|               PreprocessamentoPB-checkpoint.ipynb
|
+---Data
|   |   README.md
|   |
|   +---Processed
|   |       japanese_room_temp_prepdata.csv
|   |
|   \---Raw
|           japanese_room_temp_rawdata.csv
|
\---Docs
        README.md
```