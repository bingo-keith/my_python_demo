from django.contrib import admin

from learning_logs.models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)

# python manage.py migrate 应用迁移，修改数据库
