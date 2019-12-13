from django import forms
from .models import Topic, Post

class NewTopicForm(forms.ModelForm):
	subject = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'placeholder': 'Write your topic title',
				'class' : 'bder-cstm-clr'
			}),
			max_length=100,
			label='Topic title'
	)
	message = forms.CharField(
		widget=forms.Textarea(
			attrs={
				'rows': 5, 
				'placeholder': 'What is on your mind?',
				'class' : 'bder-cstm-clr'}
		),
		max_length=4000,
		
	)
	class Meta:
		model = Topic
		fields = ['subject', 'message']
		labels = {
			'subject': 'Topic title'
	}

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message']