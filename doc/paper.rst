
The chain collocation method: A spectrally accurate calculus of forms
=====================================================================

The figures below were used in the paper published here_.

.. _here: http://www.sciencedirect.com/science/article/pii/S0021999113005494

Figure 3
--------

Examples of periodic interpolators for :math:`N=6` (a) and :math:`7` (b), and
corresponding periodic histopolators (c) and (d), scaled by :math:`h=2\pi/N`
for clarity. While the interpolator :math:`\alpha_N` satisfies
:math:`\alpha_N(nh \mod 2\pi) = \delta_{0n} \; \forall n`, the histopolator
:math:`\beta_N` integrates to :math:`1` over the dual cell straddling
:math:`x=0`, and to :math:`0` over other dual cells in the range
:math:`[0,2\pi]`. Note that the alternating red and green colors are used to
mark out dual cells, and to illustrate that the integral of :math:`\beta_N`
over each of these dual cells sums to zero or one.

.. plot:: plot/cheb/plot_basis_fn.py

Figure 5
--------

Chebyshev primal basis functions for a grid with :math:`N=7`. We normalize the
one-form basis functions by :math:`x_n\!-\!x_{n-1}` to have approximately the
same scale in our visualizations.


.. plot:: plot/cheb/plot_basis_fn_chebyshev.py

Figure 6
--------
Chebyshev dual basis functions for a grid with :math:`N=7`.

.. plot:: plot/cheb/plot_basis_fn_chebyshev_dual.py


Figure 7
--------

Convergence graphs for a 1D Poisson equation: (a) we solve
:math:`\Delta f = e^{\sin x} (\cos^2 x - \sin x)` on a periodic domain for
either a primal, or dual :math:`0`-form :math:`f`; (b) we solve
math:`\Delta f = e^{x}` on a Chebyshev grid, for either a primal :math:`0`-form
with Dirichlet boundary conditions :math:`f(-1)=e^{-1}` and :math:`f(1)=e`, or
for a dual :math:`0`-form with Neumann boundary conditions
math:`f^\prime(-1)= e^{-1}` and :math:`f^\prime(+1)= e`. All of our results
exhibit spectral convergence (measured through the :math:`L^\infty` error
:math:`\|f - \Delta^{-1}q \|_\infty`), with the conventional plateau when we
reach the limit of accuracy of the representation of floating point numbers.

.. plot:: plot/cheb/poisson1d_periodic.py
.. plot:: plot/cheb/poisson1d_cheb.py

Figure 8
--------

Convergence graphs for a 2D Poisson equation; (a) we solve
:math:`\Delta f = e^{\sin x} (\cos^2 x - \sin x)+e^{\sin y} (\cos^2 y - \sin y)`
on a periodic domain for either a primal, or dual :math:`0`-form :math:`f`; (b)
Now for
:math:`\Delta f = e^{\sin x} (\cos^2 x - \sin x) \mathbf{d}x +e^{\sin y} (\cos^2 y - \sin y) \mathbf{d}y`;
(c) we solve :math:`\Delta f = e^{x}+e^{y}` on a Chebyshev grid, for either a
primal :math:`0`-form with Dirichlet boundary conditions
:math:`f(x,y)=e^{x}+e^{y}`, or for a dual :math:`0`-form with Neumann boundary
conditions :math:`\nabla f(x) \cdot \mathbf{n} = (e^x\;e^y)^t \;\mathbf{n}`;
(d) Now for :math:`\Delta f = e^{x} \mathbf{d}x+e^{y}\mathbf{d}y`. All of our
results exhibit spectral convergence (measured through the :math:`L^\infty`
error :math:`\|\Delta f - q \|_\infty`), with the conventional plateau in
accuracy for fine meshes.

.. plot:: plot/cheb/poisson2d_periodic.py
.. plot:: plot/cheb/poisson2d_cheb.py

Figure 9
--------

Plot for the solution of
:math:`(\star\mathbf{d}\star\mathbf{d}+\mathbf{d}\star\mathbf{d}\star)f\!=\!0`
with the boundary conditions of :math:`\star f |_{\mathcal{B}} = 0` (vector
field is tangent to the boundary) and
:math:`\star\mathbf{d}\star f |_{\mathcal{B}}\!=\!1` (the curl at the boundary
is equal to :math:`1`). The domain is :math:`[-1,1]^2`, discretized by a
:math:`10\!\times\!10` Chebyshev grid.


.. plot:: plot/cheb/poisson_2d_example.py
