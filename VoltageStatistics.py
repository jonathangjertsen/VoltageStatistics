from saleae.range_measurements import AnalogMeasurer
import numpy as np

class VoltageStatistics(AnalogMeasurer):
    supported_measurements = ["v_avg", "v_std", "v_med", "v_q05", "v_q95"]

    def __init__(self, requested_measurements):
        super().__init__(requested_measurements)
        self.batches = []

    def process_data(self, data):
        self.batches.append(data.samples)

    def measure(self):
        data = np.concatenate(self.batches)
        return {
            "v_avg": np.mean(data),
            "v_std": np.std(data),
            "v_med": np.median(data),
            "v_q05": np.quantile(data, 0.05),
            "v_q95": np.quantile(data, 0.95),
        }
