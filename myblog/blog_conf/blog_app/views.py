from django.shortcuts import render, redirect
from .models import Post, Test
from .forms import PostForm
from .forms import TestForm
# from .forms import PostForm, UploadForm

from transformers import pipeline 
from transformers import AutoModelForSequenceClassification 
from transformers import BertJapaneseTokenizer 

# パイプラインの準備
model = AutoModelForSequenceClassification.from_pretrained('daigo/bert-base-japanese-sentiment') 
tokenizer = BertJapaneseTokenizer.from_pretrained('cl-tohoku/bert-base-japanese-whole-word-masking') 
nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer) 


def frontpage(request):
    posts = Post.objects.all()
    # if (request.method == 'POST'):
    #     form = UploadForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         upload_image = form.save()
    #         upload_image.save()
    # return render(request, "frontpage.html", {"posts": posts, 'upload_form': UploadForm()})
    return render(request, "frontpage.html", {"posts": posts})

def post_create(request):
    next_cnt = "post" + str(Post.objects.count() + 1)
    print("post_create:" + request.method)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            # new_post = form.save(commit=False)
            # new_post.save()
            title = form.cleaned_data['title']
            slug = form.cleaned_data['slug']
            intro = form.cleaned_data['intro']
            body = form.cleaned_data['body']
            img = form.cleaned_data["img"]
            form = Post.objects.create(title=title, slug=slug, intro=intro, body=body, img=img)
            return redirect("frontpage")
    else:
        form = PostForm()
        
    return render(request, "post_create.html", {"next_cnt": next_cnt, "form": form})
    # return render(request, "post_create.html", {"next_cnt": next_cnt})

def post_test(request):
    tests = Test.objects.all()
    if Test.objects.count()==0:
        test = "nothing"
        nlp_test = "わかりません"
    else:
        test = tests.latest("data_added")
        nlp_test = nlp(str(test.test_title))
    if request.method == "POST":
        form = TestForm(request.POST)
        if form.is_valid():
            test_title = form.cleaned_data['test_title']
            form = Test.objects.create(test_title=test_title)
            test = tests.latest("data_added")
            nlp_test = nlp(str(test.test_title))
            return redirect("post_test")
    else:
        form = TestForm()
        
    return render(request, "post_test.html", {"form": form, "nlp_test": nlp_test})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "post_detail.html", {"post": post})
