from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from pymongo import MongoClient

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Connect to the MongoDB database
        client = MongoClient('mongodb://localhost:27017/')
        self.db = client['my_database']
    
    def login(self):
        # Get user input
        username = self.ids.username_input.text
        password = self.ids.password_input.text
        
        # Verify user credentials
        user = self.db.users.find_one({'username': username, 'password': password})
        if user:
            self.add_widget(Label(text='Login successful!'))
        else:
            self.add_widget(Label(text='Invalid username or password'))
    
    def sign_up(self):
        # Get user input
        username = self.ids.username_input.text
        password = self.ids.password_input.text
        email = self.ids.email_input.text
        
        # Insert user information into database
        user = {'username': username, 'password': password, 'email': email}
        self.db.users.insert_one(user)
        
        # Clear input fields
        self.ids.username_input.text = ''
        self.ids.password_input.text = ''
        self.ids.email_input.text = ''

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()