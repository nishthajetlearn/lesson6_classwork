import numpy as np
import matplotlib.pyplot as plt

# Sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a figure
plt.figure(figsize=(10, 5))

# Line plots
plt.plot(x, y1, label='Sine Wave', color='blue')
plt.plot(x, y2, label='Cosine Wave', color='orange')

# Scatter plot
plt.scatter(x, y1, color='red', s=10, label='Sine Points')
plt.scatter(x, y2, color='green', s=10, label='Cosine Points')

# Adding labels and legend
plt.title('Multiple Line and Scatter Plots')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid()
plt.show()


#>>>>>>>>> Bar Charts with Multiple Bars
# Sample data for bar chart
categories = ['A', 'B', 'C', 'D']
values1 = [3, 7, 2, 5]
values2 = [4, 6, 5, 3]

# Bar width
bar_width = 0.35
x = np.arange(len(categories))

# Create a figure
plt.figure(figsize=(8, 5))

# Bar plots
plt.bar(x, values1, width=bar_width, label='Group 1', color='blue', align='center')
plt.bar(x + bar_width, values2, width=bar_width, label='Group 2', color='orange', align='center')

# Adding labels and legend
plt.title('Multiple Bar Charts')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.xticks(x + bar_width / 2, categories)
plt.legend()
plt.grid()
plt.show()

#>>>>>>3. Histograms
# Sample data for histogram
data = np.random.randn(1000)

# Create a figure
plt.figure(figsize=(8, 5))

# Histogram
plt.hist(data, bins=30, alpha=0.7, color='blue')

# Adding labels and title
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid()
plt.show()

#>>>>>>. Stacked Plot
# Sample data for stacked plot
labels = ['A', 'B', 'C']
values1 = [5, 3, 2]
values2 = [2, 5, 3]
values3 = [3, 2, 4]

# Create a figure
plt.figure(figsize=(8, 5))

# Stacked plot
plt.bar(labels, values1, label='Series 1', color='blue')
plt.bar(labels, values2, bottom=values1, label='Series 2', color='orange')
plt.bar(labels, values3, bottom=np.array(values1) + np.array(values2), label='Series 3', color='green')

# Adding labels and legend
plt.title('Stacked Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.legend()
plt.grid()
plt.show()

#>>>>5. Pie Chart
# Sample data for pie chart
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']

# Create a figure
plt.figure(figsize=(8, 5))

# Pie chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Adding title
plt.title('Pie Chart')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

#>>>>>6. Subplots
# Create a figure with subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Line plot
axs[0, 0].plot(x, y1, color='blue', label='Sine Wave')
axs[0, 0].plot(x, y2, color='orange', label='Cosine Wave')
axs[0, 0].set_title('Line Plot')
axs[0, 0].legend()

# Bar plot
axs[0, 1].bar(x, values1, label='Group 1', color='blue', alpha=0.7)
axs[0, 1].bar(x + bar_width, values2, label='Group 2', color='orange', alpha=0.7)
axs[0, 1].set_title('Bar Plot')
axs[0, 1].legend()

# Histogram
axs[1, 0].hist(data, bins=30, color='blue', alpha=0.7)
axs[1, 0].set_title('Histogram')

# Pie chart
axs[1, 1].pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
axs[1, 1].set_title('Pie Chart')

# Adjust layout
plt.tight_layout()
plt.show()

