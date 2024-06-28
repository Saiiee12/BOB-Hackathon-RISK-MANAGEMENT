# risk_assessment.py

import pandas as pd

class RiskAssessment:
    def __init__(self, risk_data):
        self.risk_data = risk_data

    def calculate_risk_score(self):
        # Calculate risk score based on likelihood and impact
        risk_score = self.risk_data['likelihood'] * self.risk_data['impact']
        return risk_score

    def identify_high_risks(self, threshold):
        # Identify high risks based on risk score threshold
        high_risks = self.risk_data[self.risk_data['risk_score'] > threshold]
        return high_risks

# Example usage
risk_data = pd.DataFrame({
    'risk_id': [1, 2, 3, 4, 5],
    'likelihood': [0.8, 0.4, 0.6, 0.9, 0.7],
    'impact': [0.9, 0.6, 0.8, 0.5, 0.4],
    'description': ['Risk 1', 'Risk 2', 'Risk 3', 'Risk 4', 'Risk 5']
})

risk_assessment = RiskAssessment(risk_data)
risk_score = risk_assessment.calculate_risk_score()
high_risks = risk_assessment.identify_high_risks(0.5)

print("Risk Score:", risk_score)
print("High Risks:")
print(high_risks)
