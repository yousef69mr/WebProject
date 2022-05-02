
import six
from django.contrib.auth .tokens import PasswordResetTokenGenerator



class TokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, timestamp):
        
        #print(six.text_type(user.id)+six.text_type(timestamp)+six.text_type(user.is_verified))
        #print(six.text_type(user.id))
        #print(six.text_type(timestamp))
        #print(six.text_type(user.is_verified))
        #print(user.id)
        
        return six.text_type(user.id)+six.text_type(timestamp)+six.text_type(user.is_verified)


generate_token = TokenGenerator()