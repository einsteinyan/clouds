from flask import Flask, request, render_template
import numpy as np
app = Flask(__name__)

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

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route("/integral", methods=['GET'])
def get_integral_approximation():
    """ Returns numerical integral approximatios for 7 different scales of intervals
    for the fn, f(x) = abs(sin(x))

    Args:
        a (float): lower bound.
        b (float): upper bound.

    Returns:
        y (arra<float>): Numerical approximations
    """
    lower_bound = request.args.get('lower_bound',  type = float, default= 0)
    upper_bound = request.args.get('upper_bound',  type = float, default= 3.14)

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
   app.run()