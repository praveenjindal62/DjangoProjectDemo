from django.contrib import admin
from polls.models import Poll
from polls.models import Choice
class ChoiceInline(admin.TabularInline):
	model=Choice
	extra=5
class PollAdmin(admin.ModelAdmin):
	list_display=('question','pub_date')
	fieldsets=[
		(None,{'fields':['question']}),
		('Date Information',{'fields':['pub_date'],'classes':['collapse']}),

	]
	inlines=[ChoiceInline]
	list_filter=['pub_date']
	search_fields = ['question']
	date_hierarchy = 'pub_date'
admin.site.register(Poll,PollAdmin)
##admin.site.register(Choice)

# Register your models here.
