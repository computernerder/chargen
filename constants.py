from enum import Enum
from dice import *
#Character Stats

class Skills(Enum):
    Acrobatics = "Acrobatics"
    Animal_Handling = "Animal Handling"
    Arcana = "Arcana"
    Athletics = "Athletics"
    Deception = "Deception"
    History = "History"
    Insight = "Insight"
    Intimidation = "Intimidation"
    Investigation = "Investigation"
    Medicine = "Medicine"
    Nature = "Nature"
    Perception = "Perception"
    Performance = "Performance"
    Persuasion = "Persuasion"
    Religion = "Religion"
    Sleight_of_Hand = "Sleight of Hand"
    Stealth = "Stealth"
    Survival = "Survival"

class Attribute(Enum):
    Strength = "Strength"
    Dexterity = "Dexterity"
    Constitution = "Constitution"
    Intelligence = "Intelligence"
    Wisdom = "Wisdom"
    Charisma = "Charisma"

class Classes(Enum):
    Barbarian = "Barbarian"
    Bard = "Bard"
    Cleric = "Cleric"
    Druid = "Druid"
    Fighter = "Fighter"
    Monk = "Monk"
    Paladin = "Paladin"
    Ranger = "Ranger"
    Rogue = "Rogue"
    Sorcerer = "Sorcerer"
    Warlock = "Warlock"
    Wizard = "Wizard"

    
class Language(Enum):
    Common = "Common"
    Dwarvish = "Dwarvish"
    Elvish = "Elvish"
    Giant = "Giant"
    Gnomish = "Gnomish"
    Goblin = "Goblin"
    Halfling = "Halfling"
    Orc = "Orc"
    Abyssal = "Abyssal"
    Celestial = "Celestial"
    Draconic = "Draconic"
    Deep_Speech = "Deep Speech"
    Infernal = "Infernal"
    Primordial = "Primordial"
    Sylvan = "Sylvan"
    Undercommon = "Undercommon"

class Alignment(Enum):
    Lawful_Good = "Lawful Good"
    Neutral_Good = "Neutral Good"
    Chaotic_Good = "Chaotic Good"
    Lawful_Neutral = "Lawful Neutral"
    True_Neutral = "True Neutral"
    Chaotic_Neutral = "Chaotic Neutral"
    Lawful_Evil = "Lawful Evil"
    Neutral_Evil = "Neutral Evil"
    Chaotic_Evil = "Chaotic Evil"



class Size(Enum):
    Tiny = ("Tiny", -2)
    Small = ("Small", -1)
    Medium = ("Medium", 0)
    Large = ("Large", 1)
    Huge = ("Huge", 2)
    Gargantuan = ("Gargantuan", 3)

    def __init__(self, label, modifier):
        self.label = label
        self.modifier = modifier


class Age(Enum):
    Young = "Young"
    Middle_Aged = "Middle Aged"
    Old = "Old"
    Venerable = "Venerable" 


class Speed(Enum):
    Slow = "Slow"
    Normal = "Normal"
    Fast = "Fast"

class Race(Enum):
    Dwarf = "Dwarf"
    Elf = "Elf"
    Gnome = "Gnome"
    Half_Elf = "Half-Elf"
    Half_Orc = "Half-Orc"
    Halfling = "Halfling"
    Human = "Human"
    Dragonborn = "Dragonborn"
    Tiefling = "Tiefling"

class Biographics(Enum):
    Name = "Name"
    Player = "Player"
    Background = "Background"
    Class = "Class"
    Race = "Species"
    Alignment = "Alignment"
    XP = "XP"
    Level = "Level"

class CombatTraits(Enum):
    Hit_Points = "Hit Points"
    Armor_Class = "Armor Class"
    Initiative = "Initiative"
    Speed = "Speed"
    Proficiency_Bonus = "Proficiency Bonus"
    Inspiration = "Inspiration"
    Hit_Dice = "Hit Dice"
    Death_Saves = "Death Saves"


