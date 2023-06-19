# Local import
from otp_auth.policies import VerifiedAccessPolicy


class RankingAccessPolicy(VerifiedAccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve", "get_top5_ranking"],
            "principal": ['permission:view_ranking'],
            "effect": "allow"
        },
    ]
