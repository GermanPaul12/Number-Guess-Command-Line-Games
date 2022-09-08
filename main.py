from art import logo
from art import vs
from game_data import data
from replit import clear
import random

print(logo)
    
def guess_random():
    keep_going = True
    score = 0
    while keep_going:
        global random_1
        global random_2
        #import a random choice a 
        random_1 = random.choice(data)
        random_1_name = random_1['name']
        random_1_description = random_1['description']
        random_1_country = random_1['country']
        random_1_followers = random_1['follower_count']
        print(f"\nYour current score is: {score}\n")
        print(f"a) {random_1_name} a {random_1_description} from {random_1_country}")
        #import vs logo
        print(vs)
        #import a random choice b
        random_2 = random.choice(data)
        random_2_name = random_2['name']
        random_2_description = random_2['description']
        random_2_country = random_2['country']
        random_2_followers = random_2['follower_count']
        print(f"b) {random_2_name} a {random_2_description} from {random_2_country}")
        #let the player choose a or b
        guess = input("Who has more follower? Type 'a' for a or 'b' for b: ")
        if guess == 'a':
            if random_2_followers > random_1_followers:
                print(f"That was false. You loose! You reached a score of {score}.")
                keep_going = False
                play = input('Do you want to play? "y" for yes or "n" for no: ') 
                if play == 'y':
                    keep_going = True
                    guess_random() 
                if play == 'n':
                    keep_going = False
                    break    
            if random_1_followers > random_2_followers:
                score += 1
            if random_1_followers == random_2_followers:  
                score += 1  
        if guess == 'b':
            if random_2_followers < random_1_followers:
                print(f"That was false. You loose! You reached a score of {score}.")
                keep_going = False
                play = input('Do you want to play? "y" for yes or "n" for no: ') 
                if play == 'y':
                    keep_going = True
                    guess_random() 
                if play == 'n':
                    keep_going = False
                    break    
            if random_1_followers < random_2_followers:
                score += 1
            if random_1_followers == random_2_followers:  
                score += 1                     
                    
                   
play = input('Do you want to play? "y" for yes or "n" for no: ') 
if play == 'y':
    guess_random()    

#if guess is wrong end the game and display the final score
#if guess is right continue the game and import again random data and let the playeer guess