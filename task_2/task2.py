import numpy as np
import unittest


def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)


def aggregate_threat_scores(departments_data, importance_tags):
    total_weighted_score = 0
    total_importance = 0

    print("Debugging: Department means and their contributions to total score:")
    for department, importance in zip(departments_data, importance_tags):
        mean_threat_score = np.mean(department)
        print(f"Mean threat score: {mean_threat_score}, Importance: {importance}")
        total_weighted_score += mean_threat_score * importance
        total_importance += importance

    aggregated_score = total_weighted_score / total_importance if total_importance > 0 else 0
    print(f"Debugging: Total Weighted Score = {total_weighted_score}, Total Importance = {total_importance}")
    print(f"Aggregated Score: {aggregated_score}")
    return aggregated_score


class TestThreatScoreAggregation(unittest.TestCase):

    def test_no_outliers(self):
        np.random.seed(0)
        departments_data = [
            generate_random_data(mean=30, variance=5, num_samples=50),
            generate_random_data(mean=28, variance=5, num_samples=50),
            generate_random_data(mean=32, variance=5, num_samples=50),
            generate_random_data(mean=31, variance=5, num_samples=50),
            generate_random_data(mean=29, variance=5, num_samples=50),
        ]
        importance_tags = [5, 5, 5, 5, 5]
        aggregated_score = aggregate_threat_scores(departments_data, importance_tags)
        self.assertAlmostEqual(aggregated_score, 30, delta=2)

    def test_varying_importance(self):
        np.random.seed(0)
        departments_data = [
            generate_random_data(mean=20, variance=10, num_samples=50),
            generate_random_data(mean=25, variance=10, num_samples=50),
            generate_random_data(mean=45, variance=10, num_samples=50),
            generate_random_data(mean=30, variance=10, num_samples=50),
            generate_random_data(mean=35, variance=10, num_samples=50),
        ]
        importance_tags = [1, 2, 5, 2, 3]
        aggregated_score = aggregate_threat_scores(departments_data, importance_tags)
        self.assertTrue(20 <= aggregated_score <= 40)


def test_high_threat_department(self):
    np.random.seed(0)
    engineering = generate_random_data(mean=20, variance=10, num_samples=50)
    marketing = generate_random_data(mean=25, variance=10, num_samples=50)
    finance = generate_random_data(mean=75, variance=5, num_samples=50)  # High-risk department
    hr = generate_random_data(mean=30, variance=10, num_samples=50)
    science = generate_random_data(mean=35, variance=10, num_samples=50)

    departments_data = [engineering, marketing, finance, hr, science]
    importance_tags = [3, 3, 3, 3, 3]

    print("Debugging: Test High Threat Department")
    for idx, department in enumerate(departments_data):
        print(f"Department {idx + 1} mean threat score: {np.mean(department)}")

    aggregated_score = aggregate_threat_scores(departments_data, importance_tags)
    print(f"Aggregated Score in High Threat Department Test: {aggregated_score}")

    self.assertTrue(50 <= aggregated_score <= 70)  # Adjust this range if needed

