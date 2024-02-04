class ReliabilityMetrics:
    def __init__(self):
        self.number_of_failures = 0
        self.execution_time = 0
        self.mttf = 4  # Mean Time To Failure
        self.mttr = 10  # Mean Time To Repair
        self.mtbf = 1  # Mean Time Between Failures

    def record_failure(self):
        self.number_of_failures += 1

    def record_execution_time(self, time):
        self.execution_time += time

    def calculate_metrics(self):
        self.mtbf = self.mttf + self.mttr
        availability = 0
        if self.mtbf > 0:
            availability = self.mttf / self.mtbf * 100

        failure_rate = 0
        if self.execution_time > 0:
            failure_rate = self.number_of_failures / self.execution_time

        return {
            "MTBF": self.mtbf,
            "Availability": availability,
            "FailureRate": failure_rate
        }
