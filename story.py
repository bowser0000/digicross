# Work in Progress! Want to help? https://github.com/bowser0000/digicross/
TempName = 'DigiCross'
WIP = 'To be added!'


def Custom():
    gender = raw_input('Professor: What is your gender?').capitalize()
    print 'Professor: Ah, you are a %s!' % gender
    age = raw_input('Professor: So how old are you, exactly?')
    print 'Professor: %s years old, great!' % age
    name = raw_input('Professor: Oh, my! I almost forgot your name! What was it again?')
    print 'Professor: Hello, %s!' % name
    print 'Professor: So you are a %s, %s years old, and your name is %s?' % (gender, age, name)

    def YesNo():
        playgameconfirm = raw_input('Yes or No?').lower()
        if playgameconfirm == 'yes':
            print 'Professor: Well then, let\' get started!'
            print 'Professor: So, %s, this is route 1! This is where your adventure starts!' % (name)
            print 'Professor: %s, wait here while I go get some supplies' % (name)
            print '%s Trainer: Let\'s fight!' % (TempName)
            print 'Menu: Would you like to att-'
            print 'Professor: WHAT IS GOING ON HERE?'
            print '%s Trainer: BEKFAST!' % (TempName)
            print 'Professor: Don\'t fight him! He has no %s!' % (TempName)
            print 'Professor: That was a close one.'
            print 'Professor: I have been waiting to ask you, what should I nickname you?'

            def nickname():
                nickname = raw_input('Menu: You can set your nickname to your original name if you don\'t want one.')
                print 'Professor: So, %s, is it?' % (nickname)
                nicknameconfirm = raw_input('Yes or No?').lower()
                if nicknameconfirm == 'yes':
                    print 'Professor: So, %s, shall we go to route 2?' % (nickname)
                    print 'Professor: We also need you to pick a %s!' % (TempName)

                    def choose1():
                        digicross1 = raw_input('Menu: Will you choose Winrad, Semtec or Ilapod?').lower()

                        def finishpick():
                            print 'Professer: Here, take %s then!' % (starter)
                            print 'Professer: Take care of him!'
                            print 'Professer: I\'ll be on my way! Meet me back home!'
                            print '%s Trainer: Your first battle too? Let\'s fight!' % (TempName)
                            
                            def firstbattledef():
                            	firstbattle = raw_input('Menu: Would you like to Attack, Special or Flee?').lower()
                            firstbattledef()
                            if firstbattle == 'attack':
                            	print '%s used Rear Kick! Blooma took 7 damage!' % (Starter)
                            	print '%s Trainer: You put up a good fight, but is your strength a lie?' % (TempName)
                            	print '%s Trainer: Blooma use tickle! Erm... I mean tackle!' % (TempName)
                            	print '%s' % (WIP)
                            elif firstbattle == 'special':
                                print 'Menu: You have no specials!'
                        	firstbattledef()
                            elif firstbattle == 'flee':
                            	print 'Menu: You can\'t run from this battle!'
                            	firstbattledef()
                            else:
                            	print 'Menu: Use Attack, Special or Flee!'
                            	firstbattledef()
                        if digicross1 == 'winrad':
                            starter = 'Winrad'
                            finishpick()
                        elif digicross1 == 'semtec':
                            starter = 'Semtec'
                            finishpick()
                        elif digicross1 == 'ilapod':
                            starter = 'Ilapod'
                            finishpick()
                        else:
                            print 'Menu: Use Winrad, Semtec or Ilapod'
			    choose1()
			finishpick()
                    choose1()
                elif nicknameconfirm == 'no':
                    nicknameconfirm()
                else:
                    print 'Menu: Use Yes or No!'
                    nicknameconfirm()
            nickname()
        elif playgameconfirm == 'no':
            Custom()
        else:
            print 'Menu: Use Yes or No!'
            YesNo()
    YesNo()
Custom()
