from itertools import chain

from django.shortcuts import render, redirect
from games import models
from games import forms
import random

from games.forms import Inputletter


def games(request):
    return render(request, 'games/games.html', {"title": 'Games'})

def hangman(request):
    gameover = request.session.get('x')

    if gameover:
        if request.method == 'POST':
            subm = forms.Inputletter(request.POST)
            if subm.is_valid():
                if subm.cleaned_data.get('answer').lower() == 'y':
                    models.Hangmansesh.objects.all().delete()
                    return redirect('hangman')
                elif subm.cleaned_data.get('answer').lower() == 'n':
                    models.Hangmansesh.objects.all().delete()
                    return redirect('games')
            else: return redirect('hangman')


    if models.Hangmansesh.objects.first() == None:
        randcat = models.Hangman.objects.all()[random.randint(0, models.Hangman.objects.all().count()-1)]
        catwords = [i for i in randcat.words.split(',')]
        chalikei = models.Hangmansesh(category = randcat.category, word = random.choice(catwords), nonletters = randcat.nonletters, guesses='', disp='', lives=5)
        chalikei.save()

    baksi = models.Hangmansesh.objects.first()
    msg = None

    if baksi.disp != baksi.word and baksi.lives > 0:
        if request.method == 'POST':
            subm = forms.Inputletter(request.POST)
            if subm.is_valid():
                if subm.cleaned_data.get('answer').lower() in baksi.guesses.lower():
                    baksi.lives -= 1
                    baksi.save()
                elif subm.cleaned_data.get('answer').lower() not in baksi.word.lower():
                    baksi.lives -= 1
                    baksi.save()
                elif subm.cleaned_data.get('answer').lower() in baksi.word.lower():
                    baksi.guesses += subm.cleaned_data.get('answer').lower()
                    baksi.save()
            else:
                baksi.lives -= 1
                baksi.save()

    baksi.disp = ''
    baksi.save()
    for i in range(len(baksi.word)):
        if baksi.word[i] in baksi.guesses:
            baksi.disp += baksi.word[i]
        else:
            baksi.disp += '_'
    baksi.save()


    gameover = False
    if baksi.disp == baksi.word and baksi.lives > 0:
        msg = 'Congrats, YOU WON.'
        gameover = True
    elif baksi.lives == 0:
        msg = 'Out of Lives, YOU LOSE.'
        gameover = True

    request.session['x'] = gameover


    subm = forms.Inputletter()

    context = {"title": "Hangman", 'subm': subm, 'baksi': baksi, 'msg': msg, 'gameover': gameover }
    return render(request, 'games/hangman.html', context)


