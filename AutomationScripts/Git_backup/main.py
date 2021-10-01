import urllib.parse as urlparse
import os
import requests
import shutil
import stat
import random
from string import ascii_lowercase 

class GitBackup:
    def __init__(self,username, GithubTOKEN = None, isOrgnization = False,savingPath = None):
        personality = "orgs" if isOrgnization else "users"
        self.API_url = f"https://api.github.com/{personality}/{username}/repos"
        self.url_parts = list(urlparse.urlparse(self.API_url))
        self.query = dict(urlparse.parse_qsl(self.url_parts[4]))
        if GithubTOKEN:
            self.query.update({"access_token" : GithubTOKEN})
            self.url_parts[4] = urlparse.urlencode(self.query)

        self.API_url = urlparse.urlunparse(self.url_parts)
        if savingPath :
            self.backUpFolder = os.path.join(savingPath,'Repos')
        else:
            self.backUpFolder = os.path.join(os.getcwd(),'Repos')
        if os.path.exists(self.backUpFolder):
            self.backUpFolder += "_"+"".join(random.choice(ascii_lowercase) for _ in range(4))
        self.repoCloneLink = {}
        print(f"Data will save in --> {self.backUpFolder}")
    
    def getCloneLinks(self):
        res = requests.get(url= self.API_url)
        if res.status_code == 200:
            # if request is successfull
            self.repoCloneLink = {node['name'] : node['clone_url'] for node in res.json()}
        else :
            print("Error in API request")
        return self.repoCloneLink
    
    def clone_repo(self,name,clone_link):
        # if not in repo folder then go in that
        if os.getcwd() != self.backUpFolder:
            # create dir
            os.makedirs(self.backUpFolder, exist_ok=True)
            # move in
            os.chdir(self.backUpFolder)

            if os.path.exists(os.path.join(self.backUpFolder,name)):
                shutil.rmtree(os.path.join(self.backUpFolder,name),
                            onerror = self.delError)

        os.system(f'git clone {clone_link}')

    def delError(self,func,path,exc_info):
        # print(func) # print(path) # print( exc_info)
        os.chmod(path, stat.S_IWUSR)
        os.remove(path)

    @classmethod
    def runner(cls,username, GithubTOKEN = None, isOrgnization = False,savingPath = None):
        cl = cls(username=username, GithubTOKEN = GithubTOKEN, isOrgnization = isOrgnization,savingPath=savingPath)
        for index,(key,value) in enumerate(cl.getCloneLinks().items()):
            print(index+1,key)
            cl.clone_repo(key,value) 
            print()

if __name__ == "__main__":
    username = "rishabhjainfinal" 
    GithubTOKEN = None
    isOrgnization = False
    savingPath = None
    GitBackup.runner(username,GithubTOKEN,isOrgnization,savingPath)