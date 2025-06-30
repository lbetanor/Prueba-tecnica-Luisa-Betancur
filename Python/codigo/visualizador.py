import matplotlib.pyplot as plt
import os
from fpdf import FPDF
from .logger import log


def histograma_saldos(cuentas, ruta_histograma):
    """Genera un histograma de los saldos en UVR de las cuentas.

    Args:
        cuentas (list): Lista de objetos Cuenta.
        ruta_histograma (str): Ruta donde se guardará el histograma en formato PNG.
    """
    try:
        saldos = []
        for c in cuentas:
            if c.saldo_en_uvr is not None:
                saldos.append(c.saldo_en_uvr)

        plt.figure(figsize=(10, 6))
        plt.hist(saldos, bins=30, color="skyblue", edgecolor="black")
        plt.title("Distribución de saldos en UVR")
        plt.xlabel("Saldo_UVR")
        plt.ylabel("Frecuencia")
        plt.grid(True)

        os.makedirs(os.path.dirname(ruta_histograma), exist_ok=True)
        plt.savefig(ruta_histograma)
        plt.close()

    except Exception as e:
        log.error(f"Error generando histograma de saldos: {e}")
        raise


def exportar_png_a_pdf(ruta_png, ruta_pdf):
    """Exporta una imagen PNG a un archivo PDF.

    Args:
        ruta_png (str): Ruta de la imagen PNG que se va a exportar.
        ruta_pdf (str): Ruta donde se guardará el archivo PDF.
    """
    try:
        if not os.path.exists(ruta_png):
            raise FileNotFoundError(f"No se encontró la imagen en la ruta: {ruta_png}")

        pdf = FPDF()
        pdf.add_page()

        # Ajusta el tamaño si es necesario (aquí suponemos que la imagen cabe en la hoja)
        pdf.image(ruta_png, x=10, y=20, w=180)  # Puedes ajustar x, y, w

        pdf.output(ruta_pdf)
    except Exception as e:
        log.error(f"Error exportando PNG a PDF: {e}")
        raise
