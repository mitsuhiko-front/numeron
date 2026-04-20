def validate_input(user_input):
    if len(user_input) != 3:
        return False, "3桁で入力してください"
    
    if not user_input.isdigit():
        return False, "数字で入力してください"
    
    if len(set(user_input)) != 3:
        return False, "重複した数字は使えません"