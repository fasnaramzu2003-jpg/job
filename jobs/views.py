from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Job
from .serializers import JobSerializer


# 🔹 LIST + CREATE + SEARCH
@api_view(['GET', 'POST'])
def job_list(request):

    # ✅ GET (LIST + SEARCH)
    if request.method == 'GET':
        q = request.GET.get('q', '')   # search query

        jobs = Job.objects.all()

        # 🔍 SEARCH FEATURE
        if q:
            jobs = jobs.filter(
                Q(title__icontains=q) |
                Q(company__icontains=q) |
                Q(location__icontains=q)
            )

        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

    # ✅ POST (CREATE)
    elif request.method == 'POST':
        serializer = JobSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)


# 🔹 DETAIL + UPDATE + DELETE
@api_view(['GET', 'PUT', 'DELETE'])
def job_detail(request, pk):

    job = get_object_or_404(Job, pk=pk)

    # ✅ GET (SINGLE JOB)
    if request.method == 'GET':
        serializer = JobSerializer(job)
        return Response(serializer.data)

    # ✅ PUT (UPDATE)
    elif request.method == 'PUT':
        serializer = JobSerializer(job, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    # ✅ DELETE
    elif request.method == 'DELETE':
        job.delete()
        return Response(status=204)