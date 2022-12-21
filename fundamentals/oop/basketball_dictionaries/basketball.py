from data.players import players
from data.objects import kevin, jason, kyrie


class Player:
    def __init__(self, player_info):
        self.name = player_info["name"]
        self.age = player_info["age"]
        self.position = player_info["position"]
        self.team = player_info["team"]

    @classmethod
    def get_team(cls, list):
        new_team = []
        for player in list:
            new_team.append(Player(player))
        return new_team


# Create your Player instances here!
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

new_team = Player.get_team(players)
print(new_team)
