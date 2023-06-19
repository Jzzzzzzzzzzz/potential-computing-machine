import wikipedia
def get_wikiped_article(article):
    wikipedia.set_lang("ru")

    try:
        return f"{wikipedia.summary(article)}"
    except wikipedia.WikipediaException:
        return "Не удалось найти информацию по данному запросу"