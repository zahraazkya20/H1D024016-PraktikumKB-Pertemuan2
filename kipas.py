# Import library
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Menyiapkan Himpunan Fuzzy
suhu = ctrl.Antecedent(np.arange(0, 41, 1), 'suhu') # 0–40 °C
kelembapan = ctrl.Antecedent(np.arange(0, 101, 1), 'kelembapan') # 0–100 %
kecepatan = ctrl.Consequent(np.arange(0, 101, 1), 'kecepatan') # 0–100

# Fungsi Keanggotaan
# Suhu: Dingin, Sejuk, Hangat, Panas
suhu['Dingin'] = fuzz.trimf(suhu.universe, [0, 0, 15])
suhu['Sejuk'] = fuzz.trimf(suhu.universe, [10, 20, 30])
suhu['Hangat'] = fuzz.trimf(suhu.universe, [22, 30, 37])
suhu['Panas'] = fuzz.trimf(suhu.universe, [33, 40, 40])

# Kelembapan: Kering, Normal, Lembap
kelembapan['Kering'] = fuzz.trimf(kelembapan.universe, [0, 0, 40])
kelembapan['Normal'] = fuzz.trimf(kelembapan.universe, [30, 50, 70])
kelembapan['Lembap'] = fuzz.trimf(kelembapan.universe, [60, 100, 100])

# Kecepatan kipas: Mati, Lambat, Sedang, Cepat
kecepatan['Mati'] = fuzz.trimf(kecepatan.universe, [0, 0, 25])
kecepatan['Lambat'] = fuzz.trimf(kecepatan.universe, [15, 35, 55])
kecepatan['Sedang'] = fuzz.trimf(kecepatan.universe, [45, 60, 75])
kecepatan['Cepat'] = fuzz.trimf(kecepatan.universe, [65, 100, 100])

# Aturan Fuzzy (IF-THEN)
aturan1 = ctrl.Rule(suhu['Dingin'], kecepatan['Mati'])
aturan2 = ctrl.Rule(suhu['Sejuk'] & kelembapan['Kering'], kecepatan['Lambat'])
aturan3 = ctrl.Rule(suhu['Sejuk'] & kelembapan['Normal'], kecepatan['Lambat'])
aturan4 = ctrl.Rule(suhu['Sejuk'] & kelembapan['Lembap'], kecepatan['Sedang'])
aturan5 = ctrl.Rule(suhu['Hangat'] & kelembapan['Kering'], kecepatan['Sedang'])
aturan6 = ctrl.Rule(suhu['Hangat'] & kelembapan['Normal'], kecepatan['Sedang'])
aturan7 = ctrl.Rule(suhu['Hangat'] & kelembapan['Lembap'], kecepatan['Cepat'])
aturan8 = ctrl.Rule(suhu['Panas'], kecepatan['Cepat'])

# Inference engine & sistem fuzzy
engine = ctrl.ControlSystem([
    aturan1, aturan2, aturan3, aturan4,
    aturan5, aturan6, aturan7, aturan8
])
system = ctrl.ControlSystemSimulation(engine)

test_cases = [
    (10, 30, "Dingin & Kering → harusnya Mati/Lambat"),
    (20, 50, "Sejuk & Normal → harusnya Lambat"),
    (20, 80, "Sejuk & Lembap → harusnya Sedang"),
    (30, 40, "Hangat & Kering → harusnya Sedang"),
    (30, 75, "Hangat & Lembap → harusnya Cepat"),
    (38, 90, "Panas & Lembap → harusnya Cepat"),
]

print("=" * 60)
print("SISTEM FUZZY – KECEPATAN KIPAS ANGIN")
print("=" * 60)
print(f"{'Suhu':>6} {'Kelembapan':>11} {'Kecepatan':>11}   Keterangan")
print("-" * 60)

for suhu_val, kel_val, ket in test_cases:
    system.input['suhu'] = suhu_val
    system.input['kelembapan'] = kel_val
    system.compute()
    hasil = system.output['kecepatan']
    print(f"{suhu_val:>5}°C {kel_val:>8}% {hasil:>9.2f} {ket}")

print("=" * 60)

# Tampilkan grafik membership function
suhu.view()
kelembapan.view()

# Tampilkan grafik output dengan salah satu simulasi
system.input['suhu'] = 30
system.input['kelembapan'] = 75
system.compute()
kecepatan.view(sim=system)

import matplotlib.pyplot as plt
plt.show()