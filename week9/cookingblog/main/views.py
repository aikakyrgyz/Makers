from django.db.models import Q
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .models import Category, Recipe, Image
from .forms import RecipeForm, ImageForm
from django.contrib import messages
from django.views.generic import ListView, DetailView, DeleteView
# Create your views here.

# def index(request):
#     recipes = Recipe.objects.all()
#     return render(request, 'index.html', {'recipes':recipes})

class MainPageView(ListView):
    model = Recipe
    template_name = 'index.html'
    context_object_name = 'recipes'

    def get_template_names(self):
        template_name = super(MainPageView, self).get_template_names()
        search = self.request.GET.get('q')
        if search:
            template_name = 'search.html'

        return template_name
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get('q')
        if search:
            context['recipes'] = Recipe.objects.filter(Q(title__icontains=search|Q(description__icontains=search)))
        else:
            context['recipes'] = Recipe.objects.all()
        return context




# def category_detail(request, slug):
#     category = Category.objects.get(slug = slug)
#     recipes = Recipe.objects.filter(category_id=slug)
#     return render(request, 'category-detail.html', locals())

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category-detail.html'
    context_object_name = 'category'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.slug = kwargs['slug']
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) #it is a dictionary
        context['recipes'] = Recipe.objects.filter(category_id=self.slug)

        # print(context)
        return context


# def recipe_detail(request, pk):
#
#     recipe = get_object_or_404(Recipe, pk = pk)
#     image = recipe.get_image
#     images = recipe.images.exclude(id = image.id )
#     return render(request, 'recipe_detail.html', locals())
class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'
    context_object_name = 'recipe'

    #since we not only need the recipe details but also images we need to pass another argument

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        image = self.get_object().get_image
        context['images'] = self.get_object().images.exclude(id=image.id) #images - related name
        return context




def add_recipe(request):
    ImageFormSet = modelformset_factory(Image, form=ImageForm, max_num=5)
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())

        if recipe_form.is_valid() and formset.is_valid():
            recipe = recipe_form.save()
            for form in formset.cleaned_data:
                image = form['image']
                Image.objects.create(image=image, recipe=recipe)
            return redirect(recipe.get_absolute_url())
    else:
        recipe_form = RecipeForm()
        formset = ImageFormSet(queryset=Image.objects.none())
    return render(request, 'add_recipe.html', locals())

def update_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    ImageFormSet = modelformset_factory(Image, form=ImageForm, max_num=5)
    recipe_form = RecipeForm(request.POST or None, instance=recipe)
    formset = ImageFormSet(request.POST or None, request.FILES or None, queryset=Image.objects.filter(recipe=recipe))
    if recipe_form.is_valid() and formset.is_valid():
        recipe = recipe_form.save()
        for form in formset:
            image = form.save(commit=False)
            image.recipe = recipe
            image.save()
        return redirect(recipe.get_absolute_url())
    return render(request, 'update_recipe.html', locals())

# def delete_recipe(request, pk):
#     recipe = get_object_or_404(Recipe, pk = pk)
#     if request.method == 'POST':
#         recipe.delete()
#         messages.add_message(request, messages.SUCCESS, 'Successfully deleted')
#         return redirect('home')
#     return render(request, 'delete_recipe.html')
class DeleteRecipeView(DeleteView):
    model = Recipe
    template_name = 'delete_recipe.html'
    context_object_name = 'recipe'
    success_url = reverse_lazy('home')
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.add_message(request, messages.SUCCESS, 'Successfully deleted')
        return HttpResponseRedirect(success_url)