if __name__ == '__main__':
    # Direct test cases
    np.random.seed(42)

    # Test Case 1: No outliers, equal importance
    department_data = [
        generate_random_data(mean=30, variance=5, num_samples=100),
        generate_random_data(mean=32, variance=5, num_samples=120),
        generate_random_data(mean=29, variance=5, num_samples=110),
        generate_random_data(mean=31, variance=5, num_samples=95),
        generate_random_data(mean=30, variance=5, num_samples=105),
    ]
    importance_tags = [3, 3, 3, 3, 3]
    score = aggregate_threat_scores(department_data, importance_tags)
    print(f"Test Case 1: Aggregated Score = {score:.2f}")

    # Test Case 2: High mean scores and outliers
    department_data = [
        generate_random_data(mean=30, variance=5, num_samples=100),
        generate_random_data(mean=32, variance=5, num_samples=120),
        generate_random_data(mean=29, variance=5, num_samples=110),
        generate_random_data(mean=80, variance=5, num_samples=95),  # High-risk department
        generate_random_data(mean=30, variance=5, num_samples=105),
    ]
    importance_tags = [3, 3, 3, 5, 3]
    score = aggregate_threat_scores(department_data, importance_tags)
    print(f"Test Case 2: Aggregated Score = {score:.2f}")

    # Test Case 3: One department with high-risk users
    department_data = [
        generate_random_data(mean=10, variance=2, num_samples=100),
        generate_random_data(mean=15, variance=2, num_samples=120),
        generate_random_data(mean=12, variance=2, num_samples=110),
        generate_random_data(mean=13, variance=2, num_samples=95),
        generate_random_data(mean=40, variance=5, num_samples=105),  # Few high-risk users
    ]
    importance_tags = [3, 3, 3, 3, 3]
    score = aggregate_threat_scores(department_data, importance_tags)
    print(f"Test Case 3: Aggregated Score = {score:.2f}")

    import numpy as np
    import unittest


    def generate_random_data(mean, variance, num_samples):
        return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)


    def aggregate_threat_scores(departments_data, importance_tags):
        total_weighted_score = 0
        total_importance = 0

        print("Debugging: Department means and their contributions to total score:")
        for department, importance in zip(departments_data, importance_tags):
            mean_threat_score = np.mean(department)
            print(f"Mean threat score: {mean_threat_score}, Importance: {importance}")
            total_weighted_score += mean_threat_score * importance
            total_importance += importance

        aggregated_score = total_weighted_score / total_importance if total_importance > 0 else 0
        print(f"Debugging: Total Weighted Score = {total_weighted_score}, Total Importance = {total_importance}")
        print(f"Aggregated Score: {aggregated_score}")
        return aggregated_score


    class TestThreatScoreAggregation(unittest.TestCase):

        def test_no_outliers(self):
            np.random.seed(0)
            departments_data = [
                generate_random_data(mean=30, variance=5, num_samples=50),
                generate_random_data(mean=28, variance=5, num_samples=50),
                generate_random_data(mean=32, variance=5, num_samples=50),
                generate_random_data(mean=31, variance=5, num_samples=50),
                generate_random_data(mean=29, variance=5, num_samples=50),
            ]
            importance_tags = [5, 5, 5, 5, 5]
            aggregated_score = aggregate_threat_scores(departments_data, importance_tags)
            self.assertAlmostEqual(aggregated_score, 30, delta=2)

        def test_varying_importance(self):
            np.random.seed(0)
            departments_data = [
                generate_random_data(mean=20, variance=10, num_samples=50),
                generate_random_data(mean=25, variance=10, num_samples=50),
                generate_random_data(mean=45, variance=10, num_samples=50),
                generate_random_data(mean=30, variance=10, num_samples=50),
                generate_random_data(mean=35, variance=10, num_samples=50),
            ]
            importance_tags = [1, 2, 5, 2, 3]
            aggregated_score = aggregate_threat_scores(departments_data, importance_tags)
            self.assertTrue(20 <= aggregated_score <= 40)


    def test_high_threat_department(self):
        np.random.seed(0)
        engineering = generate_random_data(mean=20, variance=10, num_samples=50)
        marketing = generate_random_data(mean=25, variance=10, num_samples=50)
        finance = generate_random_data(mean=75, variance=5, num_samples=50)  # High-risk department
        hr = generate_random_data(mean=30, variance=10, num_samples=50)
        science = generate_random_data(mean=35, variance=10, num_samples=50)

        departments_data = [engineering, marketing, finance, hr, science]
        importance_tags = [3, 3, 3, 3, 3]

        print("Debugging: Test High Threat Department")
        for idx, department in enumerate(departments_data):
            print(f"Department {idx + 1} mean threat score: {np.mean(department)}")

        aggregated_score = aggregate_threat_scores(departments_data, importance_tags)
        print(f"Aggregated Score in High Threat Department Test: {aggregated_score}")

        self.assertTrue(50 <= aggregated_score <= 70)  # Adjust this range if needed


    if __name__ == '__main__':
        # Direct test cases
        np.random.seed(42)

        # Test Case 1: No outliers, equal importance
        department_data = [
            generate_random_data(mean=30, variance=5, num_samples=100),
            generate_random_data(mean=32, variance=5, num_samples=120),
            generate_random_data(mean=29, variance=5, num_samples=110),
            generate_random_data(mean=31, variance=5, num_samples=95),
            generate_random_data(mean=30, variance=5, num_samples=105),
        ]
        importance_tags = [3, 3, 3, 3, 3]
        score = aggregate_threat_scores(department_data, importance_tags)
        print(f"Test Case 1: Aggregated Score = {score:.2f}")

        # Test Case 2: High mean scores and outliers
        department_data = [
            generate_random_data(mean=30, variance=5, num_samples=100),
            generate_random_data(mean=32, variance=5, num_samples=120),
            generate_random_data(mean=29, variance=5, num_samples=110),
            generate_random_data(mean=80, variance=5, num_samples=95),  # High-risk department
            generate_random_data(mean=30, variance=5, num_samples=105),
        ]
        importance_tags = [3, 3, 3, 5, 3]
        score = aggregate_threat_scores(department_data, importance_tags)
        print(f"Test Case 2: Aggregated Score = {score:.2f}")

        # Test Case 3: One department with high-risk users
        department_data = [
            generate_random_data(mean=10, variance=2, num_samples=100),
            generate_random_data(mean=15, variance=2, num_samples=120),
            generate_random_data(mean=12, variance=2, num_samples=110),
            generate_random_data(mean=13, variance=2, num_samples=95),
            generate_random_data(mean=40, variance=5, num_samples=105),  # Few high-risk users
        ]
        importance_tags = [3, 3, 3, 3, 3]
        score = aggregate_threat_scores(department_data, importance_tags)
        print(f"Test Case 3: Aggregated Score = {score:.2f}")

        unittest.main(exit=False)

