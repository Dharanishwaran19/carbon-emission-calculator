import tkinter as tk
from tkinter import ttk

# Emission factors in kg CO2 per km
EMISSION_FACTORS = {
    'Car': 0.1209,
    'Bus': 0.089,
    'Train': 0.041,
    'Bicycle': 0.0,
    'Walking': 0.0
}

# Function to calculate emissions
def calculate_emissions():
    try:
        mode = transport_mode.get()
        distance = float(distance_entry.get())
        emissions = distance * EMISSION_FACTORS[mode]
        result_label.config(text=f"Estimated Emissions: {emissions:.3f} kg CO\u2082")
    except ValueError:
        result_label.config(text="Please enter a valid distance.")

# GUI Window
window = tk.Tk()
window.title("Carbon Emission Transport Calculator")
window.geometry("400x250")

# Widgets
tk.Label(window, text="Carbon Emission Transport Calculator", font=("Arial", 14, "bold")).pack(pady=10)

frame = tk.Frame(window)
frame.pack(pady=5)

tk.Label(frame, text="Transport Mode:").grid(row=0, column=0, sticky="w")
transport_mode = ttk.Combobox(frame, values=list(EMISSION_FACTORS.keys()))
transport_mode.set("Car")
transport_mode.grid(row=0, column=1)

tk.Label(frame, text="Distance (km):").grid(row=1, column=0, sticky="w")
distance_entry = tk.Entry(frame)
distance_entry.grid(row=1, column=1)

tk.Button(window, text="Calculate", command=calculate_emissions).pack(pady=10)
result_label = tk.Label(window, text="Estimated Emissions: ", font=("Arial", 12))
result_label.pack()

# Run the app
window.mainloop()
