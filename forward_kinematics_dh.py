import numpy as np

def dh_transform(theta, d, a, alpha):
    """
    Compute the individual DH transformation matrix.
    Args:
        theta: rotation angle (radians)
        d: offset along previous z to the common normal
        a: length of the common normal (distance along x)
        alpha: angle about common normal, from old z axis to new z axis
    Returns:
        4x4 numpy array representing the transformation matrix
    """
    ct = np.cos(theta)
    st = np.sin(theta)
    ca = np.cos(alpha)
    sa = np.sin(alpha)
    return np.array([
        [ct, -st*ca,  st*sa, a*ct],
        [st,  ct*ca, -ct*sa, a*st],
        [0,     sa,     ca,    d],
        [0,      0,      0,    1]
    ])

def forward_kinematics_dh(dh_params):
    """
    Compute the forward kinematics for a serial manipulator using DH parameters.
    Args:
        dh_params: List of [theta, d, a, alpha] for each joint
    Returns:
        4x4 numpy array representing the final transformation matrix
    """
    H = np.eye(4)
    for params in dh_params:
        H = H @ dh_transform(*params)
    return H
