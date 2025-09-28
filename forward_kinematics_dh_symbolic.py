# --- Simbólico ---
import sympy as sp

def dh_transform_symbolic(theta, d, a, alpha):
    """
    Compute the individual DH transformation matrix symbolically.
    Args:
        theta, d, a, alpha: sympy symbols or expressions
    Returns:
        4x4 sympy Matrix
    """
    ct = sp.cos(theta)
    st = sp.sin(theta)
    ca = sp.cos(alpha)
    sa = sp.sin(alpha)
    return sp.Matrix([
        [ct, -st*ca,  st*sa, a*ct],
        [st,  ct*ca, -ct*sa, a*st],
        [0,     sa,     ca,    d],
        [0,      0,      0,    1]
    ])

def forward_kinematics_dh_symbolic(dh_params):
    """
    Compute the forward kinematics symbolically for a serial manipulator using DH parameters.
    Args:
        dh_params: List of [theta, d, a, alpha] (can be sympy symbols)
    Returns:
        4x4 sympy Matrix representing the final transformation
    """
    H = sp.eye(4)
    for params in dh_params:
        H = H * dh_transform_symbolic(*params)
    return sp.simplify(H)
