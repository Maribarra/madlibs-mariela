# PSEUDOCODE
# loop
# prompt the player : empty dictionary to store answers
# ask (input): noun1 noun2 verb ending-ing color
# print story
# print the story
# ask to play again or not
# if yes, ask for more information
# if no, break


#prompt_user

print "Welcome to madlib, where you create your own story"

print


def prompt_user():
    """ Ask user for information to add to their story"""

    answers = {}     
    
    #ask the user for type of word, and assign a key to the word for python
    answers['noun'] = raw_input(" Can you please type me a noun? ")
    answers['noun 2'] = raw_input("another noun? ")
    answers['ing-verb'] = raw_input("verb ending in -ing? ")
    answers['color'] = raw_input("color? ")
    answers['smell'] = raw_input("name a smell? ")
    
    #put all the answers together
    return answers

def tell_story(answers):
    """Make madlib and print."""

    print
    print "Your madlib is:"
    print
    print answers['noun'] + " and " + answers['noun 2'] + " were jogging"
    print "around downtown when they saw a " + answers['color']
    print "cat " + answers['ing-verb'] + "."
    print
    print "When they saw a UFO throwing a" + answers['smell']

def play():
    """Play madlibs."""

    while True:
        answers = prompt_user()
        tell_story(answers)

        again = raw_input("Play again? ")
        if again.startswith("N") or again.startswith("n"):
            
            break

    print "Thanks for playing!"


play()