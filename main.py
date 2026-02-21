from kinematics import create_full_transformation_matrix, transform_point
from visualizer import plot_scene

def run_simulation():
    # 1. Giriş Değerleri
    drone_pos = [5, 0, 8]
    drone_ori = [0, 0, 45] # Roll, Pitch, Yaw
    point_in_B = [3, 0, 0] # Drone'un 3m önü

    # 2. Hesaplama (Logic)
    T_A_B = create_full_transformation_matrix(*drone_pos, *drone_ori)
    point_in_A = transform_point(T_A_B, point_in_B)

    print("Point in B: ")
    print(point_in_B)

    print("Point in A: ")
    print(point_in_A)

    # 3. Görselleştirme Komutu (UI)
    plot_scene(T_A_B, point_in_A, title="T_A^B Simülasyonu")

if __name__ == "__main__":
    run_simulation()