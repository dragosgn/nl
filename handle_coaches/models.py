from __future__ import unicode_literals
from django.conf import settings
from django.db import models
import os
# Create your models here.


class Coach(models.Model):
	#Detalles generales
   first_name = models.CharField(max_length=100, blank = False, null=True)
   last_name = models.CharField(max_length=100, blank = False, null=True)
   email = models.EmailField(max_length=254, blank = False, null=True)
   skype = models.CharField(max_length=100, blank = False, null=True)
   date_joined = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
   date_updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

   #Publicado
   active = models.BooleanField('Publicar', default=True)

   #Coach image
   image = models.ImageField(upload_to='profile_photos', default='static_files/None/no-img.jpg')
   
   #Rating, description 
   rating = models.IntegerField(default = 5, blank=False)
   description = models.CharField(max_length=500, default='Escribe aqui la descripcion del jugador.')

   #Price
   price_per_hour = models.IntegerField(default=0,blank=False,null=False)
   discounted = models.IntegerField(default=0, blank=False)

   #Idiomas
   spanish = models.BooleanField('Espanol', default=False)
   english = models.BooleanField('Ingles', default=False)
   french = models.BooleanField('Frances', default=False)
   russian = models.BooleanField('Ruso', default=False)

   #Coach image
   image = models.ImageField(upload_to='profile_photos', default='static_files/None/no-img.jpg')

   #Rating, description and price
   price_per_hour = models.IntegerField(default=0, blank=False)
   discounted = models.IntegerField(default=0, blank=False)
   rating = models.IntegerField(default = 5, blank=False)
   description = models.CharField(max_length=500, default='Escribe aqui la descripcion del jugador.')

   #Modalidades
   cash = models.BooleanField('Cash', default=False)
   sng = models.BooleanField('SNG', default=False)
   mtt = models.BooleanField('MTT', default=False)
   software = models.BooleanField('Software', default=False)

   #Submodalidades
   #CASH
   nl_deep_stack_6max = models.BooleanField('NL DeepStack:6 Max', default=False)
   nl_multistack_6max = models.BooleanField('NL MultiStack:6 Max', default=False)
   nl_cap_6max = models.BooleanField('NL CAP:6 Max', default=False)
   nl_deep_stack_FR = models.BooleanField('NL DeepStack:FR', default=False)
   nl_multistack_FR = models.BooleanField('NL MultiStack:FR', default=False)
   nl_cap_FR = models.BooleanField('NL CAP:FR', default=False)

   #NL heads up
   nl_heads_up_deep = models.BooleanField('NL Heads Up:FR', default=False)
   nl_heads_up_multistack = models.BooleanField('NL Heads Up:FR', default=False)
   nl_heads_up_cap = models.BooleanField('NL Heads Up:FR', default=False)

   #PLO
   plo_deepstack_6max = models.BooleanField('PLO Deepstack:6 Max', default=False)
   plo_multistack_6max = models.BooleanField('PLO MultiStack:6 Max', default=False)
   plo_hu = models.BooleanField('PLO HU', default=False)
   cash_other = models.CharField(max_length=100,null=True,blank=True)

   #SNG (Sit and go)
   sng_normal_FR = models.BooleanField('SNG Normal:FR', default=False)
   sng_turbo_FR = models.BooleanField('SNG Turbo:FR', default=False)
   sng_hyperturbo_FR = models.BooleanField('SNG Hyperturbo:FR', default=False)

   sng_normal_6max = models.BooleanField('SNG Normal:6max', default=False)
   sng_turbo_6max = models.BooleanField('SNG Turbo:6max', default=False)
   sng_hyperturbo_6max = models.BooleanField('SNG Hyperturbo:6max', default=False)

   sng_normal_hu = models.BooleanField('SNG HU:Normal', default=False)
   sng_turbo_hu = models.BooleanField('SNG HU:Turbo', default=False)
   sng_hyperturbo_hu = models.BooleanField('SNG HU:Hyperturbo', default=False)

   sng_spin_and_go = models.BooleanField('SNG Spin And Go', default=False)

   #MTT
   mtt_normal = models.BooleanField('MTT Normal', default=False)
   mtt_sng = models.BooleanField('MTT SNG', default=False)
   satelite = models.BooleanField('Satelite', default=False)

   #Software
   hold_them_manager = models.BooleanField("Hold'em Manager", default=False)
   snowie = models.BooleanField('Snowie', default=False)
   cr_ev = models.BooleanField('crEV', default=False)
   flopzilla = models.BooleanField('Floopzilla', default=False)
   posolver_simple = models.BooleanField('Piosolver Simple Postflop', default=False)
   hold_them_resources = models.BooleanField("Hold'em Resources", default=False)

   #Submodalidad 2
   #sub_modalidad_2 = models.ManyToManyField(SubModalidad2)

   """
   def get_game_type(self):
       return ",".join([str(p) for p in self.game_type.all()])

   def get_game_sub_type(self):
       return ",".join([str(p) for p in self.game_sub_type.all()])
   """
   def __unicode__(self):
       return "%s %s" %(self.first_name, self.last_name)

   class Meta:
       ordering = ('date_joined',)
























