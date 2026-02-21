from kinematics import create_full_transformation_matrix, transform_point
from visualizer import plot_scene

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

    # Fonksiyonu çağır (Parametre kalabalığı bitti!)
    plot_scene(frames=frames, points=points, title="Çoklu Çerçeve Simülasyonu")
    #print("Point in B: ")
    #print(point_in_B)

    #print("Point in A: ")
    #print(point_in_A)

   
if __name__ == "__main__":
    run_simulation()