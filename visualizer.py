import matplotlib.pyplot as plt
import numpy as np

def draw_frame(ax, T, label, scale=1.5):
    origin = T[:3, 3]
    colors = ['r', 'g', 'b']
    axis_names = ['X', 'Y', 'Z']
    
    for i in range(3):
        # Eksen vektörünü hesapla
        vector = T[:3, i] * scale
        # Oku çiz
        ax.quiver(origin[0], origin[1], origin[2], vector[0], vector[1], vector[2], 
                  color=colors[i], arrow_length_ratio=0.1, linewidth=2)
        # Eksen ismini (X, Y, Z) okun ucuna yaz
        text_pos = origin + vector * 1.1  # Harfi okun biraz ilerisine koy
        ax.text(text_pos[0], text_pos[1], text_pos[2], axis_names[i], 
                color=colors[i], fontsize=10, fontweight='bold')
    
    # Çerçevenin ismini (Dünya veya Drone) orijine yaz
    ax.text(origin[0], origin[1], origin[2]-0.5, label, fontsize=12, fontweight='black')

def plot_scene(T_A_B, P_A, title="Drone Scene"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    draw_frame(ax, np.eye(4), "Dünya (A)")
    draw_frame(ax, T_A_B, "Drone (B)")
    
    # Hedef noktayı çiz
    ax.scatter(*P_A, color='black', s=100, label="Hedef Nokta")
    
    # Drone'dan noktaya çizgi
    drone_origin = T_A_B[:3, 3]
    ax.plot([drone_origin[0], P_A[0]], [drone_origin[1], P_A[1]], [drone_origin[2], P_A[2]], 
            'k--', alpha=0.4)
    
    # Grafik sınırları ve genel etiketler
    ax.set_xlim([0, 10]); ax.set_ylim([-5, 5]); ax.set_zlim([0, 10])
    ax.set_xlabel('Dünya X'); ax.set_ylabel('Dünya Y'); ax.set_zlabel('Dünya Z')
    ax.set_title(title)
    plt.legend()
    plt.show()