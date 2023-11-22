#pip install numpy scikit-learn
import numpy as np
from sklearn.metrics import precision_score, recall_score

def read_input(N):
    """ Function to read N points from the user """
    points = []
    for _ in range(N):
        x = int(input("Enter x value (0 or 1): "))
        y = int(input("Enter y value (0 or 1): "))
        points.append((x, y))
    return points

def main():
    N = int(input("Enter the number of points (N): "))

    points = read_input(N)

    true_labels, predicted_labels = np.array(points).T

    precision = precision_score(true_labels, predicted_labels)
    recall = recall_score(true_labels, predicted_labels)

    print(f"Precision: {precision}")
    print(f"Recall: {recall}")

if __name__ == "__main__":
    main()
