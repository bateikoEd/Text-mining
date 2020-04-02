import datetime

def go_date_bbc(message):
    date_dictionary = {
        "січ" : "01",
        "лют": "02",
        "берез": "03",
        "квіт": "04",
        "трав": "05",
        "черв": "06",
        "лип": "07",
        "серп": "08",
        "вер": "09",
        "жовт": "10",
        "лист": "11",
        "груд": "12"
    }
    list_of_message = message.split()

    try:
        year = int(list_of_message[2].strip())
        date =  list_of_message[0]
        current_month = list_of_message[1].strip().lower()
        for month in date_dictionary.keys():
            if current_month.startswith(month):
                return f"{date}/{date_dictionary[month]}/{str(datetime.date.today().year)}"
    except:
        return datetime.date.today().strftime("%d/%m/%Y")