from django.forms import DateTimeInput


class XDSoftDateTimePickerInput(DateTimeInput):
    template_name = r'widgets/xdsoft_datetimepicker.html'
