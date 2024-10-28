class ReadOnlyDisabledFormFieldsMixin:
    ReadOnlyDisabledFormFields = []

    def make_fields_readonly_disabled(self):
        for field_name in self.ReadOnlyDisabledFormFields:
            if field_name in self.fields:
                self.fields[field_name].widget.attrs['disabled'] = 'disabled'
                self.fields[field_name].widget.attrs['readonly'] = 'readonly'

    def __init__(self, *args, **kwargs):
        self.make_fields_readonly_disabled()