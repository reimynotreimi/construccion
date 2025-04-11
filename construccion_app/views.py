
from django.db.models import Q  
from django.shortcuts import render, redirect
from .models import Persona
from .forms import PersonaForm

def agregar_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_persona')
    else:
        form = PersonaForm()
    return render(request, 'construccion_app/agregar_persona.html', {'form': form})

def lista_personas(request):
    query = request.GET.get('q', '').strip()  
    tarea_filter = request.GET.get('tarea', '')
    
    personas = Persona.objects.all()
    
    if query:
        query_parts = query.split()
        
        q_objects = Q(cedula__icontains=query)
        
        if len(query_parts) > 1:
            for i in range(len(query_parts)):
                for j in range(i+1, len(query_parts)):
                    q_objects |= (
                        Q(nombres__icontains=query_parts[i]) & 
                        Q(apellidos__icontains=query_parts[j])
                    ) | (
                        Q(nombres__icontains=query_parts[j]) & 
                        Q(apellidos__icontains=query_parts[i])
                    )
        
        for part in query_parts:
            q_objects |= (
                Q(nombres__icontains=part) |
                Q(apellidos__icontains=part)
            )
        
        personas = personas.filter(q_objects).distinct()
    
    if tarea_filter:
        personas = personas.filter(tarea=tarea_filter)
    
    tareas_choices = Persona.TAREAS_CHOICES
    
    return render(request, 'construccion_app/listas_personas.html', {
        'personas': personas,
        'query': query,
        'tarea_filter': tarea_filter,
        'tareas_choices': tareas_choices,
    })
