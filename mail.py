import matplotlib.pyplot as plt
import numpy as np
ice_thickness_mm = np.array([1, 2, 3, 4, 5])
ice_mass_kg = ice_thickness_mm * 0.05
heat_energy_joules = ice_mass_kg * 334000
time_seconds = np.array([1.5, 2.0, 3.2, 4.0, 5.1])
acoustic_energy_joules = 35 * time_seconds
plt.figure(figsize=(10, 6))
plt.plot(
ice_thickness_mm,
heat_energy_joules,
marker="o",
color="red",
linewidth=2,
label="Тепловая система (плавления)",
)
plt.plot(
ice_thickness_mm,
acoustic_energy_joules,
marker="s",
color="green",
linewidth=2,
label="Acoustic Smart Skin (Ультразвук)"
)
plt.title(
"Сравнение энергопотребления системы защиты от обледенения",
fontsize=14
)
plt.xlabel("Толщина слоя льда(мм)", fontsize=12)
plt.ylabel("Затраченная энергия (Джоули, log scale)", fontsize=12)
plt.yscale("log")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(fontsize=11)
plt.savefig("energy_graph,png")
plt.show()
print("=" * 50)
print("РЕЗУЛЬТАТЫ СИМУЛЯЦИИ ЭНЕРГОЭФФЕКТИВНОСТИ:")
print("=" * 50)
for i in range(len(ice_thickness_mm)): ratio = heat_energy_joules[i] / acoustic_energy_joules[i]
print(
f"Лед {ice_thickness_mm[i]} мм: Ультразвук эффективнее в {ratio:.1f} раз!"
)