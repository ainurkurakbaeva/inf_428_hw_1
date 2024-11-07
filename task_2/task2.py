 #  We have 5 departments, each with a number of users between 10 - 200
 #  Each user has a threat score between 0 and 90
 #  Each department has an importance score (1-5), which means some departments might need more attention in the overall metric.
 #  We want one score between 0 and 90 that summarizes the cybersecurity status for the whole company.
 # 1 test case: No outliers, similar mean threat scores, similar number of users, equal importance
 # 2 test case: Varying importance scores
 # 3 test case: One department has high threat scores

import numpy as np

def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)


def aggregate_threat_scores(departments_data, importance_tags):
    total_weighted_score = 0
    total_importance = 0

    for department, importance in zip(departments_data, importance_tags):
        mean_threat_score = np.mean(department)
        total_weighted_score += mean_threat_score * importance
        total_importance += importance

    aggregated_score = total_weighted_score / total_importance
    return aggregated_score


import unittest


class TestThreatScoreAggregation(unittest.TestCase):

    def test_no_outliers(self):
        np.random.seed(0)
        engineering = generate_random_data(mean=30, variance=5, num_samples=50)
        marketing = generate_random_data(mean=28, variance=5, num_samples=50)
        finance = generate_random_data(mean=32, variance=5, num_samples=50)
        hr = generate_random_data(mean=31, variance=5, num_samples=50)
        science = generate_random_data(mean=29, variance=5, num_samples=50)

        departments_data = [engineering, marketing, finance, hr, science]
        importance_tags = [3, 3, 3, 3, 3]

        aggregated_score = aggregate_threat_scores(departments_data, importance_tags)
        self.assertAlmostEqual(aggregated_score, 30, delta=2)

    def test_varying_importance(self):
        np.random.seed(0)
        engineering = generate_random_data(mean=20, variance=10, num_samples=50)
        marketing = generate_random_data(mean=25, variance=10, num_samples=50)
        finance = generate_random_data(mean=45, variance=10, num_samples=50)
        hr = generate_random_data(mean=30, variance=10, num_samples=50)
        science = generate_random_data(mean=35, variance=10, num_samples=50)

        departments_data = [engineering, marketing, finance, hr, science]
        importance_tags = [1, 2, 5, 2, 3]

        aggregated_score = aggregate_threat_scores(departments_data, importance_tags)
        self.assertTrue(0 <= aggregated_score <= 90)

    def test_high_threat_department(self):

        np.random.seed(0)
        engineering = generate_random_data(mean=20, variance=10, num_samples=50)
        marketing = generate_random_data(mean=25, variance=10, num_samples=50)
        finance = generate_random_data(mean=75, variance=5, num_samples=50)
        hr = generate_random_data(mean=30, variance=10, num_samples=50)
        science = generate_random_data(mean=35, variance=10, num_samples=50)

        departments_data = [engineering, marketing, finance, hr, science]
        importance_tags = [3, 3, 3, 3, 3]

        aggregated_score = aggregate_threat_scores(departments_data, importance_tags)
        self.assertTrue(0 <= aggregated_score <= 90)


if __name__ == '__main__':
    unittest.main()
