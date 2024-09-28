import random
bal=1000
def main():
    print("                                    "),print("                                    ")
    print("🎰 Welcome to Takeshi's Casino! 🎲")
    print("====================================")
    print("Feeling lucky today? You're in the right place!")
    print("We offer a variety of games to test your luck and skill.")
    print("From rags to riches, the fun never stops!")
    print("So grab your chips, and let's get started!")
    print("Good luck, and may the odds be ever in your favor!")
    print("====================================")
    print("                                    ")
    print("To quit this game just type and enter quit.")
    print("This current version of Takeshi's Casino supports Mines, Coinflip, Chicken Fight, Buckshot Roulette and HighLow.")  #please update this when you update this game
def coinfliproom(bal):
    print("                                    "),print("                                    ")
    print("🎉Welcome! You've entered the Coinflip Room.🎉")
    print("========================================")
    print("Get ready to test your luck! Type 'flip' to flip the coin.")
    print("Type 'exit' to leave the room at any time. Good luck!🍀")
    print("                                    "),print("                                    ")
    while True:
        coinaction=input("Please type flip,exit or check balance: ").lower()
        if coinaction == "flip":
            print("                                    "),print("                                    ")
            coinbet = int(input("Enter the amount you would like to bet.💰"))
            if coinbet>bal:
                print("Your bet cant be above your current bal which is",bal,"so the current bet will be set to your entire balance.")
                coinbet=bal
            if bal<=0:
                print("Unfortunately we see that your balance is currently in negatives/zero. Please clear your debt and then come back")
                break
            print("                                    ")
            coinguess=input("Please guess either 'Heads' or 'Tails': ")
            coinresult=random.choice(["Heads","Tails"])
            print("                                    "),print("                                    ")
            print("And the coin flipped as:",coinresult)
            if coinresult.lower()==coinguess.lower():
                print("Congrats on winning!",coinbet,"has been credited to your balance!")
                bal+=coinbet
            elif coinresult.lower()!=coinguess.lower():
                print("Looks like luck wasn't on your side today Better luck next time.",coinbet,"has been debited from your balance.")
                bal-=coinbet
        elif coinaction=="exit":
            print("                                    "),print("                                    ")
            print("Leaving the coinflip room....")
            break
        elif coinaction=="bal":
            print("                                    "),print("                                    ")
            print("Your current balance is:",bal)
            print("                                    "),print("                                    ")
        else:
            print("Please enter either play or exit")
    return bal
def chickenring(chicken1name,chicken2name,chicken1hp,chicken2hp,roundcounter):
    print(f"""
|                                                                     |
|                                Round {roundcounter}                              |
|                                                                     |
|                                                                     |
|                                                                     |
|                                                                     |
|                                                                     |
{chicken2name}                                                {chicken1name}
{chicken2hp}                                                      {chicken1hp}
|🐔                                                                🐔 | 
-----------------------------------------------------------------------
""")
    if chicken1hp<0:
        print(f"{chicken1name} is on the verge of death but it refused....He uses his last stadn to hit one single shot that can change the outcome of the match.")