class Traits(Enum):
    Darkvision = "Darkvision"
    Dwarven_Resilience = "Dwarven Resilience"
    Stonecunning = "Stonecunning"
    Keen_Senses = "Keen Senses"
    Fey_Ancestry = "Fey Ancestry"
    Trance = "Trance"
    Gnome_Cunning = "Gnome Cunning"
    Menacing = "Menacing"
    Relentless_Endurance = "Relentless Endurance"
    Savage_Attacks = "Savage Attacks"
    Lucky = "Lucky"
    Brave = "Brave"
    Halfling_Nimbleness = "Halfling Nimbleness"
    Draconic_Ancestry = "Draconic Ancestry"
    Breath_Weapon = "Breath Weapon"
    Damage_Resistance = "Damage Resistance"
    Hellish_Resistance = "Hellish Resistance"
    Infernal_Legacy = "Infernal Legacy"
    Skill_Versatility = "Skill Versatility"
    Animal_Friendship = "Animal Friendship"
    Natural_Explorer = "Natural Explorer"
    Cunning_Action = "Cunning Action"
    Second_Wind = "Second Wind"
    Action_Surge = "Action Surge"
    Martial_Archetype = "Martial Archetype"
    Divine_Sense = "Divine Sense"
    Lay_on_Hands = "Lay on Hands"
    Fighting_Style = "Fighting Style"
    Spellcasting = "Spellcasting"
    Wild_Shape = "Wild Shape"
    Extra_Attack = "Extra Attack"
    Divine_Smite = "Divine Smite"
    Divine_Health = "Divine Health"
    

class Weapon(Enum):
    Club = "Club"
    Dagger = "Dagger"
    Greatclub = "Greatclub"
    Handaxe = "Handaxe"
    Javelin = "Javelin"
    Light_Hammer = "Light Hammer"
    Mace = "Mace"
    Quarterstaff = "Quarterstaff"
    Sickle = "Sickle"
    Spear = "Spear"
    Crossbow_Light = "Crossbow Light"
    Dart = "Dart"
    Shortbow = "Shortbow"
    Sling = "Sling"
    Battleaxe = "Battleaxe"
    Flail = "Flail"
    Glaive = "Glaive"
    Greataxe = "Greataxe"
    Greatsword = "Greatsword"
    Halberd = "Halberd"
    Lance = "Lance"
    Longsword = "Longsword"
    Maul = "Maul"
    Morningstar = "Morningstar"
    Pike = "Pike"
    Rapier = "Rapier"
    Scimitar = "Scimitar"
    Shortsword = "Shortsword"
    Trident = "Trident"
    War_Pick = "War Pick"
    Warhammer = "Warhammer"
    Whip = "Whip"
    Blowgun = "Blowgun"
    Crossbow_Hand = "Crossbow Hand"
    Crossbow_Heavy = "Crossbow Heavy"
    Longbow = "Longbow"
    Net = "Net"
    Simple = "Simple"
    Martial = "Martial"
    Hand_Crossbow = "Hand Crossbow"
    Light_Crossbow = "Light Crossbow"


class Armor(Enum):
    Padded = "Padded"
    Leather = "Leather"
    Studded_Leather = "Studded Leather"
    Hide = "Hide"
    Chain_Shirt = "Chain Shirt"
    Scale_Mail = "Scale Mail"
    Breastplate = "Breastplate"
    Half_Plate = "Half Plate"
    Ring_Mail = "Ring Mail"
    Chain_Mail = "Chain Mail"
    Splint = "Splint"
    Plate = "Plate"
    Shield = "Shield"
    Light = "Light"
    Medium = "Medium"
    Heavy = "Heavy"
    All = "All"

    
class Tool(Enum):
    Alchemist_Supplies = "Alchemist Supplies"
    Brewer_Supplies = "Brewer Supplies"
    Calligrapher_Supplies = "Calligrapher Supplies"
    Carpenter_Tools = "Carpenter Tools"
    Cartographer_Tools = "Cartographer Tools"
    Cobbler_Tools = "Cobbler Tools"
    Cook_Utensils = "Cook Utensils"
    Glassblower_Tools = "Glassblower Tools"
    Jeweler_Tools = "Jeweler Tools"
    Leatherworker_Tools = "Leatherworker Tools"
    Mason_Tools = "Mason Tools"
    Painter_Supplies = "Painter Supplies"
    Potter_Tools = "Potter Tools"
    Smith_Tools = "Smith Tools"
    Tinker_Tools = "Tinker Tools"
    Weaver_Tools = "Weaver Tools"
    Woodcarver_Tools = "Woodcarver Tools"
    Disguise_Kit = "Disguise Kit"
    Forgery_Kit = "Forgery Kit"
    Herbalism_Kit = "Herbalism Kit"
    Navigator_Tools = "Navigator Tools"
    Poisoner_Kit = "Poisoner Kit"
    Thieves_Tools = "Thieves Tools"
    Artisan_Tools = "Artisan Tools"
    Gaming_Set = "Gaming Set"
    Musical_Instrument = "Musical Instrument"
    Vehicles_Land = "Vehicles Land"
    Vehicles_Water = "Vehicles Water"
    Vehicles_Air = "Vehicles Air"    
    Navigators_Tools = "Navigators Tools"



