"""
Utility functions for rotations
"""
import numpy as np
from scipy.spatial.transform import Rotation as R

def rotation_matrix_from_axis_angle(axis_angle: np.ndarray) -> np.ndarray:
    """
    Create a 3D rotation matrix from an axis-angle representation of a 3D rotation.
    """
    pass