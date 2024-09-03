from django import forms
import datetime
BirthYearChoice=['1980','1981','1982']
class Form1(forms.Form):
    name=forms.CharField(max_length=40,min_length=5,initial="My name is...",required=False)
    comment=forms.CharField(widget=forms.Textarea,required=False)
    short_message=forms.CharField(widget=forms.Textarea(attrs={'rows':3}),required=False)
    email=forms.EmailField(label="Enter your email",required=False)
    agree=forms.BooleanField(required=False,initial=True)
    date=forms.DateField(initial=datetime.date.today)
    birth_date=forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}),required=False)
    birth_year=forms.DateField(widget=forms.SelectDateWidget(years=BirthYearChoice),required=False)
    weight=forms.DecimalField(required=False)
    Color=[
        ("blue","Blue"),
        ("green","Green"),
        ("black","Black")
    ]
    favorite_color=forms.ChoiceField(choices=Color,required=False,help_text="This is the color of the box your pizza will be served in")
    Medium=[
        ("takeaway","Takeaway"),
        ("delivery","Home Delivery"),
        ("dine","Dine In")
    ]
    medium=forms.ChoiceField(widget=forms.RadioSelect,choices=Medium,required=False,label="How do you want your dish served?")
    Pizza=[
        ("alfredo","Alfredo"),
        ("bolognese","Bolognese"),
        ("margherita","Margherita")
    ]
    preferred_pizza=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=Pizza,help_text="Choose the pizza you want to eat",required=False)
    Ingredients=[
        ("Tomato","Tomato"),
        ("Mozzarella","Mozzarella"),
        ("Sausages","Sausages"),
        ("Pepperoni","Pepperoni"),
        ("Olive","Olive")
    ]
    preferred_ingredients=forms.MultipleChoiceField(choices=Ingredients,help_text="You can select more than one ingredients",required=False)
    
    
    
    
    
    