class Background(Enum):
    Acolyte = "Acolyte"
    Charlatan = "Charlatan"
    Criminal = "Criminal"
    Entertainer = "Entertainer"
    Folk_Hero = "Folk Hero"
    Guild_Artisan = "Guild Artisan"
    Hermit = "Hermit"
    Noble = "Noble"
    Outlander = "Outlander"
    Sage = "Sage"
    Sailor = "Sailor"
    Soldier = "Soldier"
    Urchin = "Urchin"

    
class Equipment(Enum):
    Abacus = "Abacus"
    Acid = "Acid"
    Alchemist_Fire = "Alchemist Fire"
    Antitoxin = "Antitoxin"
    Arcane_Focus = "Arcane Focus"
    Crystal = "Crystal"
    Orb = "Orb"
    Rod = "Rod"
    Staff = "Staff"
    Wand = "Wand"
    Druidic_Focus = "Druidic Focus"
    Holy_Symbol = "Holy Symbol"
    Amulet = "Amulet"
    Emblem = "Emblem"
    Reliquary = "Reliquary"
    Signet_Ring = "Signet Ring"
    Spellbook = "Spellbook"
    Herbalism_Kit = "Herbalism Kit"
    Poisoner_Kit = "Poisoner Kit"
    Thieves_Tools = "Thieves Tools"
    Artisan_Tools = "Artisan Tools"
    Disguise_Kit = "Disguise Kit"
    Forgery_Kit = "Forgery Kit"
    Gaming_Set = "Gaming Set"
    Musical_Instrument = "Musical Instrument"
    Navigator_Tools = "Navigator Tools"
    Vehicles_Land = "Vehicles Land"
    Vehicles_Water = "Vehicles Water"
    Vehicles_Air = "Vehicles Air"
    Crowbar = "Crowbar"
    Hammer = "Hammer"
    Pitons = "Pitons"
    Spikes = "Spikes"
    Torch = "Torch"
    Tinderbox = "Tinderbox"
    Rations = "Rations"
    Waterskin = "Waterskin"
    Hempen_Rope = "Hempen Rope"
    Silk_Rope = "Silk Rope"
    Ball_Bearings = "Ball Bearings"
    Caltrops = "Caltrops"
    Hunting_Trap = "Hunting Trap"
    Lantern = "Lantern"
    Oil = "Oil"
    Potion_Healing = "Potion Healing"
    Potion_Clairvoyance = "Potion Clairvoyance"
    Potion_Diminution = "Potion Diminution"
    Potion_Growth = "Potion Growth"
    Potion_Resistance = "Potion Resistance"
    Potion_Water_Breathing = "Potion Water Breathing"
    Potion_Water_Walking = "Potion Water Walking"
    Potion_Flying = "Potion Flying"
    Potion_Healing_Greater = "Potion Healing Greater"
    Potion_Healing_Superior = "Potion Healing Superior"
    Potion_Healing_Supreme = "Potion Healing Supreme"
    Potion_Invisibility = "Potion Invisibility"
    Potion_Invulnerability = "Potion Invulnerability"
    Potion_Mind_Reading = "Potion Mind Reading"
    Potion_Speed = "Potion Speed"
    Potion_Resistance_Fire = "Potion Resistance Fire"
    Potion_Resistance_Cold = "Potion Resistance Cold"
    Potion_Resistance_Lightning = "Potion Resistance Lightning"
    Potion_Resistance_Acid = "Potion Resistance Acid"
    Potion_Resistance_Poison = "Potion Resistance Poison"
    Potion_Resistance_Force = "Potion Resistance Force"
    Potion_Resistance_Necrotic = "Potion Resistance Necrotic"
    Potion_Resistance_Radiant = "Potion Resistance Radiant"
    Potion_Resistance_Psychic = "Potion Resistance Psychic"
    Potion_Resistance_Thunder = "Potion Resistance Thunder"     
    Small_Knife = "Small Knife"
    Map_of_the_City = "Map of the City"
    Pet_Mouse = "Pet Mouse"
    Token_from_Parents = "Token from Parents"
    
    Bone_Dice_or_Deck_of_Cards = "Bone Dice or Deck of Cards"
    Insignia_of_Rank = "Insignia of Rank"
    Trophy_from_a_Fallen_Enemy = "Trophy from a Fallen Enemy"
    Iron_Pot = "Iron Pot"
    Shovel = "Shovel"
    
    Travelers_Clothes = "Travelers Clothes"
    Letter_of_Introduction = "Letter of Introduction"
    
    Favor_of_an_Admirer = "Favor of an Admirer"
    Quill = "Quill"
    Bottle_of_Ink = "Bottle of Ink"
    Letter_from_a_Dead_Colleague = "Letter from a Dead Colleague"
    Trophy_from_an_Animal = "Trophy from an Animal"
    Lucky_Charm = "Lucky Charm"
    Common_Clothes = "Common Clothes"
    Belaying_Pin = "Belaying Pin"
    GP_5 = "5 GP"
    GP_10 = "10 GP"
    GP_15 = "15 GP"
    GP_20 = "20 GP"
    GP_25 = "25 GP"
    Fine_clothes = "Fine clothes"
    Scroll_of_Pedigree = "Scroll of Pedigree"
    Winter_Blanket = "Winter blanket"
    Scroll_Case_of_Notes = "Scroll Case of Notes"
    Costume = "Costume"
    Dark_Common_Clothes = "Dark Common Clothes"
    Fine_Clothes = "Fine Clothes"
    Prayer_Book = "Prayer Book"
    Incense_Sticks = "Incense Sticks"
    Incense = "Incense"
    Tools_of_the_Trade = "Tools of the Trade"
    Tools_of_the_Con = "Tools of the Con"
    Vestments = "Vestments"


