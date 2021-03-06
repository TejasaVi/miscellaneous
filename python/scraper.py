#!/usr/bin/python
from bs4 import BeautifulSoup
import requests
import os
import git
import shutil

  

access_url =   "http://hck.re/crowdstrike"
file_url = "http://hck.re/tHEZGP"
file_to_copy = "index.js"

def get_file(url, name):
	try:
		r = requests.get(url)
		with open(name,'wb') as f:
			f.write(r.content)
		print("Writing file Done")
	except Exception as e:
		print (e)

def scrape_page(url_link):
    response = requests.get(url_link)
    soup = BeautifulSoup(response.text, "html.parser")
    listings = [];repo_details = {}
    data_rows = len(soup.find_all("tr")) - 1
    for row in range(0, data_rows) :
        col = 3*row
        repo_details['name'] = soup.find_all("td")[col ].get_text()
        repo_details['url'] = soup.find_all("td")[col +1 ].get_text()
        repo_details['branch'] = soup.find_all("td")[col + 2].get_text()
        listings.append(repo_details)
        repo_details = {}
    return listings

def clone_git_repo(list_item):
	try:
		repo = git.Repo.clone_from(str(list_item['url']), str(list_item['name']))
		repo.git.checkout("-b", str(list_item['branch']))
	except Exception as e:
		print (e)

def git_push_remote(origin='origin', branch=None):
    try:
        # push changes to remote repo
        origin = repo.remote(origin)
        if branch is not None:
            origin.push(branch, set_upstream=True)
        else:
            origin.push()
    except Exception as e:
        print (e)

if __name__ == "__main__":
	# Scrape page
	print("Starting Webpage scraping....")
	listings = scrape_page(access_url)
	print (listings)
	print("Webpage scraping: Complete !!")

	get_file(file_url, file_to_copy)
	print("Changed file download: Complete !!")


	#FOR EACH item in List DO
	for item in listings:
		# Clone Repo
		print("Cloning Remote Repository....")
		clone_git_repo(item)
		print("Remote Repository: Complete!!")

		# Move file to local Repo
		print("Copying changes to the local Repository....")
		shutil.copyfile(file_to_copy, os.path.join(item['name'], "src/", "index.js"))
		print("Copying changes to the local Repository: Complete !!")
		# Add file to local_repo
		repo = git.Repo(str(item['name']))
                file_path = [itm.a_path for itm in repo.index.diff(None)]
                repo.index.add(file_path)
		print("Adding changed files to local Repository: Complete !!")
		# commit files to local_repo
		commit_message = "Commit Message"
		repo.index.commit(commit_message)
		print("Commit changes to local Repository: Complete !!")
                #git_push_remote(branch=str(item['branch']))
		print("Pushing changed files to Remote Repository: Complete !!")
                commit_id = repo.head.commit
                print ("Commit ID: {0}", commit_id)
