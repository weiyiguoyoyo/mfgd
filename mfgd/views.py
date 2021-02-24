from django.http import HttpResponse
from pathlib import Path
from pygit2 import *

BASE_DIR = Path(__file__).resolve().parent.parent

def format_author(commit):
    return "%s <%s>" %(commit.author.name, commit.author.email)

def print_tree(tree,indent=0):
    r = ""
    for obj in tree:
        r += "  " * indent + obj.name + "\n"
        if obj.type_str == "tree":
            r += print_tree(obj, indent+1)
    return r

def index(request):
    repo = Repository(BASE_DIR / ".git")
    branch = next(iter(repo.branches.local))
    branch_ref = repo.references["refs/heads/%s" %branch]

    r = ""
    for commit in repo.walk(branch_ref.target, GIT_SORT_TOPOLOGICAL):
        r += "%s\n%s\n%s\n" %(commit.tree_id, format_author(commit), commit.message)
        print_tree(commit.tree)

    return HttpResponse(r, content_type='text/plain')