def Oregontrail(request):

    def travel():
        event = random.choice(list(models.Oregontrailevents.objects.all()))
        odds = random.randint(1, 100)
        if event.name == 'Dysentery' and odds <= event.chances:
            stats['hp'] += event.numeffect
            stats['prevevent'] = event.name
        elif event.name == 'Injury' and odds <= event.chances:
            stats['hp'] += event.numeffect
            stats['prevevent'] = event.name
        elif event.name == 'Food Poisoning' and odds <= event.chances:
            stats['hp'] += event.numeffect
            stats['prevevent'] = event.name
        elif event.name == 'Food Stolen' and odds <= event.chances:
            if stats['food'] >= 20:
                stats['food'] += event.numeffect
                stats['prevevent'] = event.name
        elif event.name == 'Tires Stolen' and odds <= event.chances:
            if stats['tires'] >= 2:
                stats['tires'] += event.numeffect
                stats['prevevent'] = event.name
        elif event.name == 'Money Stolen' and odds <= event.chances:
            if stats['money'] >= 200:
                stats['money'] += event.numeffect
                stats['prevevent'] = event.name
        elif event.name == 'Tire Broken' and odds <= event.chances:
            if stats['tires'] >= 1:
                stats['tires'] += event.numeffect
                stats['prevevent'] = event.name
            else:
                stats['prevevent'] = event.name
                request.session['w'] = True
        elif event.name == 'Snakebite' and odds <= event.chances:
            stats['hp'] += event.numeffect
            stats['prevevent'] = event.name
        elif event.name == 'Food Foraged' and odds <= event.chances:
            stats['food'] += event.numeffect
            stats['prevevent'] = event.name
        elif event.name == 'Received Help' and odds <= event.chances:
            stats['hp'] += event.numeffect
            if stats['hp'] > 120: stats['hp'] = 120
            stats['food'] += event.numeffect
            stats['prevevent'] = event.name
        else: stats['prevevent'] = ''

        if stats['food'] >= 20:
            stats['food'] -= 20
        else:
            stats['hp'] -= (20 - stats['food'])
            stats['food'] = 0

        stats['location'] += 1



    statsini = {
        'hp': 120,
        'location': 1,
        'food': 0,
        'money': 3000,
        'bullets': 0,
        'tires': 0,
        'prevevent': ''
    }
    shopava = [1, 4, 6, 10, 12, 14]
    stats = request.session.get('z', statsini)
    isshop = request.session.get('s', False)
    ishunt = request.session.get('h', False)
    wheelmiss = request.session.get('w', False)
    msg = ''
    eventmsg = ''
    choice1 = ''
    choice2 = ''
    choice3 = ''
    choice4 = ''


    if stats['hp'] <= 0:
        stats['hp'] = 0
        msg = "You Died. Play again?"
        choice1 = '1 - Yes'
        choice2 = '2 - No'
        if request.method == 'POST':
            subm = forms.Inputletter(request.POST)
            if subm.is_valid():
                if subm.cleaned_data.get('answer') == '1':
                    request.session.clear()
                    return redirect('oregontrail')
                elif subm.cleaned_data.get('answer') == '2':
                    request.session.clear()
                    return redirect('games')
    elif stats['hp'] > 0 and stats['location'] == 17:
        msg = "Congratulations, you've reached Oregon! Play again?"
        choice1 = '1 - Yes'
        choice2 = '2 - No'
        if request.method == 'POST':
            subm = forms.Inputletter(request.POST)
            if subm.is_valid():
                if subm.cleaned_data.get('answer') == '1':
                    request.session.clear()
                    return redirect('oregontrail')
                elif subm.cleaned_data.get('answer') == '2':
                    request.session.clear()
                    return redirect('games')
    elif wheelmiss:
        msg = "Damn, your tire broke and you've no spare! Play again?"
        choice1 = '1 - Yes'
        choice2 = '2 - No'
        if request.method == 'POST':
            subm = forms.Inputletter(request.POST)
            if subm.is_valid():
                if subm.cleaned_data.get('answer') == '1':
                    request.session.clear()
                    return redirect('oregontrail')
                elif subm.cleaned_data.get('answer') == '2':
                    request.session.clear()
                    return redirect('games')
    elif isshop:
        msg = (f"Welcome to {models.Oregontrailstops.objects.filter(index=stats['location']).first().name} shop!" +
               " What would you like to buy?")
        choice1 = '1 - Buy 20 kgs of food for 250 dollars'
        choice2 = '2 - Buy 50 bullets for 100 dollars'
        choice3 = '3 - Buy 1 wagon tire for 100 dollars'
        choice4 = '4 - Leave shop'
        if request.method == 'POST':
            subm = forms.Inputletter(request.POST)
            if subm.is_valid():
                if subm.cleaned_data.get('answer') == '1':
                    if stats['money'] >= 250:
                        stats['money'] -= 250
                        stats['food'] += 20
                elif subm.cleaned_data.get('answer') == '2':
                    if stats['money'] >= 100:
                        stats['money'] -= 100
                        stats['bullets'] += 50
                elif subm.cleaned_data.get('answer') == '3':
                    if stats['money'] >= 100:
                        stats['money'] -= 100
                        stats['tires'] += 1
                elif subm.cleaned_data.get('answer') == '4':
                    request.session['s'] = False
                request.session['z'] = stats
                return redirect('oregontrail')
    elif ishunt:
        msg = f"Deer hunt time! Atleast 50 bullets required. You currently have {stats['bullets']} bullets. What would you like to do?"
        choice1 = '1 - Proceed to hunt'
        choice2 = '2 - Leave'
        if request.method == 'POST':
            subm = forms.Inputletter(request.POST)
            if subm.is_valid():
                if subm.cleaned_data.get('answer') == '1':
                    if stats['bullets'] >= 50:
                        stats['bullets'] -= 50
                        odds = random.randint(1, 100)
                        if odds >= 50:
                            stats['food'] += 10
                        elif odds < 50 and odds > 20:
                            stats['food'] += 20
                        elif odds <= 20:
                            stats['food'] += 30
                elif subm.cleaned_data.get('answer') == '2':
                    request.session['h'] = False
                request.session['z'] = stats
                return redirect('oregontrail')
    elif stats['location'] in shopava and stats['hp'] > 0:
        if stats['prevevent'] != '':
            eventmsg = f"You got {stats['prevevent']} on the road. "
        msg = (f"{eventmsg}" +
               f"Welcome to {models.Oregontrailstops.objects.filter(index=stats['location']).first().name}!" +
               f" What would you like to do?")
        choice1 = '1 - Proceed to trail'
        choice2 = '2- Shop for food and supplies'
        choice3 = '3 - Rest'
        choice4 = '4 - Hunt for food'
        if request.method == 'POST':
            subm = forms.Inputletter(request.POST)
            if subm.is_valid():
                if subm.cleaned_data.get('answer') == '2':
                    request.session['s'] = True
                elif subm.cleaned_data.get('answer') == '4':
                    request.session['h'] = True
                elif subm.cleaned_data.get('answer') == '3':
                    if stats['food'] >= 20:
                        stats['food'] -= 20
                        stats['hp'] += 30
                        if stats['hp'] > 120: stats['hp'] = 120
                    else: stats['hp'] -= 5
                elif subm.cleaned_data.get('answer') == '1':
                    travel()
                request.session['z'] = stats
                return redirect('oregontrail')
    elif stats['location'] not in shopava and stats['hp'] > 0:
        if stats['prevevent'] != '':
            eventmsg = f"You got {stats['prevevent']} on the road. "
        msg = (f"{eventmsg}" +
               f"Welcome to {models.Oregontrailstops.objects.filter(index=stats['location']).first().name}!" +
               f" What would you like to do?")
        choice1 = '1 - Proceed to trail'
        choice2 = '2 - Hunt for food'
        choice3 = '3 - Rest'
        if request.method == 'POST':
            subm = forms.Inputletter(request.POST)
            if subm.is_valid():
                if subm.cleaned_data.get('answer') == '2':
                    request.session['h'] = True
                elif subm.cleaned_data.get('answer') == '3':
                    if stats['food'] >= 20:
                        stats['food'] -= 20
                        stats['hp'] += 30
                        if stats['hp'] > 120: stats['hp'] = 120
                    else: stats['hp'] -= 5
                elif subm.cleaned_data.get('answer') == '1':
                    travel()
                request.session['z'] = stats
                return redirect('oregontrail')



    request.session['z'] = stats
    subm = forms.Inputletter()
    context = {
        'title': 'Oregon Trail',
        'stats': stats,
        'msg': msg,
        'eventmsg': eventmsg,
        'subm': subm,
        'choice1': choice1,
        'choice2': choice2,
        'choice3': choice3,
        'choice4': choice4,
    }
    return render(request, 'games/oregontrail.html', context)


