from django.db import models
from ai.selections import QUANTIZATION_TYPES, TOOL_CATEGORIES

from django.utils.timezone import now
from django.db import models
from django.contrib import admin
from django.utils.html import format_html,escape


class LLM(models.Model):
    model_name = models.CharField(max_length=200, blank=True)
    model_quantization = models.CharField(max_length=10, choices=QUANTIZATION_TYPES, default="Q4_K_M")
    version_tag = models.CharField(max_length=200, default="latest")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.model_name}:{self.version_tag}-{self.model_quantization}"

class Tool(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, choices=TOOL_CATEGORIES)
    version = models.CharField(max_length=200, default="latest")
    source_code = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}:{self.version}"

class LLMConfig(models.Model):
    internal_name = models.CharField(max_length=200, blank=True)
    enabled = models.BooleanField(default=True)
    llm = models.ForeignKey(LLM, on_delete=models.DO_NOTHING)
    temperature = models.FloatField(default=0.0)
    system_prompt = models.TextField(blank=True)
    tools = models.ManyToManyField(Tool)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.internal_name}@{self.llm.model_name}"
    

    
