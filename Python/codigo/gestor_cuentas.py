import pandas as pd
from .cuenta import Cuenta
from .visualizador import histograma_saldos, exportar_png_a_pdf
from .utils import limpiar_saldo
from .logger import log


class GestorCuentas:
    """Clase para gestionar cuentas bancarias y sus indicadores."""
    def __init__(self):
        self.cuentas: list[Cuenta] = []
        self.uvr = None
        self.reportables: list[Cuenta] = []

    def cargar_desde_csv(self, archivo_csv):
        """Carga las cuentas desde un archivo CSV y las almacena en la lista de cuentas.
        
        Args:
            archivo_csv (str): Ruta al archivo CSV que contiene los datos de las cuentas.
        """
        try:
            df = pd.read_csv(archivo_csv)  # Carga el CSV
            for _, fila in df.iterrows():
                fila = fila.to_dict()  # Convierte la fila a un diccionario
                fila["saldo_actual"] = limpiar_saldo(
                    fila["saldo_actual"]
                )  # Limpia el saldo
                c = Cuenta(fila)
                self.cuentas.append(c)
            log.info(f"Datos cargados desde {archivo_csv} con éxito.")
            log.debug(f"Total de cuentas cargadas: {len(self.cuentas)}")
        except Exception as e:
            log.error(f"Error cargando datos desde CSV: {e}")
            raise

    def cargar_uvr(self, archivo_uvr):
        """Carga el valor de la UVR desde un archivo CSV.

        Args:
            archivo_uvr (str): Ruta al archivo CSV que contiene el valor de la UVR.
        """
        try:
            df_uvr = pd.read_csv(archivo_uvr)
            valor = float(df_uvr.loc[0, "valor_uvr"])
            self.uvr = valor
            log.info(f"Valor UVR cargado: {self.uvr}")
        except Exception as e:
            log.error(f"Error cargando valor UVR: {e}")
            raise

    def calcular_indicadores(self):
        """Calcula los indicadores de cada cuenta, como días de inactividad y saldo en UVR."""
        try:
            for cuenta in self.cuentas:
                cuenta.calcular_dias_inactividad()
                cuenta.calcular_saldo_en_uvr(self.uvr)
            log.info("Indicadores calculados para todas las cuentas.")
            log.debug(f"Total de cuentas procesadas: {len(self.cuentas)}")
        except Exception as e:
            log.error(f"Error calculando indicadores: {e}")
            raise

    def filtrar_reportables(self, dias=365, uvr=322):
        """Filtra las cuentas reportables según los criterios de días 
        de inactividad y saldo en UVR.

        Args:
            dias (int): Número de días de inactividad para considerar reportable.
                default es 365.
            uvr (float): Umbral de saldo en UVR para considerar reportable.
                default es 322.
        """
        try:
            for cuenta in self.cuentas:
                if cuenta.es_reportable(dias, uvr):
                    self.reportables.append(cuenta)
            log.info(
                f"Cuentas reportables filtradas con éxito. Umbral: {dias} días, {uvr} UVR."
            )
            log.debug(f"Total de cuentas reportables: {len(self.reportables)}")
        except Exception as e:
            log.error(f"Error filtrando cuentas reportables: {e}")
            raise

    def exportar_csv(self, archivo_salida):
        """Exporta las cuentas reportables a un archivo CSV.

        Args:
            archivo_salida (str): Ruta al archivo CSV donde se guardarán las cuentas reportables.
        """
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
            raise

    def generar_histograma_saldos(self, ruta_histograma, ruta_pdf):
        """Genera un histograma de los saldos en UVR y lo exporta a PNG y PDF.
        
        Args:
            ruta_histograma (str): Ruta donde se guardará el histograma en formato PNG.
            ruta_pdf (str): Ruta donde se guardará el histograma en formato PDF.
        """
        try:
            histograma_saldos(self.cuentas, ruta_histograma)
            exportar_png_a_pdf(ruta_histograma, ruta_pdf)
            log.info(f"Histograma de saldos generado correctamente -png y pdf-.")
        except Exception as e:
            log.error(f"Error generando histograma de saldos: {e}")
            raise
            