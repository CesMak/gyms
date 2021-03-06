import unittest
from witches import witches
import numpy as np

opts_rl   = {"names": ["Max", "Lea", "Jo", "Tim"], "type": ["RL", "RL", "RL", "RL"], "nu_shift_cards": 2, "nu_cards": 15, "active_player": 3, "seed": None, "colors": ['B', 'G', 'R', 'Y'], "value_conversion": {11: "^11", 15: "J"}}
opts_rand = {"names": ["Max", "Lea", "Jo", "Tim"], "type": ["RANDOM", "RL", "RANDOM", "RANDOM"], "nu_shift_cards": 2, "nu_cards": 15, "active_player": 3, "seed": None, "colors": ['B', 'G', 'R', 'Y'], "value_conversion": {11: "^11", 15: "J"}}

class gameLogic(unittest.TestCase):
    def setUp(self):
        print ("\n\nIn method", self._testMethodName,"\n")

    def initGame(self, opts, seed=None):
        opts["seed"] = seed
        test_game     = witches(opts)
        test_game.reset()

        #print(test_game.getState().flatten().astype(np.int).shape)

        test_game.printHands()
        print("\n")
        return test_game

    #@unittest.skip
    def test_randomPlay(self):
        test_game = self.initGame(opts_rl, seed=22)

        #shift cards:
        for i in [1, 3, 9, 0, 5, 12, 10, 2]:
            rewards, corr_move, done = test_game.play_ai_move(i, print_=True)

        print("\n")
        tricks = [[47, 49, 48, 46],[53,54,57,58]]
        for i in tricks:
            for j in i:
                rewards, corr_move, done = test_game.play_ai_move(j, print_=True)

    #@unittest.skip
    def test_getBinaryOptions(self):
        test_game = self.initGame(opts_rl, seed=22)

        #shift cards:
        for i in [1, 3, 9, 0, 5, 12, 10, 2]:
            rewards, corr_move, done = test_game.play_ai_move(i, print_=False)

        tricks = [[47, 49, 48]]
        for i in tricks:
            for j in i:
                rewards, corr_move, done = test_game.play_ai_move(j, print_=True)

        play_options = test_game.getBinaryOptions(test_game.active_player, test_game.nu_players, test_game.nu_cards)
        assert len(play_options) == 60
        assert len(test_game.state2Cards(play_options)) == 5

        print("Play options:", play_options)
        print(len(play_options))
        print(test_game.state2Cards(play_options))

    #@unittest.skip
    def test_getState(self):
        test_game = self.initGame(opts_rl, seed=22)

        #shift cards:
        for i in [1, 3, 9, 0, 5, 12, 10, 2]:
            rewards, corr_move, done = test_game.play_ai_move(i, print_=False)

        print("Hand after shifting:")
        test_game.printHands()
        print("\n")

        tricks = [[47, 49, 48]]
        for i in tricks:
            for j in i:
                rewards, corr_move, done = test_game.play_ai_move(j, print_=True)

        #play_options = test_game.getBinaryOptions(test_game.active_player, test_game.nu_players, test_game.nu_cards)
        print(test_game.player_names[test_game.active_player]+" state is:")
        test_game.printCurrentState()

        res_vector = test_game.getState()
        assert len(res_vector[0]) == 255

    #@unittest.skip
    def test_colorFree(self):
        # wichtig color free darf erst auffallen nachdem ein spieler nicht mehr die farbe bekannt hat
        test_game = self.initGame(opts_rl, seed=22)

        #shift cards:
        for i in [1, 3, 9, 0, 5, 12, 10, 2]:
            rewards, corr_move, done = test_game.play_ai_move(i, print_=False)

        print("Hand after shifting:")
        test_game.printHands()
        print("\n")

        tricks = [[47, 49, 48, 46],[53,54,57,58],[7, 1, 12, 10], [3, 9, 0, 5], [25, 15, 26, 24], [55, 50, 51, 44], [56, 32]]
        for i in tricks:
            for j in i:
                rewards, corr_move, done = test_game.play_ai_move(j, print_=True)

        print("\nHand after playing some rounds:")
        test_game.printHands()

        print(test_game.player_names[test_game.active_player]+" state is:")
        test_game.printCurrentState()

        on_table, on_hand, played, play_options, add_states = test_game.splitState()
        self.assertEqual(add_states.tolist(), [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1])

    def test_randomPlaying(self):
        test_game = self.initGame(opts_rand, seed=22)

        #shift cards:
        for ai_action in [3, 12]:
            rewards, _, _ = test_game.playUntilAI(print_=True)
            rewards, corr_moves, done = test_game.stepRandomPlay(ai_action, print_=True)

        #play cards:
        for ai_action in [8, 16, 20]:
            rewards, _, _ = test_game.playUntilAI(print_=True)
            rewards, corr_moves, done = test_game.stepRandomPlay(ai_action, print_=True)

        assert test_game.active_player == 1

    def test_countResult(self):
        print("TODO play specific cards! and test counting result etc.")

        # print("Hand after shifting:")
        # test_game.printHands()
        # print("\n")
        #
        # tricks = [[47, 49, 48, 46],[53,54,57,58],[7, 1, 12, 10], [3, 9, 0, 5], [25, 15, 26, 24], [55, 50, 51, 44], [56, 32]]
        # for i in tricks:
        #     for j in i:
        #         rewards, corr_move, done = test_game.play_ai_move(j, print_=True)
        #
        # print("\nHand after playing some rounds:")
        # test_game.printHands()
        #
        # print(test_game.player_names[test_game.active_player]+" state is:")
        # test_game.printCurrentState()
        #
        # on_table, on_hand, played, play_options, add_states = test_game.splitState()
        # self.assertEqual(add_states.tolist(), [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1])


        # res_vector = test_game.getState()
        # assert len(res_vector[0]) == 255

        # print("Start playing\n")
        # for i in [1, 2]:
        #     rewards, corr_moves, done = test_game.step(i, print_=True)

        # test_game.reset()
        # print(test_game.players[1].hand)
        # test_game.playUntilAI(print_=True)
        # for i in [3, 12, 8, 2, 15, 13]:
        #     rewards, corr_moves, done = test_game.stepRandomPlay(i, print_=True)
        # print(rewards, corr_moves, done)

        # test_game.reset()
        # print(test_game.players[1].hand)
        # test_game.playUntilAI(print_=True)
        # for i in [3, 12, 8, 2, 15, 13]:
        #     print("I try now", i)
        #     rewards, corr_moves, done = test_game.stepRandomPlay(i, print_=True)
        #     print("after stepRandom", rewards, done)
        #     if done:
        #         print("inside done, reset game noew!")
        #         test_game.reset()
        #         test_game.playUntilAI(True)
        #
        # print(rewards, corr_moves, done)


    # def returnResults(rewards, round_finished, gameOver):
    #     if rewards["ai_reward"] is None: # illegal move
    #         return None, self.correct_moves, True
    #     elif gameOver and "final_rewards" in rewards:
    #         # case that ai plays last card:
    #         mean_random = (sum(rewards["final_rewards"])- rewards["final_rewards"][1])/3
    #         print("mean_random:", mean_random, rewards["final_rewards"],  self.correct_moves)
    #         return [rewards["final_rewards"][1], mean_random], self.correct_moves, gameOver
    #
    # def test_randomPlay(self):
    #     test_game     = game(         {"names": ["Max", "Lea", "Jo", "Tim"], "type": ["RANDOM", "RL", "RANDOM", "RANDOM"], "nu_shift_cards": 2, "nu_cards": 8, "seed": 18})
    #
    #     # TODO SHIFTING PHASE included!
    #     for i in [5, 8, 9, 0, 20, 22, 24, 13, 28, 25, 0]:
    #         cp = test_game.active_player
    #         if "RL" in test_game.player_type[cp]:                 # if ai is starting
    #             rewards, round_finished, gameOver = test_game.play_ai_move(i, print_=True)
    #             returnResults(rewards, round_finished, gameOver )
    #         elif "RANDOM" in test_game.player_type[cp]:           # if random is starting
    #             rewards, round_finished, gameOver = test_game.playUntilAI(print_=True)
    #             returnResults(rewards, round_finished, gameOver )
    #             rewards, round_finished, gameOver = test_game.play_ai_move(i, print_=True)
    #             returnResults(rewards, round_finished, gameOver )


    # def test_shifting(self):
    #     options   = {"names": ["Max", "Lea", "Jo", "Tim"], "type": ["RL", "RL", "RL", "RL"], "nu_shift_cards": 2, "nu_cards": 10, "seed": 13}
    #     my_game   = game(options)
    #
    #     #shifting:
    #     for i in [1, 4, 0, 5, 3, 14, 6, 38]:
    #         rewards, round_finished, done = my_game.play_ai_move(i, print_=True)
    #         state = my_game.getState().flatten().astype(np.int)
    #         print("\t",rewards, round_finished, done)
    #         print("\tNext state:")
    #         my_game.printCurrentState()
    #
    #     #playing:
    #     for i in [0, 8, 1, 2, 16, 9]:
    #         rewards, round_finished, done = my_game.play_ai_move(i, print_=True)
    #         state = my_game.getState().flatten().astype(np.int)
    #         print("\t",rewards, round_finished, done)
    #         print("\tNext state:")
    #         my_game.printCurrentState()

    #
    # def test_nuCards(self):
    #     for j in range(16):
    #         options   = {"names": ["Max", "Lea", "Jo", "Tim"], "type": ["RANDOM", "RANDOM", "RL", "RANDOM"], "nu_shift_cards": 0, "nu_cards": j, "seed": None}
    #         my_game   = game(options)
    #         print("NuCards:", j)
    #         for play in my_game.players:
    #             print(play.hand, len(play.hand))
    #             self.assertEqual(len(play.hand), j)
    #     print("\n")
    #
    # def test_idx(self):
    #     options   = {"names": ["Max", "Lea", "Jo", "Tim"], "type": ["RL", "RANDOM", "RL", "RANDOM"], "nu_shift_cards": 0, "nu_cards": 4, "seed": -1}
    #     my_game   = game(options)
    #     for i in range(my_game.nu_cards*my_game.nu_players):
    #         card = my_game.idx2Card(i)
    #         self.assertEqual(card.idx, i)
    #         print(card)
    #     print("\n")
    #
    #
    # def test_step(self):
    #     #TODO add assert here
    #     options   = {"names": ["Max", "Lea", "Jo", "Tim"], "type": ["RL", "RANDOM", "RL", "RANDOM"], "nu_shift_cards": 0, "nu_cards": 4, "seed": 5}
    #     my_game   = game(options)
    #     my_game.reset()
    #     for play in my_game.players:
    #         print(play.hand, len(play.hand))
    #     #RL plays first card:
    #     rewards, round_finished, gameOver = my_game.play_ai_move(my_game.players[0].hand[0].idx, print_=True)
    #
    #     print(rewards, round_finished, gameOver)
    #     print("\n")
    #
    #
    # def test_getValidOptions(self):
    #     print("\ntest_getValidOptions:")
    #     options   = {"names": ["Max", "Lea", "Jo", "Tim"], "type": ["RL", "RL", "RL", "RL"], "nu_shift_cards": 0, "nu_cards": 4, "seed": 5}
    #     my_game   = game(options)
    #     my_game.reset()
    #
    #     for play in my_game.players:
    #         print("\t", play.hand, len(play.hand))
    #
    #     print("\n\t>>>>Start options:")
    #     for i in range(4):
    #         options_start = my_game.getValidOptions(i)
    #         self.assertEqual(options_start, [0, 1, 2, 3])
    #
    #     print("\n\t>>>>playing a color at the start: options:")
    #     rewards, round_finished, gameOver = my_game.play_ai_move(my_game.players[0].hand[1].idx, print_=True)
    #     opt1= my_game.getValidOptions(1)
    #     opt2= my_game.getValidOptions(2)
    #     opt3= my_game.getValidOptions(3) # does not has the color!
    #     self.assertEqual(opt1, [1,3])
    #     self.assertEqual(opt2, [2,3])
    #     self.assertEqual(opt3, [0, 1, 2,3])
    #
    #     print("\n\t>>>>playing a joker at the start: options:")
    #     my_game.reset()
    #     rewards, round_finished, gameOver = my_game.play_ai_move(my_game.players[1].hand[3].idx, print_=True)
    #     for i in [0,2,3]:
    #         options = my_game.getValidOptions(i)
    #         self.assertEqual(options, [0, 1, 2, 3])
    #         print("\t\t", i, options)
    #
    #     print("\n\t>>>>playing a joker and color at the start: options:")
    #     my_game.reset()
    #     rewards, round_finished, gameOver = my_game.play_ai_move(my_game.players[2].hand[2].idx, print_=True)
    #     rewards, round_finished, gameOver = my_game.play_ai_move(my_game.players[3].hand[0].idx, print_=True)
    #     print("Active Player Hand:", my_game.players[my_game.active_player].hand)
    #     opt1= my_game.getValidOptions(0) # has no blue!
    #     opt2= my_game.getValidOptions(1)
    #     opt3= my_game.getValidOptions(2)
    #     self.assertEqual(opt1,  [0, 1, 2,3])
    #     self.assertEqual(opt2, [0,3])
    #     self.assertEqual(opt3, [0])
    #     print("\n")
    #
    # def test_getState(self):
    #     print("\ntest_getState:")
    #     options   = {"names": ["Max", "Lea", "Jo", "Tim"], "type": ["RL", "RL", "RL", "RL"], "nu_shift_cards": 0, "nu_cards": 4, "seed": 5}
    #     my_game   = game(options)
    #     my_game.reset()
    #
    #     for play in my_game.players:
    #         print("\t", play.hand, len(play.hand))
    #     #test binary options:
    #     options = my_game.players[my_game.active_player].getBinaryOptions(my_game.getInColor(), my_game.nu_players, my_game.nu_cards, shifting_phase=my_game.shifting_phase)
    #     cards = my_game.state2Cards(options)
    #     self.assertEqual(str(cards), "[13 of G_5, 12 of R_8, J of R_11, 12 of Y_12]")
    #     print(options, cards)
    #
    #     on_table, on_hand, played = my_game.getmyState(my_game.active_player, my_game.nu_players, my_game.nu_cards)
    #     for i,j in zip([on_table, on_hand, played], ["on_table", "on_hand", "played"]):
    #          print(j, i, my_game.state2Cards(i))
    #
    #     rewards, round_finished, gameOver = my_game.play_ai_move(my_game.players[0].hand[0].idx, print_=True)
    #     rewards, round_finished, gameOver = my_game.play_ai_move(my_game.players[1].hand[0].idx, print_=True)
    #     on_table, on_hand, played = my_game.getmyState(my_game.active_player, my_game.nu_players, my_game.nu_cards)
    #     for i,j in zip([on_table, on_hand, played], ["on_table", "on_hand", "played"]):
    #          print(j, i, my_game.state2Cards(i))
    #
    #     rewards, round_finished, gameOver = my_game.play_ai_move(my_game.players[2].hand[1].idx, print_=True)
    #     rewards, round_finished, gameOver = my_game.play_ai_move(my_game.players[3].hand[2].idx, print_=True)
    #     on_table, on_hand, played = my_game.getmyState(my_game.active_player, my_game.nu_players, my_game.nu_cards)
    #     for i,j in zip([on_table, on_hand, played], ["on_table", "on_hand", "played"]):
    #          print(j, i, my_game.state2Cards(i))
    #
    #     ##Testing additional State:
    #     print("\t\t>>>>Add State testing:")
    #     for play in my_game.players:
    #         print("\t", play.hand, len(play.hand))
    #     rewards, round_finished, gameOver = my_game.play_ai_move(my_game.players[2].hand[0].idx, print_=True)
    #     rewards, round_finished, gameOver = my_game.play_ai_move(my_game.players[3].hand[0].idx, print_=True)
    #     rewards, round_finished, gameOver = my_game.play_ai_move(my_game.players[0].hand[0].idx, print_=True)
    #     for i in range(4):
    #         print("Add state:",i, my_game.getAdditionalState(i), "win idx, free of B G R Y")
    #
    # def test_randomPlay(self):
    #     print("inside test random play")

if __name__ == '__main__':
    unittest.main()
