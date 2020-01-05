def preview_content(content):
    """
    Retourne les 40 premiers caractères du contenu de l'article. S'il
    y a plus de 40 caractères, il faut ajouter des points de suspension.
    """

    if content is None:
        return ""

    text = content[:40]
    if len(content) > 40:
        return '{}...'.format(text)
    else:
        return text
