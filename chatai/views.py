# analysis_app/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from chatai.analysis import perform_analysis

@login_required(login_url="my-login")
def chatai(request):
    if request.method == 'POST':
        form = request.POST
        if 'file' in request.FILES:
            uploaded_file = request.FILES['file']
            fs = FileSystemStorage()
            file_path = fs.save(uploaded_file.name, uploaded_file)

            # Perform analysis
            result = perform_analysis(file_path)

            # Pass the result to the template
            return render(request, 'chatai.html', {'result': result, 'file_path': file_path})

    else:
        form = None

    return render(request, 'chatai.html', {'form': form})


def download(request, filename):
    file_path = f'{settings.MEDIA_ROOT}/{filename}'
    return redirect(file_path)


def chat(request):
    # Implement chat functionality if needed
    return JsonResponse({'response': 'Chat functionality not implemented yet.'})
