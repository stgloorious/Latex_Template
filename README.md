# Latex_Template
## Latex Template for short and long Documents with Git Auto Commit on Build and ID Marking

* Modern title design
* Added subtitle
* Added custom fields (\version, \university, \departement etc.)
* Dots after section numbers
* Everything is stored in its own package for a clean .tex file
* Changes are automatically committed to git on build
* Every created document is unique and identifiable due to git SHA and timestamp
* All useful metadata contained in footer
* All unnecessary files are deleted automatically after build process [(Original housekeeper by Andrej Scheuer)](https://gitlab.com/Hoziax/latex/-/blob/c0d830c560070cc12519f67887c70b934c7d618d/latex_housekeeper.py)
* Smaller margins 


## Screenshot
![Screenshot](https://github.com/stgloorious/Latex_Template/blob/master/docs/screenshots.png)

## General Setup Information
Git-commit-on-build and the clean-up are achieved by having scripts executed when the build process is started. I use it with **Visual Studio Code** and the extension "Latex Workshop". Before following this guide, you should have VS Code with Latex Workshop up and running. If you plan to use it with a different environment, it probably requires heavy adjustments.

If you don't want to adjust any paths the following structure should work:

      project_directory
      |
      +--- .git
      |
      +--- src
      |    |
      |    +--- file.tex
      |    |
      |    +--- template_package.sty
      |    |
      |    +--- git_autosave.sh/.bat
      |    |
      |    +--- latex_cleanup.sh/.bat
      |    |
      |    +--- latex_housekeeper.py (Windows only)
      |
      +--- README.md
      |
      +--- ...

## Linux Setup

**To enable auto git commit, place the shell script with the .tex you're compiling and change your latex recipe so it executes the script before the build process.** 
(You need to run the recipe for the build process first, then run the auto commit (so you get your SHA) and then build again, so the SHA can be put in the pdf)

**The housekeeper consists of a simple shell script that also needs to be in the same directory as the .tex file**
(For Linux, I don't use the housekeeper.py, latex_cleanup.sh does the file deletion).

**Make sure you make both scripts executable! (e.g. with sudo chmod +x latex_cleanup.sh)**

For Latex Workshop in VS Code:
1. In settings.json (File -> Preferences -> Settings -> Find "edit in settings.json"), add "git_commit" and "latex_cleanup" to latex-workshop.latex.recipes

![recipe](https://github.com/stgloorious/Latex_Template/blob/master/docs/recipe_linux.png)

2. In the same file, add the "git_commit" and "latex_cleanup" tool to "latex-workshop.latex.tools", so it runs the scripts. 

![tool](https://github.com/stgloorious/Latex_Template/blob/master/docs/tools_linux.png)

**For some reason the paths works differently with Linux and Windows, so you'll need to uncomment the correct git integration in template_package.sty (end of file) !!!**

## Windows Setup

**To enable auto git commit, place .bat file with the .tex you're compiling and change your latex recipe so it executes the script before the build process.** 
(You need to run the recipe for the build process first, then run the auto commit (so you get your SHA) and then build again, so the SHA can be put in the pdf)

**The (python) housekeeper is also run via a .bat file that needs to be in the same directory as the .tex file**
(You could also have the Python file executed directly by Latex Workshop, would probably make more sense)

For Latex Workshop in VS Code:
1. In settings.json (File -> Preferences -> Settings -> Find "edit in settings.json"), add "git_commit" and "latex_cleanup" to latex-workshop.latex.recipes

![recipe](https://github.com/stgloorious/Latex_Template/blob/master/docs/recipe_windows.png)

2. In the same file, add the "git_commit" and "latex_cleanup" tool to "latex-workshop.latex.tools", so it runs the scripts. 

![tool](https://github.com/stgloorious/Latex_Template/blob/master/docs/tools_windows.png)

**For some reason the paths works differently with Linux and Windows, so you'll need to uncomment the correct git integration in template_package.sty (end of file) !!!**

### Acknowledgements
Thanks **barghest** for their answer [here,](https://tex.stackexchange.com/questions/261341/using-texstudio-and-git-to-automatically-commit-using-the-current-date)
thanks **CL.** for their answer [here.](https://tex.stackexchange.com/questions/455396/how-to-include-the-current-git-commit-id-and-branch-in-my-document)


