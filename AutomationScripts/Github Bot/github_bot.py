from github import Github
#user login
g=Github("username","password")


#showing all the repositories of python
repos= g.search_repositories(query="language:python")
for i  in repos:
   print(i)

#for getting all the repos of user
for repo in g.get_user().get_repos():
    print(repo.name)

#shows the no. of star of the repo
repo=g.get_repo("repository name")
repo.stargazers_count

#getting all the contents of particular repo
content=repo.get_contents("")
for content_fil in content:
    print(content_fil)

#making a repo test and creating test file
user= g.get_user()
repo=user.create_repo('test')
repo.create_file("test.txt","commit","hello coders")

#deleting file from the repo
repo=g.get_repo("")#enter repository name inside the bracket
cont=repo.get_contents("test.txt")
repo.delete_file(cont.path,"remove test",cont.sha,branch='master')