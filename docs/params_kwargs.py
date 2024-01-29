from typing import Optional
class kwargs:
    def __init__(self,
        email: Optional[str] = None,
        pswd: Optional[str] = None,
        manager: Optional[str] = None,
        name: Optional[str] = None,
        sellist1 : Optional[str] = None,
        text : Optional[str] = None) -> None:
        self.name = name
        self.pswd = pswd
        self.email = email
        pass
if __name__ == "__main__":
    user = { 
        "pswd": "Password123!"
        ,"email": "chulsoo.kim@example.com"
        ,"name": "김철수"
    }
    kwargs(**user)  # dictionary를 값으로 넘겨줄 때는 앞에 **를 붙임
    pass