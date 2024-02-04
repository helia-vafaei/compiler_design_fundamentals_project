class AlbrechtsFunctionPoints:
    def __init__(self, components_counts, characteristic_scores):
        self.components_counts = components_counts
        self.characteristic_scores = characteristic_scores

    def calculate_function_counts(self):
        weights = {
            'external_input': {'low': 3, 'average': 4, 'high': 6},
            'external_output': {'low': 4, 'average': 5, 'high': 7},
            'logical_internal_file': {'low': 5, 'average': 7, 'high': 10},
            'external_interface_file': {'low': 7, 'average': 10, 'high': 15},
            'external_inquiry': {'low': 3, 'average': 4, 'high': 6},
        }

        function_counts = sum(weights[component][complexity] * self.components_counts[component][complexity]
                             for component in self.components_counts
                             for complexity in self.components_counts[component])

        return function_counts

    def calculate_value_adjustment_factor(self):
        vaf = 0.65 + 0.01 * sum(self.characteristic_scores.values())
        return vaf

    def calculate_function_points(self):
        function_counts = self.calculate_function_counts()
        vaf = self.calculate_value_adjustment_factor()

        function_points = function_counts * vaf
        return function_points
