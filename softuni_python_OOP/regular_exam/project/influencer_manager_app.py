from typing import List

from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    VALID_INFLUENCER_TYPES = ["PremiumInfluencer", "StandardInfluencer"]
    VALID_CAMPAIGN_TYPES = ["HighBudgetCampaign", "LowBudgetCampaign"]

    def __init__(self):
        self.influencers: List[PremiumInfluencer: BaseInfluencer, StandardInfluencer: BaseInfluencer] = []
        self.campaigns: List[HighBudgetCampaign: BaseCampaign, LowBudgetCampaign: BaseCampaign] = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in self.VALID_INFLUENCER_TYPES:
            return f"{influencer_type} is not an allowed influencer type."

        influencer = next(filter(lambda i: i.username == username, self.influencers), None)
        if influencer:
            return f"{username} is already registered."

        inf_object = globals()[influencer_type]
        new_influencer = inf_object(username, followers, engagement_rate)
        self.influencers.append(new_influencer)
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.VALID_CAMPAIGN_TYPES:
            return f"{campaign_type} is not a valid campaign type."

        campaign = next(filter(lambda c: c.campaign_id == campaign_id, self.campaigns), None)
        if campaign:
            return f"Campaign ID {campaign_id} has already been created."

        c_obj = globals()[campaign_type]
        new_campaign = c_obj(campaign_id, brand, required_engagement)
        self.campaigns.append(new_campaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        influencer = next(filter(lambda i: i.username == influencer_username, self.influencers), None)
        if not influencer:
            return f"Influencer '{influencer_username}' not found."

        campaign = next(filter(lambda c: c.campaign_id == campaign_id, self.campaigns), None)
        if not campaign:
            return f"Campaign with ID {campaign_id} not found."

        eligible = campaign.check_eligibility(influencer.engagement_rate)
        if not eligible:
            return (f"Influencer '{influencer.username}' does not meet the "
                    f"eligibility criteria for the campaign with ID {campaign_id}.")

        payment = influencer.calculate_payment(campaign)
        if payment > 0.0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= payment
            influencer.campaigns_participated.append(campaign)
            return (f"Influencer '{influencer.username}' has successfully participated "
                    f"in the campaign with ID {campaign_id}.")

    def calculate_total_reached_followers(self):
        total_reached_followers = {}

        for influencer in self.influencers:
            for campaign in influencer.campaigns_participated:
                if campaign not in total_reached_followers.keys():
                    total_reached_followers[campaign] = 0
                total_reached_followers[campaign] += influencer.reached_followers(campaign.campaign_type)

        return total_reached_followers

    def influencer_campaign_report(self, username: str):
        influencer = next(filter(lambda i: i.username == username, self.influencers), None)

        result = influencer.display_campaigns_participated()

        return result

    def campaign_statistics(self):
        result = [f"$$ Campaign Statistics $$"]
        sorted_campaign = sorted(self.campaigns, key=lambda c: (len(c.approved_influencers), -c.budget))

        for campaign in sorted_campaign:
            total_reached_followers = 0
            for influencer in campaign.approved_influencers:
                total_reached_followers += influencer.reached_followers(campaign.campaign_type)
            result.append(f"  * Brand: {campaign.brand}, "
                          f"Total influencers: {len(campaign.approved_influencers)}, "
                          f"Total budget: ${campaign.budget:.2f}, "
                          f"Total reached followers: {total_reached_followers}")

        return "\n".join(result)
