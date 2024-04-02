from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class StandardInfluencer(BaseInfluencer):
    INITIAL_PAYMENT_PERCENTAGE = 0.45
    CAMPAIGN_TYPE_MAP = {"HighBudgetCampaign": 1.2, "LowBudgetCampaign": 0.9}

    def calculate_payment(self, campaign: BaseCampaign):
        return float(campaign.budget * self.INITIAL_PAYMENT_PERCENTAGE)

    def reached_followers(self, campaign_type: str):
        multiplier = self.CAMPAIGN_TYPE_MAP[campaign_type]
        result = self.followers * self.engagement_rate * multiplier
        return int(result)
