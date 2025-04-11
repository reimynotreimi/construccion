from django.db import models

class Persona(models.Model):
    TAREAS_CHOICES = [
        ('PREP', 'Preparación del terreno'),
        ('FUND', 'Fundaciones y cimentaciones'),
        ('ESTR', 'Estructura'),
        ('ALBA', 'Albañilería y acabados'),
        ('INST', 'Instalaciones: Eléctricas, Plomería, HVAC'),
        ('PINT', 'Pintura y decoración'),
        ('PAIS', 'Paisajismo y exteriores'),
        ('SUPE', 'Supervisión y control de calidad'),
    ]
    
    cedula = models.CharField(max_length=11, primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    tarea = models.CharField(
        max_length=4,
        choices=TAREAS_CHOICES,
        default='PREP',
        verbose_name='Tarea asignada'
    )

    def cedula_formateada(self):
        return f"{self.cedula[:3]}-{self.cedula[3:10]}-{self.cedula[10:]}"
    
    def get_tarea_display(self):
        return dict(self.TAREAS_CHOICES).get(self.tarea, '')