def chickenroom(bal):
    print("                                    "),print("                                    ")
    print("🐔 Welcome to the Ultimate Chicken Fighting Club!🥊")
    print("========================================")
    print("Get ready for the ultimate showdown between the fiercest roosters around!")
    print("This is where legends are made and fortunes are won... or lost.")
    print("Feel the adrenaline as you place your bets and cheer for your champion!")
    print("Type 'fight' to start a match, or 'exit' to leave the arena or 'bal' to check your balance. May the best chicken win! 🏆")
    print("                                    "),print("                                    ")
    while True:
        chickenaction=input("Please decide if you are going to send your fighter or chicken out.").lower()
        print("                                    "),print("                                    ")
        if chickenaction=="fight":
            chickenbet=int(input("Please enter the amount you want to wager on your gladiator."))
            if chickenbet>bal:
                print(f"Since you have entered a number greater than your current balance, the wager will be every single ounce left! Which is {bal}.")
                chickenbet=bal
            if bal<=0:
                print("The colosseum does not accept peasants! Feed him to the lions guards!")
                break
            chickennames=["Ultra_Chicken_3","Hpchicken","Nihalal","Chickenappa","Neochicken","The Opulent Omelette","Vcluckluck-coo-cooo","Pachari","Cluck Norris","Amitabh Bawkchan","Aamir KFC","Shah Rukh Kluk","Hrithik Rooster","Salman Roadkill","Eggbert","Wingman","Coopzilla","Beaky Blinder"]
            chickenadj=["Mighty", "Clumsy", "Fearless", "Wobbly", "Bumbling", "Ferocious", "Sneaky", "Brawny", "Dizzy", "Unstoppable", "Thunderous", "Grumpy", "Giggly", "Swift-footed", "Toothy", "Beefy", "Rowdy", "Sleepy", "Wily", "Chomping", "Pint-sized", "Whirling", "Cackling", "Thundering", "Raging", "Fluffy", "Ironclad", "Rambunctious", "Gnarly", "Bashful", "Jolly", "Snarling", "Zippy", "Cranky", "Bouncy", "Jittery", "Thunderfoot", "Loudmouthed", "Groovy", "Chilly", "Peppy", "Wild-eyed", "Chompy", "Funky", "Rugged", "Charming", "Zany", "Frothy", "Sassy", "Knock-kneed"]
            chickenadv=["astonishment", "bewilderment", "befuddlement", "bamboozlement", "confoundment", "discombobulation", "flabbergastation", "mirth", "hilarity", "guffawing", "chortling", "snickering", "giggling", "snorting", "tittering", "jaw-dropping", "eye-popping", "double-taking", "facepalming", "head-scratching", "brow-raising", "gasping", "mind-blowing", "shock", "surprise", "amazement", "perplexity", "curiosity", "wonderment", "dumbfoundment", "aghastness", "stupefaction", "astonishment", "awe", "disbelief", "stupefaction", "speechlessness", "startlement", "bewilderment", "gawking", "slack-jawed", "agape", "nonplussed", "thunderstruck", "dumbstruck", "mystification", "stunned", "bemusement", "incredulity", "side-eyed"]
            finalhit = ["a punch", "a strike", "a blow", "a jab", "a hit", "a knockout", "a kick", "a hook", "a cross", "a slap", "a shot", "a swing", "an uppercut", "a smack", "a slap", "a wallop", "a thump", "a hammer", "a smash", "a strike", "a thud", "a crack", "a whack", "a punchline", "a slug", "a fist", "a zap", "a boom", "a wallop", "a pummel", "a batter", "a cuff", "a bash", "a sock", "a haymaker", "a snipe", "a slash", "a twack", "a chop", "a biff", "a stun", "a ringer", "a whip", "a clap", "a slam", "a ding", "a blitz", "a bust", "a hammer", "a crack","a blackflash"]
            chicken1name=input("What is your warriors name? ").capitalize()
            chicken2name=chickennames[random.randint(0,17)]
            print("                                    "),print("                                    ")
            print("Announcer: Ladiesss and gentlemen in a brawl between two conbatants scheduled for 10 rounds for the World Chicken Championship.")
            print("           In the right corner, the challenger, The", chickenadj[random.randint(0, 49)], chicken1name.capitalize(), ".")
            print("           And in the left corner, we have", chickenadj[random.randint(0, 49)], chicken2name, ".")
            print("           Ladies and gentlemen are you ready for Reaaaaaaaaaaaaaaaaal Seeeeeeeeeeeeeeeeed!!!!!!!")
            moti1=input("Enter some motivation words for your chicken: ")
            if moti1.lower()=="this is what it's all about":
                print("You got this Atom!")
            chicken1hp=100
            chicken2hp=100
            roundcount=1
            while chicken1hp>0 and chicken2hp>0 and roundcount<=10:
                chicken1hp-=random.randint(0,20) 
                chickenring(chicken1name,chicken2name,chicken1hp,chicken2hp,roundcount)
                moti2=input(f"Crap! The opponent hit us! Give our beloved {chicken1name} some words of wisdom!").lower()
                if moti2=="imaginary technique hollow purple" and chicken1name.lower()=="gojo":    #easter eggs
                    print("Announcer: A fatal shot instantly exorcising",chicken2name,"a truly divine technique!")
                    chicken2hp-=9999999
                elif moti2=="the scale of the dragon, recoil, twin meteors" and chicken1name.lower()=="sukuna":
                    print("Announcer: A SLASH THAT BISECTS THE WORLD ITSELF!")
                    chicken2hp-=999999999999
                elif moti2=="thunderbolt" and chicken1name.lower()=="pikachu":
                    print("Announcer: Isn't that the dude Ryan Reynolds plays?")
                    chicken2hp-=40
                elif moti2=="uppercut":
                    chicken2hp-=10
                elif moti2=="heal":
                    chicken1hp+=12
                elif moti2=="black flash" and chicken1name.lower()=="yuji":
                    print(f"{chicken2name.capitalize()} never stood a chance against the prince of black sparks")
                elif moti2=="dragon rage" and chicken1name.lower()=="garchomp":
                    print("Cynthia simp(dont blame you)")
                    chicken2hp-=50
                else:
                    chicken2hp-=random.randint(0,20)
                    print(chicken1name,"heard you with visible",chickenadv[random.randint(0,49)],"and threw his hands as fast as he could.")
                roundcount+=1
            if chicken1hp<=0:
                print("")
                print("It was a well fought battle....",chicken1name,"tried his best however he was bested by his opps. We shall return back again winning this time!")
                print(chickenbet,"has been debited from your baalnce")
                bal-=chickenbet
            elif chicken2hp<=0:
                if moti2=="the scale of the dragon, recoil, twin meteors":
                    print(f"{chicken2name} dint stand a chance aganist the 10 shadows as Sukuna glares at the bisected chicken.")
                else:    
                    print("As",chicken2name,"lowered his defences.",chicken1name,"lands",finalhit[random.randint(0,50)],"instantly making the opponent tap out")
                    print("Your Chicken won Real Seed!!!!")
                bal+=chickenbet
            elif roundcount==11:
                print("Welp it was a hard fought battle unfortunately both parties were so bad we're calling it a draw go home the four of you.")
        elif chickenaction.lower()=="exit" or chickenaction.lower()=="quit":
            print("First rule: You do not talk about chicken club.")
            print("Second rule: You do not talk about chicken club.")
            break
        elif chickenaction.lower()=="bal":
            print(f"Your current balance is {bal}")
    return bal
