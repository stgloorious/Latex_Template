# Latex_Template
### Latex template for small documents with git auto commit on build and id marking

* Modern title design
* Added subtitle
* Added custom fields (\version, \departement)
* Everything is stored in its own package for a clean .tex file
* Changes are automatically committed to git on build
* Every created document is unique and identifiable because of git SHA and a timestamp
* All useful metadata contained in footer
* Smaller margins 

**To enable auto git commit, place .bat file with the .tex you're compiling and change your latex recipe so it executes this bat file before the build process.** 
(You need to run the recipe for the build process first, then run the auto commit (so you get your SHA) and then build again, so the SHA can be put in the pdf)

For Latex Workshop in VS Code:
1. In settings.json, add "git_commit" to latex-workshop.latex.recipes

![recipe](https://github.com/stgloorious/Latex_Template/blob/master/docs/recipe.png)

2. In the same file, add the "git_commit" tool to "latex-workshop.latex.tools",so it runs the batch file. 

![tool](https://github.com/stgloorious/Latex_Template/blob/master/docs/tools.png)

Thanks barghest for his answer [here.](https://tex.stackexchange.com/questions/261341/using-texstudio-and-git-to-automatically-commit-using-the-current-date)

![Screenshot](https://github.com/stgloorious/Latex_Template/blob/master/docs/screenshot.png)

