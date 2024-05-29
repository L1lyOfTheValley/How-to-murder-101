# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define  oldSis = Character("Old Sister")
define youngSis = Character("Young Sister")
define exBf = Character("Ex")
define blank = Character(" ")
define Neighbour = Character("Neighbour")
define mom = Character("mom")
define dad = Character("dad")
define fisherman = Character("fisherman")
define policeman = Character("policeman")

transform midleft:
    xalign 0.33 yalign 0.99

transform midright:
    xalign 0.70 yalign 0.99 



# The game starts here.

label start:


    scene bg kitchen

    show oldsis neutral

    oldSis "You got the stuff?"

    show youngsis neutral at left 

    youngSis "Yeah, did you plan on who our victim is?"  

    menu:
        "The neighbour.":
            jump VictimAnswerOne
        "The ex bf.":
            jump VictimAnswerTwo
        "Us.":
            jump VictimAnswerThree
        "Our parents":
            jump VictimAnswerFour 
            
            
    
    label VictimAnswerOne:
        youngSis "Finally it's about time that someone teaches him a lesson!"
        oldSis "Grab the stuff and let's go."
        hide oldSis
        scene bg backyard 
        show youngsis ghost at left 
        youngSis "Thihihihihihih."
        show neighbour angry at right 
        Neighbour "What are you at my property you little gremlin!"  
        youngSis "You will never catch me old man hahaha."  
        Neighbour "Come back here you poopoohead! "
        blank "The nieghbour trips on the water hose in the backyard. "
        show neighbour shoked at right 
        blank "Do you kill him with a chainsaw, or kill him with a flame thrower?"
        menu:
            "chainsaw him.":
                jump chainsawHim 

            "flame thrower him.":
                jump flameThrowerHim
        
        label chainsawHim: 

            blank "He hear's the noise of a chainsaw. " 
            hide neighbour
            hide youngsis
            show oldsis smiling at left 
            blank "He look's back and see the older sister with a chainsaw smiling at him maniacally. "
            oldSis "Say bye bye old man hihih. "
            blank "The last thing that the neighbour hears is the laughter of the sisters and the sounds of his screams."
            

            jump bodyBagCom

        label flameThrowerHim:

            blank "He hear's the noise of a flame thrower. " 
            hide neighbour
            hide youngSis
            show oldsis smiling at left 
            blank "He look's back and see the older sister with a flame thrower smiling at him maniacally. "
            show youngsis 
            youngSis "Can i please ues the flame thrower please? "
            oldSis "I was the one to ues it last time so sure."
            youngSis "Yippie!! "
            blank "The last thing that the neighbour hears is the laughter of the sisters and the sounds of his screams as he was getting burned alive."

            
            
            jump bodyBagCom 


        jump bodyBagCom



    label VictimAnswerTwo:
        youngSis "I am glad that you finally going to do somthing about that trash."
        oldSis "Grab the stuff and let's go."
        
        hide youngSis
        scene bg ex_liveingroom
        show oldsis blush at left
        show exbf cocky at right
        exBf "It has been a while since we last saw eachother."
        oldSis "Yeah! I brought cake."
        exBf "That is so sweet of you baby gurl."
        blank "Do you poison him, or drug him?"
        menu:
            "Drug him.":
                jump DrugHim 

            "Poison him.":
                jump PoisonHim

        label DrugHim: 

            exBf "I feel a little sleepy."
            oldSis "Good night little shit."
            hide exBf
            show oldsis smiling at midright
            show youngsis smiling at left 
            youngSis "I got the bodybag."
            oldSis "Good let's wrap him up."
            

            jump bodyBagCom

        label PoisonHim:

            exBf "Choking"
            oldSis "Thihihihi."
            hide exBf
            show oldsis smiling at midright
            show youngsis smiling at left  
            oldSis "Did you get the bodybag?"
            youngSis "Yeah i go them."
            
            jump bodyBagCom    

           

    label VictimAnswerThree:
        hide youngSis
        show youngsis smiling at left 
        youngSis "OMG yippie!!"
    jump DeathEnd 

    label VictimAnswerFour:
        youngSis "Can I take mom's jewellery?"
        oldSis "Grab the stuff and let's go."

        hide youngsis
        hide oldsis
        show mom angry at left 
        show dad angry at right 
        dad "I swear these girls are going to be the end of me! "
        mom "I am regretting giveing birth to them. "
        hide mom 
        hide dad 

        scene bg bathroom
        show youngsis neutral at left 
        show oldsis neutral at right 
        oldSis "Ugh they act as its our fault that we are born. "
        youngSis "I am so glad that you are old enough to own the house now."
        oldSis "Yeah, the sooner that we are done with them the better. "
        blank "Do you kill them with a circular saw , or kill them with a katana?"

        menu:
            "circular saw.":
                jump circularSaw 

            "katana.":
                jump katana

        label circularSaw: 

            scene bg kitchen
            show youngsis scared
            youngSis "MOM DAD AYESHA FAINTED IN THE BATHROOM!"
            show dad shoked at left 
            show mom shoked at right 
            dad "What! "
            mom "My god you girls dont give us a break! "

            scene bg bathroom 

            hide youngSis 
            show dad angry at left
            show mom angry at right
            mom "Where is she? "
            dad "Ruba where did you go? "
            blank "*The lights turn off* "
            blank "*Door locking sound* "
            dad "What the heck is going on! "
            mom "Girls i swear if you don't stop this instantly you will be grounded for a 5 month's!"
            oldSis "I don't think you can ground us if you guys are dead. "
            show mom shoked
            show dad shoked at midright 
            show oldsis smiling at left 
            show youngsis smiling at midleft
            youngSis "I wonder how it feel's to be killed by a circular saw? "
            blank "Ayesha starts the circular saw."
            oldSis "I guess we will figure this out soon tihihi."


            jump bodyBagCom

        label katana:

            scene bg kitchen
            show youngsis scared
            youngSis "MOM DAD AYESHA FAINTED IN THE BATHROOM!"
            show dad shoked at left 
            show mom shoked at right 
            dad "What! "
            mom "My god you girls dont give us a break! "

            scene bg bathroom 

            hide youngSis 
            show dad angry at left
            show mom angry at right
            mom "Where is she? "
            dad "Ruba where did you go? "
            blank "*The lights turn off* "
            blank "*Door locking sound* "
            dad "What the heck is going on! "
            mom "Girls i swear if you don't stop this instantly you will be grounded for a 5 month's!"
            oldSis "I don't think you can ground us if you guys are dead. "
            show mom shoked
            show dad shoked at midright 
            show oldsis smiling at left 
            show youngsis smiling at midleft
            youngSis "I am so glad that we took the sword practises tihihi. "
            oldSis "How about we use the thing's that we learnd? "
            youngSis "Yeah let's do it tihihi! "


      
        jump bodyBagCom
     
    label bodyBagCom:
        hide dad 
        hide exbf
        hide neighbour
        hide mom
        show oldsis neutral at left
        show youngsis neutral at right
        youngSis "Now that we are done what do we do with the body? "
        oldSis "we get rid of it. "
        oldSis "But the question  is where? "
        blank "Where do you want to hide the body? " 



        menu:
            "Cannibalism.":
                jump Cannibalism 

            "forest.":
                jump forest

            "lake.":
                jump lake

            "city.":
                jump city

    
        label Cannibalism: 
            
            scene bg kitchen
            show youngsis neutral at left 
            show oldsis neutral at right
            youngSis "That was yummy! "
            oldSis "We should do this more often! "

        jump Yummyfood


        label forest:
            
            scene bg forest
            show youngsis neutral at left 
            show oldsis neutral at right
            youngSis "How much more are we walking. "
            oldSis "The further away we are the less police can figure us out. "
            youngSis "Ughaaaaa. "
            hide oldSis
            hide youngSis
            blank "The girls continued to walk even further away from any people so they won't get caught by the police. "
            blank "After 1 and a half houres of walking. "
            show youngsis neutral at left 
            show oldsis neutral at right
            youngSis "Oh my god finally we are done walking. "
            oldSis "We are done walking but now we have to start shoveling. "
            youngSis "Noooo please can I do somthing else? "
            oldSis "... "
            oldSis "Sure go hunte us any animal. "
            blank "Aysha gives Ruba a hunteing knife. "
            oldSis "Don't get lost. "
            youngSis "Okay I'll be back soon. "
            blank "30 minutes later. "
            youngSis "By the way Aysha why did you ask me to hunt an animal ? "
            oldSis "You see the hole I dug. "
            youngSis "Yeah ? "
            oldSis "So if you dig a hole super deep and bury the body you fill the hole a little bit to leave some room for the animal- "
            oldSis "After you bury the animal corpse on top you finsh filling the hole. "
            oldSis "So if the police comes here and think there is something suspicious the only thing they can find is the animal corpse. "
            youngSis "Dang sis you are smart. "
            oldSis "Now that we are done let's get the hell out of here. "
            youngSis "Yeah let's go. "
            
        jump Lesson
            
        label lake:
            
            scene bg fisher
            show oldsis scared at right 
            show youngsis scared at midright
            oldSis "Let's hope that the fisherman is not here today- "
            show fisherman neutral at left 
            fisherman "What are you girls doing here?"
            fisherman "And what's in the bag it smells rotting?"
            oldSis "It's non of you're business old man leave us alone! "
            youngSis "Yeah leave us alone! "
            fisherman "It is my business now. You girls have alwas been trouble and I don't you messing with the fish! "
            blank "The fisherman grabs the bag from the girls and opens the bag."
            hide fisherman
            show fisherman shoked at left
            fisherman " OH MY GOD WHAT IS THIS!"
            fisherman "I am calling the police immediately! "

            jump fish


        label city:

            scene bg city
            show oldsis scared at right 
            show youngsis scared at left 
            youngSis "Maybe it's a bad idea to come here. "
            oldSis "It's to late to say this no- "
            hide youngSis
            show youngsis scared at midright
            show policeman neutral at left
            policeman "Girls you are under arest! "
            policeman "Seriously who comes here to hide a body. "

            jump why
            

    label DeathEnd:
        "Emo ending, you need therapy."
        jump finalend
    
    
    label Yummyfood:
        "Good ending "
        "you didn't get caught and you had a good meal :3 "
        jump finalend

    label Lesson:
        "Good ending "  
        "You're knowledge on how to dispose of a body safed you from a life in prison. "   
        jump finalend

    label fish:
        "Bad ending"
        "You got unlucky and got caught. "
        "Better luck next time. "
        jump finalend

    label why:
        "Bad ending"
        "... why just why."
        jump finalend

    label finalend:

    return