def tictactoe(request):


    def aimove():
        num = random.choice(list(tgame['avai'].keys()))
        while tgame['avai'][num] != ' ':
            num = random.choice(list(tgame['avai'].keys()))
        tgame['avai'][num] = comp
        request.session['t'] = tgame
    def win():
        if (
            (tgame['avai']['1'] == tgame['avai']['2'] == tgame['avai']['3'] != ' ') or
            (tgame['avai']['4'] == tgame['avai']['5'] == tgame['avai']['6'] != ' ') or
            (tgame['avai']['7'] == tgame['avai']['8'] == tgame['avai']['9'] != ' ') or
            (tgame['avai']['1'] == tgame['avai']['4'] == tgame['avai']['7'] != ' ') or
            (tgame['avai']['2'] == tgame['avai']['5'] == tgame['avai']['8'] != ' ') or
            (tgame['avai']['3'] == tgame['avai']['6'] == tgame['avai']['9'] != ' ') or
            (tgame['avai']['1'] == tgame['avai']['5'] == tgame['avai']['9'] != ' ') or
            (tgame['avai']['3'] == tgame['avai']['5'] == tgame['avai']['7'] != ' ')
        ): return True


    tini = {
        'avai': {
            '1': ' ',
            '2': ' ',
            '3': ' ',
            '4': ' ',
            '5': ' ',
            '6': ' ',
            '7': ' ',
            '8': ' ',
            '9': ' '
        }
    }
    tgame = request.session.get('t', tini)
    ldisp = {
        'line1': f"{tgame['avai']['1']}|{tgame['avai']['2']}|{tgame['avai']['3']}",
        'line2': f"{tgame['avai']['4']}|{tgame['avai']['5']}|{tgame['avai']['6']}",
        'line3': f"{tgame['avai']['7']}|{tgame['avai']['8']}|{tgame['avai']['9']}",
    }


    player = request.session.get('p', 'ZZZ')
    comp = request.session.get('c', 'ZZZ')
    gofirst = request.session.get('1st', None)
    lastmove = request.session.get('last', None)
    msg = ""


    if tgame == tini and player == 'ZZZ':
        msg = "O or X?"
        if request.method == 'POST':
            subm = forms.Inputletter(request.POST)
            if subm.is_valid():
                if subm.cleaned_data.get('answer').upper() == 'O' or subm.cleaned_data.get('answer').upper() == 'X':
                    request.session['p'] = subm.cleaned_data.get('answer').upper()
                    if subm.cleaned_data.get('answer').upper() == 'O': request.session['c'] = 'X'
                    else: request.session['c'] = 'O'
                    msg = "Go first? Y/N"
    elif tgame == tini and gofirst is None:
        msg = "Go first? Y/N"
        if request.method == 'POST':
            subm = forms.Inputletter(request.POST)
            if subm.is_valid():
                if subm.cleaned_data.get('answer').upper() == 'Y' or subm.cleaned_data.get('answer').upper() == 'N':
                    if subm.cleaned_data.get('answer').upper() == 'Y': request.session['1st'] = True
                    elif subm.cleaned_data.get('answer').upper() == 'N':
                        request.session['1st'] = False
                        aimove()
                        request.session['last'] = 'notme'
                        return redirect('tictactoe')
                    msg = "type the number where you want to make a move"
    elif (' ' not in tgame['avai'].values()) or win():
        if win() and lastmove == 'me': msg = "You Win! Play again? Y/N"
        elif win() and lastmove == 'notme': msg = "You Lose! Play again? Y/N"
        else: msg = "Gameover! Play again? Y/N"
        if request.method == 'POST':
            subm = forms.Inputletter(request.POST)
            if subm.is_valid():
                if subm.cleaned_data.get('answer').upper() == 'Y' or subm.cleaned_data.get('answer').upper() == 'N':
                    if subm.cleaned_data.get('answer').upper() == 'Y':
                        request.session.clear()
                        return redirect('tictactoe')
                    elif subm.cleaned_data.get('answer').upper() == 'N':
                        request.session.clear()
                        return redirect('games')
    else:
        msg = "type the number where you want to make a move"
        if request.method == 'POST':
            subm = forms.Inputletter(request.POST)
            if subm.is_valid() and subm.cleaned_data.get('answer') in tgame['avai'].keys():
                if tgame['avai'][subm.cleaned_data.get('answer')] == ' ':
                    tgame['avai'][subm.cleaned_data.get('answer')] = player
                    request.session['t'] = tgame
                    request.session['last'] = 'me'
                    if not win() and ' ' in tgame['avai'].values():
                        aimove()
                        request.session['last'] = 'notme'
                        return redirect('tictactoe')
                    return redirect('tictactoe')


    request.session['t'] = tgame
    subm = forms.Inputletter()
    context = {
        'title': 'TicTacToe',
        'tgame': tgame,
        'subm': subm,
        'msg': msg,
        'ldisp': ldisp,
    }
    return render(request, 'games/tictactoe.html', context)