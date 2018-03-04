from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.response import Response
from rest_framework import schemas
from rest_framework.decorators import api_view, renderer_classes

@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='REST API')
    return Response(generator.get_schema())