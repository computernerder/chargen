from constants import *
from dice import *


cc = CharacterConstants





class Character:
    def __init__(self, name: str, race: Race, char_class: Classes, attributes: dict[Attribute, list[int,int]], skills: dict[Skills, list[int, int]], combat: CombatTraits, background: Background, alignment: Alignment, xp: int = 0, level: int = 1):
        self.name:str = name
        self.race: Race  = race
        self.char_class: Classes = char_class
        self.attributes: dict[Attribute, list[int, int]] = attributes
        self.skills: dict[Skills, dict[str, int | Attribute | bool]] = skills
        self.combat: dict[CombatTraits, int | bool | Dice | dict[str, int]] = combat
        self.background: Background = background
        self.alignment: Alignment = alignment
        self.xp: int = xp
        self.level: int = level
        
        self.Modify = Character.Modify(self)

    def __str__(self):
        return f"Name: {self.name},\n Race: {self.race.value}\n, Class: {self.char_class.value},\n Level: {self.level},\n XP: {self.xp},\n Background: {self.background.value},\n Alignment: {self.alignment.value},\n Attributes: {self.attributes},\n Skills: {self.skills},\n Combat: {self.combat}"

    def list_attributes(self):
        print("---------Attributes---------")
        for attr, value in self.attributes.items():
            print(f"{attr.value}: {value[0]}, M:{value[1]}")

    def list_skills(self):
        print("---------Skills---------")
        for skill, value in self.skills.items():
            print(f"{skill.value}: {value[0]}, M:{value[1]}")

    def list_combat(self):
        print("---------Combat Traits---------")
        for trait, value in self.combat.items():
            print(f"{trait.value}: {value}")

    def set_attribute(self, attr: Attribute, value: int):
        self.attributes[attr][0] = value


    def set_character_attributes(self):
        # Get Characters Values
        values = Roller.initial_attributes_roll()

        # Set Characters Attributes
        for i, attr in enumerate(self.attributes):
            self.attributes[attr][0] = values[i]




    
        
    # Character modification class
    class Modify:
        def __init__(self, character):
            self.character = character

        def level_up(self):
            self.character.level += 1
            print(f"{self.character.name} has leveled up to level {self.character.level}!")

        def add_xp(self, amount: int):
            print(f"{self.character.name} has gained {amount} XP!")
            self.character.xp += amount
            new_level = cc.xp_level(self.character.xp)
            if new_level > self.character.level:
                self.character.level = new_level
                self.level_up()

        def add_attribute(self, attribute: Attribute, value: int):
            self.character.attributes[attribute][0] += value
            print(f"{self.character.name} has gained {value} in {attribute.value}!")

    
    


def main():
    player = Character(name="Bob",
                       race=Race.Dragonborn,char_class=Classes.Fighter,
                       attributes={Attribute.Strength: [15,0], Attribute.Dexterity: [10,0], Attribute.Constitution: [14,0], Attribute.Intelligence: [8,0], Attribute.Wisdom: [12,0], Attribute.Charisma: [13,0]},
                       skills={Skills.Acrobatics: [0, 0], Skills.Animal_Handling: [0, 0], Skills.Arcana: [0, 0], Skills.Athletics: [0, 0], Skills.Deception: [0, 0], Skills.History: [0, 0], Skills.Insight: [0, 0], Skills.Intimidation: [0, 0], Skills.Investigation: [0, 0], Skills.Medicine: [0, 0], Skills.Nature: [0, 0], Skills.Perception: [0, 0], Skills.Performance: [0, 0], Skills.Persuasion: [0, 0], Skills.Religion: [0, 0], Skills.Sleight_of_Hand: [0, 0], Skills.Stealth: [0, 0], Skills.Survival: [0, 0]},
                       combat={CombatTraits.Armor_Class: 16, CombatTraits.Initiative: 0, CombatTraits.Speed: 30, CombatTraits.Hit_Points: 10, CombatTraits.Hit_Dice: Dice.d8, CombatTraits.Death_Saves: {"Successes": 0, "Failures": 0}},
                       background=Background.Noble,
                       alignment=Alignment.Lawful_Good)
    
    player.list_attributes()
    player.set_character_attributes()
    player.list_attributes()
    
    
    # # print(player)
    # player.list_attributes()
    # player.list_skills()
    # player.list_combat()
    # print(f"Player XP: {player.xp}")
    # print(f"{player.attributes[Attribute.Strength][0]}")

    # player.Modify.add_xp(1000)
    # player.Modify.add_attribute(Attribute.Strength, 2)

    # print(f"Player XP: {player.xp}")
    # print(f"Strength:  {player.attributes[Attribute.Strength][0]}")



if __name__ == "__main__":
    main()