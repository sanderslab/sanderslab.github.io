# SmithLab Website

## About
Our website is based on the open source templates designed and shared by the labs of [D. Allan Drummond](http://www.allanlab.org/aboutwebsite.html), [Trevor Bedford](http://bedford.io/misc/about/) and [Stephan Sanders](https://sanderslab.github.io). We downloaded source codes from their repository and modified our contents based on shared templates. We greatly thank them for allowing reuse of their codebase. 

The website is deployed using [GitHub Pages](https://SmithLabGWSPH.github.io) and the source code is available on [GitHub](https://github.com/SmithLabGWSPH/SmithLabGWSPH.github.io). Please feel free to reuse this code (making sure to cite the Bedford lab, Drummond lab and Sanders Lab as the original sources of the lab website template).

## Maintenance

The workflow is to update and build the website locally, then push the changes to the Github repository.


### 1. Install jekyll locally

The website is built by jekyll, so we need to install jekyll locally.

First [install ruby](https://stackoverflow.com/questions/51126403/you-dont-have-write-permissions-for-the-library-ruby-gems-2-3-0-directory-ma) through terminal/command. Install customizd ruby in addition to the default ruby.

```
brew install chruby ruby-install

ruby-install ruby

echo 'source /usr/local/opt/chruby/share/chruby/auto.sh' >>~/.bash_profile
```

[Switch from](https://stackoverflow.com/questions/37058625/chruby-not-changing-to-the-proper-version-of-ruby-according-to-the-value-in-rub) default ruby to the customized ruby.

```
source /usr/local/opt/chruby/share/chruby/chruby.sh 

chruby ruby-3.1.2 

source /usr/local/opt/chruby/share/chruby/auto.sh
```

Install jekyll.

```
gem install bundler jekyll
```

### 2. Clone the site repo to local machine

```
# move to the local directory
cd <path to the local directory>  

# clone the remote repo to the local directory
gh repo clone <repo name>

# move to the cloned repo
cd <repo name> 
```

### 3. Build the website locally

```
# move to the local repo directory

# start website locally
bundle exec jekyll serve --livereload

# add if error "Load error: cannot load such file – webrick"
bundle add webrick

# open website in local browser
# Server address: http://127.0.0.1:4000/

# make changes (see details in the following section Make changes)

# build website after finishing updates
jekyll build
```
     
### 4. Push the changes to the Github

```
# check the file status: tracked/untracked
git status 

# stage the files ready to be committed
git add . 

# commit the changes locally with message
git commit -m “<description of the change>”  

# push the changes to the remote repo
git push
```

## Make changes

### 1. Add new members

- Add a square sized photo to `images/teampic/<firstnamelastname>.png`. (can [crop the photo online](https://www.iloveimg.com/crop-image))
- Add markdown file to `team/<firstnamelastname>.md`, change the content accordinly.
- Add a new item in `_data/team_members.yml`, change the content accordingly.

### 2. Add new publications

- Add a journal photo in `images/pubpic/<journalyear>.png`
- Add a new item in `_data/publist.yml`, change the content accordingly.

### 3. Add media news

- Add a new item in `_data/news.yml`, change the content accordingly.

### 4. Add code

- Add a new item in `_pages/code.md`, change the content accordingly.

### 5. Change home page

- Make change in `_pages/home.md`.






