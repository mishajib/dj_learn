from blog.models import Category, Post
from django import forms


class CategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(CategoryForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.errors:
                visible.field.widget.attrs['class'] = 'form-control is-invalid'
            else:
                visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Category
        fields = ['title', 'slug']
        error_messages = {
            'title': {
                'required': "The title is required!",
            },
        }


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(PostForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.errors:
                visible.field.widget.attrs['class'] = 'form-control is-invalid'
            else:
                visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Post
        fields = ['title', 'content', 'user', 'category']
        error_messages = {
            'title': {
                'required': "The title is required!",
            },
            'content': {
                'required': "The content is required!",
            },
            'user': {
                'required': "The user is required!",
            },
            'category': {
                'required': "The category is required!",
            },
        }
