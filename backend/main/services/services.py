from main.models import Email


def get_email_list():
    # we take all email objects from the database
    email_object_list = Email.objects.all()
    return email_object_list


def convert_email_list_to_str(email_object_list):
    # we iterate through all email objects and form a human-readable string from them
    email_list = []
    for obj in email_object_list:
        email_list.append(obj.email)
        email_list_str = ',\n'.join(email_list)
        return email_list_str
