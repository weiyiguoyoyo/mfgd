#!/usr/bin/python3
import pygit2

def format_author(commit):
	return "%s <%s>" %(commit.author.name, commit.author.email)

def print_tree(tree,indent=0):
	for obj in tree:
		print("  " * indent + obj.name)
		if obj.type_str == "tree":
			print_tree(obj, indent+1)


repo = pygit2.Repository("/home/km/dev/libkm/.git")

# list branches
# for branch in repo.branches.local:
# 	print(branch)

branch = "master"

# list commits
#branch_ref = repo.references["refs/heads/%s" %branch]
#for commit in repo.walk(branch_ref.target, pygit2.GIT_SORT_TOPOLOGICAL):
#	print("%s\n%s\n%s" %(commit.tree_id, format_author(commit), commit.message))
#	print_tree(commit.tree)
#	print()

# diff two commits
diff = repo.diff("HEAD", "HEAD^")
for delta in diff.deltas:
	print(delta.old_file, delta.new_file)
