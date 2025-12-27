import matplotlib.pyplot as plt

# Data using Python lists
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
study_hours = [2, 3, 4, 5, 6, 4, 3]
marks = [55, 60, 65, 70, 80, 75, 68]

# Line Plot
plt.plot(days, study_hours, marker='o', label="Study Hours")
plt.title("Weekly Study Progress")
plt.xlabel("Days")
plt.ylabel("Hours")
plt.legend()
plt.grid(True)

# Show plot
plt.show()
