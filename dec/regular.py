from numpy import *
import dec.spectral as sp
import dec.common
from dec.helper import bunch

def make(cls, n, xmin=0, xmax=pi):

    assert xmax > xmin
    
    N = n
    pnts = linspace(xmin, xmax, num=n)
    lenx = abs(xmax - xmin)
    delta = diff(pnts)
    
    verts = pnts
    verts_dual = verts[:-1] + 0.5*delta
    
    edges = (pnts[:-1], pnts[1:])
    tmp = concatenate(([xmin], verts_dual, [xmax]))
    delta_dual = diff(tmp)
    edges_dual = (tmp[:-1], tmp[1:])

    N = {(0, True)  : n, 
         (1, True)  : n-1,
         (0, False) : n-1,
         (1, False) : n}

    Delta = {True  : delta,
             False : delta_dual}
    
    cells = {(0, True)  : verts, 
             (1, True)  : edges,
             (0, False) : verts_dual,
             (1, False) : edges_dual,}

    B={(0, True)  : lambda i: lambda x: sp.kappa0(n, i, x), 
       (1, True)  : lambda i: lambda x: sp.kappa1_symm(n, i, x),
       (0, False) : lambda i: lambda x: sp.kappad0(n, i, x),
       (1, False) : lambda i: lambda x: sp.kappad1_symm(n, i, x),}

    D={(0, True)  : lambda f: diff(f), 
       (1, True)  : lambda f: 0,
       (0, False) : lambda f: diff(concatenate(([0], f, [0]))),
       (1, False) : lambda f: 0,}
    
    H={(0, True)  : H0_regular, 
       (1, True)  : H1_regular,
       (0, False) : H0d_regular,
       (1, False) : H1d_regular,}

    refine=dec.common.wrap_refine(to_refine, from_refine)
   
    return cls(n=n,
               xmin=xmin, 
               xmax=xmax,
               delta=Delta,
               N=N,
               cells=cells,
               dec=bunch(P=dec.common.projection(cells),
                         B=B,
                         D=D,
                         H=H,
                         W=None,
                         C=None),
             refine=refine)

def to_refine():
    def T0(f):
        raise NotImplementedError
    def T0d(f):
        raise NotImplementedError
    def T1(f):
        raise NotImplementedError
    def T1d(f):
        raise NotImplementedError
    return T0, T1, T0d, T1d


def from_refine():
    def U0(f):
        raise NotImplementedError
    def U0d(f):
        raise NotImplementedError
    def U1(f):
        raise NotImplementedError
    def U1d(f):
        raise NotImplementedError
    return U0, U1, U0d, U1d
    
def H1d_regular(f):
    r'''

    .. math::
        \widetilde{\mathbf{H}}^{1}=
            \mathbf{M}_{1}^{\dagger}
            {\mathbf{I}^{-\frac{h}{2},\frac{h}{2}}}^{-1}
            \mathbf{M}_{1}^{+}
            \mathbf{A}^{-1}
    '''
    f = f/sp.A_diag(f.shape[0])
    f = sp.mirror0(f, +1)
    N = f.shape[0]; h = 2*pi/N
    f = sp.I_space_inv(-h/2, +h/2)(f)
    f = sp.unmirror0(f)
    return f

def H0_regular(f):
    r'''

    .. math::
        \mathbf{H}^{0}=
            \mathbf{A}
            \mathbf{M}_{0}^{\dagger}
            \mathbf{I}^{-\frac{h}{2},\frac{h}{2}}
            \mathbf{M}_{0}^{+}
    '''
    f = sp.mirror0(f, +1)
    N = f.shape[0]; h = 2*pi/N
    f = sp.I_space(-h/2, h/2)(f)
    f = sp.unmirror0(f)
    f = f*sp.A_diag(f.shape[0])
    return  f

def H1_regular(f):
    r'''

    .. math::
        \mathbf{H}^{1}=
            \mathbf{M}_{1}^{\dagger}
            {\mathbf{I}^{-\frac{h}{2},\frac{h}{2}}}^{-1}
            \mathbf{M}_{1}^{+}
    '''
    f = sp.mirror1(f, +1)
    N = f.shape[0]; h = 2*pi/N
    f = sp.I_space_inv(-h/2, h/2)(f)
    f = sp.unmirror1(f)
    return f

def H0d_regular(f):
    r'''

    .. math::
        \widetilde{\mathbf{H}}^{0}=
            \mathbf{M}_{1}^{\dagger}
            \mathbf{I}^{-\frac{h}{2},\frac{h}{2}}
            \mathbf{M}_{1}^{+}
    '''
    f = sp.mirror1(f, +1)
    N = f.shape[0]; h = 2*pi/N
    f = sp.I_space(-h/2, h/2)(f)
    f = sp.unmirror1(f)
    return f
