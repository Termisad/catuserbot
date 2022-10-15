from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 1748969
    API_HASH = "5fd47ee5f8153add4b3519a1bc04e36e"
    # the name to display in your alive message
    ALIVE_NAME = "TERMINATOR"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://msyorlvw:FYWV4jz8F1vGVWjXFpSEz62LN1z1CNSU@kesavan.db.elephantsql.com/msyorlvw"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOHwBuyAd7rTQEMw3T69rvrQQ107UHRDyJ0DPwA5aYJNdvf-0187o6RJ7Q1JgeMThZT0DaEIiT7Uhptsr_jIET61pWUbbKCxRCK1JW4k68sRaDdyuxMXXWz51QZi_-oePb8qrxS9Bp9xnO8bIK1XqMDViTS2nwp8ogMFVsQm4dtSgttNfN0Wqo_e6PxUx5g--FXOPVgYxG1UeBArEbXTUjwy6XB0m_djvUcgb7h6VCPQgO2SW67QcyKqLWsQjIh1V0fTpognWuLlqKbOct_nbIJA2SGAxdD4mJn0KxIgS-uIU6kySvMTCHFjS_AVFep8sLYt4U7w0TGoz6iz7qrfpklKevD4="
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
