# -*- coding: utf-8 -*-
from src.security import models
from django import forms
from django.utils.translation import ugettext_lazy as _
import os
import shutil

FIELD_IS_ACTIVE = forms.BooleanField(
    label=_('ADMINISTRATION_MODULE_SECURITY_IMPORTEDLDAPUSER_IS_ACTIVE'),
    required=False,
    widget=forms.CheckboxInput(
        attrs={
            'id': 'is_active',
            'aria-describedby': 'is_active_icon',
            'icon': 'fa fa-check-square-o',
        },
    ),
)
FIELD_CREATED = forms.DateField(
    label=_('ADMINISTRATION_MODULE_SECURITY_IMPORTEDLDAPUSER_CREATED'),
    required=False,
    widget=forms.DateInput(
        attrs={
            'id': 'created',
            'aria-describedby': 'created_icon',
            'icon': 'fa fa-clock-o',
        },
    ),
)
FIELD_MODIFIED = forms.DateField(
    label=_('ADMINISTRATION_MODULE_SECURITY_IMPORTEDLDAPUSER_MODIFIED'),
    required=False,
    widget=forms.DateInput(
        attrs={
            'id': 'modified',
            'aria-describedby': 'modified_icon',
            'icon': 'fa fa-clock-o',
        },
    ),
)
FIELD_AVATAR = forms.ImageField(
    label=_('ADMINISTRATION_MODULE_SECURITY_IMPORTEDLDAPUSER_AVATAR'),
    required=False,
    widget=forms.FileInput(
        attrs={
            'id': 'avatar',
            'icon': 'fa fa-picture-o',
            'id_button_upload': 'avatar-button-upload',
            'id_image_upload': 'avatar-image-upload',
            'style': 'display: none;',
        },
    ),
)
FIELD_FIRST_NAME = forms.CharField(
    label=_('ADMINISTRATION_MODULE_SECURITY_IMPORTEDLDAPUSER_FIRST_NAME'),
    required=False,
    widget=forms.TextInput(
        attrs={
            'id': 'first_name',
            'class': 'form-control',
            'aria-describedby': 'first_name_icon',
            'icon': 'fa fa-globe',
        },
    ),
)
FIELD_LAST_NAME = forms.CharField(
    label=_('ADMINISTRATION_MODULE_SECURITY_IMPORTEDLDAPUSER_LAST_NAME'),
    required=False,
    widget=forms.TextInput(
        attrs={
            'id': 'last_name',
            'class': 'form-control',
            'aria-describedby': 'last_name_icon',
            'icon': 'fa fa-globe',
        },
    ),
)
FIELD_IDENTIFIER = forms.CharField(
    label=_('ADMINISTRATION_MODULE_SECURITY_IMPORTEDLDAPUSER_IDENTIFIER'),
    required=False,
    widget=forms.TextInput(
        attrs={
            'id': 'identifier',
            'class': 'form-control',
            'aria-describedby': 'identifier_icon',
            'icon': 'fa fa-user',
        },
    ),
)
FIELD_EMAIL = forms.EmailField(
    label=_('ADMINISTRATION_MODULE_SECURITY_IMPORTEDLDAPUSER_EMAIL'),
    required=False,
    widget=forms.EmailInput(
        attrs={
            'id': 'email',
            'class': 'form-control',
            'aria-describedby': 'email_icon',
            'icon': 'fa fa-envelope-o',
        },
    ),
)
FIELD_DETAIL = forms.CharField(
    label=_('ADMINISTRATION_MODULE_SECURITY_IMPORTEDLDAPUSER_DETAIL'),
    required=False,
    widget=forms.Textarea(
        attrs={
            'id': 'detail',
            'class': 'form-control',
            'aria-describedby': 'detail_icon',
            'icon': 'fa fa-globe',
            'rows': 5,
        },
    ),
)


def void___field_attribute_placeholder_locale_reload(field, locale):
    field.widget.attrs['placeholder'] = '- %s -' % (_(locale),)


def void___field_attribute_help_text_locale_reload(field, locale):
    field.help_text = '\"%s\"' % (_(locale),)


class ImportedLDAPUserDetail(forms.ModelForm):
    is_active = FIELD_IS_ACTIVE
    created = FIELD_CREATED
    modified = FIELD_MODIFIED
    avatar = FIELD_AVATAR
    first_name = FIELD_FIRST_NAME
    last_name = FIELD_LAST_NAME
    identifier = FIELD_IDENTIFIER
    email = FIELD_EMAIL
    detail = FIELD_DETAIL

    class Meta:
        model = models.ImportedLDAPUser
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)


