from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


# CATEGORIES = Category.objects.all().values_list('name', 'name')

# class PostForm(forms.ModelForm):
#     class Meta:
#         field = ('category')

#         widgets = {
#             'category': forms.Select(choices=CATEGORIES, attrs={'class': 'form-control'})
#         }