def minesui():
    rock_art = """
    ______
   /      \\
  |   ORE  |
   \\______/
    """
    print(rock_art)
    print("Options:")
    print("1. Break")
    print("2. Cashout")
def minesroom(bal):
    print("")
    print("")
    print("💣 Welcome to the Mines! 💣")
    print("====================================")
    print("Tread carefully, adventurer! Each step you take could lead to treasure... or disaster!")
    print("The ground is riddled with hidden mines. Can you avoid them and claim your rewards?")
    print("Choose your path wisely, and remember: One wrong step, and it's game over!")
    print("Good luck, and may the odds be ever in your favor! ⛏️ 💥")
    print("Type 'mine' in order to start, bal to check bal and exit to leave.")
    print("====================================\n")
    while True:
        print("")
        minesaction=input("You glare into the abyss that is the cave decide if you would ventuer forth: ").lower()
        if minesaction=="mine":
            while True:
                try:
                    print("")
                    minebet=int(input("Enter how much you would like to bet: "))
                    if minebet>bal:
                        print("Bruh the bet is more than the money.")
                    else:
                        print(f"The amount of money you bet is {minebet}.")
                        pass
                except ValueError:
                    print("Please enter a number and not this garbage.")
                print("You enter the mine.")
                minesui()
                chance=100
                minerounds=0
                while True:
                    print(f"You currently have a {chance} of winning.")
                    print("")
                    mineoption=input("Enter what would you like to do: ").lower()
                    if mineoption=="mine" or mineoption=="break" or mineoption=="1":
                        if random.randint(1,100)<=chance:
                            print("You succesfully break the rock without dying!")
                            print("")
                            chance-=10
                            minerounds+=1
                        else:
                            print("Player died trying to swim in lava.")
                            bal-=minebet
                            break
                    elif mineoption=="cashout" or mineoption=="quit" or mineoption=="dont break it" or mineoption == "2":
                        minewinnings=int(minebet*1.2*minerounds)
                        print(f"You lasted {minerounds} rounds.")
                        print(f"You cashout with an astounding {minewinnings}.")
                        bal-=minebet
                        bal+=minewinnings
                        pass
                    else:
                        print("Hey it's either break or cashout you dont get to create more options.")
                return bal
        elif minesaction=="bal":
            print(f"The balance in your account is {bal}")
        elif minesaction=="quit" or minesaction=="exit":
            print("Debt collector: No you have to pay this poan i already gave you too much time.")
            print("Me: Please just this one time i will come back with more energy and pay you extra $50.")
            print("Debt collector: hmmmmmmmmmmmmm.........")
            break
        else:
            print("Please type 'bal' or 'mine' or 'quit'.")           
