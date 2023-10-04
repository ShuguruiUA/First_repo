articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    new_article=[]
    for article in articles_dict:
        title = article['title']
        author = article['author']

        if not letter_case:
            key = key.lower()
            title = title.lower()
            author = author.lower()
        if key in title or key in author:
            new_article.append(article)
    return new_article


print(find_articles('Ark'))

    # new_article = []
    # for article in articles_dict:
    #     author = article['author']
    #     title = article['title']
    #     year = article['year']

    #     if letter_case:
    #         pair_author = key in author
    #         pair_title = key in title

    #     else:
    #         pair_author = key.lower() in author.lower()
    #         pair_title = key.lower() in title.lower()
        
    #     if pair_author or pair_title:
    #         new_article = ()
    #     new_article.update(new_article)
    # return new_article
            