"""
This is a module for testing the plot_root.py module
"""

import pytest
import numpy as np
import matplotlib.pyplot as plt
from root_finding.plot_root import plot_root


def test_plot():
    f = lambda x: x**3 - x
    df = lambda x: 3*x**2 - 1
    xmin, xmax = -2, 2
    tol1, tol2 = 1e-6, 1e-12

    fig, ax = plot_root(f, df, xmin, xmax, tol1, tol2)
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)


