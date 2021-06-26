import time
import numpy
import sys

#typewriter printing

def delay_print(s):
    #print one char at a time like a typewriter
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

#Card class
class Card:
    def __init__(self, name, type, moves, stats,  goals=0):
        self.name = name
        self.type = type
        self.moves = moves
        self.attack = stats['ATTACK']
        self.defense = stats['DEFENSE']
        self.goals = goals

    def match(self, OpponentCard):
        print("-------FOOTBALL MATCH BEGINS-----------")
        print(f"{self.name}")
        print(f"TYPE/", self.type)
        print(f"ATTACK/", self.attack)
        print(f"DEFENSE/", self.defense)
        print(f"\nVS.\n")
        print(f"{OpponentCard.name}")
        print(f"TYPE/", OpponentCard.type)
        print(f"ATTACK/", OpponentCard.attack)
        print(f"DEFENSE/", OpponentCard.defense)
        time.sleep(2)

        version = ['Def', 'Mid', 'Atk']
        for i, k in enumerate(version):
            if self.type == k:
                #both are same type
                if OpponentCard.type == k:
                    string1_attack = '\nPosition clash!'
                    string2_attack = '\nPosition clash!'

                #OpponentCard is stronger
                if OpponentCard.type == version[(i+1) % 3]:
                    OpponentCard.attack *= 2
                    OpponentCard.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string1_attack  = '\nDeflection!'
                    string2_attack = '\nWhat a shot!'

                if OpponentCard.type == version[(i+2) % 3]:
                    self.attack *= 2
                    self.defense *= 2
                    OpponentCard.attack /= 2
                    OpponentCard.defense /= 2
                    string1_attack = '\nWhat a shot!'
                    string2_attack = '\nDeflection!'

        while (self.goals < 5 and OpponentCard.goals < 5):
            print(f"{self.name}\t\tGOALS\t{self.goals}")
            print(f"{OpponentCard.name}\t\tGOALS\t{OpponentCard.goals}")

            print (f"Player 1 plays {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"{self.name} {self.moves[index-1]}!")
            time.sleep(1)
            delay_print(string1_attack)

            #determine goal
            goal_evaluate = OpponentCard.defense =- self.attack
            if goal_evaluate >0 :
                OpponentCard.score += 1
                delay_print(f"\n{self.name} is on the attack!")
                delay_print(f"...")
                delay_print(f"\nIts a goal!")
            else:
                delay_print(f"\nKeeper saves it!")

            #set score

            time.sleep(1)
            print(f"{self.name}\t\tGOALS\t{self.goals}")
            print(f"{OpponentCard.name}\t\tGOALS\t{OpponentCard.goals}")
            time.sleep(.5)

            #check to see if match is over
            if OpponentCard.goals >=5:
                delay_print("\n..." + OpponentCard.name + ' loses.')
                break

            #OpponentCard turn

            print(f"Player 2 plays {OpponentCard.name}!")
            for i, x in enumerate(OpponentCard.moves):
                print(f"{i + 1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"{OpponentCard.name} {OpponentCard.moves[index - 1]}!")
            time.sleep(1)
            delay_print(string2_attack)

            # determine goal
            goal_evaluate = self.defense =- OpponentCard.attack
            if goal_evaluate > 0:
                self.score += 1
                delay_print(f"\nIts a goal!")
            else:
                delay_print(f"\nKeeper saves it!")

            # set score

            time.sleep(1)
            print(f"{OpponentCard.name}\t\tGOALS\t{OpponentCard.goals}")
            print(f"{self.name}\t\tGOALS\t{self.goals}")
            time.sleep(.5)

            # check to see if match is over
            if self.goals >= 5:
                delay_print("\n..." + self.name + ' loses.')
                break

        exp = numpy.random.choice(5000)
        delay_print(f"\nYou gained {exp}. EXP")

if __name__ == '__main__':
    #create players

    Ronaldo = Card('Ronaldo', 'Atk', ['MAke a run','Tackle', 'Shoot', 'Cross', 'Header'], {'ATTACK':5, 'DEFENSE':1})
    Cambiasso = Card('Cambiasso', 'Mid', ['MAke a run','Tackle', 'Shoot', 'Cross', 'Header'], {'ATTACK':3, 'DEFENSE':4})

Ronaldo.match(Cambiasso)