def minesrules():
    print("1. Your an adventurer trapped in a cave but the loan collectors demand you dont return empty-handed or you will return")
    print("   to your home without-handed. Each rock you break has a higher chance to have lava behind it.")
    print("2. Yea its a quick and simple game but i cant think of anything tbh.")
    print("3. Wait this is the rules part why am I treating this like a devlog?")
    print("4. Eh its ok no one is gonna see this anyone except you so dont mind the yapping.")
    print("5. Dude ive lately been watching the bear and its sooo good man i reccomend everyone playing stop this shit game(even valo) and watch some episodes on it.") 
def buckshotrules():
    print("There is a shotgun on the table before you.")
    print("You can either shoot yourself or shoot me.")
    print("If you shoot yourself with a blank my turn gets skipped.")
    print("However, if you shoot yourself witha real bullet your turn will be skipped.")
    print("There is no bets. This is a game of life and death")
    print("Once you start this game you cant end it.")
    print("You will continue to play this game even if it means the first game is your unfortunate demise.")
def buckshotai(bullets,shells):
    if bullets<shells:
        return 1
    elif bullets>shells:
        return 2
    else:
        return 2
def buckshotroom(bal):
    while True:
        print("")
        print("Welcome...No need for introduction or name or bets. If you die, you lose everything.")
        print("You can still turn your back as you haven't signed the waiver.")
        
        buckplayerhp = 3
        buckdealerhp = 3
        
        bucklist = []
        while len(bucklist) < 12:
            bucklist.append(random.randint(0, 1))
        
        bullets = bucklist.count(1)
        shells = bucklist.count(0)

        while True:
            buckaction = input("Decide carefully: bal, exit, rules or load (type play to load the bullets). ").lower()
            buckui(buckplayerhp,buckdealerhp)
            
            if buckaction == "rules" or buckaction == "rule":
                buckshotrules()
            
            elif buckaction == "bal":
                print(f"Your current balance is {bal}")
            
            elif buckaction == "exit" or buckaction == "quit":
                print("Imagine being too scared. Play that trash mines game instead. No skill.")
                break
            
            elif buckaction == "load" or buckaction == "play":
                print(f"Great, currently there are {bullets} bullet(s) and {shells} blank(s).")
                print("You start first. Each of us has 3 lives. Each bullet removes a life. First to 0 loses.")
                turn = 1
                
                while buckdealerhp > 0 and buckplayerhp > 0 and len(bucklist) > 0:
                    if turn == 1:  
                        buckplayerturn = input("It is your turn. Type 'shoot' to shoot the dealer, or 'myself' to shoot yourself: ").lower()
                        
                        if buckplayerturn in ["shoot", "fire", "1"]:
                            if bucklist[0] == 1:
                                print("You shot the dealer.")
                                if buckdealerhp == 2 or buckdealerhp==3:
                                    print("Shot him in the shoulder. He growls in pain.")
                                else:
                                    print("You shot him in the chest. He collapses.")
                                buckdealerhp -= 1
                            else:
                                print("It was a blank!")
                            bucklist.pop(0)
                            turn = 2
                        
                        elif buckplayerturn in ["myself", "2", "kys"]:
                            print("You aim the gun at yourself...")
                            if bucklist[0] == 1:
                                if buckplayerhp == 2 or buckplayerhp==3:
                                    print("You shot yourself in the ear.")
                                else:
                                    print("You shot yourself fatally.")
                                buckplayerhp -= 1
                                turn=2
                            else:
                                print("It was a blank!")
                                turn=1
                            bucklist.pop(0)
                            
                    
                    else: 
                        print("It's the dealer's turn.")
                        if buckshotai(bucklist.count(1), bucklist.count(0)) == 1:
                            print("The dealer shoots himself.")
                            if bucklist[0] == 1:
                                buckdealerhp -= 1
                                print("It was a real bullet!")
                                turn=1
                            else:
                                print("It was a blank!")
                                turn=2
                        else:
                            print("The dealer shoots at you.")
                            if bucklist[0] == 1:
                                buckplayerhp -= 1
                                print("He hit you!")
                                turn = 1
                            else:
                                print("It was a blank!")
                                turn = 1
                        bucklist.pop(0)
                        

                if buckdealerhp == 0:
                    print("You won! You gain the dealer's balance.")
                    bal += bal
                elif buckplayerhp == 0:
                    print("You died. You lost everything.")
                    bal = 0
                elif len(bucklist) == 0:
                    print("No bullets left. It's a draw.")
                else:
                    print("Something went wrong.")
def buckui(buckplayerhp,buckdealerhp):
    print("    O                 ______________                O")
    print("   /|\\               |       🔫    |               /|\\")
    print("   / \\               |    TABLE    |               / \\")
    print("   Me                +-------------+                Dealer")
    print(f"   HP:{buckplayerhp}              /              \\               HP:{buckdealerhp}")
    print("                    /_________________\\                  ")
    print("Decide either you shoot.")
    print("1.Dealer")
    print("2.Yourself")
