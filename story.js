// If you are a contributor, you get your name here ;)
// Thanks Loquacious!
// Work in Progress! Want to help? https://github.com/bowser0000/digicross/
var WIP = ('To be added!');

function Custom()
{
  var gender = prompt('Professer: What is your gender?').toLowerCase();
  alert('Professor: Ah! You are a ' + gender + '!');
  var age = prompt('Professor: So how old are you, exactly?');
  alert('Professor: ' + age + ' years old, great!');
  var name1 = prompt('Professor: Oh my! I almost forgot your name! What was it again?');
  alert('Professor: Hello ' + name1 + '!');
  alert('Professor: So you are a ' + gender + ', ' + age + ' years old, and your name is ' + name1 + '?');
  function YesNo()
  {
    var playgameconfirm = prompt('Menu: Yes or No?').toLowerCase();
    if (playgameconfirm == 'yes')
  {
    alert('Professor: Well then, let\'s get started!');
    alert('Professor: So, ' + name1 + ', this is route one! This is where your adventure starts!');
    alert('Professor: ' + name1 + ', wait here while I go get some supplies.');
    alert('DigiCross Trainer: Let\'s fight!');
    alert('Menu: Would you like to att-');
    alert('Professor: WHAT IS GOING ON HERE?');
    alert('DigiCross trainer: BEKFAST!');
    alert('Professor: Don\'t fight him! He has no DigiCross!');
    alert('Professor: That was a close one.');
    alert('Professor: I have been waiting to ask you, what should I nickname you?');
    function nickname()
    {
      var nickname = prompt('Menu: You can set your nickname to your orignal name if you don\'t want one.');
      alert('Professor: So, ' + nickname + ', is it?');
      var nicknameconfirm = prompt('Menu: Yes or No?').toLowerCase();
      if (nicknameconfirm == 'yes')
      {
        alert('Professor: So, ' + nickname + ', shall we go to route 2?');
        alert('We also need you to pick a DigiCross!');
        function choose1()
        {
          digicross1 = prompt('Will you choose Winrad, Semtec or Ilapod?').toLowerCase();
          function finishpick()
          {
            alert('Professor: Here, take ' + digicross1 + ' then!');
            alert('Professor: Take care of him!');
            alert('Professor: I\'ll be on my way! Meet me back home!');
            alert('DigiCross Trainer: Your first battle too? Then let\'s fight!');
            function firstbattlefunc()
            {
              var firstbattle = prompt('Menu: Would you like to Attack, Special or Flee?').toLowerCase();
            }
            firstbattlefunc();
            if (firstbattle == 'attack')
            {
              alert('Menu: ' + digicross1 + ' used Rear Kick! Blooma took 7 damage!');
              alert('DigiCross Trainer: You put up a good fight, but is your strength a lie?');
              alert('DigiCross Trainer: Blooms, use tickle... erm... I mean tackle!');
              alert(WIP);
              alert(digicross1 + ' took' + 'INSERTRANDOMDAMAGEHERE' + ' damage!');
            }
            else if (firstbattle == 'special')
            {
              alert('Menu: You have no specials yet!');
              firstbattlefunc();
            }
            else if (firstbattle == 'flee')
            {
              alert('Menu: You can\'t flee from this battle!');
              firstbattlefunc();
            }
            else
            {
              alert('Menu: Use Attack, Special or Flee!');
              firstbattlefunc();
            }
          }
          if (digicross1 == 'winrad')
          {
            digicross1 = 'Winrad';
            finishpick();
          }
          else if (digicross1 == 'semtec')
          {
            digicross1 = 'Semtec';
            finishipick();
          }
          else if (digicross1 == 'ilapod')
          {
            digicross1 = 'Ilapod';
            finishpick();
          }
          else
          {
            alert('Menu: Use Winrad, Semtec or Ilapod!');
            choose1();
          }
          finishpick();
        }
        choose1();
      }
      else if (nicknameconfirm == 'no')
      {
        nickname();
      }
      else
      {
        alert('Use Yes or No!');
        nickname();
      }
      nickname();
    }
    nickname();
  }
  else if (playgameconfirm == 'no')
  {
    Custom();
  }
  else
  {
    alert('Menu: Use Yes or No!');
   YesNo();
  }
  }
  YesNo();
}
Custom();
