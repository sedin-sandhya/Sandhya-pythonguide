from django.shortcuts import get_object_or_404, redirect

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ShortURL
from .serializers import ShortURLSerializer
from .utils import generate_short_code


# Create your views here.
class ShortenURLView(APIView):

    def post(self, request):
        serializer = ShortURLSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(short_code=generate_short_code())

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShortURLDetailView(APIView):

    def get(self, request, short_code):

        short_url = get_object_or_404(ShortURL, short_code=short_code)

        short_url.access_count += 1
        short_url.save()

        serializer = ShortURLSerializer(short_url)

        return Response(serializer.data)

    def put(self, request, short_code):

        short_url = get_object_or_404(ShortURL, short_code=short_code)

        serializer = ShortURLSerializer(short_url, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, short_code):

        short_url = get_object_or_404(ShortURL, short_code=short_code)

        short_url.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ShortURLStatsView(APIView):

    def get(self, request, short_code):

        short_url = get_object_or_404(ShortURL, short_code=short_code)

        serializer = ShortURLSerializer(short_url)

        return Response(serializer.data)


class RedirectURLView(APIView):

    def get(self, request, short_code):

        short_url = get_object_or_404(ShortURL, short_code=short_code)

        short_url.access_count += 1
        short_url.save()

        return redirect(short_url.url)
