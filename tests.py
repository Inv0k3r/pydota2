import unittest

from datetime import datetime

from dota2.api import Match, Player


class TestMatches(unittest.TestCase):

    def setUp(self):
        self.data1 = {
            "match_id": 716286966,
            "match_seq_num": 645509729,
            "start_time": 1402618987,
            "lobby_type": 0,
            "players": [
                {"account_id": 4294967295,"player_slot": 0,"hero_id": 0},
                {"account_id": 4294967295,"player_slot": 132,"hero_id": 17}
            ]
        }

        self.match = Match(self.data1)

    def test_raw_data_preserved(self):
        self.assertEqual(self.data1, self.match.raw_data)

    def test_match_id_and_sequence_number_and_lobby_type(self):
        match = self.match
        self.assertEqual(match.id, 716286966)
        self.assertEqual(match.sequence_number, 645509729)
        self.assertEqual(match.lobby_type, 'Public matchmaking')

    def test_match_players(self):
        players = self.match.players

        self.assertTrue(len(players) == 2)

        for player in players:
            self.assertIsInstance(player, Player)

    def test_start_time_returns_datetime(self):
        self.assertIsInstance(self.match.start_time, datetime)

        self.assertEqual(self.match.start_time, 
            datetime(2014, 6, 12, 17, 23, 7))


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.data = {}
    def test_is_radiant(self):
        pass

    def test_player_hero_maps(self):
        pass

    def test_null_hero_(self):
        pass

    def test_anonymous_name(self):
        pass

    def test_to_detail_not_anonymous_raise(self):
        pass

    def test_available_attributes(self):
        pass


class TestDota2(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
