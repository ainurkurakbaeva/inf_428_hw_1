# import numpy as np
# import unittest
#
# departments = {
#     'Engineering': 4,
#     'Marketing': 3,
#     'Finance': 5,
#     'HR': 2,
#     'Science': 4
# }
#
# def generate_random_data(mean, variance, num_samples):
#     return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)
#
# def calculate_department_mean_threat_score(threat_scores):
#     return np.mean(threat_scores)
#
# def calculate_aggregated_threat_score(department_scores):
#     # Since we removed importance, we just calculate the mean of department scores directly
#     aggregated_score = np.mean(department_scores)
#     return min(max(aggregated_score, 0), 90)
#
# class TestAggregatedThreatScore(unittest.TestCase):
#     def setUp(self):
#         self.departments = departments
#
#     def test_calculate_department_mean_threat_score(self):
#         threat_scores = generate_random_data(45, 10, 100)
#         mean_score = calculate_department_mean_threat_score(threat_scores)
#         self.assertGreaterEqual(mean_score, 0)
#         self.assertLessEqual(mean_score, 90)
#
#     def test_calculate_aggregated_threat_score(self):
#         mean_scores = [50, 52, 49, 48, 51]
#         aggregated_score = calculate_aggregated_threat_score(mean_scores)
#         self.assertGreaterEqual(aggregated_score, 0)
#         self.assertLessEqual(aggregated_score, 90)
#
#     def test_high_importance_department_with_high_score(self):
#         # Simulate one department with a very high score
#         mean_scores = [30, 35, 85, 25, 30]  # Finance has a high score (85)
#         aggregated_score = calculate_aggregated_threat_score(mean_scores)
#         self.assertGreaterEqual(aggregated_score, 0)
#         self.assertLessEqual(aggregated_score, 90)
#
#     def test_balanced_departments(self):
#         # All departments with similar mean scores
#         mean_scores = [50, 50, 50, 50, 50]
#         aggregated_score = calculate_aggregated_threat_score(mean_scores)
#         self.assertEqual(aggregated_score, 50)
#
#     def test_same_mean_scores_with_high_threat_in_one_department(self):
#         # All departments have similar mean scores, but one has very high values for some users
#         engineering = generate_random_data(40, 10, 200)  # Mean = ~40
#         marketing = generate_random_data(40, 10, 50)  # Mean = ~40
#         finance = generate_random_data(40, 10, 150)  # Mean = ~40
#         hr = generate_random_data(40, 10, 10)  # Mean = ~40
#         science = generate_random_data(40, 10, 120)  # Mean = ~40
#
#         # One department with extremely high scores
#         finance[0:10] = [90] * 10  # Adding very high scores to finance
#
#         mean_scores = [
#             calculate_department_mean_threat_score(engineering),
#             calculate_department_mean_threat_score(marketing),
#             calculate_department_mean_threat_score(finance),  # Expected to be higher due to extreme scores
#             calculate_department_mean_threat_score(hr),
#             calculate_department_mean_threat_score(science)
#         ]
#
#         aggregated_score = calculate_aggregated_threat_score(mean_scores)
#         self.assertGreater(aggregated_score, 40)  # Aggregated score should increase due to high finance scores
#
#     def test_edge_case_low_and_high_scores(self):
#         mean_scores = [10, 15, 85, 20, 12]
#         aggregated_score = calculate_aggregated_threat_score(mean_scores)
#         self.assertGreaterEqual(aggregated_score, 0)
#         self.assertLessEqual(aggregated_score, 90)
#
# if __name__ == '__main__':
#     unittest.main()

import numpy as np
import unittest

departments = {
    'Engineering': 4,
    'Marketing': 3,
    'Finance': 5,
    'HR': 2,
    'Science': 4
}

def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)

def calculate_department_mean_threat_score(threat_scores):
    return np.mean(threat_scores)

def calculate_aggregated_threat_score(department_scores):
    # Since we removed importance, we just calculate the mean of department scores directly
    aggregated_score = np.mean(department_scores)
    return min(max(aggregated_score, 0), 90)

class TestAggregatedThreatScore(unittest.TestCase):
    def setUp(self):
        self.departments = departments

    def test_calculate_department_mean_threat_score(self):
        threat_scores = generate_random_data(45, 10, 100)
        mean_score = calculate_department_mean_threat_score(threat_scores)
        print(f"Department Threat Scores: {threat_scores}")
        print(f"Calculated Mean Score: {mean_score}")
        self.assertGreaterEqual(mean_score, 0)
        self.assertLessEqual(mean_score, 90)

    def test_calculate_aggregated_threat_score(self):
        mean_scores = [50, 52, 49, 48, 51]
        aggregated_score = calculate_aggregated_threat_score(mean_scores)
        print(f"Mean Scores: {mean_scores}")
        print(f"Aggregated Threat Score: {aggregated_score}")
        self.assertGreaterEqual(aggregated_score, 0)
        self.assertLessEqual(aggregated_score, 90)

    def test_high_importance_department_with_high_score(self):
        mean_scores = [30, 35, 85, 25, 30]
        aggregated_score = calculate_aggregated_threat_score(mean_scores)
        print(f"Mean Scores: {mean_scores}")
        print(f"Aggregated Threat Score: {aggregated_score}")
        self.assertGreaterEqual(aggregated_score, 0)
        self.assertLessEqual(aggregated_score, 90)

    def test_balanced_departments(self):
        mean_scores = [50, 50, 50, 50, 50]
        aggregated_score = calculate_aggregated_threat_score(mean_scores)
        print(f"Mean Scores: {mean_scores}")
        print(f"Aggregated Threat Score: {aggregated_score}")
        self.assertEqual(aggregated_score, 50)

    def test_same_mean_scores_with_high_threat_in_one_department(self):
        engineering = generate_random_data(40, 10, 200)
        marketing = generate_random_data(40, 10, 50)
        finance = generate_random_data(40, 10, 150)
        hr = generate_random_data(40, 10, 10)
        science = generate_random_data(40, 10, 120)

        finance[0:10] = [90] * 10  # Adding very high scores to finance

        mean_scores = [
            calculate_department_mean_threat_score(engineering),
            calculate_department_mean_threat_score(marketing),
            calculate_department_mean_threat_score(finance),
            calculate_department_mean_threat_score(hr),
            calculate_department_mean_threat_score(science)
        ]

        aggregated_score = calculate_aggregated_threat_score(mean_scores)
        print(f"Mean Scores: {mean_scores}")
        print(f"Aggregated Threat Score: {aggregated_score}")
        self.assertGreater(aggregated_score, 40)

    def test_edge_case_low_and_high_scores(self):
        mean_scores = [10, 15, 85, 20, 12]
        aggregated_score = calculate_aggregated_threat_score(mean_scores)
        print(f"Mean Scores: {mean_scores}")
        print(f"Aggregated Threat Score: {aggregated_score}")
        self.assertGreaterEqual(aggregated_score, 0)
        self.assertLessEqual(aggregated_score, 90)

if __name__ == '__main__':
    unittest.main()
