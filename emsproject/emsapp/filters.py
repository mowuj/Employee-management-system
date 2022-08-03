
import django_filters
from django_filters import DateFilter,CharFilter
from .models import*

class EmployeeFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name="date",lookup_expr='gte')
    # end_date = DateFilter(field_name="date",lookup_expr='lte')
    
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['full_name',
                    'email',
                    'district',
                    'phone',
                    'nid',
                    'ssc',
                    'hsc',
                    'honors',
                    'masters',
                    'selary',
                    'email',
                    'image',
                    'father_name',
                    'mother_name']
class ClientFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name="date",lookup_expr='gte')
    # end_date = DateFilter(field_name="date",lookup_expr='lte')
    
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ['email',
                    'nid',
                    'image',
                    'phone'
                    ]
