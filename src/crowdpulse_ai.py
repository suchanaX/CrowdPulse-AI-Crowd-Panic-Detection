
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
time_data = []
sound_variance_data = []
table_data = pd.DataFrame(
     [[0.0, 0.0, 0.0, "LOW"]],
     columns=["sound_variance", "sound_entropy", "vibration_std", "risk"]
     )
fig = plt.figure(figsize=(10, 6))
ax_graph = plt.subplot2grid((3, 3), (0, 0), colspan=3, rowspan=2)
ax_table = plt.subplot2grid((3, 3), (2, 0), colspan=3)
ax_graph.set_title("CrowdPulse : Live Crowd Monitoring")
ax_graph.set_xlabel("Time")
ax_graph.set_ylabel("Sound Variance")
line, = ax_graph.plot([], [], linewidth=2)
def calculate_risk(sound_var):
    if sound_var < 30:
        return "LOW"
    elif sound_var < 70:
        return "MEDIUM"
    else:
        return "HIGH"

    
def update(frame):
    sound_var = np.random.randint(10, 100)
    sound_entropy = round(np.random.uniform(0.5, 2.5), 2)
    vibration_std = round(np.random.uniform(0.1, 3.0), 2)
    risk = calculate_risk(sound_var)
    # Update graph
    time_data.append(frame)
    sound_variance_data.append(sound_var)
    line.set_data(time_data, sound_variance_data)
    ax_graph.set_xlim(0, max(20, frame))
    ax_graph.set_ylim(0, 110)
    # Update table data
    table_data.iloc[0] = [sound_var, sound_entropy, vibration_std, risk]
    ax_table.clear()
    ax_table.axis('off')
    table = ax_table.table(
        cellText=table_data.values,
        colLabels=table_data.columns,
        loc='center'
        )
    table.scale(1, 2)
    risk_cell = table[(1, 3)]  # (row=1 because header is row 0, col=3 is "risk")
    if risk == "LOW":
        risk_cell.set_facecolor("lightgreen")
    elif risk == "MEDIUM":
        risk_cell.set_facecolor("khaki")
    else:
        risk_cell.set_facecolor("lightcoral")
    risk_cell.set_text_props(weight='bold')
    return line,

ani = FuncAnimation(fig, update, interval=1000)

plt.tight_layout()
plt.show()
