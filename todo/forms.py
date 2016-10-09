from django import forms
from .models import Jadwal

class JadwalForm(forms.ModelForm):
	# waktu = forms.DateTimeField(input_formats=('%Y-%m-%dT%H:%M:%S+0000',))
	class Meta:
		model = Jadwal
		fields = (
			'kegiatan',
			'waktu',
		)