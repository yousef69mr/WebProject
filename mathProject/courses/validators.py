import os 
from django.core.exceptions import ValidationError

def validate_file_extension(value):
    
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.doc', '.docx', '.xlsx', '.xls','.txt']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


def validate_image_file_extension(value):
    
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.png','.jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported image file extension.')