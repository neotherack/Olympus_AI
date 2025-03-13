from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from ai.models import LLM, Tool, LLMConfig

class LLMAdmin(ImportExportModelAdmin):
  readonly_fields = ('created_at','updated_at')
  list_display = ('model_name','model_quantization','version_tag')
  search_fields = ('model_name','model_quantization','version_tag')
  ordering = ('model_name','model_quantization','version_tag')
  list_filter = ('model_name','model_quantization','version_tag')
  fields=('model_name',('model_quantization','version_tag'),('created_at','updated_at'))

try:
  admin.site.register(LLM, LLMAdmin)
except:
  pass

class ToolAdmin(ImportExportModelAdmin):
  readonly_fields = ('created_at','updated_at')
  list_display = ('name','version','category')
  search_fields = ('name','version','category')
  ordering = ('name','version','category')
  list_filter = ('name','version','category')
  fields=('name',('category','version'),'source_code',('created_at','updated_at'))

try:
  admin.site.register(Tool, ToolAdmin)
except:
  pass

class LLMConfigAdmin(ImportExportModelAdmin):
  readonly_fields = ('created_at','updated_at')
  list_display = ('internal_name','temperature','enabled')
  search_fields = ('internal_name','temperature','enabled')
  ordering = ('internal_name','temperature','enabled')
  list_filter = ('internal_name','temperature','enabled')
  fields=(('llm','internal_name'),'tools',('temperature','enabled'),('created_at','updated_at'))

try:
  admin.site.register(LLMConfig, LLMConfigAdmin)
except:
  pass
