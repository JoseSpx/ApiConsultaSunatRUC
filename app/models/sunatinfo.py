class SunatInfo:
    def __init__(self):
        self.ruc = ''
        self.razon_social = ''
        self.tipo_contribuyente = ''
        self.nombre_comercial = ''
        self.fecha_inscripcion = ''
        self.estado_contibuyente = ''
        self.condicion_contribuyente = ''
        self.domicilio_fiscal = ''
        self.actividad_economica = ''

    def serialize(self):
        return {
            'ruc': self.ruc,
            'razon_social': self.razon_social,
            'tipo_contribuyente': self.tipo_contribuyente,
            'nombre_comercial': self.nombre_comercial,
            'fecha_inscripcion': self.fecha_inscripcion,
            'estado_contibuyente': self.estado_contibuyente,
            'condicion_contribuyente': self.condicion_contribuyente,
            'domicilio_fiscal': self.domicilio_fiscal,
            'actividad_economica': self.actividad_economica
        }

