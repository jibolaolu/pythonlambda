#!/bin/python
import boto3
from random import choice
import sys

def get_iam_client_obj():
    session = boto3.session.Session(profile_name='default')
    iam_obj_cli = session.client(service_name='iam')
    return iam_obj_cli


def get_random_password():
    len_of_password = 8
    valid_character_for_password = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!$&_-+*@+=%?0123456789"
    return "".join(choice(valid_character_for_password) for each_char in range(len_of_password))


def main():
    iam_ob_cli = get_iam_client_obj()
    Iam_user_name = "seuntests@gmail.com"
    passwrd = get_random_password()
    Policy_Arn = "arn:aws:iam::aws:policy/AdministratorAccess"
    try:
        iam_ob_cli.create_user(UserName=Iam_user_name)
    except Exception as e:
        if e.response['Error']['Code'] == "EntityAlreadyExists":
            print("The User {} already exists ".format(Iam_user_name))
            sys.exit(0)
        else:
            print("Please verify the following error and retry")
            print(e)
            sys.exit(0)
    iam_ob_cli.create_login_profile(UserName=Iam_user_name, Password=passwrd, PasswordResetRequired=False)
    iam_ob_cli.attach_user_policy(UserName=Iam_user_name, PolicyArn=Policy_Arn)
    print("Here are your IAM Login Credentials Username ={} Password = {}".format(Iam_user_name, passwrd))
    return None

if __name__ == "__main__":
    main()


