from django.shortcuts import render
from django.template.context_processors import request
import random
from quiz import forms
from quiz import models
def quiz(request):
    context = {"title" : "Quiz"}
    return render(request, 'quiz/quiz.html', context)


def addquestions(request):
    context = {"title" : 'Add Questions',}
    return render(request, 'quiz/addquestions.html', context)


def addquestionsbeginner(request):
    if request.method == 'POST':
        submissions = forms.Addquestionform(request.POST)
        if submissions.is_valid():
            submissions.save()
    submissions = forms.Addquestionform()
    questions = models.Questions.objects.all()
    context = {"title" : "Add Questions - Beginner", "submissions" : submissions, "questions" : questions}
    return render(request, 'quiz/addquestionsbeginner.html', context)

def beginnerquiz(request):
    questions = models.Questions.objects.all()
    numb = len(questions)
    score = None

    if request.method == 'POST':
        prevnumlist = request.session.get('x', list(range(numb)))
        subm = forms.Answerform(request.POST, order=prevnumlist)

        if subm.is_valid():
            useranswers = [i[1] for i in subm.cleaned_data.items()]
            score = 0
            for i, x in enumerate(prevnumlist):
                if questions[x].correctans.lower() == useranswers[i].lower():
                    score += 1

    numlist = [i for i in range(questions.count())]
    random.shuffle(numlist)
    request.session['x'] = numlist
    subm = forms.Answerform(order=numlist)

    context = {
        "title": "Beginner Quiz",
        "subm": subm,
        "score": score,
        "num": numb,
        "questions": questions,
        "numlist": numlist,
    }
    return render(request, 'quiz/beginnerquiz.html', context)
