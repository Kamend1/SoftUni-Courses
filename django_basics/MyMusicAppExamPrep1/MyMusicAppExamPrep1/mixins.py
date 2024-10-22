class ReadOnlyDisabledMixin:
    read_only_disabled_fields = []

    def convert_field_to_read_only_disabled_field(self):
        for field_name in self.read_only_disabled_fields:
            if field_name in self.fields:
                self.field['field_name'].widget.attrs['disabled'] = 'disabled'
                self.field['field_name'].widget.attrs['readonly'] = 'readonly'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.convert_field_to_read_only_disabled_field()

