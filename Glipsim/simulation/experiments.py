import numpy as np
import plotly.express as px


def probability_tester(age, L=1, k=-0.1, a0=85):
    return (L / (1 + np.exp(-k * (age - a0))))


ages = np.arange(0, 120, 1)  # Altersbereich von 0 bis 60 Jahre
probabilities = probability_tester(ages)

px.line(x=ages, y=probabilities).show()

print(probabilities)
