import unittest

import deck
import blackjack

class TestDeck(unittest.TestCase):

    def test_create(self):
        expected = [{'type': 'Ace', 'value': 11, 'display': 'Ace of Spades'}, {'type': 'number', 'value': 2, 'display': '2 of Spades'}, {'type': 'number', 'value': 3, 'display': '3 of Spades'}, {'type': 'number', 'value': 4, 'display': '4 of Spades'}, {'type': 'number', 'value': 5, 'display': '5 of Spades'}, {'type': 'number', 'value': 6, 'display': '6 of Spades'}, {'type': 'number', 'value': 7, 'display': '7 of Spades'}, {'type': 'number', 'value': 8, 'display': '8 of Spades'}, {'type': 'number', 'value': 9, 'display': '9 of Spades'}, {'type': 'number', 'value': 10, 'display': '10 of Spades'}, {'type': 'Face', 'value': 10, 'display': 'Jack of Spades'}, {'type': 'Face', 'value': 10, 'display': 'Queen of Spades'}, {'type': 'Face', 'value': 10, 'display': 'King of Spades'}, {'type': 'Ace', 'value': 11, 'display': 'Ace of Hearts'}, {'type': 'number', 'value': 2, 'display': '2 of Hearts'}, {'type': 'number', 'value': 3, 'display': '3 of Hearts'}, {'type': 'number', 'value': 4, 'display': '4 of Hearts'}, {'type': 'number', 'value': 5, 'display': '5 of Hearts'}, {'type': 'number', 'value': 6, 'display': '6 of Hearts'}, {'type': 'number', 'value': 7, 'display': '7 of Hearts'}, {'type': 'number', 'value': 8, 'display': '8 of Hearts'}, {'type': 'number', 'value': 9, 'display': '9 of Hearts'}, {'type': 'number', 'value': 10, 'display': '10 of Hearts'}, {'type': 'Face', 'value': 10, 'display': 'Jack of Hearts'}, {'type': 'Face', 'value': 10, 'display': 'Queen of Hearts'}, {'type': 'Face', 'value': 10, 'display': 'King of Hearts'}, {'type': 'Ace', 'value': 11, 'display': 'Ace of Clubs'}, {'type': 'number', 'value': 2, 'display': '2 of Clubs'}, {'type': 'number', 'value': 3, 'display': '3 of Clubs'}, {'type': 'number', 'value': 4, 'display': '4 of Clubs'}, {'type': 'number', 'value': 5, 'display': '5 of Clubs'}, {'type': 'number', 'value': 6, 'display': '6 of Clubs'}, {'type': 'number', 'value': 7, 'display': '7 of Clubs'}, {'type': 'number', 'value': 8, 'display': '8 of Clubs'}, {'type': 'number', 'value': 9, 'display': '9 of Clubs'}, {'type': 'number', 'value': 10, 'display': '10 of Clubs'}, {'type': 'Face', 'value': 10, 'display': 'Jack of Clubs'}, {'type': 'Face', 'value': 10, 'display': 'Queen of Clubs'}, {'type': 'Face', 'value': 10, 'display': 'King of Clubs'}, {'type': 'Ace', 'value': 11, 'display': 'Ace of Diamonds'}, {'type': 'number', 'value': 2, 'display': '2 of Diamonds'}, {'type': 'number', 'value': 3, 'display': '3 of Diamonds'}, {'type': 'number', 'value': 4, 'display': '4 of Diamonds'}, {'type': 'number', 'value': 5, 'display': '5 of Diamonds'}, {'type': 'number', 'value': 6, 'display': '6 of Diamonds'}, {'type': 'number', 'value': 7, 'display': '7 of Diamonds'}, {'type': 'number', 'value': 8, 'display': '8 of Diamonds'}, {'type': 'number', 'value': 9, 'display': '9 of Diamonds'}, {'type': 'number', 'value': 10, 'display': '10 of Diamonds'}, {'type': 'Face', 'value': 10, 'display': 'Jack of Diamonds'}, {'type': 'Face', 'value': 10, 'display': 'Queen of Diamonds'}, {'type': 'Face', 'value': 10, 'display': 'King of Diamonds'}]
        actual = deck.make_deck()
        self.assertEqual(expected, actual)

    def test_shuffle(self):
        notExpected = [{'type': 'Ace', 'value': 11, 'display': 'Ace of Spades'}, {'type': 'number', 'value': 2, 'display': '2 of Spades'}, {'type': 'number', 'value': 3, 'display': '3 of Spades'}, {'type': 'number', 'value': 4, 'display': '4 of Spades'}, {'type': 'number', 'value': 5, 'display': '5 of Spades'}, {'type': 'number', 'value': 6, 'display': '6 of Spades'}, {'type': 'number', 'value': 7, 'display': '7 of Spades'}, {'type': 'number', 'value': 8, 'display': '8 of Spades'}, {'type': 'number', 'value': 9, 'display': '9 of Spades'}, {'type': 'number', 'value': 10, 'display': '10 of Spades'}, {'type': 'Face', 'value': 10, 'display': 'Jack of Spades'}, {'type': 'Face', 'value': 10, 'display': 'Queen of Spades'}, {'type': 'Face', 'value': 10, 'display': 'King of Spades'}, {'type': 'Ace', 'value': 11, 'display': 'Ace of Hearts'}, {'type': 'number', 'value': 2, 'display': '2 of Hearts'}, {'type': 'number', 'value': 3, 'display': '3 of Hearts'}, {'type': 'number', 'value': 4, 'display': '4 of Hearts'}, {'type': 'number', 'value': 5, 'display': '5 of Hearts'}, {'type': 'number', 'value': 6, 'display': '6 of Hearts'}, {'type': 'number', 'value': 7, 'display': '7 of Hearts'}, {'type': 'number', 'value': 8, 'display': '8 of Hearts'}, {'type': 'number', 'value': 9, 'display': '9 of Hearts'}, {'type': 'number', 'value': 10, 'display': '10 of Hearts'}, {'type': 'Face', 'value': 10, 'display': 'Jack of Hearts'}, {'type': 'Face', 'value': 10, 'display': 'Queen of Hearts'}, {'type': 'Face', 'value': 10, 'display': 'King of Hearts'}, {'type': 'Ace', 'value': 11, 'display': 'Ace of Clubs'}, {'type': 'number', 'value': 2, 'display': '2 of Clubs'}, {'type': 'number', 'value': 3, 'display': '3 of Clubs'}, {'type': 'number', 'value': 4, 'display': '4 of Clubs'}, {'type': 'number', 'value': 5, 'display': '5 of Clubs'}, {'type': 'number', 'value': 6, 'display': '6 of Clubs'}, {'type': 'number', 'value': 7, 'display': '7 of Clubs'}, {'type': 'number', 'value': 8, 'display': '8 of Clubs'}, {'type': 'number', 'value': 9, 'display': '9 of Clubs'}, {'type': 'number', 'value': 10, 'display': '10 of Clubs'}, {'type': 'Face', 'value': 10, 'display': 'Jack of Clubs'}, {'type': 'Face', 'value': 10, 'display': 'Queen of Clubs'}, {'type': 'Face', 'value': 10, 'display': 'King of Clubs'}, {'type': 'Ace', 'value': 11, 'display': 'Ace of Diamonds'}, {'type': 'number', 'value': 2, 'display': '2 of Diamonds'}, {'type': 'number', 'value': 3, 'display': '3 of Diamonds'}, {'type': 'number', 'value': 4, 'display': '4 of Diamonds'}, {'type': 'number', 'value': 5, 'display': '5 of Diamonds'}, {'type': 'number', 'value': 6, 'display': '6 of Diamonds'}, {'type': 'number', 'value': 7, 'display': '7 of Diamonds'}, {'type': 'number', 'value': 8, 'display': '8 of Diamonds'}, {'type': 'number', 'value': 9, 'display': '9 of Diamonds'}, {'type': 'number', 'value': 10, 'display': '10 of Diamonds'}, {'type': 'Face', 'value': 10, 'display': 'Jack of Diamonds'}, {'type': 'Face', 'value': 10, 'display': 'Queen of Diamonds'}, {'type': 'Face', 'value': 10, 'display': 'King of Diamonds'}]
        actual = deck.shuffle_deck(deck.make_deck())
        self.assertNotEqual(notExpected, actual)

    def test_winner1(self):
        expected = 500
        actual = blackjack.determine_winner(1000, 500, 22, 5)
        self.assertEqual(expected, actual)

    def test_winner2(self):
        expected = 1000
        actual = blackjack.determine_winner(1000, 500, 15, 15)
        self.assertEqual(expected, actual)

    def test_winner3(self):
        expected = 1500
        actual = blackjack.determine_winner(1000, 500, 15, 10)
        self.assertEqual(expected, actual)

    def test_winner4(self):
        expected = 500
        actual = blackjack.determine_winner(1000, 500, 10, 15)
        self.assertEqual(expected, actual)

    def test_winner5(self):
        expected = 1500
        actual = blackjack.determine_winner(1000, 500, 15, 22)
        self.assertEqual(expected, actual)

    def test_validBet1(self):
        expected = True
        actual = blackjack.validBet("500", 1000)
        self.assertEqual(expected, actual)
        
    def test_validBet2(self):
        expected = False
        actual = blackjack.validBet("1001", 1000)
        self.assertEqual(expected, actual)

    def test_validBet3(self):
        expected = False
        actual = blackjack.validBet("0", 1000)
        self.assertEqual(expected, actual)