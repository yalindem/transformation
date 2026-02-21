import numpy as np

def create_full_transformation_matrix(x, y, z, roll_deg, pitch_deg, yaw_deg):
    r, p, y_angle = np.radians([roll_deg, pitch_deg, yaw_deg])
    
    Rx = np.array([[1, 0, 0], [0, np.cos(r), -np.sin(r)], [0, np.sin(r), np.cos(r)]])
    Ry = np.array([[np.cos(p), 0, np.sin(p)], [0, 1, 0], [-np.sin(p), 0, np.cos(p)]])
    Rz = np.array([[np.cos(y_angle), -np.sin(y_angle), 0], [np.sin(y_angle), np.cos(y_angle), 0], [0, 0, 1]])
    
    R = Rz @ Ry @ Rx
    T = np.eye(4)
    T[:3, :3] = R
    T[:3, 3] = [x, y, z]
    return T

def transform_point(T, point):
    p = np.array([*point, 1])
    return (T @ p)[:3]