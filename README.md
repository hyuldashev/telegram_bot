# telegram_bot
bot
TUTORIAL FOR GETTING BOT TOKEN, DOWNLOADING AIOGRAM LIBRARY AND DOWNLOADING CODE FROM GITHUB
How to get a token:
       To do this, we must write to the botfather 
       /newbot in a telegram, then write a name, 
       write a username after that, the botfather gives us a token, 
       for adding our bot to the group we must change the parameters, write /setprivacy
       by default it is enable, make it disable so that our bot can be  group admin
How to install the aiogram library:
        open Windows PowerShell and write the pip install aiogram command there and press 
        enter the library should be installed, after completion we close the window
How to download the code:
        from github: open github,select the project which you want to download, 
        in the upper corner there is a button  clone or download, 
        click on it and write the name of the folder where you want to save
How to run the bot: 
        you need to create a new .bat file and in this file you need to write
        
        call %~dp0'the name of folder'\venv\Scripts\activate

        cd  %~dp0'the name of folder'

        set TOKEN='your token'

        python bot_telegram.py    ''bot_telegram.py' has in code'

        pause
        
