# -*- coding: utf-8 -*-
from . import forms
from src.security import models

# The model to administrate
MODEL = models.ImportedLDAPUser
# The path of model to administrate.
MODEL_PATH = 'importedldapuser'
# Pagination
INSTANCES_AMOUNT_PER_PAGE = 10
# The forms of model to administrate
FORM_DETAIL = forms.ImportedLDAPUserDetail
FORM_UPDATE = forms.ImportedLDAPUserUpdate
FORM_DELETE = forms.ImportedLDAPUserDelete
