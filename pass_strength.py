# import string
# import getpass

# def check_pwd():
#     password = getpass.getpass("Enter Password: ")
#     strength = 0
#     remarks = ''
#     lower_count = upper_count = num_count = wspace_count = special_count = 0

#     for char in list(password):
#         if char in string.ascii_lowercase:
#             lower_count += 1
#         elif char in string.ascii_uppercase:
#             upper_count +=1
#         elif char in string.digits:
#             num_count += 1
#         elif char == ' ':
#             wspace_count +=1
#         else:
#             special_count +=1

#     if lower_count >= 1:
#         strength +=1
#     if upper_count >= 1:
#         strength +=1
#     if num_count >= 1:
#         strength +=1
#     if wspace_count>=1:
#         strength +=1
#     if special_count>=1:
#         strength +=1

#     if strength == 1:
#         remarks = "Very Bad Password!!! Change ASAP"
#     elif strength == 2:
#         remarks = "Not A Good Password!!! Change ASAP"
#     elif strength ==3:
#         remarks = "It's a weak password, consider changing"
#     elif strength == 4:
#         remarks = "It's a hard password, but can be better"
#     elif strength == 5:
#         remarks = "A very strong password"

#     print('Your password has: ')
#     print(f"{lower_count} lowercase characters")
#     print(f"{upper_count} uppercase characters")
#     print(f"{num_count} numeric characters")
#     print(f"{wspace_count} whitespace characters")
#     print(f"{special_count} special characters")

#     print(f"Password Strength:{strength}")
#     print(f"Hint: {remarks}")

# def ask_pwd(another_pwd=False):
#     valid = False
#     if another_pwd:
#         choice=input('Do you want to enter another pwd (y/n): ')
#     else:
#         choice=input('Do you want to check pwd (y/n): ')

#     while not valid:
#         if choice.lower() == 'y':
#             return True
#         elif choice.lower() == 'n':
#             return False
#         else:
#             print('Invalid, Try Again')
# if __name__ == '__main__':
#     print('+++ welcome to PWD checker +++')
#     ask_pw = ask_pwd()
#     while ask_pw:
#         check_pwd()
#         ask_pw = ask_pwd(True)
#         if not ask_pw:
#             print('Exiting PWD checker...')
#             break
import streamlit as st
import string
import hashlib

def check_pwd():
    st.title("🔒 Password Strength & Hash Checker")
    password = st.text_input("Enter your password", type="password")

    if password:
        # # Hashing the password
        # hashed_pwd = hashlib.sha256(password.encode()).hexdigest()

        lower = any(c.islower() for c in password)
        upper = any(c.isupper() for c in password)
        digit = any(c.isdigit() for c in password)
        special = any(c in string.punctuation for c in password)
        length = len(password)

        strength = 0
        if lower: strength += 1
        if upper: strength += 1
        if digit: strength += 1
        if special: strength += 1
        if length >= 8: strength += 1

        # Decide level
        if strength <= 2:
            level = "❌ Weak"
            color = "red"
            remark = "Your password is too weak. Add uppercase, numbers & symbols."
        elif strength == 3:
            level = "🟡 Medium"
            color = "orange"
            remark = "Better, but could still be stronger!"
        elif strength == 4:
            level = "🟢 Strong"
            color = "green"
            remark = "Good job! Your password is strong."
        else:
            level = "💪 Very Strong"
            color = "darkgreen"
            remark = "Excellent! Your password is very secure."

        # Display results
        st.markdown("---")
        st.markdown(f"### Strength Level: <span style='color:{color}'>{level}</span>", unsafe_allow_html=True)
        st.progress(strength / 5)
        st.write(f"**Length:** {length} characters")
        st.write(remark)

        # with st.expander("🔐 View Hashed Password (SHA-256)"):
        #     st.code(hashed_pwd)
