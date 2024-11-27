import os
import pandas as pd
import numpy as np
import unittest


# Data generation function
def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)


# Function to save data to CSV
def save_to_csv(file_path, data):
    rows = []
    for department_id, department_data in data.items():
        for user_id, score in enumerate(department_data):
            rows.append([department_id, user_id, score])

    df = pd.DataFrame(rows, columns=['department_id', 'user_id', 'score'])
    df.to_csv(file_path, index=False)


# Function to load data from CSV
def load_from_csv(file_path):
    df = pd.read_csv(file_path)
    data = {}
    for _, row in df.iterrows():
        department_id = row['department_id']
        score = row['score']
        if department_id not in data:
            data[department_id] = []
        data[department_id].append(score)
    return data


# Unit tests class
class TestThreatScoreAggregation(unittest.TestCase):
    CSV_DIR = "test_case_data"

    def setUp(self):
        # Create directory for storing CSV files if it doesn't exist
        os.makedirs(self.CSV_DIR, exist_ok=True)

    # Function to load or generate data
    def load_or_generate_data(self, file_name, generate_function):
        file_path = os.path.join(self.CSV_DIR, file_name)
        if os.path.exists(file_path):
            return load_from_csv(file_path)
        else:
            data = generate_function()
            save_to_csv(file_path, data)
            return data

    def aggregate_threat_scores(self, departments_data):
        total_weighted_score = 0
        total_departments = 0

        print("Debugging: Department means and their contributions to total score:")
        for department in departments_data:
            mean_threat_score = np.mean(department)
            print(f"Mean threat score: {mean_threat_score}")
            total_weighted_score += mean_threat_score
            total_departments += 1

        aggregated_score = total_weighted_score / total_departments if total_departments > 0 else 0
        print(f"Debugging: Total Weighted Score = {total_weighted_score}, Total Departments = {total_departments}")
        print(f"Aggregated Score: {aggregated_score}")
        return aggregated_score

    # Example Test Case: All High Score Departments
    def test_all_high_score_departments(self):
        np.random.seed(0)
        departments_data = self.load_or_generate_data(
            "high_score_departments.csv",
            lambda: {
                0: generate_random_data(mean=80, variance=5, num_samples=50),
                1: generate_random_data(mean=75, variance=5, num_samples=50),
                2: generate_random_data(mean=85, variance=5, num_samples=50),
                3: generate_random_data(mean=90, variance=5, num_samples=50),
                4: generate_random_data(mean=70, variance=5, num_samples=50),
            }
        )
        aggregated_score = self.aggregate_threat_scores(list(departments_data.values()))
        self.assertTrue(75 <= aggregated_score <= 85)  # Expecting a high aggregated score since all are high

    # Example Test Case: All Low Score Departments
    def test_all_low_score_departments(self):
        np.random.seed(42)
        departments_data = self.load_or_generate_data(
            "low_score_departments.csv",
            lambda: {
                0: generate_random_data(mean=10, variance=2, num_samples=50),
                1: generate_random_data(mean=12, variance=2, num_samples=50),
                2: generate_random_data(mean=15, variance=2, num_samples=50),
                3: generate_random_data(mean=8, variance=2, num_samples=50),
                4: generate_random_data(mean=7, variance=2, num_samples=50),
            }
        )
        aggregated_score = self.aggregate_threat_scores(list(departments_data.values()))
        self.assertTrue(
            5 <= aggregated_score <= 15)  # Expecting a low aggregated score because all departments are low-risk

    # Additional test cases can follow the same pattern...


if __name__ == '__main__':
    unittest.main(exit=False)
