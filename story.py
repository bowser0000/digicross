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
        elif playgameconfirm == 'No':
            Custom()
        else:
            print 'Please capitalise the first letter, and use Yes or No!'
            YesNo()
