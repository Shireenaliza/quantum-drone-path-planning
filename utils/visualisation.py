import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_3d_path(node_coords, path, title="Path Visualization"):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot nodes
    for node, (x, y, z) in node_coords.items():
        ax.scatter(x, y, z, c='black', s=50)
        ax.text(x, y, z + 0.1, str(node))
        
    # Plot chosen path
    if path:
        path_xs = [node_coords[n][0] for n in path]
        path_ys = [node_coords[n][1] for n in path]
        path_zs = [node_coords[n][2] for n in path]
        ax.plot(path_xs, path_ys, path_zs, linewidth=3, label="Trajectory")
        
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(title)
    plt.tight_layout()
    plt.show()