from django import forms


class PostForm(forms.Form):
    name = forms.CharField(label='Nome')
    data = forms.DateField(label='Data')
    hour = forms.TimeField(label='Hora')
    content = forms.CharField(label='Conteúdo')
    image_post = forms.ImageField(label='Imagem do Post')
    icon_user = forms.ImageField(label='Ícone do Usuário')


class StoryForm(forms.Form):
    name = forms.CharField(label='Nome')
    image = forms.ImageField(label='Imagem')


class EventForm(forms.Form):
    name = forms.CharField(label='Nome')
    data = forms.DateField(label='Data')
    address = forms.CharField(label='Endereço')


class ChatForm(forms.Form):
    name = forms.CharField(label='Nome')
    icon_user = forms.ImageField(label='Ícone do Usuário')
