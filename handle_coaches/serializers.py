from rest_framework import serializers
from handle_coaches.models import Coach

#Serializing the Coach model
class CoachSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Coach
        fields = ('id',
            'first_name', 
            'last_name',
            'email',
            'skype',
            'image',
            'date_joined',
            'active',
            'price_per_hour',
            'rating',
            #languages
            'spanish',
            'english',
            'french',
            'russian',
            #game_modes
            'cash',
            'sng',
            'mtt',
            'software',

            #CASH: Sub-Game-Modes
            #NL
            'nl_deep_stack_6max',
            'nl_deep_stack_FR',
            'nl_multistack_6max',
            'nl_multistack_FR',
            'nl_cap_6max',
            'nl_cap_FR',

            #PLO
            'plo_deepstack_6max',
            'plo_multistack_6max',
            'plo_hu',
            'cash_other',

            #SNG
            'sng_normal_FR',
            'sng_turbo_FR',
            'sng_hyperturbo_FR',
            'sng_normal_6max',
            'sng_turbo_6max',
            'sng_hyperturbo_6max',
            'sng_normal_hu',
            'sng_turbo_hu',
            'sng_hyperturbo_hu',
            'sng_spin_and_go',

            #MTT
            'mtt_normal',
            'mtt_sng',
            'satelite',

            #Software
            'hold_them_manager',
            'snowie',
            'cr_ev',
            'flopzilla',
            'posolver_simple',
            'hold_them_resources',
            )


