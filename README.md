# Latex_Template
## Latex Template for short and long Documents with Git Auto Commit on Build and ID Marking

* Modern title design
* Added subtitle
* Added custom fields (\version, \departement)
* Dots after section numbers
* Everything is stored in its own package for a clean .tex file
* Changes are automatically committed to git on build
* Every created document is unique and identifiable because of git SHA and a timestamp
* All useful metadata contained in footer
* All unnecessary files are deleted automatically after build process [(Original housekeeper by Andrej Scheuer)](https://gitlab.com/Hoziax/latex/-/blob/c0d830c560070cc12519f67887c70b934c7d618d/latex_housekeeper.py)
* Smaller margins 

**To enable auto git commit, place .bat file with the .tex you're compiling and change your latex recipe so it executes this bat file before the build process.** 
(You need to run the recipe for the build process first, then run the auto commit (so you get your SHA) and then build again, so the SHA can be put in the pdf)

**For consistency, the housekeeper is also run via a .bat file that needs to be in the same directory as the .tex file**
(You could also have the Python file executed directly by Latex Workshop)

For Latex Workshop in VS Code:
1. In settings.json, add "git_commit" and "latex_cleanup" to latex-workshop.latex.recipes

![recipe](https://github.com/stgloorious/Latex_Template/blob/master/docs/recipe.png)

2. In the same file, add the "git_commit" and "latex_cleanup" tool to "latex-workshop.latex.tools", so it runs the batch files. 

![tool](https://github.com/stgloorious/Latex_Template/blob/master/docs/tools.png)

### Acknowledgements
Thanks **barghest** for their answer [here,](https://tex.stackexchange.com/questions/261341/using-texstudio-and-git-to-automatically-commit-using-the-current-date)
thanks **CL.** for their answer [here.](https://tex.stackexchange.com/questions/455396/how-to-include-the-current-git-commit-id-and-branch-in-my-document)

### Screenshot
![Screenshot](https://github.com/stgloorious/Latex_Template/blob/master/docs/screenshots.png)

