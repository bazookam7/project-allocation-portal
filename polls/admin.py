from django.contrib import admin

from .models import Question
from .models import Choice
from .models import Students
from .models import Instructors
from .models import AllProjects

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Students)
admin.site.register(Instructors)
admin.site.register(AllProjects)