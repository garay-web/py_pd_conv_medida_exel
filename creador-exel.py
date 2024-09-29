import pandas as pd

# Dataframe : es para la información básica con el nombre de 
# las piezas y centímetros para poder armar el Exel.-

data = {
    "piezas:": ["Pata", "Tablero", "Puerta", "Estante", "Panel lateral"],
    "Centímetros": [40, 120, 60, 30, 180]
}

df = pd.DataFrame(data)

# Guardar el Dataframe en un archivo Exel

df.to_excel("muebles_medidas.xlsx", index= False)