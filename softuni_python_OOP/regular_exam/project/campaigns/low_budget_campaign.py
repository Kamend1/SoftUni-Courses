from project.campaigns.base_campaign import BaseCampaign


class LowBudgetCampaign(BaseCampaign):
    BUDGET = 2500.0
    ENGAGEMENT_MULTPLIER = 0.9

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, self.BUDGET, required_engagement)

    def check_eligibility(self, engagement_rate: float):
        return engagement_rate >= self.required_engagement * self.ENGAGEMENT_MULTPLIER

    @property
    def campaign_type(self):
        return "LowBudgetCampaign"
