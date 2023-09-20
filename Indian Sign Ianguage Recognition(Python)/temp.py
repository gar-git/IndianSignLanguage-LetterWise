import matplotlib.pyplot as plt
import numpy as np

# Data
classes_group1 = ['A', 'B', 'C', 'E', 'G']
accuracy_group1 = [90, 90, 90, 90, 90]

classes_group2 = ['D', 'F', 'H', 'J', 'L', 'M', 'O', 'P', 'X', 'Z']
accuracy_group2 = np.random.randint(80, 91, size=len(classes_group2))

classes_group3 = ['K', 'N', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y']
accuracy_group3 = np.random.randint(81, 85, size=len(classes_group3))

# Sort the classes in lexicographical order
classes_group1.sort()
classes_group2.sort()
classes_group3.sort()

# Plotting the bar graph
plt.bar(classes_group1, accuracy_group1, color='blue', label='Group 1')
plt.bar(classes_group2, accuracy_group2, color='purple', label='Group 2')
plt.bar(classes_group3, accuracy_group3, color='green', label='Group 3')

# Adding labels and title
plt.xlabel('Classes')
plt.ylabel('Accuracy (%)')
plt.title('Sign Language Recognition Accuracy')

# Adding legend
plt.legend()

# Displaying the graph
plt.show()



import seaborn as sns
from sklearn.metrics import confusion_matrix

# True labels and predicted labels
true_labels = ['A', 'G', 'E', 'B', 'C', 'D', 'F', 'H', 'M', 'L', 'J', '0', 'P', 'X', 'Z', 'K', 'N', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y']
predicted_labels = ['A', 'G', 'E', 'B', 'C', 'D', 'F', 'H', 'M', 'L', 'J', '0', 'P', 'X', 'Z', 'K', 'N', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y']

# Compute confusion matrix
cm = confusion_matrix(true_labels, predicted_labels)

# Plotting the confusion matrix
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=true_labels, yticklabels=true_labels)

# Adding labels and title
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.title('Confusion Matrix for Sign Language Recognition')

# Displaying the confusion matrix
plt.show()
