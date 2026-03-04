from django import forms

# class ResumeUploadForm(forms.Form):
#     job_description = forms.FileField(label="Upload Job Description (.txt)")
#     resumes = forms.FileField(
#         label="Upload Resume Files (.txt)",
#         widget=forms.ClearableFileInput(attrs={'multiple': True})
#     )



#     from django import forms


# ✅ Custom widget for multiple files
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


# ✅ Custom file field
class MultipleFileField(forms.FileField):
    widget = MultipleFileInput

    def clean(self, data, initial=None):
        if isinstance(data, (list, tuple)):
            return [super().clean(d, initial) for d in data]
        return super().clean(data, initial)


class ResumeUploadForm(forms.Form):
    job_description = forms.FileField(label="Upload Job Description (.txt)")
    resumes = MultipleFileField(label="Upload Resume Files (.txt)")