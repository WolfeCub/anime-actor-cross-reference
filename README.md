# anime-actor-cross-reference
This program has you specify your [MyAnimeList](myanimelist.net) username. It then combs through your list of anime and shows for each voice actor (from anime on your list) which characters they played in which anime (that you've seen)

## Note
There are two files AnimeActrorCrossReference and AnimeActrorCrossReference3. They work with python versions 2.7 and 3.5 respectivly. The instructions below are for python 2.7. The 2.7 version is slower less complete (it only checks the 4 main actors whereas the new version will check all the actors), slower (the new version is fasted than the old one and it checks all of the actors instead of just 4) but easier to intall as it has no external dependancies. I'll write up how to use the new version shortly but if you know what your doing (or feel like figuring it out) the dependancies required are `beautifulsoup4`, `lxml` and requests.

### Short Guide for New Version
1. Download the ZIP and extract
2. Download and install python 3.5.x
3. Run the commands (sudo if required or cmd as administrator on windows)
    * `[sudo] pip3 install lxml`
    * `[sudo] pip3 install beautifulsoup4`
    * `[sudo] pip3 install requests`
4. Run the program using `python3 AnimeActrorCrossReference3`

## How to use (Old but detailed)
1. Press the Download ZIP button on the top right of the file list
2. Unzip the folder
3. Make sure you have Python 2.7 installed.
  * If you're on a mac or linux this will be installed by default
  * If you're on windows download it from [here](https://www.python.org/download/releases/2.7.2/). If you're on a 32 bit system download the `Windows x86 MSI Installer (2.7.2)` and if you're on a 64 bit system download `Windows X86-64 MSI Installer (2.7.2)` if you don't know it doesn't really matter just download the 32 bit one (`Windows X86-64 MSI Installer (2.7.2)`).
4. Then run the program from cmd or terminal
  * If you're on windows navigate in explorer to the file location then Shift-right click on the backgroun and click open command prompt here then type `python AnimeActrorCrossReference.py`
  * On mac navigate to it by opening the terminal app (found in applications then utilities) type `cd ` followed by the path to the files location then type `python AnimeActrorCrossReference.py`
