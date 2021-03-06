from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Movie
from .forms import CreateMovieForm


class MovieHomeView(ListView):

    """MovieHomeView Definition"""

    model = Movie
    paginate_by = 10
    paginate_orphans = 5
    ordering = "-created"
    template_name = "movies/movie_list.html"
    context_object_name = "movies"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "All Movies"
        return context


class MovieDetailView(DetailView):

    """Movie DetailView Definition"""

    model = Movie
    template_name = "movies/movie_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = f"[Movie] {context['object']}"
        return context


class MovieCreateView(CreateView):

    """Movie CreateView Definition"""

    form_class = CreateMovieForm
    template_name = "movies/movie_create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create Movie"
        return context


class MovieUpdateView(UpdateView):

    """Movie UpdateView Definition"""

    model = Movie
    template_name = "movies/movie_update.html"
    fields = (
        "title",
        "year",
        "category",
        "cover_image",
        "director",
        "cast",
    )
