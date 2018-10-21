from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from blog.models import blog

# Create your views here.

class PostsForm(ModelForm):
    class Meta:
        model=blog
        fields=['title','description','date','status','created_date','modified_date']
		
		
def post_list(request, template_name='blog/post_list.html'):
    posts=blog.objects.all()
    data={}
    data['object_list']=posts
    return render(request, template_name, data)
	
def post_create(request, template_name='blog/post_form.html'):
    form=PostsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('blogs/post_list')
    return render(request, template_name, {'form':form})
	
def post_delete(request, pk, template_name='blog/post_delete.html'):
    post=get_object_or_404(blog, pk=pk)
    if request.method=='POST':
        post.delete()
        return redirect('blog:post_list')
    return render(request, template_name, {'object':post})
	
def post_update(request, pk, template_name='blog/post_form.html'):
    post = get_object_or_404(blog, pk=pk)
    form = PostsForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('blog:post_list')
    return render(request, template_name, {'form': form})