def highlow(bal):
    while True:
        print("\nWelcome player, to the HighLow Room!")
        print("Get ready to guess if the next number is higher or lower.")
        print("Good luck and have fun!")
        hlinput = input("Please enter what you would like to do: ").lower()
        hlcards = {0:2, 1:3, 2:4, 3:5, 4:6, 5:7, 6:8, 7:9, 8:10, 9:"Jack", 10:"Queen", 11:"King", 12:"Ace"}
        hlsuites = {0:"Spades", 1:"Diamonds", 2:"Hearts", 3:"Clubs"}
        
        if hlinput in ["play", "deal", "start"]:
            try:
                hlbet = int(input("Please type how much you would like to bet: "))
                if hlbet > bal:
                    print("You can't use a value greater than your balance.")
                    continue
                print(f"The current bet of {hlbet} has been accepted.")
            except ValueError:
                print("Please input a valid integer.")
                continue
            hlmulti = 1
            while True:
                hlrandomnum = random.randint(0, 12)
                hlnextrandom = random.randint(0, 12)
                hlcurcard = hlcards[hlrandomnum]
                hlnextcard = hlcards[hlnextrandom]
                print(f"\nThe current card is {hlcurcard} of {hlsuites[random.randint(0, 3)]}.")
                if hlcurcard == 2:
                    print("Please guess if the next card is going to be equal or higher.")
                elif hlcurcard == "Ace":
                    print("Please guess if the next card is going to be equal or lower.")
                else:
                    print("Please guess if the next card is going to be lower, higher, or equal.")
                
                print(f"Your current multiplier is {hlmulti}x.")
                hlaction = input("Higher, lower, equal or quit: ").lower()

                if hlaction in ["leave", "quit", "cashout"]:
                    print(f"You cashed out with a multiplier of {hlmulti}.")
                    bal += hlbet * hlmulti - hlbet
                    break
                if hlaction == "equal" and hlcurcard == hlnextcard:
                    hlmulti += 100 / 13
                    print(f"Correct! The next card was {hlnextcard}. Multiplier increased to {hlmulti}x.")
                elif (hlaction in ["higher", "high", "h"] and hlnextrandom > hlrandomnum) or \
                     (hlaction in ["lower", "low", "l"] and hlnextrandom < hlrandomnum):
                    hlmulti += 1 - abs(hlnextrandom - hlrandomnum) / 100
                    print(f"Correct! The next card was {hlnextcard}. Multiplier increased to {hlmulti}x.")
                else:
                    print(f"Incorrect. The next card was {hlnextcard}. You lost!")
                    hlmulti = 0
                    break

            bal -= hlbet
            bal += hlbet * hlmulti
            print(f"Your new balance is {bal}.")
        elif hlinput in ["bal", "balance", "savings"]:
            print(f"Your current balance is {bal}.")
        elif hlinput in ["exit", "quit", "leave"]:
            print("It was nice seeing you here! Please come back again.")
            break
        elif hlinput in ["rules", "rule"]:
            highlowrules()
    return bal
def highlowrules():
    print("1. The cards are drawn randomly from an infinite deck.")
    print("2. you have to choose if a card is higher or equal or lower and equal")
    print("3. However if you pull the lowest tag(2) or the highest card(ace) you will have to decide if the next card will be equal or higher or equal or lower.")
    print("4. The higher the risk the higher the higer the pay")
    print("5. The lower the rick the lower the astley.")
    print("6. Never gonna give you up")
    print("7. Never gonna let you down")
    print("8. Never gonna run around and desert you")

main()
while True:
    room = input("Please enter which room you would like to enter: ").lower()
    if room == "coinflip" or room=="coin":
        coinfliproom(bal)
    elif room == "blackjack" or room=="bj":
        print("WIP please stay tuned when the dev stops being lazy")
    elif room == "chicken fight" or room=="cf":
        chickenroom(bal)
    elif room == "quit" or room=="exit":
        print("Thanks for playing! See you next time at Takeshi's Casino!")
        break
    elif room == "mines" or room=="mine":
        minesroom(bal)
    elif room=="buck" or room=="buckshot" or room=="buckshot roulette":
        buckshotroom(bal)
    elif room in ["bal"]:
        print(f"Your current balance is {bal}.")
    elif room in ["hl","highlow","high"]:
        highlow(bal)
    else:
        print("Typo moment.")
