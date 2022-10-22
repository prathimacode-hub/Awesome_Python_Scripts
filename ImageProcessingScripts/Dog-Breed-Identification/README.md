# ML-Based-Dog-Breed-Identifier

## Aim
To identify the breed of Dog

## Purpose
This is a Django Based Web Site To Identify the Breed of which your DOG belogs All You Need To Do is to Follow These Steps

## Workflow of the Project
From the Home user can find the tab to upload the Image and on result can be viewed on the result page.

## you need to install following libraries to run this python program in cmd
```

pip install tensorflow
pip install keras
pip install django
pip install numpy

```
## Compilation Steps

#### Step 1: Forking the repository :

To work on this project, you will first need to make your copy of the repository. To do this, you should fork the repository and then clone it so that you have a local working copy.

Get your own Fork/Copy of repository by clicking `Fork` button right upper corner.<br><br>

#### Step 2: Clone the Forked Repository

After the repository is forked, you can now clone it so that you have a local working copy of the codebase.

To make your local copy of the repository follow the steps:
- Open the Command Prompt
- Type this command:
  
```bash
$ git clone https://github.com/<your-github-username>/ML-Based-Dog-Breed-Identifier
```


#### Step 3: Creating a new branch (IMP)
This is one of the very important step that you should follow to contribute. A branch helps to manage the workflow, isolate your code and does not creates a mess. To create a new branch:
  
```bash
$ git branch <name_of_branch>
$ git checkout -b <name_of_branch>
```

Keep your cloned repo upto date by pulling from upstream (this will also avoid any merge conflicts while committing new changes)
```bash
git pull origin main
```

#### Step 4: Setting up Project

##### For Django:
**1. Create a Virtual Environment**

- *On macOS and Linux:*
  ```bash
    python3 -m venv env
  ```
- *Windows*
  ```bash
    py -m venv env
  ````

**2. Activate the Virtual Environment**
  - *On Windows*
    ```bash
    .\env\Scripts\activate
    ```
  - *On macOS and Linux:*
    ```bash
    source env/bin/activate
    ```

**4. Make Migrations**

```bash
  python manage.py makemigrations
  python manage.py migrate
```
**5. Run Server**

```bash
  python manage.py runserver
```


**5.** Go to ` http://127.0.0.1:8000/` and enjoy the application



## Outputs

### Home Page 
<img src="https://github.com/Knighthawk-Leo/ML-Based-Dog-Breed-Identifier/blob/main/Images/home.png">

### Result Page 
<img src="https://github.com/Knighthawk-Leo/ML-Based-Dog-Breed-Identifier/blob/main/Images/Result.png">

## Author(s)

<a href='https://github.com/Knighthawk-Leo'>Sanskar Dwivedi</a>

##
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/built-by-developers.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/built-with-swag.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

