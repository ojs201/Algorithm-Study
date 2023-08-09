from collections import Counter
from typing import Dict, List


class FailureRateAnalyzer:
    def __init__(self, nums_stage, stages) -> None:
        self.nums_stage: int = nums_stage
        self.nums_user: int = len(stages)
        self.stage_users: Dict = self.map_stages(stages)

    def map_stages(self, stages) -> Dict:
        counter: Counter = Counter(stages)
        users: Dict = {}
        for i in range(self.nums_stage):
            users[i + 1] = counter.get(i + 1) if counter.get(i + 1) is not None else 0
        return users

    def analyze(self) -> List:
        nums_user: int = self.nums_user
        rates: Dict = {}

        for stage, users in self.stage_users.items():
            rates[stage] = users / nums_user if users != 0 else 0
            nums_user -= users

        return sorted(rates, key=lambda x: rates[x], reverse=True)
