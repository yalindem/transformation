import matplotlib.pyplot as plt
import numpy as np

def draw_frame(ax, T, label, scale=1.0):
    origin = T[:3, 3]
    colors = ['r', 'g', 'b'] # X, Y, Z
    axis_names = ['X', 'Y', 'Z']
    for i in range(3):
        vector = T[:3, i] * scale
        ax.quiver(origin[0], origin[1], origin[2], vector[0], vector[1], vector[2], 
                  color=colors[i], arrow_length_ratio=0.1)
        # Eksen isimlerini ekle
        ax.text(*(origin + vector * 1.1), axis_names[i], color=colors[i], fontsize=8)
    ax.text(origin[0], origin[1], origin[2]-0.2, label, fontweight='bold')

def plot_scene(frames=None, points=None, title="Drone Simulation"):
    """
    frames: [{'matrix': T, 'label': 'Drone'}, ...]
    points: [{'coord': P, 'label': 'Target', 'color': 'red'}, ...]
    """
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # 1. Dünya orijini her zaman olsun
    draw_frame(ax, np.eye(4), "World (A)", scale=2.0)

    # 2. Tüm çerçeveleri döngüyle çiz
    if frames:
        for f in frames:
            draw_frame(ax, f['matrix'], f['label'])

    # 3. Tüm noktaları döngüyle çiz
    if points:
        for p in points:
            coord = p['coord']
            color = p.get('color', 'black')
            ax.scatter(coord[0], coord[1], coord[2], c=color, s=100)
            ax.text(coord[0], coord[1], coord[2], p['label'])

    # Grafik ayarları
    ax.set_xlim([-2, 12]); ax.set_ylim([-5, 10]); ax.set_zlim([0, 12])
    ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
    plt.title(title)
    plt.show()