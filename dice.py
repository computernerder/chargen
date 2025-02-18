from enum import Enum
import random as rand


class Dice(Enum):
    d4 = 4
    d6 = 6
    d8 = 8
    d10 = 10
    d12 = 12
    d20 = 20
    d100 = 100



class Roller:
    def __init__(self, dice: Dice):
        self.dice = dice
    
    @staticmethod
    def roll(times: int = 1, dice_type: Dice = Dice.d20)-> list[int]:
        """
        Rolls a specified type of dice a given number of times and returns the results.
        Args:
            times (int): The number of times to roll the dice. Defaults to 1.
            dice_type (Dice): The type of dice to roll. Defaults to Dice.d20.
        Returns:
            list: A list of integers representing the results of each dice roll.
        """        
        return [rand.randint(1, dice_type.value) for _ in range(times)]
    
    @staticmethod
    def initial_attributes_roll() -> list[int]:
        """
        Rolls dice to generate initial attributes for a character.
        This function rolls four six-sided dice (d6) six times, removes the lowest 
        roll from each set of four dice, and sums the remaining three dice. The 
        resulting sums are returned as a list of six values, representing the 
        initial attributes for a character.
        Returns:
            list: A list of six integers, each representing an initial attribute 
            value for a character.
        """
        return [sum(sorted(Roller.roll(4, Dice.d6))[1:]) for _ in range(6)]


def main():
    print(Roller.roll(3, Dice.d20))
    print(Roller.initial_attributes_roll())
    



if __name__ == "__main__":
    main()