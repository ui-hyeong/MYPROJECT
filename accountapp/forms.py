from django.contrib.auth.forms import UserCreationForm


class AccountCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 부모 클래스의 변수를 다 받아오는 것

        self.fields['username'].disabled = True