class ImportedLDAPUserUpdate(forms.ModelForm):
    is_active = FIELD_IS_ACTIVE
    avatar = FIELD_AVATAR
    first_name = FIELD_FIRST_NAME
    last_name = FIELD_LAST_NAME
    identifier = FIELD_IDENTIFIER
    email = FIELD_EMAIL
    detail = FIELD_DETAIL

    class Meta:
        model = models.ImportedLDAPUser
        fields = ['is_active', 'avatar', 'first_name', 'last_name', 'identifier', 'email', 'detail', ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        self.instance_current = kwargs.pop('instance_current')
        super().__init__(*args, **kwargs)
        #
        # is_active
        void___field_attribute_help_text_locale_reload(field=self.fields['is_active'], locale='ADMINISTRATION_MODULE_SECURITY_IMPORTEDLDAPUSER_IS_ACTIVE_HELP_TEXT')
        # first_name
        void___field_attribute_placeholder_locale_reload(field=self.fields['first_name'], locale='ADMINISTRATION_MODULE_SECURITY_IMPORTEDLDAPUSER_FIRST_NAME')
        self.fields['first_name'].widget.attrs['readonly'] = 'readonly'
        self.fields['first_name'].widget.attrs['autofocus'] = True
        # last name
        void___field_attribute_placeholder_locale_reload(field=self.fields['last_name'], locale='ADMINISTRATION_MODULE_SECURITY_IMPORTEDLDAPUSER_LAST_NAME')
        self.fields['last_name'].widget.attrs['readonly'] = 'readonly'
        # identifier
        void___field_attribute_placeholder_locale_reload(field=self.fields['identifier'], locale='ADMINISTRATION_MODULE_SECURITY_IMPORTEDLDAPUSER_IDENTIFIER')
        self.fields['identifier'].widget.attrs['readonly'] = 'readonly'
        # email
        void___field_attribute_placeholder_locale_reload(field=self.fields['email'], locale='ADMINISTRATION_MODULE_SECURITY_IMPORTEDLDAPUSER_EMAIL')
        self.fields['email'].widget.attrs['readonly'] = 'readonly'
        # detail
        void___field_attribute_placeholder_locale_reload(field=self.fields['detail'], locale='ADMINISTRATION_MODULE_SECURITY_IMPORTEDLDAPUSER_DETAIL')
        void___field_attribute_help_text_locale_reload(field=self.fields['detail'], locale='ADMINISTRATION_MODULE_SECURITY_IMPORTEDLDAPUSER_DETAIL_HELP_TEXT')
        self.fields['detail'].widget.attrs['readonly'] = 'readonly'

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')
        if self.files.get('avatar'):
            if len(self.files.get('avatar')) > 1 * 1024 * 1024:  # 1MB
                raise forms.ValidationError(_('ADMINISTRATION_MODULE_SECURITY_IMPORTEDLDAPUSER_VALIDATION The avatar should not be beggear than %(weight)s.') % {'weight': '1mb', })
        return avatar

    def clean_first_name(self):
        first_name = self.instance_current.first_name
        return first_name

    def clean_last_name(self):
        last_name = self.instance_current.last_name
        return last_name

    def clean_identifier(self):
        identifier = self.instance_current.identifier
        return identifier

    def clean_email(self):
        email = self.instance_current.email
        return email

    def clean_detail(self):
        detail = self.instance_current.detail
        return detail

    def save(self, commit=True):
        instance = super(ImportedLDAPUserUpdate, self).save(commit=False)
        #
        if commit:
            # avatar
            if self.instance_current.avatar is not None and self.instance_current.avatar != '' and instance.avatar is not None and instance.avatar != '':
                if self.instance_current.avatar != instance.avatar:
                    if os.path.exists(self.instance_current.avatar.path):
                        os.remove(self.instance_current.avatar.path)
                if self.instance_current.identifier != instance.identifier:
                    if self.instance_current.avatar != instance.avatar:
                        if os.path.exists(self.instance_current.string___folder_path()):
                            shutil.rmtree(self.instance_current.string___folder_path())
                    else:
                        instance.avatar = '%s/%s/%s/%s.jpg' % (models.FOLDER_IMPORTEDLDAPUSER_PATH, instance.ldap_group, instance.identifier, instance.identifier,)
                        if os.path.exists(self.instance_current.avatar.path) and os.path.exists(self.instance_current.string___folder_path()):
                            os.rename(self.instance_current.avatar.path, '%s/%s.jpg' % (self.instance_current.string___folder_path(), instance.identifier,))
                            os.rename(self.instance_current.string___folder_path(), self.instance.string___folder_path())
            # save to data base
            instance.save()
        return instance


class ImportedLDAPUserDelete(forms.ModelForm):
    class Meta:
        model = models.ImportedLDAPUser
        fields = ['id', ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

    def delete(self):
        # avatar
        if self.instance.avatar is not None and self.instance.avatar != '':
            if os.path.exists(self.instance.string___folder_path()):
                shutil.rmtree(self.instance.string___folder_path())
        self.instance.delete()
