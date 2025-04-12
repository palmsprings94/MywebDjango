from django import forms
from quiz.models import Questions


class Addquestionform(forms.ModelForm):

    class Meta:
        model = Questions
        fields = ['title', 'qbody', 'c1', 'c2', 'c3', 'correctans']

        labels = {
            'title': 'Title',
            'qbody': 'Question',
            'c1': 'Choice A',
            'c2': 'Choice B',
            'c3': 'Choice C',
            'correctans': 'Letter of Answer',
        }

class Answerform(forms.Form):
    def __init__(self, *args, order=None, **kwargs):
        super().__init__(*args, **kwargs)
        for i in range(len(order)):
            self.fields[f"answer{i}"] = forms.CharField(max_length=1)