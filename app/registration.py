from pydantic import BaseModel, SecretStr, validator


class User(BaseModel):
    """
    checks that login consist at least of 5 symbols
    and does not include other symbols than integers and latin  letters
    checks that password has at least 8 symbols and includes capital letters and numbers
    password can not consist of one symbol (for example, 'ssssssss' is invalid password)
    """

    login: str
    password: SecretStr

    @validator("login")
    def login_validator(self, value):
        if len(value) < 5:
            raise ValueError("Invalid login")

        return value

    @validator("password")
    def login_validator(self, value):
        if len(value) < 8:
            raise ValueError("Invalid password")
        return value
