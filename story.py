def Custom():
    gender = raw_input('What is your gender?')
    print 'Ah, you are a %s!' % gender
    age = raw_input('So how old are you, exactly?')
    print '%s years old, great!' % age
    name = raw_input('Oh, my! I almost forgot your name! What was it again?')
    print 'Hello, %s!' % name
    print 'So you are a %s, %s years old, and your name is %s?' % (gender, age, name)
    def YesNo():
        playgameconfirm = raw_input('Yes or No?')
        if playgameconfirm == 'Yes':
            print 'Well then, let\' get started!'
            print 'So, %s, this is route 1! This is where your adventure starts!' % (name)
            print '%s, wait here while I go get some supplies' % (name)
            print 'TempName Trainer: Let\'s fight!'
            print 'Would you like to att-'
            print 'WHAT\'S GOING ON HERE?'
            print 'TempName Trainer: BEKFAST!'
            print 'Don\'t fight him! He has no TempName!'
            print 'That was a close one.'
            print 'I have been waiting to ask you, what should I nickname you?'
            def nickname():
                nickname = raw_input('You can set your nickname to your original name if you don\'t want one.')
                print 'So, %s, is it?' % (nickname)
                nicknameconfirm = raw_input('Yes or No?')
                if nicknameconfirm == 'Yes':
                    print 'So, %s, shall we go to route 2?' % (nickname)
                elif nicknameconfirm == 'No':
                    nicknameconfirm()
                else:
                    print 'Please capitalise the first letter and use Yes or No'
                    nicknameconfirm()
        elif playgameconfirm == 'No':
            Custom()
        else:
            print 'Please capitalise the first letter, and use Yes or No!'
            YesNo()
