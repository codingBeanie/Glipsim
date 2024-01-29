from django.shortcuts import render, HttpResponse, redirect
from simulation.probabilities import *
from simulation.sim_controller import *
from simulation.models import Statistics
import time


def index(request):
    statistics = Statistics.objects.all()
    context = {"statistics": statistics}
    return render(request, "stats.html", context)


def restart(request):
    start_time = time.time()
    simulation_restart()
    end_time = time.time()
    elapsed_time = end_time - start_time
    return redirect('index')


def run(request):
    start_time = time.time()
    simulation_run()
    end_time = time.time()
    elapsed_time = end_time - start_time
    return redirect('index')


def households(request):
    return render(request, "households.html")


def probabilities(request):
    data_survival = []
    data_reproduction = []
    data_evaluation_reproduction_age = []

    for age in range(0, 120):
        survival_rate = probability_surviving(age)
        reproduction_rate = probability_reproduction(age)

        data_survival.append([age, survival_rate])
        data_reproduction.append([age, reproduction_rate])

    for scale in range(0, 10):
        evaluation_reproduction_age = evaluation_reproduction(scale)
        data_evaluation_reproduction_age.append([
            scale, evaluation_reproduction_age])

    print(data_evaluation_reproduction_age)

    context = {"data_survival": data_survival,
               "data_reproduction": data_reproduction, "data_evaluation_reproduction_age": data_evaluation_reproduction_age}

    return render(request, "probabilities.html", context)
