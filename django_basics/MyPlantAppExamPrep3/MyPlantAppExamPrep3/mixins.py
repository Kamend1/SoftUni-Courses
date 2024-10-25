class ReadOnlyDisabledFieldsMixin:
    ReadOnlyDisabledFields = []

    def make_fields_read_only_disabled(self):
        for field_name in self.ReadOnlyDisabledFields:
            if field_name in self.fields:
                self.fields[field_name].widget.attrs['readonly'] = True
                self.fields[field_name].widget.attrs['disabled'] = True

    def __init__(self):
        self.make_fields_read_only_disabled()
