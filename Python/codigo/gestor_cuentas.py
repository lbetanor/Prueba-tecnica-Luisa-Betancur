import pandas as pd
from cuenta import Cuenta
from visualizador import histograma_saldos, exportar_png_a_pdf
from utils import limpiar_saldo
from logger import log



class GestorCuentas:
    def __init__(self):
        self.cuentas: list[Cuenta] = []
        self.uvr = None
        self.reportables: list[Cuenta] = []

    def cargar_desde_csv(self, archivo_csv):
        try:
            df = pd.read_csv(archivo_csv) # Carga el CSV
            for _, fila in df.iterrows():
                fila = fila.to_dict()  # Convierte la fila a un diccionario
                fila["saldo_actual"] = limpiar_saldo(fila["saldo_actual"])  # Limpia el saldo
                c = Cuenta(fila)
                self.cuentas.append(c)
            log.info(f"Datos cargados desde {archivo_csv} con éxito.")
            log.debug(f"Total de cuentas cargadas: {len(self.cuentas)}")
        except Exception as e:
            log.error(f"Error cargando datos desde CSV: {e}")
            raise Exception(f"Error cargando datos desde CSV: {e}")
        
    
    def cargar_uvr(self, archivo_uvr):
        try:
            df_uvr = pd.read_csv(archivo_uvr)
            valor = float(df_uvr.loc[0, "valor_uvr"])
            self.uvr = valor
            log.info(f"Valor UVR cargado: {self.uvr}")
        except Exception as e:
            log.error(f"Error cargando valor UVR: {e}")
            raise Exception(f"Error cargando valor UVR: {e}")

    
    def calcular_indicadores(self):
        try:
            for cuenta in self.cuentas:
                cuenta.calcular_dias_inactividad()
                cuenta.calcular_saldo_en_uvr(self.uvr)
            log.info("Indicadores calculados para todas las cuentas.")
            log.debug(f"Total de cuentas procesadas: {len(self.cuentas)}")
        except Exception as e:
            log.error(f"Error calculando indicadores: {e}")
            raise Exception(f"Error calculando indicadores: {e}")

    def filtrar_reportables(self, dias=365, uvr=322): 
        try:
            for cuenta in self.cuentas:
                if cuenta.es_reportable(dias, uvr):
                    self.reportables.append(cuenta)
            log.info(f"Cuentas reportables filtradas con éxito. Umbral: {dias} días, {uvr} UVR.")
            log.debug(f"Total de cuentas reportables: {len(self.reportables)}")
        except Exception as e:
            log.error(f"Error filtrando cuentas reportables: {e}")
            raise Exception(f"Error filtrando cuentas reportables: {e}")    


    def exportar_csv(self, archivo_salida):
        try:
            # Extraer el numero de cuenta de cada cuenta reportable
            data = []
            for cuenta in self.reportables:
                data.append(cuenta.numero_cuenta)
            df = pd.DataFrame(data)
            df.to_csv(archivo_salida, index=False, header=["número_cuenta"])
            log.info(f"Cuentas reportables exportadas a {archivo_salida} con éxito.")
            log.debug(f"Total de cuentas exportadas: {len(self.reportables)}")
        except Exception as e:
            log.error(f"Error exportando CSV: {e}")
            raise Exception(f"Error exportando CSV: {e}")

    def generar_histograma_saldos(self, ruta_histograma, ruta_pdf):
        try:
            histograma_saldos(self.cuentas, ruta_histograma)
            exportar_png_a_pdf(ruta_histograma, ruta_pdf)
            log.info(f"Histograma de saldos generado correctamente -png y pdf-.")
        except Exception as e:
            log.error(f"Error generando histograma de saldos: {e}")
            raise Exception(f"Error generando histograma de saldos: {e}")



# Este código carga el archivo de cuentas y el archivo de UVR.
# Cada fila se convierte en un objeto Cuenta.
# Se calculan días de inactividad y saldo en UVR para cada cuenta.
# Se filtran las que cumplan ciertos umbrales.
# Se exportan esas cuentas a un nuevo CSV.

