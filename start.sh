echo "Cloning Repo...."
git clone https://github.com/HelloUltra44/UPLOADER-BOT-V3 /UPLOADER-BOT-V3
cd /UPLOADER-BOT-V3
pip3 install -U -r requirements.txt
echo "Starting Bot.... Please Wait. Check You Log. Bot Edit by @LISA_FAN_KL"
gunicorn app:app & python3 bot.py
