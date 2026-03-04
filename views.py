from django.shortcuts import render
from .forms import ResumeUploadForm 
from .utils import score_logic,clean_text

def resume_ranking_view(request):
    results = []

    if request.method == "POST":
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            job_file = request.FILES['job_description']
            resume_files = request.FILES.getlist('resumes')

            job_text = job_file.read().decode('utf-8')

            for resume in resume_files:
                resume_text = resume.read().decode('utf-8')
                score = score_logic(job_text, resume_text)

                results.append({
                    "name": resume.name,
                    "score": score
                })

            # Sort descending
            results = sorted(results, key=lambda x: x['score'], reverse=True)

    else:
        form = ResumeUploadForm()

    return render(request, "myapp/xyz.html", {
        "form": form,
        "results": results
    })



# def resume_ranking_view(request):
#     results = []

#     if request.method == "POST":
#         job_description = request.POST.get("job")

#         resumes = [
#             {"name": "resume1", "content": "Python developer with 3 years experience Worked extensively with Django and REST APIs.  using Docker"},
#             {"name": "resume2", "content": "Frontend developer skilled in React and JavaScript. Basic knowledge of Python. "},
#             {"name": "resume3", "content": "Frontend developer skilled in React and JavaScript. Basic knowledge of Python. "},
#         ]

#         for resume in resumes:
#             score = score_logic(job_description, resume["content"])
#             results.append({
#                 "name": resume["name"],
#                 "score": score
#             })

#         # Sort by highest score first
#         results = sorted(results, key=lambda x: x["score"], reverse=True)

#     return render(request, "myapp/xyz.html", {"results": results})






