import pytest
from brute import Brute
from unittest.mock import Mock, patch


todo = pytest.mark.skip(reason='todo: pending spec')

def describe_Brute():

    @pytest.fixture
    def cracker():
        return Brute("TDD")
    


    def describe_bruteOnce():

        def it_returns_brute_once(cracker):
            brute = cracker


        def it_woll_return_correct__if_guess_is_correct(cracker):
                assert cracker.bruteOnce("TDD") is True


        def it_will_return_true_when_attempt_is_correct():
                secret_string = "password123"
                brute = Brute(secret_string)
                assert brute.bruteOnce(secret_string) is True


        def it_will_return_false_when_guess_is_incorrect(cracker):
            assert cracker.bruteOnce("pass123") == False


        def it_will_return_false_when_attempt_wrong():
             secret_string = "password123"
             brute = Brute(secret_string)
             assert brute.bruteOnce("pass123") == False



    def describe_bruteMany():

        def it_calls_hash(cracker):
            with patch("brute.Brute.hash", return_value=cracker.hash("TDD")) as mock_hash:
                cracker.bruteMany(limit=1)
                mock_hash.assert_called()

        def it_finds_correct_guess_with_limit_of_4(cracker):
            with patch("brute.Brute.randomGuess", side_effect=["wrong1", "wrong2", "TDD", "wrong3"]) as mock_random_guess:
                time = cracker.bruteMany(limit=4)
                mock_random_guess.assert_called()
                assert time > 0 

        def it_fails_to_find_correct_guess_with_limit_of_4(cracker):
            with patch(
                "brute.Brute.randomGuess",
                side_effect=["wrong1", "wrongpass", "wrongpass3", "wrongpass4"]) as mock_random_guess:
                time = cracker.bruteMany(limit=4)
                mock_random_guess.assert_called()
                assert time == -1