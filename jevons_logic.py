class JevonsCompass:
    def __init__(self, product_name, baseline_waste_kg):
        self.product = product_name
        self.baseline_waste = baseline_waste_kg
        self.efficiency_gain = 0.0 # Percentage (0.0 to 1.0)
        self.production_volume = 1000 # Standard batch

    def apply_ai_efficiency(self, gain_percent, rebound_volume_increase):
        """
        Simulates the Jevons Paradox:
        If efficiency goes UP, does production volume SPIKE?
        """
        self.efficiency_gain = gain_percent
        
        # Calculate waste per unit after efficiency improvement
        # (e.g., less scrap due to better nesting)
        waste_per_unit = (self.baseline_waste / self.production_volume) * (1 - self.efficiency_gain)
        
        # The Paradox: Volume increases because it's cheaper/faster to make
        new_volume = self.production_volume + rebound_volume_increase
        
        # Total New Waste
        total_new_waste = waste_per_unit * new_volume
        
        return self.audit_result(total_new_waste)

    def audit_result(self, total_new_waste):
        print(f"--- AUDIT: {self.product} ---")
        print(f"Baseline Waste: {self.baseline_waste}kg")
        print(f"New Waste (Post-Efficiency): {total_new_waste:.2f}kg")
        
        if total_new_waste > self.baseline_waste:
            return "STATUS: RED ZONE (Jevons Paradox Detected). Efficiency increased pollution."
        else:
            return "STATUS: GREEN ZONE. True Decoupling Achieved."

# --- SIMULATION: Standard Sneaker Development ---
# Scenario: AI makes sampling 50% faster, so the design team makes 3x more samples.

audit = JevonsCompass("Trail Runner V4", baseline_waste_kg=500)
status = audit.apply_ai_efficiency(gain_percent=0.50, rebound_volume_increase=2000)

print(status)
