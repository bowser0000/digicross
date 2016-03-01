# Work in Progress! Want to help? https://github.com/bowser0000/digicross/
TempName = 'DigiCross'
WIP = 'To be added!'


def Custom():
    gender = raw_input('What is your gender?').capitalize()
    print 'Ah, you are a %s!' % gender
    age = raw_input('So how old are you, exactly?')
    print '%s years old, great!' % age
    name = raw_input('Oh, my! I almost forgot your name! What was it again?')
    print 'Hello, %s!' % name
    print 'So you are a %s, %s years old, and your name is %s?' % (gender, age, name)

    def YesNo():
        playgameconfirm = raw_input('Yes or No?').lower()
        if playgameconfirm == 'yes':
            print 'Well then, let\' get started!'
            print 'So, %s, this is route 1! This is where your adventure starts!' % (name)
            print '%s, wait here while I go get some supplies' % (name)
            print '%s Trainer: Let\'s fight!' % (TempName)
            print 'Would you like to att-'
            print 'WHAT\'S GOING ON HERE?'
            print '%s Trainer: BEKFAST!' % (TempName)
            print 'Don\'t fight him! He has no %s!' % (TempName)
            print 'That was a close one.'
            print 'I have been waiting to ask you, what should I nickname you?'

            def nickname():
                nickname = raw_input('You can set your nickname to your original name if you don\'t want one.')
                print 'So, %s, is it?' % (nickname)
                nicknameconfirm = raw_input('Yes or No?').lower()
                if nicknameconfirm == 'yes':
                    print 'So, %s, shall we go to route 2?' % (nickname)
                    print 'We also need you to pick a %s!' % (TempName)

                    def choose1():
                        digicross1 = raw_input('Will you choose Winrad, Semtec or Ilapod?').lower()

                        def finishpick():
                            print '%s' % (WIP)
                        if digicross1 == 'winrad':
                            starter = 'Winrad'
                            finishpick()
                        elif digicross1 == 'semtec':
                            starter = 'Semtec'
                            finishpick()
                        elif digicross1 == 'ilapod':
                            starter = 'ilapod'
                            finishpick()
                        else:
                            print 'Use Winrad, Semtec or Ilapod'
			    choose1()
                    choose1()
                elif nicknameconfirm == 'no':
                    nicknameconfirm()
                else:
                    print 'Use Yes or No!'
                    nicknameconfirm()
            nickname()
        elif playgameconfirm == 'no':
            Custom()
        else:
            print 'Use Yes or No!'
            YesNo()
    YesNo()
Custom()
