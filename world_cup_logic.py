import random
from copy import deepcopy


class WorldCup:
    def __init__(self, rankings):
        self.round_of_16_matches = []
        self.quarter_final_matches = []
        self.semi_finals_matches = []

        self.rankings = rankings
        # create 4 pots of teams based on the rankings
        self.pots = self.pots__of_teams()
        # divide the 32 into 8 groups and take into account the ranking
        self.groups = self.group_stage(self.pots)
        # get the 16 teams that go to the next stage
        self.knockout_teams = self.knockout_stage()
        # 8 teams, the winners of the round of 16.
        self.round_of_16 = self.round_of_16(self.knockout_teams)
        # 4 teams, the winners of the quarter-finals.
        self.quarter_finals = self.quarter_finals(self.round_of_16)
        # 2 teams, the winners of the semi-finals.
        self.semi_finals = self.semi_finals(self.quarter_finals)
        #  The team that finished in third place.
        self.third_place = self.third_place_playoff(self.semi_finals, self.quarter_finals)
        # The first and second places of the FIFA World Cup.
        self.first_place, self.second_place = self.final_result(self.semi_finals)

    def generate_matches(self, teams, randomSelect=True):
        """Generate the matches for a stage of the FIFA World Cup.

        Args:
            teams (list): A list of teams.

        Returns:
            list: A list of tuples, each containing two teams. The number of tuples
                is equal to half the number of teams.
        """
        if randomSelect:
            random.shuffle(teams)
            return [(teams[i], teams[len(teams) - 1 - i]) for i in range(len(teams) // 2)]

        return [(teams[i], teams[i + 1]) for i in range(0, len(teams), 2)]


    def simulate_matches(self, matches):
        """Simulate the matches for a stage of the FIFA World Cup.

        Args:
            matches (list): A list of tuples, each containing two teams.

        Returns:
            list: A list of tuples, each containing two teams.
        """
        results = []
        for match in matches:
            # randomly assign a winner for the match
            winner = match[0] if random.randint(0, 1) == 0 else match[1]
            results.append((match[0], match[1], winner))
        return results

    def determine_winners(self, matches):
        """Determine the winners of a stage of the FIFA World Cup.

        Args:
            matches (list): A list of tuples, each containing two teams and a result.

        Returns:
            list: A list of teams, the winners of the stage. The number of teams
                is equal to half the number of matches.
        """
        winners = []
        for match in matches:
            if match[2] == match[0]:
                winners.append(match[0])
            else:
                winners.append(match[1])
        return winners

    def pots__of_teams(self):
        # get a list of the team names
        teams = list(self.rankings.keys())

        # sort the teams by ranking
        teams_sorted = sorted(teams, key=lambda x: self.rankings[x])

        # create a list of four empty lists (for the four pots)
        pots = [[] for _ in range(4)]

        # divide the teams into the four pots
        for i, team in enumerate(teams_sorted):
            pots[i // 8].append(team)

        return pots

    def group_stage(self, pots):
        pots = deepcopy(pots)

        # shuffle each pot
        for pot in pots:
            random.shuffle(pot)

        # create a list of eight empty lists (for the eight groups)
        groups = [[] for _ in range(8)]

        # divide the teams into the eight groups
        for i, group in enumerate(groups):
            for pot in pots:
                group.append(pot.pop(0))

        return groups

    def knockout_stage(self):
        # create a list to store the teams that advance to the knockout stage
        knockout_teams = []

        # simulate the group stage matches
        for group in self.groups:
            # create a dictionary to store the points for each team
            points = {team: 0 for team in group}

            # simulate the matches in the group
            for i, team1 in enumerate(group):
                for team2 in group[i + 1:]:
                    # randomly assign a winner for the match
                    winner = team1 if random.randint(0, 2) == 0 else team2 if random.randint(0, 2) == 1 else 'draw'
                    if winner == 'draw':
                        points[team1] += 1
                        points[team2] += 1
                    else:
                        points[winner] += 3

            # sort the teams by points
            sorted_teams = sorted(points, key=lambda x: points[x], reverse=True)

            # add the top two teams to the list of knockout teams
            knockout_teams.extend(sorted_teams[:2])

        return knockout_teams

    def round_of_16(self, teams):

        matches = self.generate_matches(teams)
        self.round_of_16_matches = matches
        matches_with_results = self.simulate_matches(matches)
        return self.determine_winners(matches_with_results)

    def quarter_finals(self, teams):
        matches = self.generate_matches(teams, False)
        self.quarter_final_matches = matches
        matches_with_results = self.simulate_matches(matches)
        return self.determine_winners(matches_with_results)

    def semi_finals(self, teams):
        matches = self.generate_matches(teams, False)
        self.semi_finals_matches = matches
        matches_with_results = self.simulate_matches(matches)
        return self.determine_winners(matches_with_results)

    def third_place_playoff(self, semi_final_teams, quarter_final_teams):
        # find the losing semi-finalists
        losing_semi_finalists = [team for team in quarter_final_teams if team not in semi_final_teams]

        # simulate the third place play-off match
        third_place_match = (losing_semi_finalists[0], losing_semi_finalists[1])
        third_place_winner = third_place_match[0] if random.randint(0, 1) == 0 else third_place_match[1]

        return third_place_winner

    def final_result(self, semi_final_teams):
        final_match = (semi_final_teams[0], semi_final_teams[1])
        first_place = final_match[0] if random.randint(0, 1) == 0 else final_match[1]
        second_place = final_match[0] if first_place == final_match[1] else final_match[1]

        return first_place, second_place


def main():
    rankings = {
        "Brazil": 1,
        "Germany": 2,
        "Spain": 3,
        "Argentina": 4,
        "France": 5,
        "Belgium": 6,
        "Portugal": 7,
        "Switzerland": 8,
        "England": 9,
        "Colombia": 10,
        "Mexico": 11,
        "Uruguay": 12,
        "Croatia": 13,
        "Russia": 14,
        "Denmark": 15,
        "Sweden": 16,
        "Poland": 17,
        "Senegal": 18,
        "Nigeria": 19,
        "Japan": 20,
        "Iran": 21,
        "South Korea": 22,
        "Egypt": 23,
        "Australia": 24,
        "Peru": 25,
        "Costa Rica": 26,
        "Serbia": 27,
        "Iceland": 28,
        "Tunisia": 29,
        "Panama": 30,
        "Morocco": 31,
        "Saudi Arabia": 32
    }

    wc = WorldCup(rankings)

    for pot in wc.pots:
        print(pot)
    print("-" * 50)

    print("Group stage:")
    for group in wc.groups:
        print(group)
    print("-" * 50)

    print("knockout stage:", wc.knockout_teams)
    print("-" * 50)
    print("Round of 16:", wc.round_of_16)
    print("-" * 50)
    print("Quarter-finals:", wc.quarter_finals)
    print("-" * 50)
    print("Semi-finals:", wc.semi_finals)
    print("-" * 50)
    print("Third place:", wc.third_place)
    print("-" * 50)
    print("Second place:", wc.second_place)
    print("-" * 50)
    print("First place:", wc.first_place)
    print("-" * 50)


if __name__ == "__main__":
    main()
