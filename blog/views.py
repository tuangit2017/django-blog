#from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
#from django.http import Http404
from django.http import HttpResponse
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from .forms import CommentForm


def blog_index(request):
    post_list = Post.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(post_list, 2)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'page': page,
        'posts': posts,
        'page_title':'Home',
    }
    return render(request,"post/home.html",context)


def post_detail(request, post_id):
    #print(post_id)
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("the Post does not exist")


    return render(request, 'post/details.html', {'post': post})


#def detail(request, question_id):
#    return HttpResponse("You're voting on question %s." % question_id)
'''
def sec_post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    #comments = get_object_or_404(Comment, pk=post_id)
    context = {
        'post': post,
        #'comments':comments,
    }
    return render(request, 'post/sec_details.html', context)
'''

def blog_post_detail_view(request, slug):
	# 1 object -> detail view
	obj = get_object_or_404(Post, slug=slug)

	template_name = 'post/third_detail.html'
	# List of active comments for this post
	comments = obj.comments.filter(approved_comment=True)
	#new_comment = None

	if request.method == 'POST':
		#post_slug = request.POST['slug']
		#print(post_slug)
		author = request.POST['author']
		comment_text = request.POST['comment_text']
		comment = Comment.objects.create(
			#post = post_slug,
			#post= obj.title,
			author = author,
			comment_text = comment_text

		)
		#return redirect(template_name, slug=post.slug)


		'''
		# A comment was posted
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			# Create Comment object but don't save to database yet
			new_comment = comment_form.save(commit=False)
			# Assign the current post to the comment
			new_comment.obj = obj
			print(new_comment)
			#new_comment.obj[slug] = slug
			# Save the comment to the database
			new_comment.save()
	else:
		comment_form = CommentForm()
		'''

	context = {
		'post': obj,
		'comments': comments,
		#'new_comment': new_comment,
		#'comment_form': comment_form,

		}
	return render(request, template_name, context)
