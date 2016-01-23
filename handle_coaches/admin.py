from django.contrib import admin
from .models import Coach

# Register your models here.



class CoachAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                ('first_name', 'last_name'),
            	('skype','email','rating','description'), 
                ('active','price_per_hour'),
            	('spanish','english','french','russian'),
                ('cash','sng','mtt','software'),
                ('discounted','image'),
            	('nl_deep_stack_6max','nl_multistack_6max','nl_cap_6max'),
            	('nl_deep_stack_FR','nl_multistack_FR','nl_cap_FR'),
            	('nl_heads_up_deep','nl_heads_up_multistack','nl_heads_up_cap','cash_other'),
            	('plo_deepstack_6max','plo_multistack_6max','plo_hu'),
            	('sng_normal_FR','sng_turbo_FR','sng_hyperturbo_FR'),
            	('sng_normal_6max','sng_turbo_6max','sng_hyperturbo_6max'),
            	('sng_normal_hu','sng_turbo_hu','sng_hyperturbo_hu','sng_spin_and_go'),
            	('hold_them_manager','snowie','cr_ev','flopzilla','posolver_simple','hold_them_resources')
            	),
            'description': 'Anadir los entrenadores desde aqui.',
            'classes' : ('wide','extrapretty'),
        }),
    )
    list_filter = ('english', 'french')



admin.site.register(Coach, CoachAdmin)