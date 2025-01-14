import random as rs
import winsound
import matplotlib.pyplot as plt

lambda1 = 0.005
init_nucleus = 80
time_max = 500
nuclei_remaining = init_nucleus

times = []
nuclei = []
decay_events = []  # Storing the number of decays per time step
total_decays = 0   # Counting the total number of decay events

for time in range(time_max + 1):
    decayed = 0
    for nucleus in range(nuclei_remaining):
        if rd.random() < lambda1:
            decayed += 1
            winsound.Beep(600, 100)  # Beep for each decay
    nuclei_remaining -= decayed
    total_decays += decayed
    times.append(time)
    nuclei.append(nuclei_remaining)
    decay_events.append(decayed)

plt.figure(figsize=(7, 5))
plt.subplot(2, 1, 1)
plt.plot(times, nuclei, color='red')
plt.title('Spontaneous Decay')
plt.xlabel('Time')
plt.ylabel('Number of Elements')

plt.subplot(2, 1, 2)
plt.bar(times, decay_events, color='red', width=1.0)
plt.title('Decay Events per Time Step')
plt.xlabel('Time')
plt.ylabel('Number of Decay Events')

plt.tight_layout()
plt.show()

# Number of steps that caused decays
print(f"Total number of decay events: {total_decays}")
