import numpy as np
from scipy.spatial.transform import Rotation as R

def quaternion_multiply(q1, q2):
    """İki kuaterniyonu (w, x, y, z) çarpar."""
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    return np.array([
        w1*w2 - x1*x2 - y1*y2 - z1*z2,
        w1*x2 + x1*w2 + y1*z2 - z1*y2,
        w1*y2 - x1*z2 + y1*w2 + z1*x2,
        w1*z2 + x1*y2 - y1*x2 + z1*w2
    ])

def create_quaternion_from_euler(roll, pitch, yaw):
    """Saf matematik kullanarak Euler'den [x, y, z, w] üretir."""
    # Dereceyi radyana çevir
    r, p, y = np.radians([roll, pitch, yaw])
    
    # Yarım açıların sinüs ve kosinüslerini hesapla
    cy = np.cos(y * 0.5)
    sy = np.sin(y * 0.5)
    cp = np.cos(p * 0.5)
    sp = np.sin(p * 0.5)
    cr = np.cos(r * 0.5)
    sr = np.sin(r * 0.5)

    # Kuaterniyon bileşenlerini oluştur
    w = cr * cp * cy + sr * sp * sy
    x = sr * cp * cy - cr * sp * sy
    y = cr * sp * cy + sr * cp * sy
    z = cr * cp * sy - sr * sp * cy

    return np.array([x, y, z, w])
    
def rotate_point_with_quaternion(point, quat_xyzw):
    """Bir noktayı Quaternion kullanarak döndürür (Sandwich Product)."""
    x, y, z, w = quat_xyzw
    q = np.array([w, x, y, z]) # w başa (hesaplama formatı)
    q_inv = np.array([w, -x, -y, -z]) # eşlenik (inverse)
    
    # Noktayı Pure Quaternion yap (w=0)
    p = np.array([0, point[0], point[1], point[2]])
    
    # P' = q * p * q_inv
    temp = quaternion_multiply(q, p)
    p_rotated_quat = quaternion_multiply(temp, q_inv)
    
    return p_rotated_quat[1:] # Sadece x, y, z kısmını döndür

def transform_point_quaternion(point, translation, quat_xyzw):
    """Noktayı önce döndürür sonra öteler."""
    rotated_p = rotate_point_with_quaternion(point, quat_xyzw)
    return rotated_p + np.array(translation)

# Görselleştirme için hala matrislere ihtiyacımız var (plot_scene için)
def get_matrix_from_quat_and_pos(pos, quat_xyzw):
    r = R.from_quat(quat_xyzw)
    T = np.eye(4)
    T[:3, :3] = r.as_matrix()
    T[:3, 3] = pos
    return T