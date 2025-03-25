
import pandas as pd

def calcular_medias(ruta): 
    df = pd.read_csv(ruta, sep=";")
    media = df["Edad"].mean()
    return media


if __name__ == "__main__":
    ruta = r"C:\Users\i.monsalve.rodilla\prueba_clase\data\hacer_media_datos.csv"
    media = calcular_medias(ruta)
    print(f"La media de mis alumn@s es: {media}")