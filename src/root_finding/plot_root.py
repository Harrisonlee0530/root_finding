"""
A module that provides visualization tools for root finding algorithms.
"""

# import numpy as np
# import matplotlib.pyplot as plt
from typing import Callable, Sequence
from root_finding.hybrid import hybrid
import numpy as np
import matplotlib.pyplot as plt


def plot_root(
    f: Callable[[float], float],
    dfdx: Callable[[float], float],
    xmin: float,
    xmax: float,
    tol1: float,
    tol2: float,
    max_iter1: int = 500, 
    max_iter2: int = 500, 
    npts: int = 1000,
    n: int = 50,
):
    r"""
    Plot a scalar function and visualize its roots using a hybrid
    bisection-Newton root-finding algorithm.

    This function computes the roots of a scalar function `f` within a
    given interval using the `hybrid` method and displays both the
    function and the detected roots on a 2D plot.

    Parameters
    ----------
    f : callable
        Scalar function to be plotted. Must accept a single scalar argument.
    dfdx : callable
        Derivative of `f`. Must accept a single scalar argument.
    xmin : float
        Lower bound of the plotting and root-search interval.
    xmax : float
        Upper bound of the plotting and root-search interval.
    tol1 : float
        Convergence tolerance passed to the bisection-based root search
        stage of the hybrid method. Must be strictly positive.
    tol2 : float
        Relative convergence tolerance passed to the Newton-Raphson
        refinement stage of the hybrid method. Must be strictly positive.
    max_iter1 : int, optional
        Maximum number of iterations allowed for the bisection-based
        root search. Default is 500.
    max_iter2 : int, optional
        Maximum number of iterations allowed for Newton's method.
        Default is 500.
    npts : int, optional
        Number of points used to discretize the interval ``[xmin, xmax]``
        for plotting the function. Default is 1000.
    n : int, optional
        Number of subintervals used by the bisection-based root search.
        Passed to the hybrid solver. Default is 50.

    Returns
    -------
    None
        This function produces a plot and does not return a value.

    See Also
    --------
    bisection_find_roots :
        Bisection-based method for detecting multiple candidate roots.
    newton1d :
        Newton-Raphson method for one-dimensional root finding.
    hybrid :
        Combined bisection and Newton-Raphson root-finding algorithm.

    Notes
    -----
    The function ``f(x)`` is plotted over the interval ``[xmin, xmax]``,
    along with the x-axis for reference. Roots detected by the hybrid
    algorithm are marked on the plot as points.

    The quality and completeness of the detected roots depend on the
    resolution of the bisection search and the convergence behavior of
    Newton's method.

    Examples
    --------
    >>> f = lambda x: x**2 - 4
    >>> df = lambda x: 2*x
    >>> plot_root(f, df, -3, 3, tol1=1e-6, tol2=1e-12)
    """
    
    roots = hybrid(f, dfdx, xmin, xmax, tol1, tol2, max_iter1, max_iter2, n)
    
    x = np.linspace(xmin, xmax, npts)
    f = np.vectorize(f)

    plt.plot(x, f(x), label="f(x)")
    for r in roots:
        plt.scatter(r, f(r), label="x = {}".format(r))
    plt.legend()
    plt.ylim(-1, 1)
    plt.show()

    return None