from django import forms
from .models import Jadwal
from bootstrap3_datetime.widgets import DateTimePicker

class JadwalForm(forms.ModelForm):
	# waktu = forms.DateTimeField(input_formats=('%Y-%m-%dT%H:%M:%S+0000',))
	class Meta:
		model = Jadwal
		fields = (
			'kegiatan',
			'waktu',
		)

	
	# def __init__(self, *args, **kwargs):
	# 	super(JadwalForm, self).__init__(*args, **kwargs)
	# 	self.fields['waktu'].widget.attrs['id'] = 'datetimepicker4'
	# 