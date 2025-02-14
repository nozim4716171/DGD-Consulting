from modeltranslation.translator import register, TranslationOptions
from .models import Category, News, Projects, Employees

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'category', 'slug','created_at')


@register(Projects)
class ProjectsTranslationOptions(TranslationOptions):
    fields = ('title', 'events')


@register(Employees)
class EmployeesTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'position')

    