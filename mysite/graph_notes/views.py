from django.shortcuts import render, get_object_or_404

from django.utils import timezone

from .models import Note


def index(request):
    latest_note_list = Note.objects.order_by("-published_time")[:5]

    context = {
        "latest_note_list": latest_note_list,
    }

    return render(request, "graph_notes/index.html", context)


def detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)

    return render(request, "graph_notes/detail.html", {"note": note})


def create(request):
    return render(request, "graph_notes/create.html")


def save(request):
    note_title = request.POST["title"]
    note_content = request.POST["content"]
    published_time = timezone.now()

    print(f"note_title: {note_title}")
    print(f"note_content: {note_content}")

    # create new note
    new_note = Note(
        title=note_title,
        content=note_content,
        published_time=published_time,
        modified_time=published_time,
    )

    new_note.save()

    # send user back to index
    return index(request)
