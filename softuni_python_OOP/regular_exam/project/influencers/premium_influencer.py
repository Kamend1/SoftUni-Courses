from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class PremiumInfluencer(BaseInfluencer):
    INITIAL_PAYMENT_PERCENTAGE = 0.85
    CAMPAIGN_TYPE_MAP = {"HighBudgetCampaign": 1.5, "LowBudgetCampaign": 0.8}

    def calculate_payment(self, campaign: BaseCampaign):
        return float(campaign.budget * self.INITIAL_PAYMENT_PERCENTAGE)

    def reached_followers(self, campaign_type: str):
        multiplier = self.CAMPAIGN_TYPE_MAP[campaign_type]
        result = self.followers * self.engagement_rate * multiplier
        return int(result)
