// RiskMitigation.java

import java.util.ArrayList;
import java.util.List;

public class RiskMitigation {
    private List<Risk> risks;

    public RiskMitigation(List<Risk> risks) {
        this.risks = risks;
    }

    public void mitigateRisks() {
        for (Risk risk : risks) {
            if (risk.getRiskScore() > 0.5) {
                // Implement risk mitigation strategies
                System.out.println("Mitigating risk: " + risk.getDescription());
                //...
            }
        }
    }

    public static class Risk {
        private int riskId;
        private double riskScore;
        private String description;

        public Risk(int riskId, double riskScore, String description) {
            this.riskId = riskId;
            this.riskScore = riskScore;
            this.description = description;
        }

        public int getRiskId() {
            return riskId;
        }

        public double getRiskScore() {
            return riskScore;
        }

        public String getDescription() {
            return description;
        }
    }

    public static void main(String[] args) {
        List<Risk> risks = new ArrayList<>();
        risks.add(new Risk(1, 0.8, "Risk 1"));
        risks.add(new Risk(2, 0.4, "Risk 2"));
        risks.add(new Risk(3, 0.6, "Risk 3"));
        risks.add(new Risk(4, 0.9, "Risk 4"));
        risks.add(new Risk(5, 0.7, "Risk 5"));

        RiskMitigation riskMitigation = new RiskMitigation(risks);
        riskMitigation.mitigateRisks();
    }
}
