import os
import dotenv as dv

dv.load_dotenv()
mysecret = os.getenv("MYSECRET")
