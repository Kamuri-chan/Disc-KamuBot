import wikipedia


def wikipedia_search(arg):
    wikipedia.set_lang("pt")
    try:
        return (wikipedia.summary(arg))
    except wikipedia.DisambiguationError:
        return "Desculpe, não encontrei o resultado. Seja mais específico!"
