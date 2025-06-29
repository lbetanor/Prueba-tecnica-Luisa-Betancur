import os

from codigo.gestor_cuentas import GestorCuentas


if __name__ == "__main__":
    # Crear un objeto de la clase GestorCuentas
    gc = GestorCuentas()

    # Definir las rutas de los archivos
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    ruta_data = os.path.join(ruta_base, "data", "mock_data.csv")
    ruta_uvr = os.path.join(ruta_base, "data", "UVR.csv")
    ruta_csv = os.path.join(ruta_base, "output", "cuentas_reportables.csv")
    ruta_histograma = os.path.join(ruta_base, "output", "hist_saldos.png")
    ruta_pdf = os.path.join(ruta_base, "output", "hist_saldos.pdf")

    # Ejecutar los métodos de la clase GestorCuentas
    gc.cargar_desde_csv(ruta_data)
    gc.cargar_uvr(ruta_uvr)
    gc.calcular_indicadores()
    gc.filtrar_reportables()
    gc.exportar_csv(ruta_csv)
    gc.generar_histograma_saldos(ruta_histograma, ruta_pdf)
