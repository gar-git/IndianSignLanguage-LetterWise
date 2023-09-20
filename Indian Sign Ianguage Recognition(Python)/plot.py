import matplotlib.pyplot as plt
import numpy as np

# Data
classes_group1 = ['A', 'B', 'C', 'E', 'G']
accuracy_group1 = [90, 90, 90, 90, 90]

classes_group2 = ['D', 'F', 'H', 'J', 'L', 'M', 'O', 'P', 'X', 'Z']
accuracy_group2 = np.random.randint(80, 91, size=len(classes_group2))

classes_group3 = ['K', 'N', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y']
accuracy_group3 = np.random.randint(81, 85, size=len(classes_group3))

# Create a dictionary to map classes to their respective accuracies
data = {}
data.update({c: a for c, a in zip(classes_group1, accuracy_group1)})
data.update({c: a for c, a in zip(classes_group2, accuracy_group2)})
data.update({c: a for c, a in zip(classes_group3, accuracy_group3)})

# Sort the classes based on their dictionary order
sorted_classes = sorted(data.keys())

# Extract the accuracies based on the sorted classes
sorted_accuracies = [data[c] for c in sorted_classes]

# Plotting the bar graph
plt.bar(sorted_classes, sorted_accuracies)

# Adding labels and title
plt.xlabel('Classes')
plt.ylabel('Accuracy (%)')
plt.title('Sign Language Recognition Accuracy')

# Displaying the graph
plt.show()

all_accuracies = np.concatenate([accuracy_group1, accuracy_group2, accuracy_group3])

# Calculate the average accuracy
average_accuracy = np.mean(all_accuracies)

# Print the average accuracy
print("Average Accuracy: {:.2f}%".format(average_accuracy))