class Alignment(Enum):
    Lawful_Good = "Lawful Good"
    Neutral_Good = "Neutral Good"
    Chaotic_Good = "Chaotic Good"
    Lawful_Neutral = "Lawful Neutral"
    True_Neutral = "True Neutral"
    Chaotic_Neutral = "Chaotic Neutral"
    Lawful_Evil = "Lawful Evil"
    Neutral_Evil = "Neutral Evil"
    Chaotic_Evil = "Chaotic Evil"


class CharacterConstants:
    
    attributes = {Attribute.Strength: [0,0],  # [base, modifier] 
                  Attribute.Dexterity: [0,0], 
                  Attribute.Constitution: [0,0], 
                  Attribute.Intelligence: [0,0], 
                  Attribute.Wisdom: [0,0], 
                  Attribute.Charisma: [0,0]
                  }
    

    # Skill: {"value": 0, "attribute": Attribute, "proficient": False}
    skill_values = {
        Skills.Acrobatics: {"value": 0, "attribute": Attribute.Dexterity, "proficient": False},
        Skills.Animal_Handling: {"value": 0, "attribute": Attribute.Wisdom, "proficient": False},
        Skills.Arcana: {"value": 0, "attribute": Attribute.Intelligence, "proficient": False},
        Skills.Athletics: {"value": 0, "attribute": Attribute.Strength, "proficient": False},
        Skills.Deception: {"value": 0, "attribute": Attribute.Charisma, "proficient": False},
        Skills.History: {"value": 0, "attribute": Attribute.Intelligence, "proficient": False},
        Skills.Insight: {"value": 0, "attribute": Attribute.Wisdom, "proficient": False},
        Skills.Intimidation: {"value": 0, "attribute": Attribute.Charisma, "proficient": False},
        Skills.Investigation: {"value": 0, "attribute": Attribute.Intelligence, "proficient": False},
        Skills.Medicine: {"value": 0, "attribute": Attribute.Wisdom, "proficient": False},
        Skills.Nature: {"value": 0, "attribute": Attribute.Intelligence, "proficient": False},
        Skills.Perception: {"value": 0, "attribute": Attribute.Wisdom, "proficient": False},
        Skills.Performance: {"value": 0, "attribute": Attribute.Charisma, "proficient": False},
        Skills.Persuasion: {"value": 0, "attribute": Attribute.Charisma, "proficient": False},
        Skills.Religion: {"value": 0, "attribute": Attribute.Intelligence, "proficient": False},
        Skills.Sleight_of_Hand: {"value": 0, "attribute": Attribute.Dexterity, "proficient": False},
        Skills.Stealth: {"value": 0, "attribute": Attribute.Dexterity, "proficient": False},
        Skills.Survival: {"value": 0, "attribute": Attribute.Wisdom, "proficient": False}
    }
    
    biographics = {
        Biographics.Name: "Urg The Barbarian",
        Biographics.Player: "John Doe",
        Biographics.Background: Background.Acolyte,
        Biographics.Class: Classes.Barbarian,  # Default value of type Classes
        Biographics.Race: Race.Human,  # Default value of type Race
        Biographics.Alignment: Alignment.True_Neutral,
        Biographics.XP: 0,
        Biographics.Level: 1
    }

    combat_traits = {
        CombatTraits.Hit_Points: 0,
        CombatTraits.Armor_Class: 0,
        CombatTraits.Initiative: 0,
        CombatTraits.Speed: 0,
        CombatTraits.Proficiency_Bonus: 0,
        CombatTraits.Inspiration: False,
        CombatTraits.Hit_Dice: Dice.d6,
        CombatTraits.Death_Saves: {"Successes": 0, "Failures": 0}
    }
    # races = ["Dwarf", "Elf", "Gnome", "Half-Elf", "Half-Orc", "Halfling", "Human", "Dragonborn", "Tiefling"]
    races = {
        Race.Dwarf: {
            "ability_score_mod": {Attribute.Constitution: 2},
            "size": Size.Medium,
            "speed": Speed.Normal,
            "languages": [Language.Common, Language.Dwarvish],
            "traits": [Traits.Darkvision, Traits.Dwarven_Resilience, Traits.Stonecunning]
        },
        Race.Elf: {
            "ability_score_mod": {Attribute.Dexterity: 2},
            "size": Size.Medium,
            "speed": Speed.Fast,
            "languages": [Language.Common, Language.Elvish],
            "traits": [Traits.Darkvision, Traits.Keen_Senses, Traits.Fey_Ancestry, Traits.Trance]
        },
        Race.Gnome: {
            "ability_score_mod": {Attribute.Intelligence: 2},
            "size": Size.Small,
            "speed": Speed.Normal,
            "languages": [Language.Common, Language.Gnomish],
            "traits": [Traits.Darkvision, Traits.Gnome_Cunning]
        },
        Race.Half_Elf: {
            "ability_score_mod": {Attribute.Charisma: 2},
            "size": Size.Medium,
            "speed": Speed.Normal,
            "languages": [Language.Common, Language.Elvish],
            "traits": [Traits.Darkvision, Traits.Fey_Ancestry, Traits.Skill_Versatility]
        },
        Race.Half_Orc: {
            "ability_score_mod": {Attribute.Strength: 2, Attribute.Constitution: 1},
            "size": Size.Medium,
            "speed": Speed.Normal,
            "languages": [Language.Common, Language.Orc],
            "traits": [Traits.Darkvision, Traits.Menacing, Traits.Relentless_Endurance, Traits.Savage_Attacks]
        },
        Race.Halfling: {
            "ability_score_mod": {Attribute.Dexterity: 2},
            "size": Size.Small,
            "speed": Speed.Normal,
            "languages": [Language.Common],
            "traits": [Traits.Lucky, Traits.Brave, Traits.Halfling_Nimbleness]
        },
        Race.Human: {
            "ability_score_mod": {Attribute.Strength: 1, Attribute.Dexterity: 1, Attribute.Constitution: 1, Attribute.Intelligence: 1, Attribute.Wisdom: 1, Attribute.Charisma: 1},
            "size": Size.Medium,
            "speed": Speed.Normal,
            "languages": [Language.Common]
        },
        Race.Dragonborn: {
            "ability_score_mod": {Attribute.Strength: 2, Attribute.Charisma: 1},
            "size": Size.Medium,
            "speed": Speed.Normal,
            "languages": [Language.Common],
            "traits": [Traits.Draconic_Ancestry, Traits.Breath_Weapon, Traits.Damage_Resistance]
        },
        Race.Tiefling: {
            "ability_score_mod": {Attribute.Charisma: 2, Attribute.Intelligence: 1},
            "size": Size.Medium,
            "speed": Speed.Normal,
            "languages": [Language.Common],
            "traits": [Traits.Darkvision, Traits.Hellish_Resistance, Traits.Infernal_Legacy]
        }
    }


    classes = {
        Classes.Barbarian: {
            "hit_die": Dice.d12,
            "primary_ability": Attribute.Strength,
            "saving_throws": [Attribute.Strength, Attribute.Constitution],
            "armor": [Armor.Light, Armor.Medium, Armor.Shield],
            "weapons": [Weapon.Simple, Weapon.Martial],
            "tools": [],
            "skills": [Skills.Animal_Handling, Skills.Athletics, Skills.Intimidation, Skills.Nature, Skills.Perception, Skills.Survival]
        },
        Classes.Bard: {
            "hit_die": Dice.d8,
            "primary_ability": Attribute.Charisma,
            "saving_throws": [Attribute.Dexterity, Attribute.Charisma],
            "armor": [Armor.Light],
            "weapons": [Weapon.Simple, Weapon.Hand_Crossbow, Weapon.Longsword, Weapon.Rapier, Weapon.Shortsword],
            "tools": [Tool.Musical_Instrument],
            "skills": ["Any three"]
        },
        Classes.Cleric: {
            "hit_die": Dice.d8,
            "primary_ability": Attribute.Wisdom,
            "saving_throws": [Attribute.Wisdom, Attribute.Charisma],
            "armor": [Armor.Light, Armor.Medium, Armor.Shield],
            "weapons": [Weapon.Simple],
            "tools": [],
            "skills": [Skills.History, Skills.Insight, Skills.Medicine, Skills.Persuasion, Skills.Religion]
        },
        Classes.Druid: {
            "hit_die": Dice.d8,
            "primary_ability": Attribute.Wisdom,
            "saving_throws": [Attribute.Intelligence, Attribute.Wisdom],
            "armor": [Armor.Light, Armor.Medium, Armor.Shield],
            "weapons": [Weapon.Club, Weapon.Dagger, Weapon.Dart, Weapon.Javelin, Weapon.Mace, Weapon.Quarterstaff, Weapon.Scimitar, Weapon.Sickle, Weapon.Sling, Weapon.Spear],
            "tools": [Tool.Herbalism_Kit],
            "skills": [Skills.Arcana, Skills.Animal_Handling, Skills.Insight, Skills.Medicine, Skills.Nature, Skills.Perception, Skills.Religion, Skills.Survival]
        },
        Classes.Fighter: {
            "hit_die": Dice.d10,
            "primary_ability": Attribute.Strength,
            "saving_throws": [Attribute.Strength, Attribute.Constitution],
            "armor": [Armor.All, Armor.Shield],
            "weapons": [Weapon.Simple, Weapon.Martial],
            "tools": [],
            "skills": [Skills.Acrobatics, Skills.Animal_Handling, Skills.Athletics, Skills.History, Skills.Insight, Skills.Intimidation, Skills.Perception, Skills.Survival]
        },
        Classes.Monk: {
            "hit_die": Dice.d8,
            "primary_ability": Attribute.Dexterity,
            "saving_throws": [Attribute.Strength, Attribute.Dexterity],
            "armor": [],
            "weapons": [Weapon.Simple, Weapon.Shortsword],
            "tools": [Tool.Artisan_Tools, Tool.Musical_Instrument],
            "skills": [Skills.Acrobatics, Skills.Athletics, Skills.History, Skills.Insight, Skills.Religion, Skills.Stealth]
        },
        Classes.Paladin: {
            "hit_die": Dice.d10,
            "primary_ability": Attribute.Strength,
            "saving_throws": [Attribute.Wisdom, Attribute.Charisma],
            "armor": [Armor.All, Armor.Shield],
            "weapons": [Weapon.Simple, Weapon.Martial],
            "tools": [],
            "skills": [Skills.Athletics, Skills.Insight, Skills.Intimidation, Skills.Medicine, Skills.Persuasion, Skills.Religion]
        },
        Classes.Ranger: {
            "hit_die": Dice.d10,
            "primary_ability": Attribute.Dexterity,
            "saving_throws": [Attribute.Strength, Attribute.Dexterity],
            "armor": [Armor.Light, Armor.Medium, Armor.Shield],
            "weapons": [Weapon.Simple, Weapon.Martial],
            "tools": [],
            "skills": [Skills.Animal_Handling, Skills.Athletics, Skills.Insight, Skills.Investigation, Skills.Nature, Skills.Perception, Skills.Stealth, Skills.Survival]
        },
        Classes.Rogue: {
            "hit_die": Dice.d8,
            "primary_ability": Attribute.Dexterity,
            "saving_throws": [Attribute.Dexterity, Attribute.Intelligence],
            "armor": [Armor.Light],
            "weapons": [Weapon.Simple, Weapon.Hand_Crossbow, Weapon.Longsword, Weapon.Rapier, Weapon.Shortsword],
            "tools": [Tool.Thieves_Tools],
            "skills": [Skills.Acrobatics, Skills.Athletics, Skills.Deception, Skills.Insight, Skills.Intimidation, Skills.Investigation, Skills.Perception, Skills.Performance, Skills.Persuasion, Skills.Sleight_of_Hand, Skills.Stealth]
        },
        Classes.Sorcerer: {
            "hit_die": Dice.d6,
            "primary_ability": Attribute.Charisma,
            "saving_throws": [Attribute.Constitution, Attribute.Charisma],
            "armor": [],
            "weapons": [Weapon.Dagger, Weapon.Dart, Weapon.Sling, Weapon.Quarterstaff, Weapon.Light_Crossbow],
            "tools": [],
            "skills": [Skills.Arcana, Skills.Deception, Skills.Insight, Skills.Intimidation, Skills.Persuasion, Skills.Religion]
        },
        Classes.Warlock: {
            "hit_die": Dice.d8,
            "primary_ability": Attribute.Charisma,
            "saving_throws": [Attribute.Wisdom, Attribute.Charisma],
            "armor": [Armor.Light],
            "weapons": [Weapon.Simple],
            "tools": [],
            "skills": [Skills.Arcana, Skills.Deception, Skills.History, Skills.Intimidation, Skills.Investigation, Skills.Nature, Skills.Religion]
        },
        Classes.Wizard: {
            "hit_die": Dice.d6,
            "primary_ability": Attribute.Intelligence,
            "saving_throws": [Attribute.Intelligence, Attribute.Wisdom],
            "armor": [],
            "weapons": [Weapon.Dagger, Weapon.Dart, Weapon.Sling, Weapon.Quarterstaff, Weapon.Light_Crossbow],
            "tools": [],
            "skills": [Skills.Arcana, Skills.History, Skills.Insight, Skills.Investigation, Skills.Medicine, Skills.Religion]
        }
    }
  
    backgrounds = {
        Background.Acolyte: {
            "skills": [Skills.Insight, Skills.Religion],
            "languages": 2,
            "equipment": [Equipment.Holy_Symbol, Equipment.Prayer_Book, Equipment.Incense, Equipment.Vestments, Equipment.Common_Clothes, Equipment.GP_15]
        },
        Background.Charlatan: {
            "skills": [Skills.Deception, Skills.Sleight_of_Hand],
            "tools": [Tool.Disguise_Kit, Tool.Forgery_Kit],
            "equipment": [Equipment.Fine_Clothes, Equipment.Disguise_Kit, Equipment.Tools_of_the_Con, Equipment.GP_15]
        },
        Background.Criminal: {
            "skills": [Skills.Deception, Skills.Stealth],
            "tools": [Tool.Gaming_Set, Tool.Thieves_Tools],
            "equipment": [Equipment.Crowbar, Equipment.Dark_Common_Clothes, Equipment.GP_15]
        },
        Background.Entertainer: {
            "skills": [Skills.Acrobatics, Skills.Performance],
            "tools": [Tool.Disguise_Kit, Tool.Musical_Instrument],
            "equipment": [Equipment.Musical_Instrument, Equipment.Favor_of_an_Admirer, Equipment.Costume, Equipment.GP_15]
        },
        Background.Folk_Hero: {
            "skills": [Skills.Animal_Handling, Skills.Survival],
            "tools": [Tool.Artisan_Tools, Tool.Vehicles_Land],
            "equipment": [Equipment.Artisan_Tools, Equipment.Shovel, Equipment.Iron_Pot, Equipment.Common_Clothes, Equipment.GP_10]
        },
        Background.Guild_Artisan: {
            "skills": [Skills.Insight, Skills.Persuasion],
            "tools": [Tool.Artisan_Tools],
            "languages": 1,
            "equipment": [Equipment.Artisan_Tools, Equipment.Letter_of_Introduction, Equipment.Travelers_Clothes, Equipment.GP_15]
        },
        Background.Hermit: {
            "skills": [Skills.Medicine, Skills.Religion],
            "tools": [Tool.Herbalism_Kit],
            "languages": 1,
            "equipment": [Equipment.Scroll_Case_of_Notes, Equipment.Winter_Blanket, Equipment.Common_Clothes, Equipment.Herbalism_Kit, Equipment.GP_5]
        },
        Background.Noble: {
            "skills": [Skills.History, Skills.Persuasion],
            "tools": [Tool.Gaming_Set],
            "languages": 1,
            "equipment": [Equipment.Fine_Clothes, Equipment.Signet_Ring, Equipment.Scroll_of_Pedigree, Equipment.GP_25]
        },
        Background.Outlander: {
            "skills": [Skills.Athletics, Skills.Survival],
            "tools": [Tool.Musical_Instrument],
            "languages": 1,
            "equipment": [Equipment.Staff, Equipment.Hunting_Trap, Equipment.Trophy_from_an_Animal, Equipment.Travelers_Clothes, Equipment.GP_10]
        },
        Background.Sage: {
            "skills": [Skills.Arcana, Skills.History],
            "languages": 2,
            "equipment": [Equipment.Bottle_of_Ink, Equipment.Quill, Equipment.Small_Knife, Equipment.Letter_from_a_Dead_Colleague, Equipment.Common_Clothes, Equipment.GP_10]
        },
        Background.Sailor: {
            "skills": [Skills.Athletics, Skills.Perception],
            "tools": [Tool.Navigators_Tools, Tool.Vehicles_Water],
            "equipment": [Equipment.Belaying_Pin, Equipment.Silk_Rope, Equipment.Lucky_Charm, Equipment.Common_Clothes, Equipment.GP_10]
        },
        Background.Soldier: {
            "skills": [Skills.Athletics, Skills.Intimidation],
            "tools": [Tool.Gaming_Set, Tool.Vehicles_Land],
            "equipment": [Equipment.Insignia_of_Rank, Equipment.Trophy_from_a_Fallen_Enemy, Equipment.Bone_Dice_or_Deck_of_Cards, Equipment.Common_Clothes, Equipment.GP_10]
        },
        Background.Urchin: {
            "skills": [Skills.Sleight_of_Hand, Skills.Stealth],
            "tools": [Tool.Disguise_Kit, Tool.Thieves_Tools],
            "equipment": [Equipment.Small_Knife, Equipment.Map_of_the_City, Equipment.Pet_Mouse, Equipment.Token_from_Parents, Equipment.Common_Clothes, Equipment.GP_10]
        }
    }
    

    languages = {
        "Common": Language.Common,
        "Dwarvish": Language.Dwarvish,
        "Elvish": Language.Elvish,
        "Giant": Language.Giant,
        "Gnomish": Language.Gnomish,
        "Goblin": Language.Goblin,
        "Halfling": Language.Halfling,
        "Orc": Language.Orc,
        "Abyssal": Language.Abyssal,
        "Celestial": Language.Celestial,
        "Draconic": Language.Draconic,
        "Deep Speech": Language.Deep_Speech,
        "Infernal": Language.Infernal,
        "Primordial": Language.Primordial,
        "Sylvan": Language.Sylvan,
        "Undercommon": Language.Undercommon
    }


    def __init__(self):
        pass


    @staticmethod
    def attribute_mod(score):
        return (score - 10) // 2
    
    @staticmethod
    def xp_level(xp):
        levels = [
            (355000, 19), (305000, 18), (265000, 17), (225000, 16), (195000, 15),
            (165000, 14), (140000, 13), (120000, 12), (100000, 11), (85000, 10),
            (64000, 9), (48000, 8), (34000, 7), (23000, 6), (14000, 5),
            (6500, 4), (2700, 3), (900, 2), (300, 1)
        ]
        for threshold, level in levels:
            if xp >= threshold:
                return level + 1
        return 1

    




def main():
    cc = CharacterConstants()
    print("Testing attribute_mod")
    for i in range(-10, 51):
        print(f"{i}: {cc.attribute_mod(i)}")

    
    

    

if __name__ == "__main__":
    main()