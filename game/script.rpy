# 游戏的脚本可置于此文件中。
# images
image bg sky = "sky.jpg"
image bg town = "town.jpg"
image bg black = "black.jpg"
image bg house_outside = "house_outside.jpg"
image bg house_live = "house_livingroom.jpg"
# character images
default char = "nil.png"
image player_img = "char-[char]"
image earthRep_img = "earthRep.png"
image wildRep_img = "wildRep.png"
image neighbor_img = "earthRep.png"
# variables
define total_month = 5
define money = 100
define effort = 100
define happiness = 100
define salary = 0
define social_good = 0
define time = 0
# other variables
define company = ""
define detective = ""
define city = ""
# define characters
define player = Character("Anonymous")
define earthRep = Character("Earthquake Non-Profit Representative")
define wildRep= Character("WildLife NonProfit")
define neighbor = Character("Neighbor")

# 游戏在此开始。

label start:

    #"Choose your character image"
    $ renpy.notify("Choose your character")
    call screen char_choice
    $ char = _return
    
    scene bg black
    show player_img
    
    $ renpy.notify("Name your character")
    $ player = renpy.input("")
    $ player = player.strip()
    
    if player == "":
        $ player = "Anonymous"

    hide player_img

    # start
    scene bg sky

    "Hey [player], Congratulations on graduating from college. You really put a lot of hard work into finishing your degree, and it’s paid off – you have your pick of several different jobs.And now that you’re out of school, you have to commit to one of them."
    "There’s that job at {b}Spectra Tech{/b}, which definitely pays the best, and it looks fun! But you’d have to move to the city, which is pretty far from your family, and rent there is expensive."
    "{b}Gold Star Development{/b}  is closer, so you wouldn’t have to move. The two hour drive is a bit much for every morning, but you could make it work. Rent here is very reasonable, and you’d hate to give that up. The pay is still good, though not as good as Spectra Tech."
    "{b}Green Valley Engineering{/b} is even closer to home – like a fifteen minute drive from your apartment! – and the hours looked better too. Sure it pays less than the other two companies, but you’d have more free time to pursue other interests."
    "Speaking of other interests, there was also that volunteer position at {b}OneWorld Software{/b}. You’d have to raise your own support for your living expenses, like all the employees there do, but you’d get to help a lot of people by working there."
    "Where are you going to work for the next couple of years?"
    menu:
        "Spectra Tech":
            $ company = "large"
        "Gold Star Development":
            $ company = "mid"
        "Green Valley Engineering":
            $ company = "small"
        "OneWorld Software":
            $ company = "non-profit"

    scene bg black

    if company == "large":
        $ salary = 370
    elif company == "mid":
        $ salary = 270
    elif company == "small":
        $ salary == 200

    label month_start:
        $ time = 30
        if company == "larger":
            $ time -= 1
        if company == "non-profit":
            $ salary = renpy.random.randint(0, 300)
            $ social_good = 10
        if company == "small":
            $ happiness += 10
        call screen schedule(money,happiness,effort,salary,social_good,time)
        $ total_month -= 1

        # moth start
        $ num_event = renpy.random.randint(1, 3)
        while num_event > 0:
            $ event = renpy.random.randint(0, 100)
            if event < 10:
                call earthquake
            elif event < 35:
                call wildlife
            elif event < 40:
                call suggestion
            elif event < 45:
                call eatout
            elif event < 50:
                call sibling
            elif event < 60:
                call lottery
            elif event < 70:
                call workextra
            elif event < 80:
                call mugging
            elif event < 90:
                call suggestion
            else:
                call knockdoor
            show bg black
            $ num_event -= 1


        "Month end"
        if total_month > 0 :
            jump month_start
        else:
            jump ending

        # random event
    label earthquake:
        show bg town
        "An earthquake happened in the city."
        show earthRep_img at right
        show player_img at left
        earthRep "Hello my name is John. I am here in part of the Natural Disaster Relief Association, NDRA, and would like to ask if you could kindly donate some money."
        player "Well, what if I donate my time instead?"
        earthRep "That would be appreciated as well! As a Non-profit we care more about the people facing natural disasters and less on the money accumulated. Help in whichever way you can!"
        hide earthRep_img
        hide player_img
        menu:
            "Make a donation of $100.":
                if money - 100 < 0:
                    "You do not have enough money in your account."
                    return
                else:
                    $money -= 100
                    return
            "Volunteer to do repairs for 1 day.":
                if $time - 1 < 0:
                    "You run out of time."
                else:
                    $time -= 1
                    return
            "Do nothing.":
                return

    label wildlife:
        show bg town
        "You come across an advertisement of the world wildlife fund."
        show wildRep_img at right
        show player_img at left
        wildRep "Hello watchers. My name is Flora and I would like you to see what we are doing to these innocent creatures..."
        player "Oh gosh! That song and those precious eyes. Maybe I should donate some money... or I can keep scrolling these channels!"
        hide wildRep_img
        hide player_img
        menu:
            "Make a donation of $30.":
                if money - 30 < 0:
                    "You do not have enough money in your account."
                    return
                else:
                    $money -= 30
                    return
            "Keep scrolling.":
                return

    label suggestion:
        "You are responsible for coming up with a marketing campaign for your company."
        menu:
            "Suggest sponsoring an all-women hackathon.":
                $effort += 30
                return
            "Suggest using television advertisements which guarantee success.":
                $money += 100
                return

    label eatout:
        "It's Friday night."
        menu:
            "Reward yourself with a fancy Michelin-star dinner.":
                $happiness += 50
                $money -= 30
                return
            "Try out an exotic recipe you found on the Internet the other day.":
                $happiness += 20
                return

    label sibling:
        "Your younger sister just graduated from high school."
        menu:
            "Spend $100 to travel to the graduation.":
                $money -= 100
                $happiness += 50
                return
            "Call to congratulate.":
                return
            "Send a congratulation gift.":
                $money -= 30
                return

    label lottery:
        "You just won a $30 lottery."
        $money += 30
        return
    label workextra:
        "It's weekend, and your plan is to go volunteering at an orphanage renovation site. Your colleague calls asking for urgent coverage, and the shift is double-time pay."
        menu:
            "Go to the construction site for 2 days.":
                $happiness += 50
                $effort += 100
                $time -=2
                return
            "Agree to help your colleague out.":
                $money += 100
                $effort -= 50
                return
    label mugging:
        "While rushing to work, you witness an old lady being mugged."
        menu:
            "Keep commuting. You're running late":
                return
            "Stop to help anyway. The lady is in danger.":
                $effort += 30
                return
    label knockdoor:
        show bg house_live
        "A female neighbor come talk to you about a bake-off event to raise fund for environmental cause."
        show earthRep_img at right
        show player_img at left
        neighbor "Hello neighbor! I see you were in the neighborhood and I... well I would like to invite you to my daughter's bake-sale. This year they are donating their money to NAPER, and we both know how much you love the environment!"
        player "Hmm, you're right. However, I havent been scraving sweets lately, but I do know how to bake a good batch of brownies."
        hide earthRep_img
        hide player_img
        menu:
            "Make a donation of  $30.":
                $money -= 30
                $effort += 10
                return
            "Participate in the event as a baker for a day.":
                $time -= 1
                $effort += 30
                $happiness += 20
                return

    # ending
    label ending:
        if effort < 50 and money > 200 and happiness < 50:
            show text "You’ve worked really hard the last few years, but for what? Sure you have a lot of money, but you might also be seeing the ghosts of Christmases Past, Present, and Future one day soon..." at truecenter
        elif effort > 200 and money > 200 and happiness > 200:
            show text "You’ve worked hard for at your job and for your community, and you’ve managed to also make some time for yourself. Congratulations; you’re an excellent role model for others to come after you." at truecenter
        elif effort > 200 and money < 50 and happiness > 200:
            show text "You may not have a lot of material goods, but you’ve built up an excellent community and that’s what matters to you. You’re right on track to become the next Mother Teresa." at truecenter
        elif effort > 200 and money > 200 and happiness < 50:
            show text "You’ve worked hard at your job and for your community, but you’re feeling burnt out. All this work and you haven’t taken time for yourself. If you try to keep going at this rate you’re going to have trouble getting any work done at all." at truecenter
        else:
            show text "Middle class, fairly happy with your life, trying to do the best you can in this messed up world. You’re the picture of an average American. Maybe you could do better than average, but you’re not doing bad, so you might as well just keep on keeping on." at truecenter
        pase 10.0
return
