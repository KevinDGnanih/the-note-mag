""" View Django File """
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Post, Category
from .forms import CommentForm


class PostList(generic.ListView):
    """ Structure the rendering of the post list """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class CategoryPosts(generic.ListView):
    paginate_by = 6
    def get(self, request, cats):
        category_posts = Post.objects.filter(category=cats)
        return render(
            request,
            'category_posts.html',
            {
                'cats': cats,
                'category_posts': category_posts,   
            }
        )


#def CategoryPosts(request, cats):
#    category_posts = Post.objects.filter(category=cats)
#    return render(request, 'category_posts.html', {'cats': cats.title(), 'category_posts':category_posts})


class PostDetail(View):
    """ Structure the rendering of the post detail """
    def get(self, request, slug, *args, **kwargs):
        """ Get the information a post """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """ Get the information a post """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': True,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )


class PostLike(View):
    
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class AddPost(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = ('title', 'slug', 'category', 'content', 'featured_image',
              'status')


class EditPost(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ('title', 'slug', 'category', 'content', 'featured_image',
              'status')


class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
