from fastapi import FastAPI
import numpy as np
import uvicorn

app = FastAPI(
    title="Clouds API",
    description="Clouds course REST API",
)

def numerically_integrate(f, a, b):
    """ Integrates a given fn

    Args:
        f (fn): function to be evaluated.
        a (float): lower bound.
        b (float): upper bound.

    Returns:
        y (float): numerical approximenation of the given function
    """
    return (b-a)*np.mean(f)

@app.get("/")
async def get_integral_approximation(lower_bound: float, upper_bound: float):
    """ Returns numerical integral approximatios for 7 different scales of intervals
    for the fn, f(x) = abs(sin(x))

    Args:
        a (float): lower bound.
        b (float): upper bound.

    Returns:
        y (arra<float>): Numerical approximations
    """
    intervals = [10**i for i in range(1, 8)]
    approximations = []

    for interval in intervals:
        step_size = (upper_bound - lower_bound) / interval
        x_range = np.arange(lower_bound, upper_bound + step_size, step_size)
        fx = np.abs(np.sin(x_range))
        result = numerically_integrate(fx, lower_bound, upper_bound)
        approximations.append(result)

    return {"result": approximations}

if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=8000)