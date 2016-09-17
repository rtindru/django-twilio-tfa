from django.dispatch import Signal


register_user_tfa = Signal(providing_args=["email", "phone_number", "country_code"])
send_tfa_new_user = Signal(providing_args=["email", "phone_number", "country_code"])
