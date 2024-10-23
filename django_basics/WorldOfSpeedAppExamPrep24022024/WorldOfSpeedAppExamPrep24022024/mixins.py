class ReadOnlyDisabledFieldMixin:
    read_only_and_disabled_fields = []

    def make_fields_read_only_and_disabled(self):
        for field_name in self.read_only_and_disabled_fields:
            if field_name in self.fields:
                self.fields[field_name].widget.attrs['disabled'] = 'disabled'
                self.fields[field_name].widget.attrs['readonly'] = 'readonly'

    def __init__(self, *args, **kwargs):
        self.make_fields_read_only_and_disabled()
