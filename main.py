meme_dict = {
            "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
            "LOL": "Una risposta comune a qualcosa di divertente",
            "SHEESH" : "leggera disapprovazione",
            "CREEPY" : ["spaventoso" , "inquietante"],
            "PARA" : ["preoccuparsi per qualcosa", "paranoiarsi"]
            }

for i in range(6):
    counter = 5
    parola = input("Scrivi una parola che non capisci")
    if parola.upper() in meme_dict.keys():
        print("\n",meme_dict[parola.upper()])
        print("\n","ti rimangono",counter - i  , " parole")
    else:
        print("\n","la parola non esiste,scrivine un altra")
        print("\n","ti rimangono",counter - 1, " parole")
