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
  for rows in soup.find_all("tr"):
    for row in rows.find_all("td"): 
      repo_details["name"] = rows.find_all("td")[0].get_text()
      repo_details["url"] = rows.find_all("td")[1].get_text()
      repo_details["branch"] = rows.find_all("td")[2].get_text()
    listings.append(repo_details)
  return listings

def clone_git_repo():
	repo_clone_url = "https://bitbucket.org/zeeshan_07/cs2/src/master/"
	local_repo = "my_dir"
	test_branch = "crowdstrike2"
	repo = git.Repo.clone_from(repo_clone_url, local_repo)
	print("Done")
	os.system("ls ./my_dir")
	#shutil.rmtree("my_dir")

	
if __name__ == "__main__":
	# Scrape page
	print("Starting Webpage scraping....")
	scrape_page(access_url)
	listings = scrape_page(access_url)
	#print (listings)
	print("Webpage scraping: Complete !!")
	# Get File
	get_file(file_url, file_to_copy)
	print("Changed file download: Complete !!")
	# Clone Repo
	print("Cloning Remote Repository....")
	clone_git_repo()
	print("Remote Repository: Complete!!")
  
	# Move file to local Repo
	print("Copying changes to the local Repository....")
	shutil.copyfile(file_to_copy, "my_dir/src/".join("index.js"))
	print("Copying changes to the local Repository: Complete !!")
	
	# Add file to local_repo
	repo_dir = "my_dir"
	repo = Repo(repo_dir)
	repo.index.add(file_to_copy)
	print("Adding changed files to local Repository: Complete !!")
	# commit files to local_repo
	commit_message = "Commit Message"
	repo.index.commit(commit_message)
	origin = repo.remote("crowdstrike1")
	print("Commit changes to local Repository: Complete !!")
	# push changes to remote repo
	origin.push()
	print("Pushing changed files to Remote Repository: Complete !!")