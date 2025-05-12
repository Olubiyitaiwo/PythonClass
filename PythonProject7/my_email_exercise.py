import os
import yagmail
from dotenv import load_dotenv

load_dotenv()

yg = yagmail.SMTP(
   user= os.getenv("email"),
   password= os.getenv("password")
)

content = """Dynamites is the best cohort
             not only in semicolon
             but in the whole of     
             Nigeria
            """
recipients = ["uzochukwuisrael4@gmail.com", "israeljohnson0464@gmail.com", "olubiyipeter@gmail.com","onyinyeekezie2017@gmail.com"]
subject = "Dynamites is the best cohort"
image = "bird.png"

yg.send(to=recipients, contents=content, attachments=image)
