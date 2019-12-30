from rest_framework import serializers
from .models import contact

class contactSerializer(serializers.ModelSerializer):
	class Meta:
		model = contact
		fields = ('id', 'first_name', 'last_name', 'telephone', 'note', 'company_name', 'date_created', 'last_modified')