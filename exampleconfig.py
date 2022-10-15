from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 1748969
    API_HASH = "5fd47ee5f8153add4b3519a1bc04e36e"
    # the name to display in your alive message
    ALIVE_NAME = "TERMINATOR"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "mongodb+srv://royalboi:priyanshu1@cluster0.iywcx.mongodb.net/?retryWrites=true&w=majority"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOHwBu3bM4Ag-scvMEktsZ_F5FLAyXK3FRDCZ2fKulTUQ8TKSXk6mvgCog2pY8J4qpiMWuPqIOLEibiAUd76DHUkM4eQsRuFdfRW5dst9LN0RosWseKAcaNEDlhdwMRu_Stby3IAqbX8fn0JoMsHTfPyMPhIlCrGGPJb-WJmgR2qYNwaXlm6QMwLBBemLCMcaGG_TjA3AS16jVECfi7SekhwpNdeHDVXdB_afi48fyLPyklc6-4wFy8wbq3y-mzdwvMDW0M0m3iTNf5R7fnmC8RBXlcyvRvhdaZwm8T7SWvPmKfqHUHmbAQPIn8GBMtcLzJMJN635vxQQhqxoXcUToaSmvtE="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "5565589711:AAEdnihPOPdGj8fOO0KucuMQ3PMTrnTYNOU"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001458925419
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
