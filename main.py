from kinematics import create_full_transformation_matrix, transform_point
from quaternion_kinematics import create_quaternion_from_euler, transform_point_quaternion, get_matrix_from_quat_and_pos
from visualizer import plot_scene

def run_simulation_quaternion():
    # 1. Giriş Değerleri
    drone_pos = [5, 0, 8]
    drone_quat = create_quaternion_from_euler(0, 0, 45) # Roll, Pitch, Yaw -> Quat
    
    # Kamera 1 (Drone üzerindeki konumu ve açısı)
    c1_pos_drone = [0.2, -0.05, 0.1]
    c1_quat_drone = create_quaternion_from_euler(-90, 0, -90)

    # Kameraya göre olan hedef nokta (Target B)
    point_B_camera1 = [0, 0, 2] 

    # 2. HESAPLAMA (MATRİS ÇARPIMI YERİNE ZİNCİRLEME TRANSFORM)
    
    # Adım A: Noktayı Camera1 frame'inden Drone frame'ine taşı
    point_B_in_drone = transform_point_quaternion(point_B_camera1, c1_pos_drone, c1_quat_drone)
    
    # Adım B: Drone frame'ine gelen noktayı Dünya (World) frame'ine taşı
    point_B_world = transform_point_quaternion(point_B_in_drone, drone_pos, drone_quat)

    # --- Görselleştirme İçin Matrisleri Yine de Oluşturalım ---
    T_world_drone = get_matrix_from_quat_and_pos(drone_pos, drone_quat)
    
    # Kamera 1'in dünyadaki tam matrisi (Görselleştirmede eksenleri görmek için)
    # T_world_c1 = T_world_drone @ T_drone_c1
    T_drone_c1 = get_matrix_from_quat_and_pos(c1_pos_drone, c1_quat_drone)
    T_world_camera1 = T_world_drone @ T_drone_c1

    frames = [
        {'matrix': T_world_drone,   'label': 'Drone (B)'},
        {'matrix': T_world_camera1, 'label': 'Cam 1 (C1)'}
    ]

    points = [
        {'coord': point_B_world, 'label': 'Target B', 'color': 'blue'}
    ]

    plot_scene(frames=frames, points=points, title="Quaternion Sandwich Simulation")

def run_simulation():
    # 1. Giriş Değerleri
    drone_pos = [5, 0, 8] # in world coordinates
    drone_ori = [0, 0, 45] # Roll, Pitch, Yaw
    point_A_drone = [3, 0, 0] # Drone'un 3m önü
    point_B_camea1 = [0, 0, 2] # camera 1 frameine göre bir cisim

    camera1_pos_drone = [0.2, -0.05, 0.1]
    camera1_ori_drone = [-90, 0, -90]  

    camera2_pos_drone = [0.2, 0.05, 0.1]
    camera2_ori_drone = [-90, 0, -90]  

    # 2. Hesaplama (Logic)
    T_world_drone = create_full_transformation_matrix(*drone_pos, *drone_ori)
    point_A_world = transform_point(T_world_drone, point_A_drone)

    T_drone_camera1 = create_full_transformation_matrix(*camera1_pos_drone, *camera1_ori_drone)
    T_drone_camera2 = create_full_transformation_matrix(*camera2_pos_drone, *camera2_ori_drone)
    
    T_world_camera1 = T_world_drone @ T_drone_camera1
    T_world_camera2 = T_world_drone @ T_drone_camera2

    point_B_world = transform_point(T_world_camera1, point_B_camea1)

    frames = [
        {'matrix': T_world_drone,   'label': 'Drone (B)'},
        {'matrix': T_world_camera1, 'label': 'Cam 1 (C1)'},
        {'matrix': T_world_camera2, 'label': 'Cam 2 (C2)'}
    ]

    # Çizilecek Noktalar Listesi
    points = [
        {'coord': point_A_world, 'label': 'Target A', 'color': 'black'},
        {'coord': [2, 3, 0],   'label': 'Obstacle', 'color': 'red'},
        {'coord': point_B_world, 'label': 'Target B', 'color': 'black'}
    ]

    plot_scene(frames=frames, points=points, title="Çoklu Çerçeve Simülasyonu")

   
if __name__ == "__main__":
    #run_simulation()
    run_simulation_quaternion()