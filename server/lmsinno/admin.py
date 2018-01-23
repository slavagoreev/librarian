from django.contrib import admin
from .models import User, Document, TagOfDocument, Tag, Author, Copy, DocumentOfAuthor, Bestseller, Order

admin.site.register(User)
admin.site.register(Document)
admin.site.register(TagOfDocument)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Copy)
admin.site.register(DocumentOfAuthor)
admin.site.register(Bestseller)
admin.site.register(Order)