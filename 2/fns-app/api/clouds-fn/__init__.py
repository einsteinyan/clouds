import logging
import numpy as np
import azure.functions as func

def numerically_integrate(f, a, b):
    return (b-a)*np.mean(f)


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    lower_bound = req.params.get('lower_bound')
    upper_bound = req.params.get('upper_bound')

    intervals = [10**i for i in range(1, 8)]
    approximations = []

    if not lower_bound:
        lower_bound = 0
    
    if not upper_bound:
        upper_bound = 3.14

    for interval in intervals:
        step_size = (upper_bound - lower_bound) / interval
        x_range = np.arange(lower_bound, upper_bound + step_size, step_size)
        fx = np.abs(np.sin(x_range))
        result = numerically_integrate(fx, lower_bound, upper_bound)
        approximations.append(result)

    return func.HttpResponse(str(approximations))