import numpy as np
import sympy as sp

class ForwardKinematicsDH:
    @staticmethod
    def dh_transform(theta, d, a, alpha):
        """
        Compute the individual DH transformation matrix (numeric).
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

    @staticmethod
    def dh_transform_symbolic(theta, d, a, alpha):
        """
        Compute the individual DH transformation matrix (symbolic).
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

    @staticmethod
    def numeric(dh_params):
        """
        Compute the forward kinematics numerically.
        """
        H = np.eye(4)
        for params in dh_params:
            H = H @ ForwardKinematicsDH.dh_transform(*params)
        return H

    @staticmethod
    def symbolic(dh_params):
        """
        Compute the forward kinematics symbolically.
        """
        H = sp.eye(4)
        for params in dh_params:
            H = H * ForwardKinematicsDH.dh_transform_symbolic(*params)
        return sp.simplify(H)
