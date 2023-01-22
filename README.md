## Convert .mp4 to .gif .
For convert mp4 to .gif, MoviePy module  must be installed first.
- Download the latest [Python installer](https://www.python.org/downloads/) for your OS.
I used [this website](https://www.alphr.com/pip-is-not-recognized-as-an-internal-or-external-command/#:~:text=Reinstall%20Python%20to%20Fix%20'Pip,components%20to%20fix%20the%20problem.) for help, you can have a look if you want.
-  Users who want to use pip for installing the MoviePy module on Windows in the command prompt have to use the command:
```
pip install moviePy
```
- To verify that was successfully installed on the system with the pip, run a command in the command window.
```
pip show moviePy
```
We write the video name to be converted in ' VideoFileClip("videoName.mp4") ' with its extension.
After the convert, we write the name and extension in ' video.write_gif("lastGifName.gif") '.

<img src="https://github.com/AtakanTurgut/python-mp4gif/blob/main/gifGame.gif" alt="carGame" width="300" height="150"/>

---
## Git Large File Storage (LFS)

To push large files to github, we must first install the open source git plugin [Git LFS](https://git-lfs.com/).
After the installation is finished, we go to the repository directory and start large file tracking for the relevant repo with the help of the following command.
```
git lfs install
```
Then, we give the following command to specify which types of files to consider as "large file". In this example, I wanted it to follow the files with the `.gif` extension.
```
git lfs track "*.gif"
```
After this process, we add the `.gitattributes` file created to the repository.
```
git add .gitattributes
```
Now you can continue your normal flow by adding your files to the repo.