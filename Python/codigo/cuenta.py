from datetime import datetime
from logger import log


class Cuenta:
    def __init__(self, fila):
        try:
            if not str(fila["número_cuenta"]).isdigit():
                raise ValueError(f"Número de cuenta inválido: {fila['número_cuenta']}")

            self.numero_cuenta = str(fila["número_cuenta"])
            self.tipo_cuenta = fila["tipo_cuenta"]
            self.saldo_actual = fila["saldo_actual"]
            self.fecha_ultimo_movimiento = fila["fecha_ultimo_movimiento"]

            self.dias_inactividad = None
            self.saldo_en_uvr = None
        
        except Exception as e:
            log.error(f"Error al crear cuenta: {e}")
            raise ValueError(f"Error al crear cuenta: {fila}")

    def calcular_dias_inactividad(self):
        try:
            fecha_ult_mov = datetime.strptime(self.fecha_ultimo_movimiento, "%d/%m/%Y").date()
            hoy = datetime.today().date()
            self.dias_inactividad = (hoy - fecha_ult_mov).days
        except Exception as e:
            raise ValueError(f"Error al calcular días de inactividad: {e}")

    def calcular_saldo_en_uvr(self, uvr):
        try:
            self.saldo_en_uvr = self.saldo_actual / uvr
        except Exception as e:
            log.error(f"Error al calcular saldo en UVR: {e}")
            raise ValueError(f"Error al calcular saldo en UVR: {e}")

    def es_reportable(self, dias, uvr):
        return (
            self.dias_inactividad is not None and
            self.saldo_en_uvr is not None and
            (self.dias_inactividad > dias and self.saldo_en_uvr < uvr)
        )